from datetime import datetime

from flask import Flask
from flask import render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_xstatic import FlaskXStatic

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
xs = FlaskXStatic(app)

xs.add_module('moment')
app.extensions['bootstrap']['cdns']['bootstrap'] = app.extensions['bootstrap']['cdns']['local']
app.extensions['bootstrap']['cdns']['jquery'] = app.extensions['bootstrap']['cdns']['local']


@app.route('/')
def hello_world():
    return render_template('user.html', name='wang',
                           current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()