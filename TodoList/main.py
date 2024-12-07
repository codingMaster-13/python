from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_route():
    if request.method == 'POST':
        print('post request is send')
        return render_template("TodoList.html", user_img=request.form.get('username', 'undefined'))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)