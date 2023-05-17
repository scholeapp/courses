import io
from base64 import b64encode

from flask import Flask, request, render_template, redirect
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'gif', 'jpg', 'jpeg'}  # 画像の拡張子の集合

def is_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if not is_allowed_file(file.filename):
            return redirect(request.url)
        image = Image.open(file)
        # グレースケール画像もRGBA画像もすべてRGBに変換。
        # グレースケール画像の場合、RGBに変換すると、kmeansの計算で無駄がありますが、いったんこれで進めます。
        image = image.convert('RGB')
        image = np.array(image)
        x = image.reshape(-1, 3)
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
