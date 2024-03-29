from flask import Flask, render_template, redirect, request
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.post('/add')
def add():
    item_title = request.form.get('item_title')
    add_item(item_title)
    return redirect('/')
