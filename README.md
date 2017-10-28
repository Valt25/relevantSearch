# Instalation

To install this solution, you must have python 3+, virtualenv for python 3+  tools installed.

At first you need to clone this repository with command: `git clone https://github.com/Valt25/googleSearch.git`

Then go in appeared folder. `cd googleSearch`

Now you have to create virtual environment: `virtualenv venv`

Then activate venv: `source venv/bin/activate`

Now you have to install 3-rd party libraries: `pip install -r requirements.txt`

And now you are ready to work. Of course all scripts in folder with project must have permissions to execute script and read specified files(look further).


# Working

The main file is manage.py. To run it: `python manage.py`

It requires to specify working mode and other parameters.

The first mode is creating index from document set, you can do it via create_index argument:

 `python manage.py create_index documents`

The last argument is path to directory with document set, it is optional. By default it is folder `documents` in root project directory.

The second mode is searching. You can run it:

 `python manage.py search query`

Where query is path to file, where search query is located.

# Documents form
Every document that is wanted to be indexed, have to be in specified folder.

Each document is text in next form: 'Document <doc_number> \n doc_content \n ********************************************\n'.

In other words the first line specify document number, the other lines before line with stars is content, it is body for indexer.

Document number should not repeat in 1 document set.

Documents can be distributed over different files, with any distribution. Only limitation is OS and python constraints.

I use given corpus archive for testing and evaluating system. But anyway it can work with bigger collections.


# Query form

Query allow using NOT, OR, AND operations. In query it have to be in form LOGNOT, LOGOR, LOGAND, not to get the same words as OR, NOT, AND in query.

Queries support not-AND notation. So 'digital computing' means 'digital LOGAND computing'. In every place where operator is missing, LOGAND would be appeared

# Design

I use distinct packages for distinct features. Packeage for creating index, and the other one for searching(parsing, processing).

# References

In this solution [NLTK](http://www.nltk.org/) python library was used for NLP issues. Because i did not think, that I am expected to write own stemmers, lemmatizers, tokeniers.

Also I have copied and modified code from next [github repository](https://github.com/spyrant/boolean-retrieval-engine)( @github/spyrant ). I used part of this code for parsing boolean retrieval queries.

# Screenshots

![index](https://image.ibb.co/eMOwuF/image.png)

![searching](https://image.ibb.co/f3kLMv/image.png)

![query](https://image.ibb.co/fp5RuF/image.png)
