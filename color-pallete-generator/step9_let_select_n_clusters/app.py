from base64 import b64encode

from flask import Flask, render_template, request, flash, redirect
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
        # request.form.get('n_clusters')は文字列型なのでintで整数に変換。
        n_clusters = int(request.form.get('n_clusters'))
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans.fit(x)

        file.seek(0)
        file_bytes = file.read()
        decodedImg = b64encode(file_bytes).decode("utf-8")
        return render_template(
            'index.html',
            colors=kmeans.cluster_centers_,
            image=decodedImg
        )
    return render_template('index.html', colors=[], image=None)

if __name__ == '__main__':
    app.run(debug=True)
