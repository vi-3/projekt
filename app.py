from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route("/")
def index():
    return render_template('home.html')

# Страница поиска
@app.route("/search")
def search():
    return render_template('search.html')

# Личный кабинет
@app.route("/profile")
def user_profile():
    return render_template('user_profile.html')

# Регистрация
@app.route("/registration")
def registration():
    return render_template('registration.html')

# Страница групп
@app.route("/groups")
def groups():
    return render_template('groups.html')

# Детали группы
@app.route("/Group_Detail")
def Group_Detail():
    return render_template('Group_Detail.html')


@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)