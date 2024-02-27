#now, take input from html file and then give the required output
from flask import Flask, render_template, request
import requests

#now building a flask app
app=Flask(__name__)
#now, at first, I need to showcase the html file to the user
@app.route("/")
def homepage():
    return render_template("index.html")
#now, from above code, at home location i'll be able to get my enter page
#now, user will try to enter the inputs in the intro page
#jab search dabaoge toh link mein /weatherapp add ho jayega
#but since uss route pe kuch nhi h abhi tak isliye kuch execute nhi hoga and error dega
#now adding the route to /weatherapp
@app.route("/weatherapp",methods=["POST","GET"])#dono methods likhne h isme
def get_weatherdata():
    city=request.form.get("city")
    unit=request.form.get("units")
    apikey=request.form.get("appid")
    url="https://api.openweathermap.org/data/2.5/weather"
    param={"q":city,"appid":apikey,"units":unit}
    response=requests.get(url,params=param)
    """data=response.json()
    return data"""
    #iss upar waale se bhi hojaega but json page aayega
    data=response.json()
    return f"data:{data}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5002)

#now deploying this code on the cloud
#in this vscode, things are pre installed but cloud mein aisa nhi hota
#you have to install the libraries in the cloud
#keeping this in mind we have created requirements.txt and we will add all dependencied in it 
#jo bhi install krna h, bulk installation mein requiremnts.txt help krta h
#now move to requirements.txt
    
#came here from requirements
#pushing the code in github 
#create a repository
#now open terminal and usme move to weather_app folder using cd weather_app in terminal
#after this, type ls and jo 3 cheeze h, we need to push these 3 inside my repo
#and now github pe jo code h woh terminal mei likhte jao