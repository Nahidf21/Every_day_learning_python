from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def Welcome():
    return "<html><H1> Welcome to my new project </H1></html>"

@app.route('/index',methods =['GET'] )
def Index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'The name of the person is {name}'
    return render_template('form.html')




if __name__ == "__main__":
    app.run(debug=True)