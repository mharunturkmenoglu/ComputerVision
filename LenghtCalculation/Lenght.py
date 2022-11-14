import math
import LenghtCalculation.utilities as utilities 
import cv2
import numpy as np
import time

def getDistance(coords):
    ''' 
    This functions measures lenght of distance between coords. Coords must be in-order.!
    :param coords: in-order list of coords.
    :return: The result of the lenght calculation. Sum of distance between points.
    '''
    lenght = 0.0
    for i in range(0, len(coords) - 1):
        current_coord = coords[i]
        next_coord = coords[i+1]

        if abs(current_coord[0] - next_coord[0]) + abs(current_coord[1] - next_coord[1]) == 2:
            lenght += math.sqrt(2)
            # print(f"sqrt for {current_coord}")
        else:
            # print(f"1 for {current_coord}")
            lenght += 1

    return lenght + 1 

def IsPointInTheArray(arr, point):
    ''' 
    This functions checks point is in the array or not. 
    :param arr: array
    :param point: point
    :return: If it is in the array returns True, else returns False.
    '''
    for coord in arr:
        if coord == point:
            return True
    return False

def deleteCoordInArray(array, coord):
    ''' 
    This functions deletes point if point is in the array. 
    :param arr: array
    :param point: point
    :return: array.
    '''
    for i in range(0, len(array)):
        if coord == array[i]:
            array.remove(coord)
            return array
    return array

def getExtremePoints(coords):
    ''' 
    This functions finds coords only have one pixel neighbour and returns that coords. 
    :param coords: array
    :return: array.
    '''
    extreme = []
    for coord in coords:
        if len(getNeighboursOfPixel(coords, coord, [], [-1,-1])) == 1:
            extreme.append(coord)
    return extreme

def getNeighboursOfPixel(coords, point, duplicated, exception = None):
    ''' 
    This functions finds all neighbours of a pixels (coords) that is not in duplicated array and exception array. 
    :param coords: array
    :param point: array
    :param duplicated: array
    :param exception: array
    :return: array of neigbours.
    '''
    neighbours = []
    arr = []
    x = point[0]
    y = point[1]

    arr.append([x+1, y])
    arr.append([x-1, y])
    arr.append([x, y+1])
    arr.append([x, y-1])
    arr.append([x+1, y+1])
    arr.append([x+1, y-1])
    arr.append([x-1, y-1])
    arr.append([x-1, y+1])

    for coord in arr:
        if IsPointInTheArray(coords, coord) == True and exception != coord and IsPointInTheArray(duplicated, coord) == False:
            neighbours.append(coord)
    return neighbours

def getDuplicatedPixels(coords):
    ''' 
    This functions finds duplicate pixels or unnecessary pixels in given array. It doesn't broke the chain of pixels.
    :param coords: array
    :return: array of duplicated array
    '''
    duplicated = []
    for coord in coords:
        if IsPointInTheArray(duplicated, coord) == True:
            continue 
        neighbours = getNeighboursOfPixel(coords, coord, duplicated , [-1,-1])
        if len(neighbours) > 2:
            # print(f'neighbours of {coord}:')
            # print(neighbours)
            for point in neighbours:
                r_neighbours = getNeighboursOfPixel(coords, point, duplicated, coord)
                # print(f"r_neighbours of {point}")
                # print(r_neighbours)
                flag = False
                for x in r_neighbours:
                    if IsPointInTheArray(neighbours, x) == False:
                        flag = True
                if flag == False:
                    # print("duplicated:", point)
                    duplicated.append(point)
                else:
                    flag = False
    return duplicated

def createImageWithCoords(img, coords):
    image = np.zeros([img.shape[0],img.shape[1]], dtype=np.uint8)
    # coords = np.array(coords)
    # print(coords)
    for coord in coords:
        x = coord[0]
        y = coord[1]
        image[x][y] = 255
    print(img.shape)
    cv2.imshow("result", image)
    cv2.waitKey(0)

def getLenght(img):
    ''' 
    This functions calculates lenght of given image
    :param img: image
    '''
    start = time.time()
    ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    thinned_image = utilities.applyThinningAlogirthm(img)

    coords = utilities.getCoordinates(thinned_image)
    old_coords =coords
    coords = coords.tolist()
    duplicated_coords = getDuplicatedPixels(coords)

    for coord in duplicated_coords:
        coords = deleteCoordInArray(coords, coord)

    extreme_points = getExtremePoints(coords)
    print("Extreme Points")
    print(extreme_points)

    coords_inorder = utilities.getScratchInOrder(thinned_image, extreme_points[1])

    print("min lenght:", len(coords))
    lenght = getDistance(coords_inorder)
    print("lenght:", lenght)

    end = time.time()
    print("execution time:", end - start)
    createImageWithCoords(img, coords)

    return old_coords, coords


img = cv2.imread('LenghtCalculation/samples/snake_sample3.png')
cv2.imshow('original image', img)
cv2.waitKey(0)

coords, coords_inorder = getLenght(img)
utilities.getLenght(img)

np_img = np.array(img)


for i in range(0, len(coords)):
    coord = coords[i]
    np_img[coord[0], coord[1]] = (255, 0,0)

cv2.imshow("blue image", np_img)
cv2.waitKey(0)

for i in range(0, len(coords_inorder)):
    coord = coords_inorder[i]
    np_img[coord[0], coord[1]] = (0, 0, 255)

cv2.imshow("red image", np_img)
cv2.waitKey(0)
