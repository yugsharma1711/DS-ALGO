def reverse(x):
        upper_range = '2147483647'
        lower_range = '2147483648'
        if x < 0:
            x_str = str(x)
            x_str = x_str[1:]
            x_str = x_str[::-1]
            if len(x_str) == len(lower_range):
                for i in range(len(x_str)):
                    if int(x_str[i]) < int(lower_range[i]):
                        return int('-' + x_str)
                    elif int(x_str[i]) == int(lower_range[i]):
                        continue
                    else:
                        return 0
                return int('-' + x_str)
            elif len(x_str) > len(lower_range):
                return 0
            else:
                return int('-'+ x_str)
        if x >= 0:
            x_str = str(x)
            x_str = x_str[::-1]
            if len(x_str) == len(upper_range):
                for i in range(len(x_str)):
                    if int(x_str[i]) < int(upper_range[i]):
                        return int(x_str)
                    elif int(x_str[i]) == int(upper_range[i]):
                        continue
                    else:
                        return 0
                return int(x_str)
            elif len(x_str) > len(upper_range):
                return 0
            else:
                return int(x_str)
print(reverse(-2147483412))