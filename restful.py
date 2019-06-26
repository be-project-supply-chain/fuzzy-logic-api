import flask
from flask import request, jsonify
from flask_cors import CORS 
from Fuzz import output
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/neural',methods= ['GET','POST'])
def abc():
    data=request.data
    
    
    experience=(data["experience"])
    timeliness=data["timeliness"]
    support=data["support"]
    interaction=data["interaction"]
    quality=data["quality"]
    trouble=data["trouble"]
    l=output(experience,timeliness,support,interaction,quality,trouble)
    out = l
    # print(out)
    # print(dataDict["location"])
    return out
    

if __name__ == '__main__':
    app.run(debug=True)
