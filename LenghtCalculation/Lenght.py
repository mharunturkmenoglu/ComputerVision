import matplotlib.pyplot as plt
from numpy import random
import numpy as np
import math 
import cv2

def createDummyPixelAreaMatrix(img):
    height, width, channel = img.shape
    dummy_array = random.random_sample((height, width))

    return dummy_array

def IsPointInTheArray(arr, point):
    for coord in arr:
        if coord == point:
            return True
    return False

def getLenghtOfPointDistance(points, area_matrix):
    x = points[:,0]
    y = points[:,1]

    min_x = np.argmin(x)
    max_x = np.argmax(x)

    min_y = np.argmin(y)
    max_y = np.argmax(y)

    array = []
    f = getPolynomialFitFunction(points)
    for i in range(0, len(x), 1):
        y_val = int(f(x[i]))
        array.append([y_val, x[i]])
    
    lenght = 0.0
    for i in range(0, len(array) - 1):
        coord = array[i]
        coord2 = array[i+1]
        x_lenght = 0.0
        y_lenght = 0.0

        for x in range(coord[0], coord2[0]):
            pass

        for y in range(coord[1], coord2[1]):
            pass

    img2 = cv2.imread('LenghtCalculation/samples/deneme2.png')
    img2 = img2[485:516, 3383:3440]

    array = np.array(array)
    #array = array.sort()
    #ret,img2 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
    combined_image2 = cv2.polylines(img2, [array], False, (0,0,255))
    cv2.imshow('temp image', combined_image2)
    cv2.waitKey(0)
        

def getLenghtPointbyPoint(points, area_matrix):
    x = points[:,0]
    y = points[:,1]

    min_x = np.argmin(x)
    max_x = np.argmax(x)
    min_y = np.argmin(y)
    max_y = np.argmax(y)

    inverse_points = []
    for i in range(0, len(x)):
        inverse_points.append([y[i], x[i]])
    inverse_points = np.array(inverse_points)

    f = getPolynomialFitFunction(points)
    f_inverse = getPolynomialFitFunction(inverse_points)

    reverse_result = []
    for i in range(y[max_y], y[min_y]-1, -1):
        reverse_result.append([f_inverse(i), i])
    reverse_result = np.array(reverse_result)
    
    result = []
    for i in range(x[min_x], x[max_x]+1, 1):
        result.append([i, f(i)])
    result = np.array(result)

    final_array = np.concatenate((result, reverse_result), axis = 0)

    lenght = 0.0
    for i in range(0, len(final_array)-1):
        coord = final_array[i]
        coord2 = final_array[i+1]

        lenght += math.sqrt(
            math.pow(abs(coord[0] - coord2[0]), 2)
            +
            math.pow(abs(coord[1] - coord2[1]), 2)
            )
        
    print("getLenghtPointbyPoint:", lenght)
    print("worst lenght:", len(points) * math.sqrt(2))
    

def getLenght(img):
    area_matrix = createDummyPixelAreaMatrix(img)

    cv2.imshow('image', img)
    cv2.waitKey(0)

    thinned_image = applyThinningAlogirthm(img)
    cv2.imshow('image2', thinned_image)
    cv2.waitKey(0)

    coords = getCoordinates(thinned_image)

    f = getPolynomialFitFunction(coords)

    x = coords[:,0]
    y = coords[:,1]

    lenght = 0.0
    for coord in coords:
        x = coord[0]
        y = coord[1]

        lenght += math.sqrt(area_matrix[x][y])

    # getLenghtOfPointDistance(coords, area_matrix)
    getLenghtPointbyPoint(coords, area_matrix)
    
    # mooved_coords = moveThinned(img, thinned_image)
    # combined_image = cv2.polylines(img, [mooved_coords], False, (255,0,0))
    # cv2.imshow('combined image', combined_image)
    # cv2.waitKey(0)

    scratch = getScratchInOrder(thinned_image, [214,38])
    
