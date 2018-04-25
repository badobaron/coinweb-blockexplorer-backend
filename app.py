# Flask basic imports for usage routing & rendering features
from flask import Flask, render_template

# Registering our app
app = Flask(__name__)

# Error handling section
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(410)
def gone(e):
    return render_template('410.html'), 410

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

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

# Bets category routing
# TODO: add render method for bets template
@app.route('/bets')
def bets():
    pass

# Blocks category routing
# TODO: add render method for blocks template
@app.route('/blocks')
def blocks():
    pass

# Broadcasts category routing
# TODO: add render method for broadcasts template
@app.route('/broadcasts')
def broadcasts():
    pass

# Burns category routing
# TODO: add render method for burns template
@app.route('/burns')
def burns():
    pass

# Dividends category routing
# TODO: add render methods for dividends template
@app.route('/dividends')
def dividends():
    pass

# Issuances category routing
# TODO: add render methods for issuances template
@app.route('/issuances')
def issuances():
    pass

# Markets category routing
# TODO: add render methods for markets template
@app.route('/markets')
def markets():
    pass

# Mempool category routing
# TODO: add render methods for mempool template
@app.route('/mempool')
def mempool():
    pass

# Orders category routing
# TODO: add render methods for orders template
@app.route('/orders')
def orders():
    pass

# Sends category routing
# TODO: add render methods for sends template
@app.route('/sends')
def sends():
    pass

# API category routing
# TODO: add render methods for API template
@app.route('/api')
def api():
    pass

# Status category routing
# TODO: add render methods for status template
@app.route('/status')
def status():
    pass

# Wallets category routing
# TODO: add render methods for wallets template
@app.route('/wallets')
def wallets():
    pass

# About category routing
# TODO: add render methods for about template
@app.route('/about')
def about():
    pass

if __name__ == '__main__':
    app.run()