from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Displays Hello World page"""
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Greets using specified name"""
    return f"Hello {name}"


@app.route('/convert/<celsius>')
def convert(celsius=0):
    """Constructs HTML page"""
    fahrenheit = f"{convert_celsius_to_fahrenheit(float(celsius))}"
    return (f"<h1><u>Celsius to Fahrenheit Converter</u></h1>"
            f"<h2>Celsius: {celsius}"
            f"<br> "
            f"Fahrenheit: {fahrenheit}</h2>")


def convert_celsius_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
