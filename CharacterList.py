from Character import Character

class CharacterList:
    def __init__(self):
        '''
            Creates a list of characters which appear in text
        '''
        self.characters = []

    def get_characters(self):
        return self.characters
    
    def get_names(self):
        '''
            Gets the names of all characters inside of the characters list
        '''
        names = []
        for character in self.characters:
            names.append(character.get_name())
        return names

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