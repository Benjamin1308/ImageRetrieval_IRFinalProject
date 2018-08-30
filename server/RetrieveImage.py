import numpy as np
from collections import defaultdict
import math
import json
import base64
import ObjectRecognize

src = 'document.json'
path_input = 'ImageDataset'

#Get the stop word list
file_list = dict()
with open(src, 'r') as json_file:
    json_data = json.load(json_file)
    id = 0;
    for file in json_data:
        file_list.update({id:file['name']})
        id += 1
    json_file.close() 

doc_vector_list = []
with open('doc_vector_list.json', 'r') as json_file:
    doc_vector_list = json.load(json_file)
    json_file.close() 

inverted_index = defaultdict(list)
with open('inverted_index.json', 'r') as json_file:
    inverted_index = json.load(json_file)
    json_file.close() 

################### RELEVANCE CALCULATION METHODS ##############################################

content_list = []

#Read input 
print('Reading dataset')
with open(src, 'r') as json_file:
    json_data = json.load(json_file)
    for file in json_data:
        #Get file content
        content = file['key']
        #List store file content
        content_list.append(content)  
    json_file.close()
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
#Angle
def dot_product(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))

def length(v):
    return math.sqrt(dot_product(v, v))

def angle(v1, v2):
    if(length(v1) != 0 and length(v2) != 0):
        return dot_product(v1, v2) / (length(v1) * length(v2))
    else:
        return -1
#Search
def retrieveImage(_base64):
    #Query vector
    # print('Input query: ')
    # query = input()
    # query = preprocess(query)
    query = ObjectRecognize.get_keyword(_base64)
    query_vector = tf_idf(query, inverted_index.keys())
    returnImg = []
    result = dict()
    for i in range(len(doc_vector_list)):
        result.update({i:angle(doc_vector_list[i], query_vector)})
    # print(result)
    result_sorted = sorted(result.items(),key=lambda tup: tup[1], reverse = True)
    # print(result_sorted)
    #Print top 10 result
    for i in range(10):
        url = 'https://res.cloudinary.com/doq4th6f3/image/upload/v1535467892/ImageRetrieve/' + file_list[result_sorted[i][0]]
        returnImg.append(url)
    return returnImg