import string


### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'


class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    # Applied method
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        

        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower_letters_double = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        upper_letters_double = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        final_dict = {}

        for letter in lower_letters:
            letter_index = lower_letters_double.find(letter)
            replacement_letter_index = letter_index + shift

            final_dict[letter] = lower_letters_double[replacement_letter_index]

        for letter in upper_letters:
            letter_index = upper_letters_double.find(letter)
            replacement_letter_index = letter_index + shift
            final_dict[letter] = upper_letters_double[replacement_letter_index]

        return final_dict

    # Applied method
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        char_list = list(self.message_text)
        for i in range(len(char_list)):
            if char_list[i] in string.ascii_letters:
                replacement_letter = shift_dict.get(char_list[i])
                char_list[i] = replacement_letter

        message = "".join(char_list)

        return message


# Applied class
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


# Applied class
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # initialize shift as 0
        shift = 0
        # initialize highest_words as 0
        highest_words = 0
        # initialize best_shift as 0
        best_shift = 0
        # initialize best message as an empty string
        best_message = ""
        # shift can't be bigger than 26
        while shift <= 26:
            # each time we measure how many words are correct, we have to start from 0
            words = 0

            # this is the decryption try with the shift given at this operation
            decrypted_message = Message.apply_shift(self, shift)
            # self.message_text is splitted to be the list of words
            message_word_list = decrypted_message.split(" ")

            # we have the number of correct words in the words variable
            for word in message_word_list:
                if is_word(self.valid_words, word) == True:
                    words += 1
                else:
                    continue

            if words >= highest_words:
                highest_words = words
                best_shift = shift
                best_message = decrypted_message

            shift += 1

        return (best_shift, best_message)


# Applied function
def decrypt_story():
    '''
    Helper function get_story_string() that returns the encrypted version of the story as a string. 
    Create a CiphertextMessage object using the story string 
    and use decrypt_message to return the appropriate shift value and unencrypted story string.
    '''
    story = CiphertextMessage(get_story_string())

    decryption_result = story.decrypt_message()

    return decryption_result
