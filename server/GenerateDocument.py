import os
import re
import json
import ObjectRecognize
path_input = 'ImageDataset'
def generateDoc():
	print('READING DATASET')
	photos = []
	content_list = []

	for photo in os.listdir(path_input):
	    #Store name and class of a file into dictionary
	    objectArray = ObjectRecognize.obj_detection(path_input+'/'+photo)
	    keyString = ""
	    for obj in objectArray:
	    	keyString += obj["name"] + " "
	    newPhoto = {"name": photo, "key": keyString}
	    photos.append(newPhoto)
	    #Read content of a file
	print(photos)
	with open('./document.json', 'w') as outfile:
	    json.dump(photos, outfile)
	outfile.close()
generateDoc()