import json
import re
import argparse
from DictionaryParser import get_indivisual_dictionary, start_cutting


parser = argparse.ArgumentParser()
parser.add_argument("Name")
args = parser.parse_args()
print args


def search_func(f_word, length):
    length += 1
    with open('Dictionary/json_dumps_sorted/group ' + str(length) + '.txt', 'r') as f:

        temp_data = f.read()
        dictionary = json.loads(temp_data)

    my_word = get_indivisual_dictionary(f_word)
    for x, y in dictionary.iteritems():

        if set(my_word.items()).difference(set(y.items())) == set([]):
            print x
    return dictionary


def solve(word):
    # Main Method of this App, Pass The word and get the anagrams
    f_word = re.sub('[\s+]', '', word)
    results = search_func(f_word, len(f_word))
    # for result in results:
    #     print result


# To be run First, For it Creates individual group of Words divided according to their length, then only make a json
# out of them
def create_sorted_words():
    start_cutting('Words/words.txt')
    start_cutting('Words/words2.txt')
    start_cutting('Words/words3.txt')


solve('assessment')
