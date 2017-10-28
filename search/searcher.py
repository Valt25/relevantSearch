from search.QueryParser import parse_query
from search.QueryProcess import query_process

def search(filename):
    f = open(filename)
    search_query = f.read()
    queue = parse_query(search_query)
    result = query_process(queue)
    print(result)