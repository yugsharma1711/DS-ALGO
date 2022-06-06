def phoneKeypad(str, output, i, powerset):
    if i == len(str):
        output = "".join(output)
        powerset.append(output)
    else:
        for s in str[i]:
            output_cpy = output[:]
            output_cpy.append(s)
            phoneKeypad(str, output_cpy, i+1, powerset)

str = '23'
encdoing = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
act = []
for i in str:
    act.append(encdoing[i])
output = []
powerset = []
phoneKeypad(act, output, 0, powerset)
print(powerset)