def number_to_array(n):
    answer = []
    while n >0:
        answer.append(n % 10)
        n = n // 10
    return answer
def multiplication(number1, number2):
    answer = []
    carry  = 0
    number_1_arr = number_to_array(number1)
    for i in range(len(number_1_arr)):
        temp = number_1_arr[i]*number2+carry
        if temp < 0:
            carry = 0
            answer.append(temp)
        else:
            answer.append(temp%10)
            carry = temp // 10
    if carry != 0:
        answer.append(carry)
    return answer
def main():
    number_1 = 12
    number_2 = 12
    answer = multiplication(number_1, number_2)
    s = ''
    for i in range(len(answer)-1, -1, -1):
        s += str(answer[i])
    print(s)
if __name__ == '__main__':
    main()