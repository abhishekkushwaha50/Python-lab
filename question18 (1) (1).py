f = open("file.txt", "w")
f.write("Hello World\n")
f.close()

f = open("file.txt", "a")
f.write("Append line\n")
f.close()