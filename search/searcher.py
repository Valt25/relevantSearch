from IndexCreator.Creator import tokenize, normalize, import_index
import string

def proceed_query(query):
    query = query.translate(''.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    tokens = tokenize(query)
    normalized_tokens = normalize(tokens)
    return normalized_tokens

def search(filename):
    f = open(filename)
    search_query = f.read()
    query_as_a_bag = proceed_query(search_query)
    index = import_index()
    result = index.search(query_as_a_bag)
    print(result)