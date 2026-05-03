from flask import Flask, flash, url_for, redirect, render_template, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("main/index.html")


