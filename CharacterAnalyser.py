import sys
# spaCy must be installed on device
'''
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
'''
import spacy

nlp = spacy.load("en_core_web_sm")

def parse_file():
    return 0

def check_for_names(paragraph):
    '''
        Using spaCy, an object containing tokens from paragaph will be created. From this object,
        tokens will be checked for the label type "PERSON", singally that a name was found. Words
        from this paragraph with the label "PERSON" are returned. If no words with the label
        "PERSON" are found, then an empty list is returned.
        Args:
            Paragraph (String): A paragraph, as defined in the context of english grammar
        Return:
            List of names in paragraph
    '''
    # Object created using spaCy
    doc = nlp(paragraph)
    return [ent.text for ent in doc.ents if ent.label_ == "PERSON"]


def usage_msg():
    '''
        Prints out a usefull usage message to the console before exiting the program
    '''
    print("Usage: python CharacterAnalyser.py <input_file.txt> <output_file.txt>")
    exit()

def open_file_safely(fileName):
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
        usage_msg()

def main():
    '''
        Checks that the user gives correct arguments, given usefull statements when invalid 
        arguments are given. Stores the input and output file given from the arguments before
        calling for the file parsing to begin.
    '''
    # Check that the correct number of arguments were given to the program
    if(len(sys.argv) > 3):
        print("Too many arguments given!")
        usage_msg()
    elif(len(sys.argv) <= 2):
        print("Not enough arguments given!")
        usage_msg()

    # Store the input and output files before parsing
    inputFile = open_file_safely(sys.argv[1])
    outputFile = sys.argv[2]
    # Call parsing to begin
    parse_file()

if __name__ == "__main__":
    main()