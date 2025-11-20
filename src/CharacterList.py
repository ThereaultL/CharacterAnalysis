from Character import Character

class CharacterList:
    def __init__(self):
        '''
            Creates a list of characters which appear in text
        '''
        self.characters = []

    def get_characters(self):
        '''
            Gets the characters array
        '''
        return self.characters
    
    def get_character(self, name):
        '''
            Given a name, iterates thorugh all characters inside of characters, searching for the
            character with the same name given. If found, the character object is returned.
            Otherwise, an empty string is returned
            Args:
                name (String): name of the character
            Return:
                Character object of matching name or empty string
        '''
        for character in self.characters:
            if character.get_name() == name:
                return character
    
    def add_sentence(self, name, sentence):
        '''
            Adds a sentence spoken by this character into the words array
            Args:
                sentence (String[]): Array of strings representing words in a sentence
        '''
        character = self.get_character(name)
        for w in sentence:
            character.add_word(w)
    
    def get_names(self):
        '''
            Gets the names of all characters inside of the characters list
        '''
        names = []
        for character in self.characters:
            names.append(character.get_name())
        return names
    
    def set_most_frequent_words(self):
        for character in self.characters:
            character.set_catchphrase(character.most_frequent_word())

    def add_character(self, name):
        '''
            Adds a character to the character list based on whether or not the character is 
            already in the characters list. If the character exists inside of the characters list,
            then that character object's appearance is incremented. Otherwise, a new character is
            created before being appended to the end of the characters list.
            Args:
                name (String): name of the character
        '''
        names = self.get_names()
        if name in names:
            i = names.index(name)
            existing_character = self.characters[i]
            existing_character.increment_appearances()
        else:
            new_character = Character(name)
            self.characters.append(new_character)