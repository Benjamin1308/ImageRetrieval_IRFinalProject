# Image Retrieval - Information Retrieval Final Project

## Demo

[![Demo](https://i.imgur.com/t7QvKxI.jpg)](https://youtu.be/iG0ulB-qF6w "Demo")

## Screenshots

<p display="block" margin="auto">
    <img src="https://i.imgur.com/0h0pqv4.jpg">
    <img src="https://i.imgur.com/IiXUHGm.jpg">
</p>

## How to Run

- Clone the repo

- Open ```build/index.html``` to run the React app

- Start the Flask server
  - NOTE: **PYTHON 3** is required to run the python app
  
    ```cd server && pip install -r requirements_local.txt```

    ```python app.py```

## Applied Techniques
- TF/IDF, vector ...
    - We use the Object_regcognize api to retrieve information about an image then simply concate the names of its objects to get a keyword string. We apply this technique to a set of 200 images to generate the base corpus to construct inverted index file
    - After that we apply tf_idf to create a vector list for those document.
    - The input image is also converted to query string and respective vector using the technique in 2 steps above. Then we use cosine similarity to identify similar images in the dataset.
- Flask & Flask_RESTful to create a simple RESTful API with Python
- React for a simple UI

  
      We also tried to deploy the API and the React app on remote hosts, but there was timeout error (Heroku timeout limit) due to the Object Recognition API. Because the lack of dataset so we only have a limit number of keywords involved, so querying an image with not-existed yet keyword in corpus will lead to irrelevant results. Hence please use it with caution.
      
      React app can be found here: http://info-retrieval-app.s3-website.ap-south-1.amazonaws.com/
      The API can be found here: https://image-retrieval-api.herokuapp.com/images/
