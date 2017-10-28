from sys import argv
from IndexCreator.Creator import create_index
from search.searcher import search


arg_num = len(argv)

if (arg_num > 1):
    if argv[1] == 'create_index':
        if arg_num > 2:
            create_index(argv[2])
        create_index()
    elif argv[1] == 'search':
        if arg_num > 2:
            filename = argv[2]
            search(filename)
        else:
            print('Please, specify search query, usign _AND_ , _OR_, _NOT_')
    else:
        print('No such option' + argv[1])