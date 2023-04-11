import pickle
from flask import Flask, request, render_template
import numpy as np





app = Flask("__name__")

filename = 'heartattackprediction.pkl'
loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
q = ""

@app.route("/")
def loadPage():
    return render_template('sample.html', query="") 

@app.route("/", methods=['POST'])
def HeartattackPrediction():
    
          
    
    query2 = request.form['gender']
    query3 = request.form['cp']
   
    query8 = request.form['thalachh']
    query9 = request.form['exng']
    query10 = request.form['oldpeak']
   
    query12 = request.form['caa']
    query13 = request.form['thall']

    data=(query2,query3,query8,query9,query10,query12,query13)
    
    
    
    inputdata=np.asarray(data)
  
    newinput=inputdata.reshape(1,-1)

    prediction=loaded_model.predict(newinput)
    
    if(prediction[0]==0):
        output = "The patient is not diagnosed with Heart disease"
              
    else:
        output = "The patient is diagnosed with Heart disease"
              

    return render_template('sample.html', 
           output1=output, 
          
           query2 = request.form['gender'],
           query3 = request.form['cp'],
           
           query8 = request.form['thalachh'],
           query9 = request.form['exng'],
           query10 = request.form['oldpeak'],
          
           query12 = request.form['caa'],
           query13 = request.form['thall'])

if __name__ == '__main__':
    app.run()
