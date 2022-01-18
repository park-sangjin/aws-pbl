from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell():
    return '<h1> 이 화면은 메인화면 입니다. 주소 뒤에 /test를 붙이면 다른 화면이 나타납니다<h1>'

@app.route('/test')
def test():
    return '뒤에 /test를 붙이면 나타납니다.'

if __name__ == '__main__':
    app.run("0.0.0.0",port = 8080)

