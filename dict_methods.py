#reverse lookup
def reverse_lookup(diction, val):
    for key in diction:
        if diction[key] == val:
            return key
    raise LookupError()

d = {'name':'john','age':12, "religion":'christian','nationality':'kenya','birth_place':'kenya'} 
print(reverse_lookup(d, 'kenyan'))



#forward lookup
def lookup(strings):
    d = dict()
    #iterating through every key in the string provided as an arguement
    for key in strings:
        #checking whether the key is already present in the dictionary
        # if not, we create a new item with the key being the character from the arguement and with the value being 1
        if key not in d:
            d[key] = 1
        #if the key exixts, we increament the value of that key
        else:
            d[key] += 1
    return d
result = lookup('parrot')
print(result)


#converting values to keys and key to values
#this function is using the results of the lookup function above
def inverted_dict(d):
    inverse = dict()
    #iterating through the dictionary provided
    for key in d:
        val = d[key]
        #checking whether the value of a certain key exists in the inverse dictionary
        #if not the value becomes the key
        if val not in inverse:
            inverse[val] = [key]
        #if the value exists as a key in the dictionary, we append to that value
        else:
            inverse[val].append(key)
    return inverse
result_inverse = inverted_dict(result)
print(result_inverse)