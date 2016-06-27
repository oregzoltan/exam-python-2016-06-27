# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

def write_three_times(filename, string):
    content = string*3
    try:
        f = open(filename, 'w')
        f.write(content)
        f.close()
    except:
        pass

write_three_times('three.txt','apple')
