class Word:
    '''
        Creates a new word as represented in text, keeping count of its frequency inside of text
    '''

    def __init__(self, word, frequency):
        '''
            Creates a new word and sets its frequency in context
        '''
        self.word = word
        # Word must exist once to be created
        self.frequency = 1

    def getWord(self):
        '''
            Gets the word
            Returns:
                The word
        '''
        return self.word

    def getFrequency(self):
        '''
            Gets the frequency of the word
            Returns:
                The frequency of the word
        '''
        return self.frequency

    def incrementFrequency(self):
        '''
            Increments the frequency of the word by one
        '''
        self.frequency += 1