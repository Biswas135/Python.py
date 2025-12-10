# Open the file in read mode
f = open("demo.txt", "r")

# Read entire content
d = f.read()
print("Full content:\n", d)

# Move the file pointer to the beginning
f.seek(0)  # reset pointer to start

# Read lines one by one
line1 = f.readline()
print("Line 1:", line1.strip())  # strip() removes extra newline

line2 = f.readline()
print("Line 2:", line2.strip())

# Close the file
f.close()
