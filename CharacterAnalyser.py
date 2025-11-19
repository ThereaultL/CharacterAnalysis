import sys

def parseFile():
    return 0

def usageMsg():
    '''
        Prints out a usefull usage message to the console before exiting the program
    '''
    print("Usage: python CharacterAnalyser.py <input_file.txt> <output_file.txt>")
    exit()

def openFileSafely(fileName):
    '''
        Safely opens a given file to read. If the file exists, then the opened file is returned.
        If the file given does not exist, or cannot be found, then a usefull error message is
        given to the console before the method usageMsg() is called, exiting the program.
        Args:
            fileName (String): name of the file to open
        Return:
            opened file in read mode
        Throws:
            FileNotFoundError: the given fileName does not exist/cannot be found
    '''
    try:
        return open(fileName, 'r')
    except FileNotFoundError:
        print("File \"" + fileName + "\" was not found! Ensure it has the correct file path.")
        usageMsg()

def main():
    '''
        Checks that the user gives correct arguments, given usefull statements when invalid 
        arguments are given. Stores the input and output file given from the arguments before
        calling for the file parsing to begin.
    '''
    # Check that the correct number of arguments were given to the program
    if(len(sys.argv) > 2):
        print("Too many arguments given!")
        usageMsg()
    elif(len(sys.argv) <= 1):
        print("Not enough arguments given!")
        usageMsg()

    # Store the input and output files before parsing
    inputFile = openFileSafely(sys.argv[0])
    outputFile = sys.argv[1]
    # Call parsing to begin
    parseFile()

if __name__ == "__main__":
    main()