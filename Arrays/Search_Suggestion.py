def search(products, searchWord):
        products.sort()
        suggestion = [[]]
        for i in range(len(searchWord)):
            lst = []
            j = 0
            while j < len(products):
                if i < len(products[j]): 
                    if searchWord[i] != products[j][i]:
                        products.remove(products[j])
                        j -= 1
                else:
                    products.remove(products[j])
                j += 1
            suggestion.append(products[0:3])
        return suggestion[1:]
print(search(["mobile","mouse","moneypot","monitor","mousepad"], 'mouse'))