from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',)
def index_route():
    return render_template("index.html")
@app.route('/signIn')
def signin_route():
    return render_template('signin.html')

@app.route('/signUp')
def signup_route():
    return render_template('signup.html')
if __name__=="__main__":
    app.run(debug=True)