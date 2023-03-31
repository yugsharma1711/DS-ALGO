str = ''
_str = ''
for i in str:
    if i == ' ':
        _str += ','
    elif i == 'N':
        _str += 'null'
    else:
        _str += i
print(_str)