from requests.auth import HTTPBasicAuth

URL = "http://public.coindaddy.io:14000/api/"
HEADERS = {'content-type': 'application/json'}
AUTH = HTTPBasicAuth('rpc', '1234')