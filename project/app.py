from flask import Flask, render_template

print("booting simple-app...")

application = Flask(__name__)

@application.route('/')
def homepage():
    return render_template('homepage.html')

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.

    application.debug = True
    application.run()