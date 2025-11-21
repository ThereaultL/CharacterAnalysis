import sys
from CharacterList import CharacterList
# spaCy must be installed on device
'''
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
'''
import spacy

nlp = spacy.load("en_core_web_sm")

def check_for_names(text):
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
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

def store_name(characters, name):
    '''
        Stores the name of a character inside of the characters list
        Args:
            characters (list): list of characters
            name (String): name of the character
    '''
    characters.add_character(name)

def parse_paragraph(characters, paragraph):
    '''
        Seperates a paragraph based on where there is and isn't speach, given closed quotations.
        If speech is found in a paragraph, then the character speaking is determined using 
        find_character. Once the character speaking is found, the text enclosed in quotations is
        added to list of words inside of the Character class using add_sentence from CharacterList
        Args:
            characters (list): list of characters
            paragraph (String): a paragraph, as defined in the context of english grammar
    '''
    # Splits paragraph by text between quotations
    quote_seperation = seperate_text(paragraph, "\"")
    quotes = quote_seperation[1::2]
    text = quote_seperation[::2]
    # TODO create a list of articles and pronouns to not me counted as "most frequent words"
    if(quotes):
        name = find_character(text)
        for segment in quotes:
            sentence = seperate_text(segment, " ")
            remove_common_words(sentence)
            characters.add_sentence(name, sentence)

def remove_common_words(arr):
    remove = common_words()
    for word in arr:
        if word in remove:
            arr.remove(word)


def common_words():
    return ["the", "I", "and", "a", "an", "on", "you", "in", "they", "they're", "there", "their", 
            "she", "her", "he", "him"]

def find_character(text_list):
    '''
        Given text within quotes, uses the check_for_names function to determine which character
        is speaking. The character speaking is determined by the first apperance of a name withn 
        the list of names in mentioned in a the text.
        Args:
            text_list (list): a list of strings representing words
        Return:
            Name of the character speaking
    '''
    name = ""
    is_character = True
    for text in text_list:
        words = seperate_text(text, " ")
        for w in words:
            name_list = check_for_names(w)
            if(name_list and is_character):
                name = name_list[0]
                is_character = False
    return name


def parse_characters(characters, paragraph):
    '''
        Parses the characters in a paragraph by checking for names. The names list is then 
        iterated, and each name present in the names list is added to the characters 
        Args:
            characters (list): list of characters
            paragraph (String): a paragraph, as defined in the context of english grammar
    '''
    names = check_for_names(paragraph)
    for name in names:
        store_name(characters, name)

def seperate_text(text, regex):
    '''
        Splits a text based on paragraphs which are represented by the new line character
        Args:
            text (String): text to split based on regex
            regex (String): expression to seperate the text by
        Return:
            A list containing tokens of the text split based on the regex
    '''
    return text.split(regex)

def usage_msg():
    '''
        Prints out a usefull usage message to the console before exiting the program
    '''
    print("Usage: python CharacterAnalyser.py <input_file.txt> <output_file.txt>")
    exit()

def parse_file(input_file, output_file):
    '''
        parse a text file by seperating the txt by paragraphs (represented by a new line char).
        Method then iterates through each paragraph in text, parsing each character in a given
        paragraph. After iterating through each paragraph, all characters are then written to
        the output_file
        Args:
            input_file (file): file to read and parse
            output_file (String): file name to write to
    '''
    text = input_file.read()
    paragraphs = seperate_text(text, "\n")
    characters = CharacterList()
    for paragraph in paragraphs:
        parse_characters(characters, paragraph)
        parse_paragraph(characters, paragraph)
    
    characters.set_most_frequent_words()
    write_to_file(output_file, characters)

def write_to_file(output_file, characters):
    '''
        Opens the output_file (or creates new file if not already present) in write mode before
        iterating through the characters inside of characters object. For each character, their
        name and appearances in text and written on its own line inside of the output_file. 
    '''
    characters = characters.get_characters()
    with open(output_file, "w") as f:
        for character in characters:
            f.write(character.get_name() + " : " + str(character.get_appearances()) + " : " 
                    + character.get_catchphrase() + "\n")

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
    input_file = open_file_safely(sys.argv[1])
    output_file = sys.argv[2]
    # Call parsing to begin
    parse_file(input_file, output_file)

if __name__ == "__main__":
    main()