from flask import Flask, render_template,request, send_file
import pandas
from geopy.geocoders import ArcGIS


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success-table', methods=['POST'])
def success_table():
    file = request.files['file']
       
    df = pandas.read_csv(file)
    nom = ArcGIS()
    v = df.columns.values.tolist()

    
    
    if "Address" in v:
            df["LAT"] = df["Address"].apply(nom.geocode)
            df["LAT"] = df["LAT"].apply(lambda x: x.latitude)
            df["LON"] = df["Address"].apply(nom.geocode)
            df["LON"] = df["LON"].apply(lambda x: x.longitude)
            df.to_csv('filename.csv', index = None)
            df = pandas.read_csv('filename.csv')
            return render_template('success_table.html', text=df.to_html(), btn = 'download.html')    
    elif "address" in v:
            df.rename(columns={'address': 'Address'}, inplace=True)
            df["LAT"] = df["Address"].apply(nom.geocode)
            df["LAT"] = df["LAT"].apply(lambda x: x.latitude)
            df["LON"] = df["Address"].apply(nom.geocode)
            df["LON"] = df["LON"].apply(lambda x: x.longitude)
            df.to_csv('filename.csv', index = None)
            df = pandas.read_csv('filename.csv')
            return render_template('success_table.html', text = df.to_html(), btn = 'download.html')        
    else:
            return render_template("index.html", text = "Please make sure you have an Address column in your CSV file")  
    
    
@app.route('/download')
def download():
    return send_file('filename.csv', attachment_filename='yourfile.csv', as_attachment= True)
            
    
        
        
        
        
    

    



if __name__ == '__main__':

    app.run(debug=True)

