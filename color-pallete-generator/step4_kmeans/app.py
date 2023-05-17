from flask import Flask, request
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
        # kmeansのために、[H*W, 3]のshapeに変更。-1は自動計算される。
        x = image.reshape(-1, 3)
        kmeans = KMeans(n_clusters=3, random_state=0)
        kmeans.fit(x)
        print(kmeans.cluster_centers_)  # 重心3つ。 [3, 3]

    return '''
    <form method=post enctype=multipart/form-data>
        <input type=file name=file id="file"/>
        <input type=submit value="送信" />
    </form>'''

if __name__ == '__main__':
    app.run(debug=True)
