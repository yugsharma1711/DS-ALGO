def CheckBinaryPalindrome(n, i, j):
    if i >= j:
        return True
    if n[i] == n[j]:
        return CheckBinaryPalindrome(n, i+1, j-1)
    else:
        return False
def toBinary(n):
    binary_number = (bin(n))
    binary_number = binary_number[2:]
    return binary_number
n = toBinary(7)
print(CheckBinaryPalindrome(n, 0, (len(n)-1)))
