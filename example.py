import json

from flask import Flask, render_template, flash, request, redirect, url_for, get_flashed_messages
from json import dumps, loads
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"hello"