class Word:
    '''
        Creates a new word as represented in text, keeping count of its frequency inside of text
    '''

    def __init__(self, word):
        '''
            Creates a new word and sets its frequency in context
        '''
        self.word = word
        # Word must exist once to be created
        self.frequency = 1

    def get_word(self):
        '''
            Gets the word
            Returns:
                The word
        '''
        return self.word

    def get_frequency(self):
        '''
            Gets the frequency of the word
            Returns:
                The frequency of the word
        '''
        return self.frequency

    def increment_frequency(self):
        '''
            Increments the frequency of the word by one
        '''
        self.frequency += 1