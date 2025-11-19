import Word

class Character:
    '''
        Creates a character based on their name, their catchphrase, and how many times their name
        appears in text.
    '''

    # Array of words spoken by this character
    words = []
    frequency = []
    
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

    def getName(self):
        '''
            Gets the name of the character
            Returns:
                Character's name
        '''
        return self.name
    
    def setName(self, name):
        '''
            Sets the characters name
            Args:
                name (String): new name of character
        '''
        self.name = name

    def getCatchphrase(self):
        '''
            Gets this character's catchphrase
            Returns:
                Character's catchphrase
        '''
        return self.catchphrase
    
    def setCatchphrase(self, catchphrase):
        '''
            Sets the characters catchphrase
            Args:
                catchphrase (String): the most common word spoken by this character
        '''
        self.catchphrase = catchphrase

    def getAppearances(self):
        '''
            Gets the number of apperances of this character name in text
            Returns:
                Number of apperances for character
        '''
        return self.appearances
    
    def incrementAppearances(self):
        '''
            Increments the appearances of this character by one
        '''
        self.appearances += 1

    def addWord(self, word):
        '''
            Adds a single word to the end of the words array for this character
            Args:
                word (String): word spoken by this character
        '''
        if word in self.words:
            i = self.words.index(word)
            existingWord = self.words[i]
            existingWord.incrementFrequency()
        else:
            newWord = Word(word)
            self.words.append(newWord)

    def addSentence(self, sentence):
        '''
            Adds a sentence spoken by this character into the words array
            Args:
                sentence (String[]): Array of strings representing words in a sentence
        '''
        for w in sentence:
            self.addWord(w)

    def mostFrequentWord(self):
        '''
            Gets the most frequent word inside of the words array. If two or more words appear the
            same number of times at the highest count, then the first of the words to appear in
            text is choosen as the most frequent.
            Returns:
                The most frequent word in the words array
        '''
        highestCount = 0
        mostFrequent = ""
        for w in self.words:
            if(w.getFrequency() > highestCount):
                highestCount = w.getFrequency()
                mostFrequent = w.getWord()
        return mostFrequent