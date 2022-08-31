
from flask import Flask,render_template,request
from function import house



app=Flask(__name__)

@app.route('/')

def index():
    return render_template('house.html')

@app.route('/predict',methods=['GET','POST'])

def pred():
    if request.method == "POST":
        
        data=request.form
        area_type=int(data['area_type'])
        bath=int(data['bath'])
        balcony=int(data['balcony'])
        size=int(data['size'])
        sqft=float(data['sqft'])
        location=int(data['site_location'])

    price=house(area_type,bath,balcony,size,sqft,location)

    res=price.predict()
    return render_template('house.html',predicted_price=res)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)





