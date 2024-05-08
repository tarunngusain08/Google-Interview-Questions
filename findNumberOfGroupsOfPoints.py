# Given a list of 2d points, if any two points have distance(straight line) <= k , 
# group them together. For example. [P1,P2,P3], P1 to P2 <=k, P2 to p3<=k, p1 to p3>k. 
# they are still in the same group. (distance relationship is chainable ) 
# ask how many groups can you find ?

def union(pointA, pointB):
    groups[find(pointA)] = find(pointB)

def find(point):
    if point == groups[point]: return point
    return find(groups[point])

def distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def findNumberOfGroupsOfPoints(points, k):
    groups = [i for i in range(len(points))]
    for i in range(1,len(points)):
        x1,y1 = points[i]
        x2,y2 = points[i-1]
        if distance(x1,y1,x2,y2) <= k: union(i,i-1)

    print(groups)
    print(len(set(groups)))

points = [(0,0),(2,4),(3,3),(5,2),(-1,20),(-4,-5),(6,7),(-12,0),(3,-6)]
k = 3
findNumberOfGroupsOfPoints(points, k)
