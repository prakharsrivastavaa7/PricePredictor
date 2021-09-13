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

The landing page of the website takes user inputs for the various parameters as shown below-

![image](https://user-images.githubusercontent.com/63156822/133137229-6dc0847b-ce12-4489-b75f-f81af027e708.png)

![image](https://user-images.githubusercontent.com/63156822/133137239-a6e53018-508c-40c0-a606-d70ddbfd3d7e.png)


There are various parameters for which the user will select from the drop down menu.

![image](https://user-images.githubusercontent.com/63156822/133137578-9fe9dba0-cd31-4c1e-b1d2-ecb589f93376.png) ![image](https://user-images.githubusercontent.com/63156822/133137605-00c9f085-abfa-47dd-83f3-8d809803b841.png)


After clicking on price predict the output price will be shown as follows:

![image](https://user-images.githubusercontent.com/63156822/133137468-769639a1-b4d8-4e99-9caa-c05de385770a.png)




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
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 

## Future Scope

* Use multiple Algorithms
* Optimize Flask app.py
* Imporve Front-End 
