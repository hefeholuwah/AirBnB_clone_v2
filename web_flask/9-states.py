#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_list():
    """Display list of states"""
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def one_state(id):
    key = "State.{}".format(id)
    if key in storage.all('State'):
        states = storage.all('State')["State.{}".format(id)]
    else:
        states = None
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def session_off(self):
    """Shuts down app"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
