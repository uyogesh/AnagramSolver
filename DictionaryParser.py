import os
import json
import re


def start_cutting(file_path):
    word = 'a'      # So That the first iteration of 'WHILE' loop is possible
    with open(file_path, 'r') as filein:
        while word:
            word = filein.readline()

            # Method Call to create the Sorted word list weighted by length
            make_group(word)


def get_indivisual_dictionary(word):
    # YOu can call this method to create dictionary out of a word, of form
    # {'WORD':{<each letter in the word and their frequency>}}
    dictionary = {}
    n = 0
    for letter in word.lower():
        if dictionary.has_key(letter):
            dictionary[letter] += 1
        else:
            dictionary[letter] = n
    return dictionary


def make_group(word):
    word_length = len(word)

    #  Divide the words to different files according to their length
    file_name = 'Dictionary/Sorted_Words/group ' + str(word_length) + '.txt'
    f = open(file_name, 'a')
    f.write(word)
    f.close()


def make_json_dump():
    files_list = os.listdir('Dictionary/Sorted_Words/')

    word = 'a'
    for file_name in files_list:

        final_dict = {}
        with open('Dictionary/Sorted_Words/'+file_name, 'r') as f:
            while word:
                dictionary = {}
                word = f.readline()

                dictionary[word] = get_indivisual_dictionary(word)
                final_dict.update(dictionary)
        fo = open('Dictionary/json_dumps_sorted/'+file_name, 'a')
        fo.write(json.dumps(final_dict).strip('\n'))
        fo.close()
        word = 'a'



def alphabatize(word):
    for letter in word:

        return word



def Alphabatized_Word_list():
    files_list = os.listdir('Dictionary/Sorted_Words/')

    word = 'a'
    for file_name in files_list:

        final_dict = {}
        with open('Dictionary/Sorted_Words/' + file_name, 'r') as f:
            while word:
                dictionary = {}
                word = f.readline()

                dictionary[word] = get_indivisual_dictionary(word)
                final_dict.update(dictionary)
        fo = open('Dictionary/json_dumps_sorted/' + file_name, 'a')
        fo.write(json.dumps(final_dict).strip('\n'))
        fo.close()
        word = 'a'
