from flask import Flask, request, render_template

app = Flask(__name__)
import pickle
import numpy as np
@app.route('/', methods =  ['GET'])
def Index():
    return render_template('index.html') 
@app.route('/index.html', methods =  ['GET'])
def About():
    return render_template('index.html') 
@app.route('/Predictor.html', methods = ['POST', 'GET'])
def predict():
    if request.method == 'POST':
        print(request.form)
        Age = int(request.form.get('Age'))
        Gender=request.form.get('Gender')
        if(Gender=='Male'):
            Gender=1
        else:
            Gender=0
        BMI=request.form.get('BMI')
        NC=request.form.get('NC')
        Type=request.form.get('Type')
        if(Type=='Smoker'):
            Type=1
        else:
            Type=0
        Region=request.form.get('Region')
        if(Region=='NorthEast'):
            Region=0
        elif(Region=='NorthWest'):
            Region=1
        elif(Region=='SouthEast'):
            Region=2
        else:
            Region=3
        with open('gbr.pkl','rb') as f:
            model=pickle.load(f)
            input = np.array([Age,Gender,BMI,NC,Type,Region]).reshape(1,6)
            p=model.predict(input)
            print(p[0])
        return '''
        <html style = "background-image: url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aW5zdXJhbmNlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60'); background-repeat: no-repeat; background-attachment: fixed; background-size: cover;>
        <div style="background-color:powderblue;">
        <h1 style="color:blue; text-align: center">The predicted cost is {}</h1>
        </div>
        <a href="/Predictor.html" style = "background-color: #4CAF50; border: none; color: white; padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px; margin-left:40rem">Predict for another Value</a>
        '''.format(p[0])
    else:
        return render_template('Predictor.html')

@app.route('/Teamdetails.html', methods =  ['GET'])
def Team():
    return render_template('Teamdetails.html')   

@app.route('/LinearRegression.html', methods =  ['GET'])
def LinearRegression():
    return render_template('LinearRegression.html')  

@app.route('/RidgeRegression.html', methods =  ['GET'])
def RidgeRegression():
    return render_template('RidgeRegression.html')  

@app.route('/SVR.html', methods =  ['GET'])
def SVR():
    return render_template('SVR.html')

@app.route('/GB.html', methods =  ['GET'])
def GR():
    return render_template('GB.html')

@app.route('/Models.html', methods =  ['GET'])
def Models():
    return render_template('Models.html')  

@app.route('/References.html', methods =  ['GET'])
def Reference():
    return render_template('References.html')   


if __name__=="__main__":
    app.run(debug=True)
