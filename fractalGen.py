import numpy as np
import matplotlib.pyplot as plt
import random as rand
import math


def main():
    #Initilizes vertices, vertices is a 2D array that contains the x and
    #y values of each vertex of the triangle
    vertices = plotTriangle()
    
    #Main loop function
    i = 0
    while i < 5000:
        i += 1
        print(i)
        #Pick a random side and random point
        side = pickSide(vertices)
        point = pickPoint(vertices)

        #Creates a new triangle based on the random side and random point
        newTriangle = [side[0], side[1], point]
        
        #Finds the center of the new triangle
        center = findCentroid(newTriangle)
        
        #newTriangle = np.vstack([newTriangle, newTriangle[0]])
        #plt.plot(newTriangle[:, 0], newTriangle[:, 1])
        
        #Plots the center of the new triangle
        plt.plot(center[0], center[1], marker='x', markersize = 1)

def plotTriangle():
    #Plots a triange, uses math to find the third vertex based on the first two
    vertex1 = [0,0]
    vertex2 = [10,0]
    
    x1 = vertex1[0]
    x2 = vertex2[0]
    y1 = vertex1[1]
    y2 = vertex2[1]

    
    #Third vertex of an equalateral triangle given by:
        #   (x3,y3) = (x1+x2+sqrt(3) * (y1-y2)/2 , (y1+y2+sqrt(3) * (x1-x2) / 2))
        # I multiplied the y value by -1 so the triangle points upwards
    
    vert3x = ((x1 + x2 + np.sqrt(3) * (y1 - y2))/2)
    vert3y = -1 * ((y1 + y2 + np.sqrt(3) * (x1 - x2))/2)
    
    vertex3 = [vert3x, vert3y]
    
    #Creates the array of vertices, the last entry is equal to the first entry
    #This ensure matplotlib plots each line of the triangle
    vertices = np.array([vertex1, vertex2, vertex3])
    vertices = np.vstack([vertices, vertices[0]])
    
    plt.plot(vertices[:, 0], vertices[:, 1])
    
    return vertices

def pickSide(vertices):
    #print(vertices)
    
    
    #Picks a number between 1 and 3
    choice = rand.randint(1, 3)
    
    #Each number that can be chosen points to the vertices that create a side
    #Of the triangle
    if choice == 1:
        point1 = vertices[0]
        point2 = vertices[1]
    elif choice == 2:
        point1 = vertices[1]
        point2 = vertices[2]
    elif choice == 3:
        point1 = vertices[2]
        point2 = vertices[0]
    else:
        print(choice)
        print("invalid roll")
        
    side = [point1, point2]
    #print(side)
    return side
    
def pickPoint(vertices):
    #Picks as random point, as a float, and uses the pointInPolygon function
    #To determine if point is in the triangle or not
    #The function loops until a point within the triangle is found
    looping = True
    while looping:
        x = rand.uniform(0,10)
        y = rand.uniform(0, 10)
        point = [x,y]
        #This removes the last entry of the vertices list
        polygon = vertices[:-1].copy()
        
        if pointInPolygon(point, polygon):
            looping = False
            return point
        else:
            looping = True

def pointInPolygon(point, polygon):
    #Uses a ray-casting method. A point is determined to be within a polygon
    #If it intersects a line an odd number of times
    
    num_vertices = len(polygon)
    x = point[0]
    y = point[1]
    inside = False
 
    # Store the first point in the polygon and initialize the second point
    p1 = polygon[0]
 
    # Loop through each edge in the polygon
    for i in range(1, num_vertices + 1):
        # Get the next point in the polygon
        p2 = polygon[i % num_vertices]
 
        # Check if the point is above the minimum y coordinate of the edge
        if y > min(p1[1], p2[1]):
            # Check if the point is below the maximum y coordinate of the edge
            if y <= max(p1[1], p2[1]):
                # Check if the point is to the left of the maximum x coordinate of the edge
                if x <= max(p1[0], p2[0]):
                    # Calculate the x-intersection of the line connecting the point to the edge
                    x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
 
                    # Check if the point is on the same line as the edge or to the left of the x-intersection
                    if p1[0] == p2[0] or x <= x_intersection:
                        # Flip the inside flag
                        inside = not inside
 
        # Store the current point as the first point for the next iteration
        p1 = p2
 
    # Return the value of the inside flag
    return inside
    

def findIncenter(vertices):
    

    # Suppose (x1, y1), (x2, y2), (x3, y3) are the vertecies of a triangle ABC, 
    # and a, b, and c are the side lengths. the incenter can be calculated with:
    #     ((ax1+bx2+cx3)/a+b+c) , ((ay1 + bx2 + cx3)/a+b+c))
    
    x1 = vertices[0][0]
    x2 = vertices[1][0]
    x3 = vertices[2][0]
    
    y1 = vertices[0][1]
    y2 = vertices[1][1]
    y3 = vertices[2][1]
    
    a = math.hypot(x2 - x1, y2 - y1)
    b = math.hypot(x3 - x2, y3 - y2)
    c = math.hypot(x1 - x3, y1 - y3)
    p = a+b+c
    
    incenterX = ((a*x1) + (b*x2) + (c*x3)) / p
    incenterY = ((a*y1) + (b*y2) + (c*y3)) / p

    incenter = [incenterX, incenterY]
    print("incenter", incenter)
    return incenter
 
def findCentroid(vertices):
    
    #The centroid is the average of all x values and all y values, given by:
    # (x, y) = ((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3)
    
    x1 = vertices[0][0]
    x2 = vertices[1][0]
    x3 = vertices[2][0]
    
    y1 = vertices[0][1]
    y2 = vertices[1][1]
    y3 = vertices[2][1]
    
    sumOfX = x1 + x2 + x3
    sumOfY = y1 + y2 + y3
    
    centroidX = (sumOfX / 3)
    centroidY = (sumOfY / 3)
   # print("vertices", vertices)
    #print("x1: ", x1, "x2: ", x2, "x3: ", x3, "y1: ", y1, "y2: ", y2, "y3: ", y3, "sumX: ", sumOfX, "sumY: ", sumOfY, "centroidX", centroidX, "CentroidY:" , centroidY )
    
    centroid = [centroidX, centroidY]
    
    return centroid
main()