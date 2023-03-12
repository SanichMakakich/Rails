import json

from flask import Flask, render_template, flash, request, redirect, url_for, get_flashed_messages
from json import dumps, loads
import os

app = Flask(__name__)

app.secret_key = "secret_key"

id = 0


@app.route("/")
def index():
    '''
    message = get_flashed_messages(with_categories=True)
    with open('user.json') as file:
        data = json.loads(file.read())

    return render_template(
        "index.html",
        message=message,
        data=data
    )
'''
    return f"Hello world"

@app.route('/users/new')
def new_users():
    users = []
    errors = []

    return render_template(
        'users/new.html',
        errors=errors,
        users=users,
    )


def validate(item):
    errors = {}
    if len(item['name']) < 4:
        errors['name'] = 'NickName must be grater than 4 charters'
    if not item["email"]:
        errors["name"] = "Email is empty"
    return errors


@app.post('/users')
def post_users():
    data = request.form.to_dict()

    global id
    id += 1
    data['id'] = id

    errors = validate(data)
    result = []

    if errors:
        return render_template(
            "users/new.html",
            users=data,
            errors=errors,

        ), 422

    if os.stat("user.json").st_size == 0:
        result.append(data)
    else:
        with open('user.json') as file:
            db = json.loads(file.read())
            result = db
            result.append(data)

    with open('user.json', "w+") as file:
        file.write(json.dumps(result))

    flash('Users has been created', 'success')

    return redirect(url_for("index"))


@app.route("/users/<id>/edit")
def edit_users(id):
    errors = list()
    user = dict()
    with open("user.json") as file:
        read_file = json.loads(file.read())
        for elem in read_file:
            if elem['id'] == id:
                user = elem
    return render_template(
        "/users/edit.html",
        errors=errors,
        user=user
    )


@app.get("/users/<int:id>")
def show_users(id):
    with open("user.json") as file:
        read_file = json.loads(file.read())
        for elem in read_file:
            if elem['id'] == id:
                return f"{elem}"
    return f"User not found"


@app.route("/users/<id>/patch", methods=['POST'])
def patch_user(id):
    data = request.form.to_dict()
    user = dict()
    with open("user.json") as file:
        read_file = json.loads(file.read())
        for elem in read_file:
            if elem['id'] == id:
                user = elem
    errors = validate(data)
    if errors:
        return render_template(
            "users/edit.html",
            user=user,
            errors=errors
        )
    user["name"] = data["name"]
    with open('user.json') as file:
        db = json.loads(file.read())
        result = db
        result.append(user)

    with open('user.json', "w+") as file:
        file.write(json.dumps(result))

    flash('School has been updated', 'success')
    return redirect(url_for("index"))
