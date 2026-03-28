file_name = input("Enter the file name:")

lines = list()

#what the difference there is the mode is a(append), only add the new entered line into the already exist
# while the mode is w(write) it over write the entire file 
with open(f"{file_name}.txt", mode="a") as f:
    while True:
        line = input("Enter your text [type END to finish]: ")
        if line.upper() == "END":
            break
        line += "\n"
        lines.append(line)
    f.writelines(lines)