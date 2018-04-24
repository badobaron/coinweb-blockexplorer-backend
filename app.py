# Flask basic imports for usage routing & rendering features
from flask import Flask, render_template

# Registering our app
app = Flask(__name__)

# Site root routing
@app.route('/')
def index():
    return render_template('index.html')

# Assets category routing
@app.route('/assets')
def assets():
    return render_template('assets.html')

@app.route('/assets/all')
def assets_all():
    return render_template('assets_all.html')

@app.route('/assets/named')
def assets_named():
    return render_template('assets_named.html')

@app.route('/assets/subassets')
def assets_subassets():
    return render_template('assets_subassets.html')

@app.route('/assets/numeric')
def assets_numeric():
    return render_template('assets_numeric.html')

if __name__ == '__main__':
    app.run()