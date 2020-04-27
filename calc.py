import os
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def calc():
    if request.method == 'GET':
        return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Калькулятор!</title>
                      </head>
                      <body>
                        <h1>Калькулятор!!!</h1>
                        <form name="test" method="post" action="/">
                         <p>
                          <input type="number" size="15" name="number1" placeholder='Введите число' id="number1">
                         </p>
                         <p>
                          <input type="number" size="15" name="number2" placeholder='Введите число' id="number2">
                         </p>
                         <p>
                          <div class="form-check">
                           <input class="form-check-input" type="radio" name="operation" id="plus" value="plus" checked>
                            <label class="form-check-label" for="+">
                             +
                            </label>
                          </div>
                          <div class="form-check">
                            <input class="form-check-input" type="radio" name="operation" id="minus" value="minus">
                             <label class="form-check-label" for="-">
                              -
                             </label>
                          </div>
                          <div class="form-check">
                            <input class="form-check-input" type="radio" name="operation" id="multiplication" value="multiplication">
                             <label class="form-check-label" for="*">
                              *
                             </label>
                          </div>
                          <div class="form-check">
                            <input class="form-check-input" type="radio" name="operation" id="division" value="division">
                             <label class="form-check-label" for="/">
                              /
                             </label>
                          </div>
                          </p>
                         <p>
                          <input type='submit' value='Получить результат'>
                         </p>
                        </form>
                      </body>
                    </html>"""

    elif request.method == 'POST':
        print(request.form['number1'])
        print(request.form['number2'])
        number1 = int(request.form['number1'])
        number2 = int(request.form['number2'])
        print(request.form['operation'])
        if request.form['operation'] == 'plus':
            return str(number1 + number2)
        elif request.form['operation'] == 'minus':
            return str(number1 - number2)
        elif request.form['operation'] == 'multiplication':
            return str(number1 * number2)
        elif request.form['operation'] == 'division':
            if number2 == 0:
                return 'Сладкий, так нельзя'
            else:
                return str(number1 / number2)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')