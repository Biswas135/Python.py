# Function to check if a specific word exists in a file

def check_for_word():
    word = "learning"                    # word to search for
    with open("pratice.txt", "r") as f: # open file in read mode
        data = f.read()                  # read entire content of the file
        if data.find(word) != -1:        # check if word exists (-1 means not found)
            print("Found")               # word exists
        else:
            print("Not found")           # word does not exist

check_for_word()                        # call the function
