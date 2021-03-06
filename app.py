# Flask basic imports for usage routing & rendering features
from flask import Flask, render_template, request

import core.assets as core_assets
import core.bets as core_bets
import core.broadcasts as core_broadcasts
import core.burns as core_burns
import core.dividends as core_dividends
import core.issuances as core_issuances
import core.mempool as core_mempool
import core.orders as core_orders
import core.sends as core_sends
import core.blocks as core_blocks
import core.index as core_index

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
@app.route('/blocks')
def blocks():
    return render_template('blocks.html')


# Broadcasts category routing
@app.route('/broadcasts')
def broadcasts():
    return render_template('broadcasts.html')


# Burns category routing
@app.route('/burns')
def burns():
    return render_template('burns.html')


# Dividends category routing
@app.route('/dividends')
def dividends():
    return render_template('dividends.html')


# Issuances category routing
@app.route('/issuances')
def issuances():
    return render_template('issuances.html')


# Markets category routing
# TODO: add render methods for markets template
@app.route('/markets')
def markets():
    pass


# Mempool category routing
@app.route('/mempool')
def mempool():
    return render_template('mempool.html')


# Orders category routing
@app.route('/orders')
def orders():
    return render_template('orders.html')


# Sends category routing
@app.route('/sends')
def sends():
    return render_template('sends.html')


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
# INDEX PAGE
@app.route('/indexInfo', methods=['POST'])
def index_page_info():
    return core_index.get_index_info()


# ASSETS
# All assets
@app.route('/assetsAll', methods=['POST'])
def assets_all_get_info():
    per_page = request.json['per_page']
    # Average time 17.5 sec!!! Very slow
    return core_assets.get_all_assets(per_page)


# Named assets
@app.route('/assetsNamed', methods=['POST'])
def assets_named_get_info():
    per_page = request.json['per_page']
    # Average time 17.5 sec!!! Very slow
    return core_assets.get_named_assets()


# Subassets
@app.route('/assetsSub', methods=['POST'])
def assets_sub_get_info():
    per_page = request.json['per_page']
    return core_assets.get_sub_assets()


# Numeric assets
@app.route('/assetsNumeric', methods=['POST'])
def assets_numeric_get_info():
    per_page = request.json['per_page']
    # Average time 17.5 sec!!! Very slow
    return core_assets.get_numeric_assets()


# BETS
@app.route('/betsAll', methods=['POST'])
def bets_all_get_info():
    per_page = request.json['per_page']
    data = request.json
    return core_bets.get_bets(data['per_page'], data['offset'])


# BLOCKS
# TODO: add get_info function for blocks
@app.route('/blocksAll', methods=['POST'])
def blocks_all_get_info():
    per_page = request.json['per_page']
    return core_blocks.get_blocks(per_page)


# BROADCASTS
@app.route('/broadcastsAll', methods=['POST'])
def broadcasts_all_get_info():
    per_page = request.json['per_page']
    return core_broadcasts.get_broadcasts(per_page)


# BURNS
@app.route('/burnsAll', methods=['POST'])
def burns_all_get_info():
    per_page = request.json['per_page']
    return core_burns.get_burns(per_page)


# DIVIDENDS
@app.route('/dividendsAll', methods=['POST'])
def dividends_all_get_info():
    per_page = request.json['per_page']
    return core_dividends.get_dividends(per_page)


# ISSUANCES
@app.route('/issuancesAll', methods=['POST'])
def issuances_all_get_info():
    per_page = request.json['per_page']
    return core_issuances.get_issuances(per_page)


# MEMPOOL
@app.route('/mempoolAll', methods=['POST'])
def mempool_all_get_info():
    return core_mempool.get_mempool()


# ORDERS
@app.route('/ordersAll', methods=['POST'])
def orders_all_get_info():
    per_page = request.json['per_page']
    return core_orders.get_orders(per_page)


# SENDS
@app.route('/sendsAll', methods=['POST'])
def sends_all_get_info():
    per_page = request.json['per_page']
    return core_sends.get_sends(per_page)


if __name__ == '__main__':
    app.run(debug=True)
