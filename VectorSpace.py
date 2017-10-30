from collections import Counter
import math
import operator

class Term():
    term = ''
    document_frequency = 0

    def __str__(self):
        return self.term + ' ' + str(self.document_frequency)

class Document():
    terms = dict() ## This dictionary contains term as a key and its term frequency in this document as a value
    doc_number = -1

class VectorSpace():
    _terms = [] # This dictionary contains term as a key and its document frequency in this document as a value
    _documents = []
    N_docs = 0


    def add_document(self, document, doc_number):# Document is a bag of words

        new_document_counter = Counter() ## This dictionary contains term as a key and its term frequency in this document as a value

        for new_term in document:
            new_document_counter[new_term] += 1



        for term, tf in new_document_counter.items():
            term_id = self._get_existed_term_id(term)
            if term_id == -1:
                new_term_object = Term()
                new_term_object.term = term
                new_term_object.document_frequency = 1
                self._terms.append(new_term_object)
            else:
                term = self._terms[term_id]
                term.document_frequency += 1

        document = Document()
        document.doc_number = doc_number
        document.terms = {}

        for term, tf in new_document_counter.items():
            term_id = self._get_existed_term_id(term)
            document.terms[term_id] = tf

        self.N_docs += 1
        self._documents.append(document)



    def _get_existed_term_id(self, new_term):
        for i in range(0, len(self._terms)):
            if new_term==self._terms[i].term:
                return i
        return -1

    def compute_tf_idf(self):

        for doc in self._documents:
            for term_id, tf in doc.terms.items():
                term_id = int(term_id)
                df = self._terms[term_id].document_frequency
                doc.terms[term_id] = 1 + math.log(tf)

            vector_length = 0
            for term_id, score in doc.terms.items():
                vector_length += score ** 2
            vector_length = math.sqrt(vector_length)
            for term_id, score in doc.terms.items():
                doc.terms[term_id] = score / vector_length


    def cosine(self, first, second):
        first = self._documents[first]
        second = self._documents[second]

        inner_product = 0

        for i in range(0, len(self._terms)):
            if i in first.terms and i in second.terms:
                inner_product += first.terms[i] * second.terms[i]

        first_length = 0
        for term_id, score in first.terms.items():
            first_length += score**2
        first_length = math.sqrt(first_length)

        second_length = 0
        for term_id, score in second.terms.items():
            second_length += score ** 2
        second_length = math.sqrt(second_length)

        return inner_product/(first_length*second_length)

    def search(self, query):
        query = self._add_query_as_document(query)
        result_relevance = {}
        for i in range(0, len(self._documents)-1):
            result_relevance[self._documents[i].doc_number] = self.cosine(i, len(self._documents)-1)
        result_relevance = sorted(result_relevance.items(), key=operator.itemgetter(1), reverse=True)
        return result_relevance[0:20]



    def _add_query_as_document(self, query):
        new_document_counter = Counter()  ## This dictionary contains term as a key and its term frequency in this document as a value

        for new_term in query:
            new_document_counter[new_term] += 1

        document = Document()
        document.doc_number = -1
        document.terms = {}

        for term, tf in new_document_counter.items():
            term_id = self._get_existed_term_id(term)
            if term_id != -1:
                document_frequency = self._terms[term_id].document_frequency
                document.terms[term_id] = (1+math.log(tf))*math.log((self.N_docs+1)/document_frequency)

        vector_length = 0
        for term_id, score in document.terms.items():
            vector_length += score**2
        vector_length=math.sqrt(vector_length)
        for term_id, score in document.terms.items():
            document.terms[term_id] = score/vector_length

        self.N_docs += 1
        self._documents.append(document)
        return document

        # def sort(self):
    #     for document in self._documents:
    #         document.terms = dict(sorted(document.terms))