def getPolynomialFitFunction(points):
    # get x and y vectors
    x = points[:,0]
    y = points[:,1]

    # calculate polynomial
    z = np.polyfit(x, y, 10)
    f = np.poly1d(z)

    # calculate new x's and y'sq
    x_new = np.linspace(x[0], x[-1], 3)
    y_new = f(x_new)

    # plt.plot(x,y,'o', x_new, y_new)
    # plt.xlim([x[0]-1, x[-1] + 1 ])
    # plt.show()

    return f

def getCoordinates(img):
    coords = np.argwhere(img == 255)
    return coords

def pixelCalculator(img):
    pixel = cv2.countNonZero(img)
    #print(pixel)

def cropImage(img):
    start_point = (1750, 300)
    end_point = (1900, 400)
    thickness = 2
    color = (255, 0, 0)

    #image = cv2.rectangle(img, start_point, end_point, color, thickness)

    cropped_image = img[300:400, 1750:1900]
    return cropped_image

def applyThinningAlogirthm(img):
    thinned = cv2.ximgproc.thinning(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
    ret,thinned = cv2.threshold(thinned,127,255,cv2.THRESH_BINARY)
    return thinned

def moveThinned(img, thinned_img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_coords = getCoordinates(img)
    thinned_coords = getCoordinates(thinned_img)

    y_img = img_coords[:,0]
    x_img = img_coords[:,1]

    y_thin = thinned_coords[:,0]
    x_thin = thinned_coords[:,1]

    min_index_img = np.argmin(x_img)
    min_index_thinned = np.argmin(x_thin)

    x_img_val = x_img[min_index_img]
    y_img_val = y_img[min_index_img]

    x_thin_val = x_thin[min_index_thinned]
    y_thin_val = y_thin[min_index_thinned]

    x_differance = x_thin_val - x_img_val
    y_differance = y_thin_val - y_img_val

    edited_coords = []

    for i in range(len(thinned_coords)):
        x_thin[i] = x_thin[i] - x_differance
        y_thin[i] = y_thin[i] - y_differance

        edited_coords.append([x_thin[i], y_thin[i]])
    
    return np.array(edited_coords)

def getScratchInOrder(thinned_image, initial_coord):
    result = []
    result.append(initial_coord)
    current_coord = initial_coord
    while(True):
        x = current_coord[0]
        y = current_coord[1]
        if thinned_image[x+1][y] == 255 and IsPointInTheArray(result, [x+1, y]) == False:
            result.append([x+1, y])
            current_coord = [x+1, y]
            continue
        elif thinned_image[x-1][y] == 255 and IsPointInTheArray(result, [x-1, y]) == False:
            result.append([x-1, y])
            current_coord = [x-1, y]
            continue
        elif thinned_image[x][y + 1] == 255 and IsPointInTheArray(result, [x, y+1]) == False:
            result.append([x, y+1])
            current_coord = [x, y+1]
            continue
        elif thinned_image[x][y - 1] == 255 and IsPointInTheArray(result, [x, y-1]) == False:
            result.append([x, y-1])
            current_coord = [x,y-1]
            continue
        elif thinned_image[x+1][y+1] == 255 and IsPointInTheArray(result, [x+1, y+1]) == False:
            result.append([x+1, y+1])
            current_coord = [x+1, y+1]
            continue
        elif thinned_image[x+1][y-1] == 255 and IsPointInTheArray(result, [x+1, y-1]) == False:
            result.append([x+1, y-1])
            current_coord = [x+1, y-1]
            continue
        elif thinned_image[x-1][y-1] == 255 and IsPointInTheArray(result, [x-1, y-1]) == False:
            result.append([x-1, y-1])
            current_coord = [x-1, y-1]
            continue
        elif thinned_image[x-1][y+1] == 255 and IsPointInTheArray(result, [x-1, y+1]) == False:
            result.append([x-1, y+1])
            current_coord = [x-1, y+1]
            continue
        else:
            break

    #print(result)    
    return result