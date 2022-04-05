# 3.5.2
# the_word = input('Please enter a word: ')
# print('_ ' * len(the_word))
#
#
# letter = input("Guess a letter:")
#
# if (len(letter) != 1) and not letter.isalpha() :
#     print('E3')
# elif len(letter) != 1:
#     print('E1')
# elif not letter.isalpha():
#     print('E2')
# else:
#     print(letter.lower())
#
# def is_valid_input(letter_guessed):
#     """checks if a parameter is a single english letter
#      :param letter_guessed: the argument to check
#       :type letter_guessed: all
#       :return: true if a single english letter, false if anything else
#       :rtype: bool"""
#     if (len(letter_guessed) != 1) or not letter_guessed.isalpha():
#         return False
#     else:
#         return True
#
# def check_valid_input(letter_guessed, old_letters_guessed):
#     """checks if 'letter_guessed' is a single english letter that hasn't been guessed already
#          :param letter_guessed: the argument to check
#          :param param old_letters_guessed: a list of old guesses
#           :type letter_guessed: all
#           :type old_letters_guessed: list
#           :return: true if a single english letter that is not in old_letters_guessed, false if anything else
#           :rtype: bool"""
#     if (len(letter_guessed) != 1) or not letter_guessed.isalpha():
#         return False
#     if letter_guessed.lower() in old_letters_guessed:
#         return False
#     else:
#         return True
#
# def try_update_letter_guessed(letter_guessed, old_letters_guessed):
#     """ adds letter_guest to to old_letters_guessed only if letter_guest valid
#      :param letter_guessed: the argument to check
#      :param param old_letters_guessed: a list of old guesses
#       :type letter_guessed: all
#       :type old_letters_guessed: list
#       :return: True if letter added to list, 'X'\n old_letters_list\n false
#       :rtype: bool"""
#     if check_valid_input(letter_guessed, old_letters_guessed):
#         old_letters_guessed.append(letter_guessed.lower())
#         return True
#     else:
#         print('X')
#         old_sorted = sorted(old_letters_guessed)
#         print(' -> '.join(old_sorted))
#         return False
#
# def show_hidden_word(secret_word, old_letters_guessed):
#     guessed_str = ''
#     for i, l in enumerate(secret_word):
#         if secret_word[i] in old_letters_guessed:
#             guessed_str = guessed_str + secret_word[i]
#         else:
#             guessed_str = guessed_str + '_ '
#     return guessed_str
#
#
# def check_win(secret_word, old_letters_guessed):
#     secret_word_list = []
#     for i in secret_word:
#         secret_word_list.append(i)
#     for i in secret_word_list:
#         if i not in old_letters_guessed:
#             return False
#     return True
#
# 8.4.1
# def print_hangman(num_of_failes):
#     print(HANGMAN_PHOTOS[num_of_failes])
#
# 9.4.1
# def choose_word(file_path, index):
#     file_text = open(file_path, 'r')
#     words = file_text.read()
#     file_text.close()
#     words = words.replace('\n', ' ')
#     words = words.split(' ')
#     print(words)
#     while index > len(words):
#         index -= len(words)
#     chosen = index - 1
#     return len(set(words)), words[chosen]
#
#
# pl_file = r'C:\Users\idand\Desktop\New Text Document.txt'
# # print(choose_word(pl_file, 100))
# choose_word(pl_file, 60)
# #
# ==========another practice=============
# practice 3.4.2
# a = "ddar astronaut. pldase, stop drasing md!"
# print(a[0] + a[1:].replace(a[0], "e"))
#
# 4.2.2
# pal = input("enter somthing: ").lower()
# pal = pal.replace(' ','')
# print(pal)
# if pal == pal[::-1]:
#     print("ok")
# else:
#     print("NOT")
#
# 4.2.3
# temp = input('enter the temp to convert: ')
# cels = ['c', 'C']
# farn = ['F', 'f']
# if temp[-1] in cels:
#     print(((9 * float(temp[:-1]) + 32 * 5) / 5), 'F')
# elif temp[-1] in farn:
#     print(((5 * float(temp[:-1]) - 160) / 9), 'C')
# else:
#     print('not a temperature')
#
# 4.2.4
# import calendar
# from calendar import weekday
# date = input('enter a date: ')
# a = (weekday(int(date[-4:]), int(date[3:5]), int(date[0:2])))
# print(a)
# day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
# print(day_names[a])
#
# 5.3.4
# def last_early(my_str):
#     my_strl = my_str.lower()
#     if my_strl.find(my_strl[-1], 0, -1) >= 0:
#         return True
#     else:
#         return False
#
#
# print(last_early('x'))
#
# 5.3.5
# def distance(num1, num2, num3):
#     if (abs(num2 - num1) == 1) or (abs(num3 - num1) == 1):
#         print('close')
#         if (abs(num2 - num1) >= 2) or (abs(num3 - num1) >= 2) and (abs(num3 - num2) >= 2):
#             print('far')
#             return True
#         else:
#             print('not far')
#             return False
#     else:
#         print('not close')
#         return False
#
#
# print(distance(-1, -2, -3))
#
# 5.3.6
# def fix_age(age):
#     if (13 <= age <= 14) or (17 <= age <= 19):
#         age = 0
#     return age
#
#
# def filter_teens(a=13, b=13, c=13):
#     a = fix_age(a)
#     b = fix_age(b)
#     c = fix_age(c)
#     return a + b + c
#
#
# print(filter_teens(2, 1.5, 15))
#
# 5.3.7
# def chocolate_maker(small, big, x):
#     if small >= x:
#         return True, 1
#     if small + (big * 5) < x:
#         return False, 1
#     if big * 5 >= x:
#         if x % 5 == 0:
#             return True, 2
#         elif ((x // 5) * 5 + small) >= x:
#             return True
#         else:
#             return False
#     else:
#         return True
#
#
# print(chocolate_maker(3, 2, 10))
#
# 6.1.2
# def shift_left(my_list):
#     my_list.append(my_list[0])
#     my_list.pop(0)
#     return my_list
# ls = [0, 1, 2]
# print(shift_left(ls))
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7]
# list3 = list1 + list2
# list4 = [list1 + list2]
# print(list3)
# print(list4)
#
# 6.2.3
# my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
# my_list_new = (my_list[:-1:2] + [str('and ' + my_list[-1])])
# print(",".join(my_list_new))
#
# 6.2.4
# ??????????
#
# 6.3.1
#
# list1 = [0.6, 1, 2, 3]
# list2 = [3, 2, 0.6, 1]
# list3 = [9, 0, 5, 10.5]
#
#
# def are_lists_equal(ls1, ls2):
#     return ls1.sort() == ls2.sort()
#
#
# print(are_lists_equal(list1, list2))
# print(list1)
#
# 6.3.2
# list1 = ["111", "234", "2000", "goru", "birthday", "09"]
#
#
# def longest(my_list):
#     a = sorted(my_list, key=len)
#     return a[-1]
#
#
# print(longest(list1))
#
# i = 11
# while i > 0:
#     i -= 1
#     if i == 5:
#         continue
#     print(i)
#
# 7.1.4
#
# def squared_numbers(start, stop):
#     raised = []
#     while start <= stop:
#         raised += [start ** 2]
#         start += 1
#     return raised
#
#
# print(squared_numbers(-3, 3))
#
# 7.2.1
# def is_greater(my_list, n):
#     bigger_num_list = []
#     for i in my_list:
#         if i > n:
#             bigger_num_list += [i]
#     return bigger_num_list
#
#
# print(is_greater([1, 30, 25, 60, 27, 28], 28))
#
# 7.2.2
# def numbers_letters_count(my_str):
#     digits = 0
#     not_digits = 0
#     for char in my_str:
#         if char.isdigit():
#             digits += 1
#         else:
#             not_digits += 1
#     return list((digits, not_digits))
#
#
# print(numbers_letters_count("Python 3.6.3"))
# for num in range(-9, 1, 3):
#     print(num)
#
# 7.2.4
# def seven_boom(end_number):
#     boom_list = []
#     for num in range(end_number + 1):
#         if (num % 7 == 0) or ('7' in str(num)):
#             boom_list += ['boom']
#         else:
#             boom_list += [num]
#     return boom_list
#
#
# print(seven_boom(17))
#
# 7.2.5
# def sequence_del(my_str):
# my_str.split()
# def sequence_del(my_str):
#     new_string = ''
#     for (i, letter) in enumerate(my_str):
#         if letter != my_str[(i - 1)]:
#             new_string += letter
#     return new_string
#
#
# print(sequence_del("Heeyyy   yyouuuu!!!"))
#
# 7.2.6
#
# if __name__ == '__main__':
#     shopping_list = input('insert your shopping list: ')
#     list_shopping_list = shopping_list.split(',')
#     while True:
#         prog_type = int(input('what would you like to do? (1-9): '))
#         if prog_type == 1 :
#             print(list_shopping_list)
#         elif prog_type == 2:
#             print(len(list_shopping_list))
#         elif prog_type == 3:
#             product_to_check = input('enter product you like to check if in list: ')
#             if product_to_check in list_shopping_list:
#                 print(product_to_check, 'is in shopping list')
#             else:
#                 print(product_to_check, 'is not in shopping list')
#         elif prog_type == 4:
#             product_to_check = input('enter product you like to count in list: ')
#             print(list_shopping_list.count(product_to_check))
#         elif prog_type == 5:
#             product_to_delete = input('enter product you like to delete from list: ')
#             list_shopping_list.remove(product_to_delete)
#         elif prog_type == 6:
#             product_to_add = input('enter product you like adding to list: ')
#             list_shopping_list.append(product_to_add)
#         elif prog_type == 7:
#             for i in list_shopping_list:
#                 if (len(i) < 3) or (not i.isalpha()):
#                     print(i)
#         elif prog_type == 8:
#             list_shopping_list = list(set(list_shopping_list))
#         elif prog_type == 9:
#             exit()
#
# 7.2.7
# def arrow(my_char, max_length):
#     for i in range(max_length):
#         print((my_char + ' ') * (i + 1))
#     for i in range(max_length):
#         print((my_char + ' ') * (max_length - (i + 1)))
#
#
# arrow('%', 10)
#
# # nowa
# list_1 = [1, 2, 3, 4, 5]
# list_2 = [5, 4, 3, 2, 1]
# # part a check if the list are same length
# if len(list_1) != len(list_2):
#     print('list are not the same length')
# else:
#     largest_value_list = []
#     for i in range(len(list_1)):
#         if list_1[i] > list_2[i]:
#             largest_value_list += [list_1[i]]
#         else:
#             largest_value_list += [list_2[i]]
#     print(largest_value_list)
#
#
# 8.2.1
# data = ('silf', 'py', 1.543)
# format_string = 'hello'
#
# print(f'{format_string} {data[0]}.{data[1]} learner, you have only {data[2]} units left befor you master the course!')
#
# 8.2.2
# def sort_prices(list_of_tuples):
#     sorted_list = sorted(list_of_tuples, key=lambda tup: float(tup[1]), reverse=True)
#     return sorted_list
#
#
# products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
# print(sort_prices(products))
#
# 8.2.3
# def mult_tuple(tuple1, tuple2):
#     tuple_options = []
#     for item in tuple1:
#         for item1 in tuple2:
#             tuple_options.append(tuple([item, item1]))
#     for item in tuple2:
#         for item1 in tuple1:
#             tuple_options.append(tuple([item, item1]))
#     return tuple(tuple_options)
#
#
# first_tuple = (1, 2, 3)
# second_tuple = (4, 5, 6)
# print(mult_tuple(first_tuple, second_tuple))
#
# 8.2.4
# def sort_anagrams(list_of_strings):
#     sorted_letters_strings = []
#     for index, word in enumerate(list_of_strings):
#         word1 = list(word)
#         word1.sort()
#         word2 = ''.join(word1)
#         sorted_letters_strings.append((word2, index))
#
#     print(sorted_letters_strings)
#
#
# list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
# 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
# sort_anagrams(list_of_words)
#
# 8.3.3
# def count_chars(my_str):
#     char_count_dict = {}
#     for letter in my_str:
#         if not letter.isalpha():
#             continue
#         elif letter in char_count_dict:
#             char_count_dict[letter] += 1
#         else:
#             char_count_dict[letter] = 1
#     return char_count_dict
#
#
# magic_str = "abra cadabra"
# print(count_chars(magic_str))
#
#
# 9.1.2
# C:\Users\idand\Desktop\New Text Document.txt
# text = open(input('which file to open?: '), 'r')
# prog = input('type "last/ rev/ sort": ')
# if prog == 'sort':
#     text_list = text.read()
#     text.close()
#     text_list = text_list.split(" ")
#     unique = set(text_list)
#     text_list = list(unique)
#     text_list.sort()
#     print(text_list)
#
# 9.3.1
# def my_mp3_playlist(file):
#     text = open(file, 'r')
#     playlist = text.read()
#     text.close()
#     playlist = playlist.split('\n')
#     list_pl_ls = []
#     for string in playlist:
#         string = string.split(';')
#         list_pl_ls.append(string)
#     playlist_dict = {}
#     for song in list_pl_ls:
#         playlist_dict[song[0]] = song[1:3]
#     print(playlist_dict)
#     return len(playlist_dict)
#
#
# pl_file = r'C:\Users\idand\Desktop\New Text Document.txt'
# print(my_mp3_playlist(pl_file))
