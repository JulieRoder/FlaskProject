from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius temperatures to fahrenheit units"""
    return celsius * 9.0 / 5 + 32


@app.route('/c2f/<celsius>')
def c2f(celsius):
    return "{} celsius is {} fahrenheit".format(celsius, convert_celsius_to_fahrenheit(float(celsius)))


if __name__ == '__main__':
    app.run()
