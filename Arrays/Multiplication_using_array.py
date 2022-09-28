def single_mul(arr, n):
    j= len(arr)
    answer= []
    carry=0
    for j in range(0,(len(arr))):
        temp = n * arr[j] + carry
        if temp < 10:
            answer.append(temp)
        else:
            answer.append(temp%10)
            carry= temp // 10
            if j==len(arr)-1:
                answer.append(carry)
                carry=0
    return answer
def mul_using_arr(arr1,arr2):
    counter = 1
    answer=single_mul(arr1, arr2[0])
    for i in range(1,len(arr2)):
        temp_arr = []
        for k in range(counter):
            temp_arr.append(0)
        temp_arr += single_mul(arr1, arr2[i])
        answer = add_2_array(answer, temp_arr)
        counter += 1
    return answer
def add_2_array(arr1, arr2):
    carry = 0
    answer = []
    if len(arr2) >= len(arr1):
        for i in range(len(arr2)):
            if i >= len(arr1):
                temp_sum = arr2[i] + carry
            else:
                temp_sum = arr1[i] + arr2[i] + carry
            carry=0
            if temp_sum < 10:
                answer.append(temp_sum)
            else:
                answer.append(temp_sum%10)
                carry = temp_sum // 10
        if carry !=0:
            answer.append(carry)
        return answer
    else:
        for i in range(len(arr1)):
            if i >= len(arr1):
                temp_sum = arr1[i] + carry
            else:
                temp_sum = arr1[i] + arr2[i] + carry
            carry=0
            if temp_sum < 10:
                answer.append(temp_sum)
            else:
                answer.append(temp_sum%10)
                carry = temp_sum // 10
        if carry !=0:
            answer.append(carry)
        return answer

def string_to_arr(s):
    answer = []
    for i in s:
        answer.append(int(i))
    return answer[::-1]
def main():
    number_1 = '100'
    number_2 = '10'
    arr1 = string_to_arr(number_1)
    arr2 = string_to_arr(number_2)
    answer = mul_using_arr(arr1, arr2)
    answer = answer[::-1]
    print(answer)
    
if __name__ == '__main__':
    main()
    