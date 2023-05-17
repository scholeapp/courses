from base64 import b64encode

from flask import Flask, request, render_template
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        image = Image.open(file)
        image = np.array(image)
        x = image.reshape(-1, 3)
        kmeans = KMeans(n_clusters=3, random_state=0)
        kmeans.fit(x)
        
        print(file.tell())  # 全てのbytesを読み出した後なので、ファイルの末尾を指している
        file.seek(0)  # 0バイト目に移動
        print(file.tell()) # 0バイト目を指している
        file_bytes = file.read()  # 全てのbytesを読み出す
        print(file.tell())  # 再び末尾に移動
        decoded_img = b64encode(file_bytes).decode("utf-8")
        return render_template(
            'index.html',
            colors=kmeans.cluster_centers_,
            image=decoded_img
        )
    return render_template('index.html', colors=[], image=None)

if __name__ == '__main__':
    app.run(debug=True)
