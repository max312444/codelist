from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # 실제 비밀 키로 변경하세요
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite 데이터베이스 사용
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# 사용자 모델
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)

# 로그인 로직
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 로그인 폼
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# 회원가입 폼
class RegisterForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', '남성'), ('Female', '여성')], validators=[DataRequired()])
    height = StringField('Height (cm)', validators=[DataRequired()])
    weight = StringField('Weight (kg)', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

# 비밀번호 재설정 폼
class ResetPasswordForm(FlaskForm):
    new_password = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

@app.route('/')
def home():
    return render_template('index.html')

# 회원가입
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(
            username=form.username.data,
            gender=form.gender.data,
            height=float(form.height.data),
            weight=float(form.weight.data),
            contact=form.contact.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('회원가입이 완료되었습니다!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('로그인 성공!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('로그인 실패! 아이디나 비밀번호를 확인하세요.', 'danger')
    return render_template('login.html', form=form)

# 대시보드 (로그인 후 접근)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# 로그아웃
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# 비밀번호 찾기 (여기서는 단순히 비밀번호 재설정 페이지로 연결)
@app.route('/reset_password', methods=['GET', 'POST'])
@login_required
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        current_user.password = generate_password_hash(form.new_password.data, method='sha256')
        db.session.commit()
        flash('비밀번호가 재설정되었습니다!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('reset_password.html', form=form)

# 아이디 찾기 (이메일을 통해 아이디 찾기)
@app.route('/find_username', methods=['GET', 'POST'])
def find_username():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            flash(f'아이디는 {user.username} 입니다.', 'info')
        else:
            flash('이메일에 해당하는 사용자가 없습니다.', 'danger')
    return render_template('find_username.html')

if __name__ == '__main__':
    with app.app_context():  # 애플리케이션 컨텍스트 설정
        db.create_all()
    app.run(debug=True)

# HTML 템플릿은 templates 디렉토리에 아래 파일들로 저장:
# index.html
"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>홈</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        div {
            text-align: center;
        }
    </style>
</head>
<body>
    <div>
        <h1>환영합니다!</h1>
        <p><a href="{{ url_for('login') }}">로그인</a></p>
        <p><a href="{{ url_for('register') }}">회원가입</a></p>
    </div>
</body>
</html>
"""

# register.html
"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>회원가입</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        form {
            text-align: center;
        }
    </style>
</head>
<body>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }}: {{ form.username(size=32) }}<br>
        {{ form.gender.label }}: {{ form.gender() }}<br>
        {{ form.height.label }}: {{ form.height(size=32) }}<br>
        {{ form.weight.label }}: {{ form.weight(size=32) }}<br>
        {{ form.contact.label }}: {{ form.contact(size=32) }}<br>
        {{ form.password.label }}: {{ form.password(size=32) }}<br>
        {{ form.submit() }}
    </form>
</body>
</html>
"""

# login.html
"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>로그인</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        form {
            text-align: center;
        }
    </style>
</head>
<body>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }}: {{ form.username(size=32) }}<br>
        {{ form.password.label }}: {{ form.password(size=32) }}<br>
        {{ form.submit() }}
    </form>
</body>
</html>
"""

# dashboard.html
"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>대시보드</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        div {
            text-align: center;
        }
    </style>
</head>
<body>
    <div>
        <h1>안녕하세요, {{ current_user.username }}!</h1>
        <p><a href="{{ url_for('logout') }}">로그아웃</a></p>
    </div>
</body>
</html>
"""

# reset_password.html
"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>비밀번호 재설정</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        form {
            text-align: center;
        }
    </style>
</head>
<body>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.new_password.label }}: {{ form.new_password(size=32) }}<br>
        {{ form.submit() }}
    </form>
</body>
</html>
"""

# find_username.html
"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>아이디 찾기</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        form {
            text-align: center;
        }
    </style>
</head>
<body>
    <form method="POST">
        이메일: <input type="email" name="email" size=32 required><br>
        <button type="submit">아이디 찾기</button>
    </form>
</body>
</html>
"""
