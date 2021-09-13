from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('file.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        property_type = request.form["property_type"] 
        if(property_type=='1'):
            property_type=1
        elif(property_type=='2'):
            property_type=2
        elif(property_type=='3'):
            property_type=3
        elif(property_type=='4'):
            property_type=4
        elif(property_type=='5'):
            property_type=5
        elif(property_type=='6'):
            property_type=6
        elif(property_type=='7'):
            property_type=7
        elif(property_type=='8'):
            property_type=8
        elif(property_type=='9'):
            property_type=9
        elif(property_type=='10'):
            property_type=10
        elif(property_type=='11'):
            property_type=11
        elif(property_type=='12'):
            property_type=12
        elif(property_type=='13'):
            property_type=13
        elif(property_type=='14'):
            property_type=14
        elif(property_type=='15'):
            property_type=15
        elif(property_type=='16'):
            property_type=16
        elif(property_type=='17'):
            property_type=17
        elif(property_type=='18'):
            property_type=18
        elif(property_type=='19'):
            property_type=19
        elif(property_type=='20'):
            property_type=20
        elif(property_type=='21'):
            property_type=21
        elif(property_type=='22'):
            property_type=22
        elif(property_type=='23'):
            property_type=23
        elif(property_type=='24'):
            property_type=24
        elif(property_type=='25'):
            property_type=25
        elif(property_type=='26'):
            property_type=26
        elif(property_type=='27'):
            property_type=27
        elif(property_type=='28'):
            property_type=28
        elif(property_type=='29'):
            property_type=29
        elif(property_type=='30'):
            property_type=30
        elif(property_type=='31'):
            property_type=31    
        elif(property_type=='32'):
            property_type=32
        elif(property_type=='33'):
            property_type=33
        elif(property_type=='34'):
            property_type=34  
        else:
            property_type=0 

        host_response_ratee = int(request.form["host_response_rate"])
        host_response_rate = float(host_response_ratee/100)
        number_of_reviews=int(request.form['number_of_reviews']) 
        review_scores_ratings =int(request.form['review_scores_rating'])
        review_scores_rating = float(review_scores_ratings/100)
        amenities_count=int(request.form['amenities_count'])

        bathrooms =request.form['bathrooms']
        if(bathrooms=='0.5'):
            bathrooms=0.5
        elif(bathrooms=='1.0'):
            bathrooms=1.0
        elif(bathrooms=='3.0'):
            bathrooms=3.0
        elif(bathrooms=='4.0'):
            bathrooms=4.0
        elif(bathrooms=='5.0'):
            bathrooms=5.0
        elif(bathrooms=='6.0'):
            bathrooms=6.0
        elif(bathrooms=='7.0'):
            bathrooms=7.0
        elif(bathrooms=='8.0'):
            bathrooms=8.0
        elif(bathrooms=='1.5'):
            bathrooms=1.5
        elif(bathrooms=='2.5'):
            bathrooms=2.5
        elif(bathrooms=='3.5'):
            bathrooms=3.5
        elif(bathrooms=='4.5'):
            bathrooms=4.5
        elif(bathrooms=='5.5'):
            bathrooms=5.5
        elif(bathrooms=='6.5'):
            bathrooms=6.5
        elif(bathrooms=='7.5'):
            bathrooms=7.5
        elif(bathrooms=='2.0'):
            bathrooms=2.0
        else:
            bathrooms=0.0 

        
        room_type =request.form['room_type']
        if(room_type=='One'):
            room_type=1
        elif(room_type=='Two'):
            room_type=2
        else:
            room_type=3

        bedrooms =request.form['bedrooms']
        if(bedrooms=='One'):
            bedrooms=1.0
        elif(bedrooms=='Two'):
            bedrooms=2.0
        elif(bedrooms=='Three'):
            bedrooms=3.0
        elif(bedrooms=='Four'):
            bedrooms=4.0
        elif(bedrooms=='Five'):
            bedrooms=5.0
        elif(bedrooms=='Six'):
            bedrooms=6.0
        elif(bedrooms=='Seven'):
            bedrooms=7.0
        elif(bedrooms=='Eight'):
            bedrooms=8.0
        elif(bedrooms=='Nine'):
            bedrooms=9.0
        elif(bedrooms=='Ten'):
            bedrooms=10.0
        else:
            bedrooms=0.0

        beds =request.form['beds']
        if(beds=='One'):
            beds=1.0
        elif(beds=='Two'):
            beds=2.0
        elif(beds=='Three'):
            beds=3.0
        elif(beds=='Four'):
            beds=4.0
        elif(beds=='Five'):
            beds=5.0
        elif(beds=='Six'):
            beds=6.0
        elif(beds=='Seven'):
            beds=7.0
        elif(beds=='Eight'):
            beds=8.0
        elif(beds=='Nine'):
            beds=9.0
        elif(beds=='Ten'):
            beds=10.0
        elif(beds=='Eleven'):
            beds=11.0
        elif(beds=='Twelve'):
            beds=12.0
        elif(beds=='Thirteen'):
            beds=13.0
        elif(beds=='Fourteen'):
            beds=14.0
        elif(beds=='Fiveteen'):
            beds=15.0
        elif(beds=='Sixteen'):
            beds=16.0
        else:
            beds=0.0    

        Source = request.form["Source"]
        if (Source == 'NYC'):
            city_NYC  = 1
            city_Boston = 0
            city_Chicago  = 0
            city_DC  = 0
            city_LA  = 0
            city_SF = 0 
        
        elif (Source == 'LA'):
            city_NYC  = 0
            city_Boston = 0
            city_Chicago  = 0
            city_DC  = 0
            city_LA  = 1
            city_SF = 0 

        elif (Source == 'Boston'):
            city_NYC  = 0
            city_Boston = 1
            city_Chicago  = 0
            city_DC  = 0
            city_LA  = 0
            city_SF = 0 

        elif (Source == 'Chicago'):
            city_NYC  = 0
            city_Boston = 0
            city_Chicago  = 1
            city_DC  = 0
            city_LA  = 0
            city_SF = 0 

        elif (Source == 'DC'):
            city_NYC  = 0
            city_Boston = 0
            city_Chicago  = 0
            city_DC  = 1
            city_LA  = 0
            city_SF = 0 

        else:
            city_NYC  = 0
            city_Boston = 0
            city_Chicago  = 0
            city_DC  = 0
            city_LA  = 0
            city_SF = 1 

        

        accommodates =request.form['accommodates']
        if(accommodates=='One'):
            accommodates=1
        elif(accommodates=='Two'):
            accommodates=2
        elif(accommodates=='Three'):
            accommodates=3
        elif(accommodates=='Four'):
            accommodates=4
        elif(accommodates=='Five'):
            accommodates=5
        elif(accommodates=='Six'):
            accommodates=6
        elif(accommodates=='Seven'):
            accommodates=7
        elif(accommodates=='Eight'):
            accommodates=8
        elif(accommodates=='Nine'):
            accommodates=9
        elif(accommodates=='Ten'):
            accommodates=10
        elif(accommodates=='Eleven'):
            accommodates=11
        elif(accommodates=='Twelve'):
            accommodates=12
        elif(accommodates=='Thirteen'):
            accommodates=13
        elif(accommodates=='Fourteen'):
            accommodates=14
        elif(accommodates=='Fiveteen'):
            accommodates=15
        else:
            accommodates=16

        cancellation_policy=request.form['cancellation_policy'] 
        if(cancellation_policy=='Three'):
            cancellation_policy=3
        elif(cancellation_policy=='Two'):
            cancellation_policy=2
        elif(cancellation_policy=='Four'):
            cancellation_policy=4
        else:
            cancellation_policy=1

        cleaning_fee=request.form['cleaning_fee'] 
        if(cleaning_fee=='One'):
            cleaning_fee=1
        else:
            cleaning_fee=0 

        
        
        host_identity_verified=request.form['host_identity_verified'] 
        if(host_identity_verified=='One'):
            host_identity_verified=1
        else:
            host_identity_verified=0 

        
        values = [[property_type,accommodates,accommodates,bathrooms,cancellation_policy,	cleaning_fee	,host_identity_verified	,host_response_rate	, number_of_reviews, review_scores_rating	,bedrooms	,beds	,city_Boston	,city_Chicago	,city_DC	,city_LA	,city_NYC	,city_SF	,amenities_count]]
      # created a list of all the user inputed values, then using it for prediction
        prediction = model.predict(values)	
        outputt=np.exp(prediction)
        output=np.round(outputt,2)
        return render_template("main.html", pred = "AirBnB price is {} Dollars".format(float(output)))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

