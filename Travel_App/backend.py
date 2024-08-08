from flask import Flask, render_template, request
# send_static_file for static objects with use in API

# linking static items like 
# href="{{ url_for('static', filename='style.css') }}
# mlink to static

# url_for('index') is for dynamic routes
# dynamic handling is a little different (constantly changing)

app = Flask(__name__)

# url below to trigger function
@app.route("/") 
def index(): 
    return render_template('index.html') 

# serve static file through api endpoint
# fancy way of saying doing a function when an http request is received
# can be PUT, GET, etc
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


  
# run the application 
if __name__ == "__main__": 
    app.run(debug=True)