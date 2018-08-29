from flask import Flask, Response, request
import requests
import RetrieveImage

app = Flask(__name__)

# def some_long_calculation(number):
#   '''
#   here will be some long calculation using this number
#   let's simulate that using sleep for now :)
#   '''
#   import time
#   time.sleep(5)

#   return number

@app.route('/images', methods=['POST'])
def check():
    if (request.method == 'POST'):
      request.get_data()
      base64 = request.json['base64']
      def generate():
          yield ""   # notice that we are yielding something as soon as possible
          with app.test_request_context():
            yield str(RetrieveImage.retrieveImage(base64))
      return Response(generate(), mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)