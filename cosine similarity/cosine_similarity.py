from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import pandas as pd
from scipy import spatial
from nltk.stem import LancasterStemmer

stop_words = set(stopwords.words('english'))
lancaster = LancasterStemmer()

#loop to get all the files in the directory and make a lixst of all the text
current_directory = os.getcwd()
file_directory = os.listdir(current_directory)
document_list = {}
for doc in file_directory:
        if ".txt" in doc:
                document_list[doc]= None

#making a dictionary with the document name as the key and all the word with the stopwords removed as the value and parallely making the same for stemmed words also 
stemmed_doc_list = {}
make_dataframe = {}
make_dataframe['document'] = list(document_list.keys())
all_words = list()
stemmed_words = list()
for document in make_dataframe['document']:
        document_path = os.getcwd()+"\\"+document
        opened_file = open(document_path,'r').read()
        document_list[document] = [word for word in word_tokenize(opened_file.lower()) if word not in stop_words]
        stemmed_doc_list[document] = [lancaster.stem(word) for word in document_list[document]]
        stemmed_words = stemmed_words + stemmed_doc_list[document]
        all_words = all_words + document_list[document]

all_words = set(all_words)
stemmed_words = set(stemmed_words)
#making a dictionary with word count in each document to make a dataframe
for word in all_words:
        make_dataframe[word] = []
        for document in make_dataframe['document']:
            make_dataframe[word].append(document_list[document].count(word))

stemmed_dataframe = {}
stemmed_dataframe['document'] = list(document_list.keys())

#making a dictionary with word count in each document for all the stemmed words
for document in stemmed_dataframe['document']:
        stemmed_dataframe[document] = []
        for word in stemmed_words:
            stemmed_dataframe[document].append(stemmed_doc_list[document].count(word))

    
dataframe = pd.DataFrame(make_dataframe)
var = dataframe.values
document_dictionary = dict()

for row in var:
    row = list(row)
    document_dictionary[row[0]] = row[1:]

# function to find the cosine similarity 
def cosine_similarity(doc1, doc2):
    return 1 - spatial.distance.cosine(doc1, doc2)

doc_cosine_similarities = dict()
doc_cosine_stemmed_similarities = dict()

# making dictionaries for two dataframes, one for holding all the cosine similarities of non stemmed documents
# and another for all the stemmed documents
doc_cosine_similarities['Name'] = make_dataframe['document']
doc_cosine_stemmed_similarities['Name'] = make_dataframe['document']

for doc1 in make_dataframe['document']:
    doc_cosine_similarities[doc1] = []
    doc_cosine_stemmed_similarities[doc1] = []
    for doc2 in make_dataframe['document']:
        doc_cosine_similarities[doc1].append(cosine_similarity(document_dictionary[doc1], document_dictionary[doc2]))
        doc_cosine_stemmed_similarities[doc1].append(cosine_similarity(stemmed_dataframe[doc1], stemmed_dataframe[doc2]))

doc_cosine_similarities = pd.DataFrame(doc_cosine_similarities)
doc_cosine_stemmed_similarities = pd.DataFrame(doc_cosine_stemmed_similarities)
print(doc_cosine_similarities)
print(doc_cosine_stemmed_similarities)


doc1 = input("Enter document 1 name:")
doc2 = input("Enter document 2 name:")

print("Cosine Similarity of non stemmed documents: ",cosine_similarity(document_dictionary[doc1], document_dictionary[doc2]))
print("Cosine Similarity of stemmed documents: ",cosine_similarity(stemmed_dataframe[doc1], stemmed_dataframe[doc2]))