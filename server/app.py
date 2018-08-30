# from flask import Flask, Response, request
# from flask_cors import CORS, cross_origin
# import requests
# import RetrieveImage

# app = Flask(__name__)
# CORS(app)

# # def some_long_calculation(number):
# #   '''
# #   here will be some long calculation using this number
# #   let's simulate that using sleep for now :)
# #   '''
# #   import time
# #   time.sleep(5)

# #   return number

# @app.route('/images', methods=['POST'])
# def check():
#     if (request.method == 'POST'):
#       request.get_data()
#       base64 = request.json['base64']
#       def generate():
#           yield ''   # notice that we are yielding something as soon as possible
#           with app.test_request_context():
#             yield RetrieveImage.retrieveImage(base64)
#       return Response(generate(), mimetype='text/html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from RetrieveImage import retrieveImage

app = Flask(__name__)
CORS(app)
api = Api(app)

class ImageList(Resource):
    def post(self):
      parser = reqparse.RequestParser()
      parser.add_argument("base64")
      args = parser.parse_args()

      images = retrieveImage(str(args["base64"]))
      if len(images) == 0:
        return "No matching result", 200
      return images, 200
      
api.add_resource(ImageList, '/images')

if __name__ == '__main__':
  app.run(debug=True)