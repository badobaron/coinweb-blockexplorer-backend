# Flask basic imports for usage routing & rendering features
from flask import Flask, render_template, request

import core.assets as core_assets
import core.bets as core_bets

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


# Bets category routing
@app.route('/bets')
def bets():
    return render_template('bets.html')


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


##################
# Requests handlers
##################
# ASSETS
# All assets
@app.route('/assetsAll', methods=['POST'])
def assets_all_get_info():
    page = request.json['per_page']
    # Average time 3.7 sec
    return core_assets.get_assets()


# Named assets
@app.route('/assetsNamed', methods=['POST'])
def assets_named_get_info():
    pass


# BETS
@app.route('/betsAll', methods=['POST'])
def bets_all_get_info():
    return core_bets.get_bets()


if __name__ == '__main__':
    app.run()
