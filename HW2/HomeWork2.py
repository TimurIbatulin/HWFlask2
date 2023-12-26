# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан cookie-файл с данными пользователя, 
# а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными
#  пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, make_response, redirect, request, render_template
global context
app = Flask(__name__)


@app.get('/submit')

def submit_get():
    return render_template('form.html')


@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    email = request.form.get('email')
    context = {
        'username': name,
        'email' : email
    }
    return render_template('second.html', name = name)

@app.route('/submit')
def cookies_file():
    response = make_response('Мы используем cookie')
    response.set_cookie('username', 'iii')
    return response


@app.route('/submit')
def get_cookies():
    name = request.cookies.get('username')
    return f'Значение куки {name}'

if __name__ == '__main__':
    app.run(debug=True)