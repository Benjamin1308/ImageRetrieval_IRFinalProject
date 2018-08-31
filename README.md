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
- TF/IF, vector ...
- Flask & Flask_RESTful to create a simple RESTful API with Python
- React for a simple UI

  
      We also tried to deploy the API and the React app on remote hosts, but there was timeout error (Heroku timeout limit) due to the Object Recognition API.
      
      React app can be found here: 
      The API can be found here: https://image-retrieval-api.herokuapp.com/images/