# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def every_second_element(raw_list):
    if type (raw_list) != list:
        raise ValueError('Expected a list')
    modified_list = []
    for i in range(1,len(raw_list),2):
        modified_list.append(raw_list[i])
    return modified_list

print(every_second_element([1, 2, 3, 4, 5]))
