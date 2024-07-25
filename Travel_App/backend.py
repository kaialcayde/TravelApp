from flask import Flask, render_template, request
# send_static_file for static objects with use in API

# linking static items like 
# href="{{ url_for('static', filename='style.css') }}
# mlink to static

# url_for('index') is for dynamic routes

app = Flask(__name__)

# url below to trigger function
@app.route("/") 
def index(): 
    return render_template('index.html') 
  
# run the application 
if __name__ == "__main__": 
    app.run(debug=True)