#read - error if it dosn't exist

f = open("name.txt")
# print(f.read()) #read all the file
# print(f.read(2)) #read the 2 first caracter of the file
# print(f.readline()) #read the first line of the file

for line in f:
    print(line)

f.close()

try: 
    f = open("name_list.txt")
    print(f.read())
except:
    print ("tu ments")
finally:
    f.close()


# f = open("name.txt", "a")
# f.write("Neil\n")
# f.close()

f = open("context.txt", "w")
f.write("bye bye")
f.close()

f = open("ali.txt", "x")
f.write("yooo")
f.close()

f = open("ali.txt")
print(f.read())
f.close()