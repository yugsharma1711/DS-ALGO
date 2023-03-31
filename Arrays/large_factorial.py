def number_to_array(n):
    answer = []
    while n >0:
        answer.append(n % 10)
        n = n // 10
    return answer
def multiplication(number1, number2):
    answer = []
    carry  = 0
    for i in range(len(number1)):
        temp = number1[i]*number2+carry
        if temp < 0:
            carry = 0
            answer.append(temp)
        else:
            answer.append(temp%10)
            carry = temp // 10
    if carry != 0:
        answer.append(carry)
    return answer
def large_factorial(n):
    