from flask import Flask, request, jsonify              
from PIL import Image

app = Flask(__name__)

@app.route('/im_data', methods=['POST'])
def index():
    if request.method == "POST":
        files = request.files['img']
        img = Image.open(files).convert('L')
        img = img.transpose(method=Image.FLIP_TOP_BOTTOM) 
        img.save('static/img/'+ files.filename) 
    print({ 'msg': 'FILE SAVE SUCCESS'})
    return jsonify({ 'msg': 'FILE SAVE SUCCESS'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)