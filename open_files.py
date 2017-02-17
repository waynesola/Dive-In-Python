# example 01
# create a file named "a_file.txt"
a_file = open(r'F:\程序\Python\PyCharm\Dive_in_Python\a_file.txt', 'w')

# write something
a_file.write('hello world,lol!')

# close steam
a_file.close()

# example 02
# read a file named "a_file.txt"
a_file = open(r'F:\程序\Python\PyCharm\Dive_in_Python\a_file.txt', 'r')

# read the fifth bytes
p1 = a_file.read(5)

# read the rest bytes
p2 = a_file.read()

# print the bytes
print(p1)
print(p2)

# close steam
a_file.close()
