def PalindromeGen(N,X):
    if N == 1 and X == 1:
        return ['a']
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    palindrome = ['a'] * N
    if N >= (2*X -1):
        current_index = 0
        last_index = N - 1
        for i in range(1,X):
            palindrome[current_index] = alphabets[i]
            palindrome[last_index] = alphabets[i]
            current_index += 1
            last_index -= 1          
        return palindrome
    else:
        return -1
def starter(N,X):
    palin = PalindromeGen(N,X)
    if palin == -1:
        print(-1)
    else:
        print(''.join(palin))
T = int(input())
while T>0:
    N,X = map(int, input().split())
    starter(N,X)
    T -= 1