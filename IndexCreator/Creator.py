from VectorSpace import VectorSpace
import string
import nltk
from nltk.stem.porter import PorterStemmer
from os import listdir
from os.path import isfile, join

from VectorSpace import Term, Document as VSDocument


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
    index = VectorSpace()
    for doc in docs:
        doc.content = doc.content.translate(''.maketrans(string.punctuation, ' '*len(string.punctuation)))
        tokens = tokenize(doc.content)
        normalized_tokens = normalize(tokens)
        index.add_document(normalized_tokens, doc.doc_number)
    return index

def create_index(dirname="./documents"):
    docs = get_docs(dirname)
    index = create_index_form_docs(docs)
    # index.sort()
    index.compute_tf_idf()
    export_index(index, 'index')


def export_index(index, filename):
    export_terms(filename, index)
    export_docs(filename, index)


def export_terms(filename, index):
    f = open(filename + '_terms', 'w')
    i = 0
    for term in index._terms:
        f.write(term.term + ':' + str(term.document_frequency) + ':' + str(i) + '\n')
        i += 1
    f.close()


def export_docs(filename, index):
    f = open(filename + '_docs', 'w')
    for document in index._documents:
        f.write(str(document.doc_number) + ':')
        for term_id, value in document.terms.items():
            f.write(str(term_id) + ' ' + str(value) + ';')
        f.write('\n')
    f.close()


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
    index = VectorSpace()

    f = open(index_path+'_terms', 'r')
    next_line = f.readline()

    while next_line != '':
        tokens = next_line.split(':')
        term = Term()
        term.term = tokens[0]
        term.document_frequency = int(tokens[1])

        index._terms.append(term)
        next_line = f.readline()

    f.close()


    f = open(index_path + '_docs', 'r')
    next_line = f.readline()

    while next_line != '':
        current_char = 0
        doc_number = ''
        while next_line[current_char] != ':':
            doc_number += next_line[current_char]
            current_char += 1
        next_line = next_line[current_char+1:len(next_line)-1]
        doc_number = int(doc_number)

        terms = next_line.split(';')
        document = VSDocument()
        document.doc_number = doc_number
        document.terms = {}

        for term in terms:
            if term:
                tokens = term.split(' ')
                document.terms[int(tokens[0])] = float(tokens[1])

        index._documents.append(document)
        index.N_docs += 1
        next_line = f.readline()
    print('Index has been imported')
    return index
