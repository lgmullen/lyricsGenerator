import random
import sys
sys.path.append('../data')



# -----------------------------------------------------------------------------
# NGramModel class ------------------------------------------------------------
# Core functions to implement: prepData, weightedChoice, and getNextToken
# Reach functions to implement: getNextNote

class NGramModel(object):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  This is the NGramModel constructor. It sets up an empty
                  dictionary as a member variable. It is called from the
                  constructors of the NGramModel child classes. This
                  function is done for you.
        """
        self.nGramCounts = {}

    def __str__(self):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  returns the string to print when you call print on an
                  NGramModel object. This function is done for you.
        """
        return 'This is an NGramModel object'

    def prepData(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: nothing
        Effects:  returns a copy of text where each inner list starts with
                  the symbols '^::^' and '^:::^', and ends with the symbol
                  '$:::$'. For example, if an inner list in text were
                  ['hello', 'goodbye'], that list would become
                  ['^::^', '^:::^', 'hello', 'goodbye', '$:::$'] in the
                  returned copy.

                  Make sure you are not modifying the original text
                  parameter in this function.
        """
        textCopy = []
        import copy
        textCopy = copy.deepcopy(text)
        rows = len(textCopy)
        for i in range(rows):
            textCopy[i].insert(0, '^:::^')
            textCopy[i].insert(0, '^::^')
            textCopy[i].insert(len(textCopy[i]),'$:::$')
        return textCopy

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts
        Effects:  this function populates the self.nGramCounts dictionary.
                  It does not need to be modified here because you will
                  override it in the NGramModel child classes according
                  to the spec.
        """
        return

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns a bool indicating whether or not this n-gram model
                  can be used to choose the next token for the current
                  sentence. This function does not need to be modified because
                  you will override it in NGramModel child classes according
                  to the spec.
        """
        
        return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. This function does not need to be
                  modified because you will override it in the NGramModel child
                  classes according to the spec.
        """
        return {}

    def weightedChoice(self, candidates):
        """
        Requires: candidates is a dictionary; the keys of candidates are items
                  you want to choose from and the values are integers
        Modifies: nothing
        Effects:  returns a candidate item (a key in the candidates dictionary)
                  based on the algorithm described in the spec.
        """
        token = []
        count = []
        # make a list of keys and a list of values'''
        for keyname in candidates:
            token.append(keyname)
            count.append(candidates[keyname])
        # creat a third list
        cumulative = []
        if count != []:
            cumulative.append(count[0])
            for i in range(1,len(count)):
                cumulative.append(cumulative[i - 1] + count[i])
        else:
            return
        random_number = random.randrange(0, cumulative[- 1])
        # find the index of the value and return the coresponding token
        for i in cumulative:
            if i > random_number:
                return token[cumulative.index(i)]
        return token[-1]

    def getNextToken(self, sentence):
        """
        Requires: sentence is a list of strings, and this model can be used to
                  choose the next token for the current sentence
        Modifies: nothing
        Effects:  returns the next token to be added to sentence by calling
                  the getCandidateDictionary and weightedChoice functions.
                  For more information on how to put all these functions
                  together, see the spec.
        """
        return self.weightedChoice(self.getCandidateDictionary(sentence))

    # def getNextNote(self, musicalSentence, possiblePitches):
    #     """
    #     Requires: musicalSentence is a list of PySynth tuples,
    #               possiblePitches is a list of possible pitches for this
    #               line of music (in other words, a key signature), and this
    #               model can be used to choose the next note for the current
    #               musical sentence
    #     Modifies: nothing
    #     Effects:  returns the next note to be added to the "musical sentence".
    #               For details on how to do this and how this will differ
    #               from the getNextToken function from the core, see the spec.

    #               Please note that this function is for the reach only.
    #     """
    #     allCandidates = self.getCandidateDictionary(musicalSentence)
    #     constrainedCandidates = {}        
    #     for key in allCandidates:
    #         noNumPitch = ''.join(i for i in key[0] if not i.isdigit())
    #         if noNumPitch == '$:::$' or noNumPitch in possiblePitches:
    #                 constrainedCandidates[key] = allCandidates[key]
                    
    #     if constrainedCandidates == {}:
    #         pitch = random.choice(possiblePitches) + '4'
    #         duration = random.choice(NOTE_DURATIONS)
    #         return (pitch, duration)
    #     else:
    #         return self.weightedChoice(constrainedCandidates)

    # def getFastNote(self, musicalSentence, possiblePitches):
    #     allCandidates = self.getCandidateDictionary(musicalSentence)
    #     constrainedCandidates = {}
    #     for key in allCandidates:
    #         noNumPitch = ''.join(i for i in key[0] if not i.isdigit())
    #         if noNumPitch == '$:::$' or noNumPitch in possiblePitches:
    #                 constrainedCandidates[key] = allCandidates[key]
                    
    #     if constrainedCandidates == {}:
    #         pitch = random.choice(possiblePitches) + '4'
    #         duration = random.choice(FAST_NOTE_DURATIONS)
    #         return (pitch, duration)
    #     else:
    #         for key in constrainedCandidates:
    #             temp = random.choice(FAST_NOTE_DURATIONS)
    #             key = (key[0], temp)
    #         return self.weightedChoice(constrainedCandidates)

    # def getMediumNote(self, musicalSentence, possiblePitches):
    #     allCandidates = self.getCandidateDictionary(musicalSentence)
    #     constrainedCandidates = {}
    #     for key in allCandidates:
    #         noNumPitch = ''.join(i for i in key[0] if not i.isdigit())
    #         if noNumPitch == '$:::$' or noNumPitch in possiblePitches:
    #                 constrainedCandidates[key] = allCandidates[key]
                    
    #     if constrainedCandidates == {}:
    #         pitch = random.choice(possiblePitches) + '4'
    #         duration = random.choice(MEDIUM_NOTE_DURATIONS)
    #         return (pitch, duration)
    #     else:
    #         for key in constrainedCandidates:
    #             temp = random.choice(MEDIUM_NOTE_DURATIONS)
    #             key = (key[0], temp)
    #         return self.weightedChoice(constrainedCandidates)

    # def getSlowNote(self, musicalSentence, possiblePitches):
    #     allCandidates = self.getCandidateDictionary(musicalSentence)
    #     constrainedCandidates = {}
    #     for key in allCandidates:
    #         noNumPitch = ''.join(i for i in key[0] if not i.isdigit())
    #         if noNumPitch == '$:::$' or noNumPitch in possiblePitches:
    #                 constrainedCandidates[key] = allCandidates[key]
                    
    #     if constrainedCandidates == {}:
    #         pitch = random.choice(possiblePitches) + '4'
    #         duration = random.choice(SLOW_NOTE_DURATIONS)
    #         return (pitch, duration)
    #     else:
    #         for key in constrainedCandidates:
    #             temp = random.choice(SLOW_NOTE_DURATIONS)
    #             key = (key[0], temp)
    #         return self.weightedChoice(constrainedCandidates)
        



# -----------------------------------------------------------------------------
# Testing code ----------------------------------------------------------------

if __name__ == '__main__':
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    choices = { 'the': 2, 'quick': 1, 'brown': 1 }
    sentence = ['the']
    nGramModel = NGramModel()
    # add your own testing code here if you like
    print (nGramModel.prepData(text))
    print (nGramModel.weightedChoice(choices))
    
