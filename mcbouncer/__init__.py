from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('mcbouncer.default_config')
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

def start(debug=False):
    """
    Sets up a basic deployment ready to run in production in light usage.

    Ex: ``gunicorn -w 4 -b 127.0.0.1:4000 "mcbouncer:start()"``

    This code from https://github.com/TkTech/notifico
    """
    import os
    import os.path
    from werkzeug import SharedDataMiddleware

    app.config.from_object('mcbouncer.default_config')

    if app.config.get('HANDLE_STATIC'):
        # We should handle routing for static assets ourself (handy for
        # small and quick deployments).
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/': os.path.join(os.path.dirname(__file__), 'static')
        })

    if debug:
        # Override the configuration's DEBUG setting.
        app.config['DEBUG'] = True

    if not app.debug:
        # If the app is not running with the built-in debugger, log
        # exceptions to a file.
        import logging
        file_handler = logging.FileHandler('mcbouncer.log')
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)

    # Let SQLAlchemy create any missing tables.
    #db.create_all()

    return app
