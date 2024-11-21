from flask import Flask

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero", 400
    return str(a / b), 200


@app.route("/")
def home():
    return "Hello, Docker!"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    result = add_numbers(a, b)
    return str(result)

@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    result = subtract_numbers(a, b)
    return str(result)

@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    result = multiply_numbers(a, b)
    return str(result)

@app.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    result, status = divide_numbers(a, b)
    return result, status


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



