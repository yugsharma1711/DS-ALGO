def minJump(arr):
        jumps = 0
        i=0
        while i < len(arr):
            if i == len(arr) - 1:
                return jumps
            if arr[i] == 0:
                return -1
            ele = arr[i]
            if i + ele >= len(arr)-1:
                jumps += 1
                return jumps
            max_ele = arr[i+arr[i]]
            curr_pointer = i+arr[i]
            k=0
            for j in range(i+arr[i],i,-1):
                temp = arr[j]
                temp -=k
                k+=1 
                if temp >= max_ele:
                    curr_pointer = j
                    max_ele = temp
            i = curr_pointer
            jumps += 1
        return jumps

arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
print(minJump(arr))
        
        
        
#Basically what i did was i found out the maximum element between
#the two jumps but while finding the maximum element i also took care
#of the distance of it , that is the element which would be farther would
#get more advantage , look afte the substraction done in k = 0 part . 
 