import numpy as np
from collections import defaultdict
import math
import json

src = 'document.json'

#Get the stop word list
file_list = dict()
with open(src, 'r') as json_file:
    json_data = json.load(json_file)
    id = 0;
    for file in json_data:
        file_list.update({id:file['name']})
        id += 1
    json_file.close()  

################# 2 #####################################################################

#List store all words 
vocabulary  = np.empty(0)
#List store file content 
content_list = []

#Read input 
print('Reading dataset')
with open(src, 'r') as json_file:
    json_data = json.load(json_file)
    for file in json_data:
        #Get file content
        content = file['key']
        #append all words of the doc to the vocabulary
        vocabulary = np.append(vocabulary, content.split())
        #List store file content
        content_list.append(content)  
    json_file.close()
   
#Filter unique words 
vocabulary = np.unique(vocabulary)
#Transform Numpy to Python list for randomization
vocabulary = vocabulary.tolist()

#Get 500 random words from vocabulary
corpus = sorted(vocabulary)
# INVERTED INDEX 
inverted_index = defaultdict(list)
for word in corpus:
    for i in range(len(content_list)):
        if(word in content_list[i]):
            inverted_index[word].append(i)

with open('./inverted_index.json', 'w') as outfile:
    print(inverted_index)
    json.dump(inverted_index, outfile)
    outfile.close()
###################### 3 ##########################################################################


# TF-IDF 

def tf(sentence, term):
    count = 0
    words = sentence.split()

    for word in words:
        if(word == term):
            count += 1
    return count

def idf(term):
    return math.log(len(content_list)/len(inverted_index[term]), 10)

def tf_idf(sentence, term_list):
    vector = []
    for term in term_list:
        vector.append(tf(sentence, term) * idf(term))
    return vector

#Create list of document vector based on tf-idf scoring 
doc_vector_list = []
for content in content_list:
    doc_vector_list.append(tf_idf(content, inverted_index.keys()))
with open('./doc_vector_list.json', 'w') as outfile:
    json.dump(doc_vector_list, outfile)
    outfile.close()

