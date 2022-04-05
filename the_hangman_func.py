def check_win(secret_word, old_letters_guessed):
    """
    checks if the secret_word guessed successfully by checking if all letters in
    secret_word exist in the list of old_letters_guessed
    :param secret_word: the word needs to be guessed
    :param old_letters_guessed: a list of letters already guessed
    :return: True if all letters from secret_word are in old_letters_guessed
    and False if not
    :rtype: bool
    """
    secret_word_list = []
    for i in secret_word:
        secret_word_list.append(i)
    for i in secret_word_list:
        if i not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    builds a string for secret_word with blank lines for the letters yet to be guessed
    and letters at the correct position from old_
    letters_guessed
    :param secret_word: the word needs to be guessed
    :param old_letters_guessed: a list of letters already guessed
    :return: a string with blanks and letters
    :rtype: str
    """
    guessed_str = ''
    for i, l in enumerate(secret_word):
        if secret_word[i] in old_letters_guessed:
            guessed_str = guessed_str + f'{secret_word[i]} '
        else:
            guessed_str = guessed_str + '_ '
    return guessed_str


def check_valid_input(letter_guessed, old_letters_guessed):
    """checks if 'letter_guessed' is a single english letter that hasn't been guessed already
         :param letter_guessed: the argument to check
         :param param old_letters_guessed: a list of old guesses
          :type letter_guessed: all
          :type old_letters_guessed: list
          :return: true if a single english letter that is not in old_letters_guessed, false if anything else
          :rtype: bool"""
    if (len(letter_guessed) != 1) or not letter_guessed.isalpha():
        return False
    if letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ adds letter_guest to to old_letters_guessed only if letter_guest valid
     :param letter_guessed: the argument to check
     :param param old_letters_guessed: a list of old guesses
      :type letter_guessed: all
      :type old_letters_guessed: list
      :return: True if letter added to list, or print of ('X'\n old_letters_list\n) false
      :rtype: bool"""
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print('X')
        old_sorted = sorted(old_letters_guessed)
        print(' -> '.join(old_sorted))
        return False


def choose_word(file_path, index):
    """
    get address to a text file containing words with space between them,
    and an integer for the index of the chosen word.
    the function return a tuple with the number of unique words in the file
    and the word chosen
    :param file_path: a string with address of the words file
    :param index: an int representing the index of the word to choose
    :type file_path: str
    :type index: int
    :return: a tuple with the number of unique words in the file
    and the word chosen
    :rtype: tuple
    """
    file_text = open(file_path, 'r')
    words = file_text.read()
    file_text.close()
    words = words.replace('\n', ' ')
    words = words.split(' ')
    while index > len(words):
        index -= len(words)
    chosen = index - 1
    return len(set(words)), words[chosen]


HANGMAN_PHOTOS = {1:
                      """
    x-------x
""",
                  2:
                      """
    x-------x
    |
    |
    |
    |
    |
""",
                  3:
                      """
    x-------x
    |       |
    |       0
    |
    |
    |
""",
                  4:
                      """
    x-------x
    |       |
    |       0
    |       |
    |
    |
""",
                  5:
                      """
    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |
""",
                  6:
                      """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |
""",
                  7:
                      """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |
"""}


def print_hangman(num_of_tries):
    return HANGMAN_PHOTOS[num_of_tries + 1]


HANGMAN_ASCII_ART = """
    Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
MAX_FAILES = 6
