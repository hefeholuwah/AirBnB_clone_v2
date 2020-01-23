#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def states_lister(id=None):
    """Display states list html"""
    return render_template('9-states.html', id=id, states=storage.all(State))


@app.teardown_appcontext
def session_off(self):
    """Shuts down app"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
