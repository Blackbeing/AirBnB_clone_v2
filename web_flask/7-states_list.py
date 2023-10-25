#!/usr/bin/python3
"""
Create a simple flask app with a route
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(request):
    """Purge session after request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """List all states, render in html"""
    all_states = sorted(storage.all(cls=State).values(), key=lambda x: x.name)
    return render_template("7-states_list.html", all_states=all_states)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app.run(host=host, port=port)
