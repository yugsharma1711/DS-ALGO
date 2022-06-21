def groupAnagrams(strs):
        values = {}
        for i in strs:
            string_value = []
            for j in i:
                string_value.append(j)
            string_value.sort()
            string_value = ''.join(string_value)
            if values.get(string_value):
                values[string_value].append(i)
            else:
                values[string_value] = [i]
        final_list = [[]]
        for key in values:
            final_list.append(values[key])
        return final_list[1:]
