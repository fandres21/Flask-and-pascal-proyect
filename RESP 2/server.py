from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

dataDD = {'EA': [], '25': [], '10': []}

@app.route('/data', methods=['POST'])
def index():
    if request.method == "POST":
        data = request.get_json(force=True)
        dataDD['EA'] = data['EA']
        dataDD['25'] = data['25']
        dataDD['10'] = data['10']
    return jsonify({ 'msg': 'FILE SAVE SUCCESS'})

@app.route('/get_data', methods=['GET'])
def data_get():
    if request.method == "GET": return dataDD

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=4000)
