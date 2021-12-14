from flask import Flask, request, jsonify               
from PIL import Image

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def index():
    if request.method == "POST":
        files = request.files['imgs']
        img = Image.open(files)
        img = img.convert('L')
        img = img.transpose(method=Image.FLIP_TOP_BOTTOM) 
        img.save('static/img_from_lazarus/'+ files.filename)        
    return jsonify({ 'msg': 'FILE SAVE SUCCESS'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)