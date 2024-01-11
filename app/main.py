from flask import Flask, render_template

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

