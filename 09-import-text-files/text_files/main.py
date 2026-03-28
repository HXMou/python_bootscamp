fd = open("example.txt")
print(fd.read(), type(fd))

for index, line in enumerate(fd):
    print(f"[{index+1}] {line}")

fd.close() #must have the close method to clean the memory 

#but when using 'with'statement, doesn't need the close()
with open("example.txt", mode="r") as fd:
    for line in fd:
        print(line[:-1])

with open("new_file.txt", mode="w") as f:
    f.write("this is the new text line.")