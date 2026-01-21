from flask import Flask, render_template, request
app = Flask(__name__)

# route for home page, renders form to input name
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# route to handle form, captures the name and displays welcome msg
@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form.get('name')
    return render_template('welcome.html', name=name)

if __name__ == '__main__':
    app.run()