if __name__ == '__main__':
    from the_hangman_func import *
    # print opening screen
    print(HANGMAN_ASCII_ART, "\n", MAX_FAILES)
    # get words file and index
    file_address = input('enter your words file: ')
    # C:\Users\idand\Desktop\New Text Document.txt
    word_index = int(input('enter a number to choose your word: '))
    live_old_letters_guessed = []
    num_of_fails = 0
    # choose word
    live_secret_word = choose_word(file_address, word_index)[1]
    # start the game print first position and ask for letter
    while (not check_win(live_secret_word, live_old_letters_guessed)) \
            and num_of_fails < 6:
        print(print_hangman(num_of_fails))
        print(show_hidden_word(live_secret_word, live_old_letters_guessed))
        temp_letter = input('try to guess the secret word letter by letter: ')
        if try_update_letter_guessed(temp_letter, live_old_letters_guessed):
            if temp_letter not in live_secret_word:
                print('):')
                num_of_fails += 1
        else:
            print("you didn't enter a new single english letter")
    if num_of_fails < 6:
        print(f'{print_hangman(num_of_fails)}'
              f'\n{live_secret_word}\n YOU WON!!!')
    else:
        print(f'{print_hangman(num_of_fails)}\nGAME OVER')
