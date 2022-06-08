import copy
def pathFinder(arr, route, i, j,str):
    if arr[i][j] == 0:
        return
    if i == len(arr)-1 and j == len(arr[0])-1:
        route_str = "".join(route[1:])
        str.append(route_str)
        return
    Down = False
    Up = False
    right = False
    left = False
    if i != 0:
        Up = True
    if i != len(arr)-1:
        Down = True
    if j != 0:
        left = True
    if j != len(arr[0])-1:
        right = True
    
    arr_cpy = copy.deepcopy(arr)

    if Up:
        if arr_cpy[i-1][j] == 1:
            arr_cpy[i][j] = 0
            route_cpy = route[:]
            route_cpy.append('U')
            pathFinder(arr_cpy, route_cpy, i-1, j,str)
    if Down:
            if arr_cpy[i+1][j] == 1:
                arr_cpy[i][j] = 0
                route_cpy = route[:]
                route_cpy.append('D')
                pathFinder(arr_cpy, route_cpy, i+1, j,str)
    if left:
            if arr_cpy[i][j-1] == 1:
                arr_cpy[i][j] = 0
                route_cpy = route[:]
                route_cpy.append('L')
                pathFinder(arr_cpy, route_cpy, i, j-1,str)
    if right:
            if arr_cpy[i][j+1] == 1:
                arr_cpy[i][j] = 0
                route_cpy = route[:]
                route_cpy.append('R')
                pathFinder(arr_cpy, route_cpy, i, j+1,str)

arr = [[1,1,1,0], [1,1,0,1], [1,1,0,0], [0,1,1,1]]
str = []    
pathFinder(arr, [' '], 0, 0, str)
str.sort()
print(str)