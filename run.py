from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm, PostForm, LoginForm
import urllib.parse

from werkzeug.urls import url_parse
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
#Comentario

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
#APP CONFIG DE LA BASE DE DATOS EN MAQUINA VIRTUAL DANI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bravo:bravo@179.9.115.60/software'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['USE_SESSION_FOR_NEXT']=True
app.config['SQLALCHEMY_POOL_SIZE']=100

login_manager = LoginManager(app)
login_manager.login_view = "login"

db = SQLAlchemy(app)


import models

with app.app_context():
    db.create_all()

posts = []

@app.route("/")
def index():
    posts = models.Post().get_all()
    return render_template("index.html", posts=posts)

@app.route("/p/<string:slug>/")
def show_post(slug):
    post = models.Post().get_by_slug(slug)
    if post is None:
        abort(404)
    return render_template("post_view.html", post=post)


@app.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        post = model.Post(user_id=current_user.id, title=title, content=content)
        post.save()
        return redirect(url_for('index'))
    return render_template("admin/post_form.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)



@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Comprobamos que no hay ya un usuario con ese email
        user = User.get_by_email(email)
        if user is not None:
            error = f'El email {email} ya está siendo utilizado por otro usuario'
        else:
            # Creamos el usuario y lo guardamos
            user = User(name=name, email=email)
            user.set_password(password)
            user.save()
            # Dejamos al usuario logueado
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template("signup_form.html", form=form, error=error)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))
