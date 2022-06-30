
def stringSequence(str, powerset, output, i):
    if i == len(str):
        output_str = ''.join(output)
        powerset.append(output_str)
        return
    else:
        output_cpy = list(output)
        stringSequence(str, powerset, output_cpy, i+1)
        output.append((str[i]))
        output_cpy = list(output)
        stringSequence(str, powerset, output_cpy, i+1)

str = 'bbb'
powerset = [[]]
stringSequence(str, powerset, [], 0)
powerset = powerset[2:]
print(powerset)