#Introduction

This is upgraded copy of my previous work about boolean search and inverted index.

Here I use vector space model and lnc.ltc weighting scheme.

#Complexity of algorithms

In previous work, it cost much time to index all documents.

In thi work complexity stays nearly the same. But since we might have much less document list, we can expect indexing in a fast way.

Since I don't use any hueristic for avoid computing cosine similarity for all of the documents, the time of processing queries bocomes bigger, but with our document list it is not crucial.

#Different weighting schemas

I use simple tf weighting schema, log-weighted tf, tf-idf. But results didn't change a lot.

#Evaluating of work
I use the 500 first documents from corpus fo documnets we have been provided on Moodle.

At first I try to find documents about the World War The Second(next terms were included:Russia 1941 was involved in a great war).But in corpus my system finds only documents about World War the First, or Russia or something.

Then i realize that given corpus is about libraries(a lot of words librari*). And I changemy query to:'Libraries becomes much better in last 1000 years'

Now I get better results. A lot of given documents says about history or growing of libraries.

So precision is 0.4. I assume that all other documents are irrelevant for query, because it would spend a lot of time to read and claify all of the 500 documents. Since that recall will be 1 for us.

Knowing that f1-score is 0.57

I didn't compute this parameters for previous query, but I expect to get 0 true positive variants, so all of the parameters going to be 0.

#Comparing with previous work

At first I did not understand how to modify my solution to bring ranked system, because i thought that it is different aproaches.But at the end, I change only file representation of index and indexing with searching itself. All the others software design approaches stays the same. But during this work I found out messtakes that slows my solution greatly, and also mistake in design of system. Even I didn't change a lot of functionalities. I change code in different packages. And now it seems that i have changed almost every file.

| Before | After |
|---|---|
|![search_before](https://image.ibb.co/f3kLMv/image.png)|![search_after](https://image.ibb.co/fq3wfm/image.png)|
|![index_before](https://image.ibb.co/eMOwuF/image.png)|![index_after](https://image.ibb.co/mYDCLm/image.png)|
# Instalation

To install this solution, you must have python 3+, virtualenv for python 3+  tools installed.

At first you need to clone this repository with command: `git clone https://github.com/Valt25/relevantSearch.git`

Then go in appeared folder. `cd relevantSearch`

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

Here we use free text queries

# Design

I use distinct packages for distinct features. Package for creating index, and the other one for searching(parsing, processing).

# References

In this solution [NLTK](http://www.nltk.org/) python library was used for NLP issues. Because i did not think, that I am expected to write own stemmers, lemmatizers, tokeniers.

# Screenshots

![query](https://image.ibb.co/hF2Tt6/image.png)
