from flask import redirect, render_template, url_for
from flask_login import login_user, logout_user

from app import app, db, forms, models


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/log-in", methods=["GET", "POST"])
def log_in():
    form = forms.LogInForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email_address=form.email_address.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("home"))
    return render_template("log_in.html", form=form)


@app.route("/log-out")
def log_out():
    logout_user()
    return redirect(url_for("home"))


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        user = models.User(email_address=form.email_address.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for("home"))
    return render_template("sign_up.html", form=form)
