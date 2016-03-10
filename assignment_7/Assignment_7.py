#Kyle O'Connor kyjoconn@ucsc.edu CMPE 5P assignment 7
import math
import string
import sys
from collections import Counter
import operator

def process_document():
    ''' this function calls the config.txt file and returns
        a dict of dicts for each book in config.txt '''
    corpus_word_count = dict()
    #open config file
    individual_book = [book.strip() for book in open(sys.argv[1])]
    #read through each book in config file
    for book in individual_book:
        word_count = dict()
        # normalize text and collect word counts for each book
        for line in open(book, 'r'):
            line = line.lower()
            for mark in string.punctuation:
                if mark in line:
                    line = line.replace(mark, '')
            line = line.split()
            for word in line:
                if word not in word_count:
                    word_count[word] = 1
                if word in word_count:
                    word_count[word] += 1
        corpus_word_count[book] = word_count
    return corpus_word_count

def tf_idf():
    '''this uses process_document() to get corpus dictionary
        and then converts and returns tf-idf values '''
    corpus_word_tf_idf = process_document()
    word_count = Counter()
    for word in corpus_word_tf_idf.values():
        word_count.update(list(word))
    for book in corpus_word_tf_idf:
        # formula for tf-idf from assignment
        for word in corpus_word_tf_idf[book]:
            count = word_count[word]
            corpus_word_tf_idf[book][word] *= math.log(3 / count + 1)
    return corpus_word_tf_idf

def process_user(user_input):
    ''' same thing as tf_idf() except for user input, not a dictionary of dictionaries '''
    corpus_word_tf_idf = process_document()
    word_count = Counter()
    for word in corpus_word_tf_idf.values():
        word_count.update(list(word))
    user_dict = {}
    for mark in string.punctuation:
        if mark in user_input:
            user_input = user_input.replace(mark, '')
    user_input = user_input.split()
    for word in user_input:
        if word not in user_dict:
            user_dict[word] = 1
        if word in user_dict:
            user_dict[word] += 1
        if word not in word_count:
            count = 0.0
        count = word_count[word]
        user_dict[word] *= math.log(float(3) / float(count + 1))
    return user_dict

def vector_length_corpus(tf_idf_values_dict):
    ''' finds length of each book in the corpus dictionary and
        returns dictionary with lengths of each book '''
    length = 0
    length_dict = {}
    # vector length formula from assignment
    for book in tf_idf_values_dict:
        for word in tf_idf_values_dict[book]:
            tf_idf_values_dict[book][word] **= 2
    for book in tf_idf_values_dict:
        length_dict[book] = 1
        for word in tf_idf_values_dict[book]:
            length += tf_idf_values_dict[book][word]
        length_dict[book] *= round(math.sqrt(length), 2)
    return length_dict

def vector_length_user(tf_idf_user):
    '''
        finds length of the user input '''
    length = 0
    for word in tf_idf_user:
        tf_idf_user[word] **= 2
        length += tf_idf_user[word]
    length = round(math.sqrt(length), 2)
    return length

def compare_docs():
    ''' compares user input to each book in corpus and returns list of similarity values '''
    doc_1 = process_user(user_input)
    doc_2 = tf_idf()
    doc_2_length_dict = vector_length_corpus(tf_idf())
    dot_dict = {}
    dot_sum = 0
    # compute and store dot product for user input with each book in corpus
    for book in doc_2:
        dot_dict[book] = 1
        for word in doc_1:
            if word not in doc_2[book]:
                doc_2[book][word] = 0
            dot = doc_1[word] * doc_2[book][word]
            dot_sum += dot
        dot_dict[book] *= dot_sum
        dot_dict[book] /= vector_length_user(doc_1) * doc_2_length_dict[book]
    return sorted(dot_dict.iteritems(), key=operator.itemgetter(1), reverse=True)

if __name__ == "__main__":
    user_input = raw_input('Please enter searchable text: ')
    dot_dict = compare_docs()
    print 'Here are documents similar to your search (most similar first)'
    print dot_dict








