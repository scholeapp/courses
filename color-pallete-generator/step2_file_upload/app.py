from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        print(file.filename)  # ファイル名
        data = file.read()  # bytes
        print(len(data))  # byte数
        print(data[0:100])  # 先頭100bytesを表示
    return '''
    <form method=post enctype=multipart/form-data>
        <input type=file name=file id="file"/>
        <input type=submit value="送信" />
    </form>'''

if __name__ == '__main__':
    app.run(debug=True)
