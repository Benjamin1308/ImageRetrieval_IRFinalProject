from flask import Flask
from flask_restful import Resource, Api, reqparse
from RetrieveImage import retrieveImage

app = Flask(__name__)
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

app.run(debug=True)