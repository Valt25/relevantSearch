from InvertedIndex import InvertedIndex
import string
import nltk
from nltk.stem.porter import PorterStemmer
from os import listdir
from os.path import isfile, join


class Document():
    doc_number = -1;
    content = ''

def tokenize(doc):
    return nltk.word_tokenize(doc)

def normalize(tokens):
    result = []
    porter_stemer = PorterStemmer()
    for token in tokens:
        result.append(porter_stemer.stem(token))
    return result


def create_index_form_docs(docs):
    index = InvertedIndex()
    for doc in docs:
        doc.content = doc.content.translate(''.maketrans(string.punctuation, ' '*len(string.punctuation)))
        tokens = tokenize(doc.content)
        normalized_tokens = normalize(tokens)
        index.add_list(normalized_tokens, doc.doc_number)
    return index

def create_index(dirname="./documents"):
    docs = get_docs(dirname)
    index = create_index_form_docs(docs)
    index.sort()
    export_index(index, 'index')


def export_index(index, filename):
    f = open(filename, 'w')
    for token, doc_list in index._tokens.items():
        f.write(token + ':')
        for doc in doc_list:
            f.write(str(doc) + ' ')
        f.write('\n')
    f.close

def get_docs(dirname="./documents"):
    onlyfiles = [f for f in listdir(dirname) if isfile(join(dirname, f))]
    result_docs = []
    for filename in onlyfiles:
        f = open(dirname + '/' + filename)
        new_line = f.readline()
        while new_line != '':
            new_doc = Document()
            new_doc.doc_number = int(new_line[8:13])
            new_line = f.readline()
            while new_line != '********************************************\n':
                new_doc.content += new_line
                new_line = f.readline()
            new_line = f.readline()
            result_docs.append(new_doc)
        f.close()
    return result_docs


def import_index(index_path = 'index'):
    print('Begin importing')
    f = open(index_path, 'r')
    next_line = f.readline()
    index = InvertedIndex()
    while next_line != '':
        current_char = 0
        token = ''
        while next_line[current_char] != ':':
            token += next_line[current_char]
            current_char += 1
        next_line = next_line[current_char+1:len(next_line)-1]
        docs = next_line.split(' ')
        for doc in docs:
            if len(doc) > 0:
                index.add(token, int(doc))
        next_line = f.readline()
    print('Index has been imported')
    return index
