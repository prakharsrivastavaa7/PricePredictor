# AirBnB Price Prediction: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [About](#About)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Technologies Used](#technologies-used)
  * [Future scope of project](#future-scope)


## Demo
Link: https://airbnbpriceprediction.herokuapp.com/


## Overview
This is a Flask web app which predicts the price of an AirBnB.

  ### Input Screenshots      

The landing page of the website takes user inputs for the various parameters as shown below-

![image](https://user-images.githubusercontent.com/63156822/133137229-6dc0847b-ce12-4489-b75f-f81af027e708.png)

![image](https://user-images.githubusercontent.com/63156822/133137239-a6e53018-508c-40c0-a606-d70ddbfd3d7e.png)


There are various parameters for which the user will select from the drop down menu.

![image](https://user-images.githubusercontent.com/63156822/133137578-9fe9dba0-cd31-4c1e-b1d2-ecb589f93376.png) ![image](https://user-images.githubusercontent.com/63156822/133137920-5e02f787-9c79-45d7-8792-6720f20c839a.png)

   ### Output Screenshots

After clicking on price predict the output price will be shown as follows:

![image](https://user-images.githubusercontent.com/63156822/133137468-769639a1-b4d8-4e99-9caa-c05de385770a.png)

In this way based on the user input and selection for the various parameters mentioned above we are able to predict the price of the Airbnb and the website redirects to main page where price is displayed. The navbar on top is responsive and will redirect to the index page to give new inputs.
The price is displayed on a separate page and on clicking the responsive nav-bar Price Predictor at the top we can go back to the main page to give new inputs

  ### Flowchart

There are two main components of the project - Machine Learning based Model Fitting and Web Deployment Using Flask.
For model training the data is loaded and reduced in size to ensure proper deployment of herkou app. The data is preprocessed and unneccessary items are dropped from the data following which model training is done. We use XGB and RandomForestRegressor to traain the dataset. Hyperparameter tuning is also used in case of RandomForestRegressor to get the best parameters. Based on the R2 value obtained from both the models we select RandomForestRegressor model for fitting. The model is then saved using pickle to deploy it on heroku. 

![image](https://user-images.githubusercontent.com/63156822/133221564-39c8fb23-09bc-4240-8916-ac865184e009.png)

After website is deployed using heroku the user can access it from the link. The user will input the various parameters required for calculating the price and based on the inputs the model will predict the price and display it.

![image](https://user-images.githubusercontent.com/63156822/133221441-dfdefdd6-c3f2-43fb-b631-3a93ad47bd9a.png)


## About
The project has been designed as part of the evaluation scheme of my college course UCS757 - Building Innovative Systems. This project involves the use of Machine Learning to predict the price of an AirBnb based on the user inputs.The dataset used was https://www.kaggle.com/stevezhenghp/airbnb-price-prediction. The data is preprocessed, visualised and then fitted on two models. The RandomForestRegressor is pickled to predict the price since it gave better results. In thisw way the project has been created using the various concepts taught to us in our course curriculum.

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── templates
│   ├── index.html
│   ├── main.html	
├── README.md
├── app.py
├── AirBnB_Predictor.ipynb		
├── file.pkl
├── Procfile
├── requirements.txt
├── Novelty.pdf
├── Flowchart_DS.pdf
├── I_O_Screenshots_DS.pdf
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 

## Future Scope

* Use multiple Algorithms
* Optimize Flask app.py
* Imporve Front-End 
