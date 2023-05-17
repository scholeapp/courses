from flask import Flask, request
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        image = Image.open(file)
        image = np.array(image)
        print(image)  # 画像のデータを表示して確認。
        print(image.shape)  # RGBなら[H, W, 3]

    return '''
    <form method=post enctype=multipart/form-data>
        <input type=file name=file id="file"/>
        <input type=submit value="送信" />
    </form>'''

if __name__ == '__main__':
    app.run(debug=True)

