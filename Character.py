import Word

class Character:
    '''
        Creates a character based on their name, their catchphrase, and how many times their name
        appears in text.
    '''
    
    def __init__(self, name):
        '''
            Creates a new character based off their name. A new characters catchphrase defaults to
            an empty string and their appearances in text defaults to one.
            Args:
                name (String): name of the character
        '''
        self.name = name
        # Most common word spoken by the charater
        self.catchphrase = ""
        # In order for a character to be created, their name must be mentioned at least once
        self.appearances = 1
        # Array of words spoken by this character
        self.words = []

    def get_name(self):
        '''
            Gets the name of the character
            Returns:
                Character's name
        '''
        return self.name
    
    def set_name(self, name):
        '''
            Sets the characters name
            Args:
                name (String): new name of character
        '''
        self.name = name

    def get_catchphrase(self):
        '''
            Gets this character's catchphrase
            Returns:
                Character's catchphrase
        '''
        return self.catchphrase
    
    def set_catchphrase(self, catchphrase):
        '''
            Sets the characters catchphrase
            Args:
                catchphrase (String): the most common word spoken by this character
        '''
        self.catchphrase = catchphrase

    def get_appearances(self):
        '''
            Gets the number of apperances of this character name in text
            Returns:
                Number of apperances for character
        '''
        return self.appearances
    
    def increment_appearances(self):
        '''
            Increments the appearances of this character by one
        '''
        self.appearances += 1

    def get_words(self):
        '''
            Gets the string value from the word objects inside of words, placing them into a list
            before return the new list of word names. 
            Return:
                List of string word values from words
        '''
        word_names = []
        for w in self.words:
            word_names.append(w.get_word())
        return word_names

    def add_word(self, word):
        '''
            Adds a single word to the end of the words array for this character
            Args:
                word (String): word spoken by this character
        '''
        word_names = self.get_words()
        if word in word_names:
            i = word_names.index(word)
            existing_word = self.words[i]
            existing_word.incrementFrequency()
        else:
            new_word = Word(word)
            self.words.append(new_word)

    def add_sentence(self, sentence):
        '''
            Adds a sentence spoken by this character into the words array
            Args:
                sentence (String[]): Array of strings representing words in a sentence
        '''
        for w in sentence:
            self.add_word(w)

    def most_frequent_word(self):
        '''
            Gets the most frequent word inside of the words array. If two or more words appear the
            same number of times at the highest count, then the first of the words to appear in
            text is choosen as the most frequent.
            Returns:
                The most frequent word in the words array
        '''
        highest_count = 0
        most_frequent = ""
        for w in self.words:
            if(w.get_frequency() > highest_count):
                highest_count = w.get_frequency()
                most_frequent = w.get_word()
        return most_frequent