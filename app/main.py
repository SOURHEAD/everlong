from flask import Flask, render_template
import requests

def create_page():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        message = "Hello, World"
        return render_template('index.html', message=message)

    return app

if __name__ == "__main__":
    app = create_page()
    app.run(host="0.0.0.0", debug=True)

def request_get(url):
    print("Sending request to ", url)
    response = requests.get(url)                                #connects and pings the url in its given parameter and return the status code                    
    print("Requst code recieved is", response.status_code)      #for unit tests as we need to check if the website is up,(200-299 is fine but I just used 200)
    return response.status_code
