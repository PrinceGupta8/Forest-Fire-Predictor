from flask import Flask,render_template,url_for,request,jsonify
import pickle
from sklearn.preprocessing import StandardScaler


app=Flask(__name__)
model=pickle.load(open('data.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
    return 'Welcome to AI world'
@app.route('/form',methods=['GET','POST'])
def form():
    try:
        if request.method=='POST':
            temperature=float(request.form.get('Temperature'))
            rh=float(request.form.get('RH'))
            ws=float(request.form.get('Ws'))
            rain=float(request.form.get('Rain'))
            FFMC=float(request.form.get('FFMC'))
            dmc=float(request.form.get('DMC'))
            dc=float(request.form.get('DC'))
            isi=float(request.form.get('ISI'))
            bui=float(request.form.get('BUI'))
            classes=float(request.form.get('Classes'))
            region=float(request.form.get('Region'))

            data_scaled=scaler.transform([[temperature,rh,ws,rain,FFMC,dmc,dc,isi,bui,classes,region]])
            result=model.predict(data_scaled)
            if not all ([temperature,rh,ws,rain,FFMC,dmc,dc,isi,bui,classes,region]):
                print('All feilds are required!')

            return (f'The value of FWI: {result[0].round(2)}')
        
        return render_template ('data.html')
    except Exception as e:
        print(e)
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")