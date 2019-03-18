from bottle import route, run, template
import test_json

@route('/')
def index():
    return '<h1>Hello, World,test</h1>'


if __name__ == '__main__':
    run(debug=True, reloader=True)
