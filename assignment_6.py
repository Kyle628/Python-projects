# Kyle O'Connor kyjoconn@ucsc.edu assignment 6
import operator
import string
from collections import Counter

PUNCT = string.punctuation

def process_book(book_file):
    ''' This function takes a text file, and returns two dictionaries: word_count, letter_count
    '''
    f = open(book_file, 'r')
    word_count = {}
    #normalize text
    for line in f:
        line = line.lower()
        for i in PUNCT:
            line = line.replace(i, '')
        line = line.split()
        #add and count words in the dictionary
        for word in line:
            for i in range(len(line)):
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    f.close()
    #count letter occurrences in text
    with open(book_file) as f:
        text = f.read().lower()
        letter_count = dict((l,text.count(l)) for l in string.ascii_lowercase)
    return word_count, letter_count


def top_thirty(word_count):
    '''This function takes a word_count dictionary and returns a list of tuples representing the 30 most frequently
    used words'''
    dict_as_list = sorted(word_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    top_thirty = dict_as_list[:30]
    return top_thirty

def get_word_frequencies(word_count):
    '''takes a word_count dictionary and returns the top 30 word percentages'''
    total = float(sum(word_count.values())) / 100
    top_30_word_count = top_thirty(word_count)
    top_30_word_count_freq = [(i[0],round(i[1]/total, 2)) for i in top_30_word_count]
    return top_30_word_count_freq

def get_letter_frequencies(letter_count):
    '''takes a letter_count dictionary and returns the letter usage percentages'''
    total = float(sum(letter_count.values())) / 100
    letter_tuples = sorted(letter_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    letter_freq = [(i[0],round(i[1]/total, 2)) for i in letter_tuples]
    return letter_freq

if __name__ == "__main__":
    word_count = process_book('wells.txt')[0]
    letter_count = process_book('wells.txt')[1]
    print 'The 30 most frequent words in War of The Worlds are: {0}'.format(top_thirty(word_count))
    print 'These were the most frequently used letters in book_1: {0}'.format(sorted(letter_count.iteritems(), key=operator.itemgetter(1), reverse=True))
    print ' '
    word_freqs_1 = get_word_frequencies(word_count)
    letter_freqs_1 = get_letter_frequencies(letter_count)
    word_count = process_book('dickens.txt')[0]
    letter_count = process_book('dickens.txt')[1]
    word_freqs_2 = get_word_frequencies(word_count)
    letter_freqs_2 = get_letter_frequencies(letter_count)
    print 'The 30 most frequent words in Great Expectations are: {0}'.format(top_thirty(word_count))
    print 'These were the most frequently used letters in book 2: {0}'.format(sorted(letter_count.iteritems(), key=operator.itemgetter(1), reverse=True))
    print ' '
    word_count = process_book('stevenson.txt')[0]
    letter_count = process_book('stevenson.txt')[1]
    word_freqs_3 = get_word_frequencies(word_count)
    letter_freqs_3 = get_letter_frequencies(letter_count)
    print 'The 30 most frequent words in The Strange Case of Dr. Jekyll and Mr. Hyde are: {0}'.format(top_thirty(word_count))
    print 'These were the most frequently used letters in book_3: {0}'.format(sorted(letter_count.iteritems(), key=operator.itemgetter(1), reverse=True))
    print ' '
    combined = [word_freqs_1, word_freqs_2, word_freqs_3]
    combined_ltr = [letter_freqs_1, letter_freqs_2, letter_freqs_3]
    combined_words = sum(
        (Counter(dict(x)) for x in combined),
        Counter())
    for key in combined_words:
        combined_words[key] /= 3
    combined_letters = sum(
        (Counter(dict(x)) for x in combined_ltr),
        Counter())
    for key in combined_letters:
        combined_letters[key] /= 3
    print 'The 30 most frequently used words from all three books were these: {0}'.format(combined_words)
    print 'The most frequently used letters from all three books were these: {0}'.format(combined_letters)



