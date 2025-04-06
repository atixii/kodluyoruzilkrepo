#1.assigment#
def flatten (lst):
    result=[]
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output = flatten(input_list)
print(output)


#2.assigment#
def reversedlist(lst):
    reversed_list = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_list.append(reversedlist(item)) 
        else:
            reversed_list.append(item)
    return reversed_list

input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reversedlist(input_list)
print(output)