def minimumPlatform(arrival, departure):                
    arrDeparture = []
    for i in range(len(arrival)):
        arrDeparture.append((arrival[i],'a'))
        arrDeparture.append((departure[i], 'd'))
    arrDeparture = sorted(arrDeparture)
    minimum = 0
    max_platform = 0
    for i in arrDeparture:
        if i[1] == 'a':
            minimum += 1
        else:
            minimum -= 1
        if minimum >= max_platform:
            max_platform = minimum
    return max_platform    
arr1 = [900, 940, 950, 1100, 1500, 1800]
arr2 = [910, 1200, 1120, 1130, 1900, 2000]

print(minimumPlatform(arr1, arr2))