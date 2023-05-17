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
        x = image.reshape(-1, 3)  # -1は自動計算される
        kmeans = KMeans(n_clusters=3, random_state=0)
        kmeans.fit(x)
        return render_template('index.html', colors=kmeans.cluster_centers_)
    return render_template('index.html', colors=[])

if __name__ == '__main__':
    app.run(debug=True)
