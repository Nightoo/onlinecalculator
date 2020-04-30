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
                          <input type="str" size="15" name="name" placeholder='Введите имя' id="name">
                         </p>
                         <p>
                          <input type="number" size="15" required name="number1" placeholder='Введите число' id="number1">
                         </p>
                         <p>
                          <input type="number" size="15" required name="number2" placeholder='Введите число' id="number2">
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
                          <div class="form-check">
                            <input class="form-check-input" type="radio" name="operation" id="degree" value="degree">
                             <label class="form-check-label" for="^">
                              ^
                             </label>
                          </div>
                          <div class="form-check">
                            <input class="form-check-input" type="radio" name="operation" id="root" value="root">
                             <label class="form-check-label" for="root">
                              n-th root 
                             </label>
                          </div>
                          </p>
                         <p>
                          <input type='submit' value='Получить результат'>
                         </p>
                         <p>
                          <a href="https://github.com/Nightoo/Conceptual-Tetris-Game"><img src="conctetris.png" alt="Концептуальный тетрис"></a>
                          <a href="https://github.com/Nightoo/Galaga"><img src="startscreen.png" alt="Концептуальная галага"></a>
                         </p>
                        </form>
                      </body>
                    </html>"""

    elif request.method == 'POST':
        print(request.form['number1'])
        print(request.form['number2'])
        name = request.form['name']
        if name != '':
            name += ','
        number1 = int(request.form['number1'])
        number2 = int(request.form['number2'])
        if str(number1) == '' or str(number1) == '':
            return f'{name}, введите числа'
        print(request.form['operation'])
        if request.form['operation'] == 'plus':
            return f'{name} Ваш ответ: {str(number1 + number2)}'
        elif request.form['operation'] == 'minus':
            return f'{name} Ваш ответ: {str(number1 - number2)}'
        elif request.form['operation'] == 'multiplication':
            return f'{name} Ваш ответ: {str(number1 * number2)}'
        elif request.form['operation'] == 'division':
            if number2 == 0:
                return 'Так нельзя'
            else:
                return f'{name} Ваш ответ: {str(number1 / number2)}'
        elif request.form['operation'] == 'root':
            if number2 == 0:
                return 'Так нельзя'
            else:
                return f'{name} Ваш ответ: {str(number1 ** (1 / number2))}'
        elif request.form['operation'] == 'degree':
            if number2 >= 10 or number1 > 99:
                return 'Очень большое число'
            else:
                return f'{name} Ваш ответ: {str(number1 ** number2)}'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')