from requests.auth import HTTPBasicAuth

URL = "http://public.coindaddy.io:4000/api/"
HEADERS = {'content-type': 'application/json'}
AUTH = HTTPBasicAuth('rpc', '1234')
