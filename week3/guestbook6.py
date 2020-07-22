from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index1.html')
@app.route('/sign')
def sign():
    return render_template('sign1.html')
@app.route('/process',methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    return render_template('index1.html',name=name,comment=comment)
if __name__ == '__main__':
    app.run(debug=True)