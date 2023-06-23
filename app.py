from flask import Flask, url_for, redirect
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'hgfds'
oauth = OAuth(app)


@app.route("/")
def hi():
    return "HI"


oauth.register(
    name='authentik',
    server_metadata_url= 'http://localhost:9000/application/o/supportgenie/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'},
    client_id= 'KRQka4mEFOX8QDZrffbfR5f9BSOEnHqqE2sbrETY',
    client_secret= 'cruaTUKccNbIuWOR8s7tFP9Tjb6MFUmIBERf3pt1blpi0FX5RC1rVGpAxdIa7v2fJkc2n2QiP4v4wenJ4PShwFtgk2aZHMadqFyooqlK47jLLG4R0MnD287a2wbnmUmN',
)

@app.route('/login', methods=['GET','POST'])
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.authentik.authorize_redirect(redirect_uri)


@app.route('/authorize', methods=['GET','POST'])
def authorize():
    token = oauth.authentik.authorize_access_token()
    print(token)
    # resp = oauth.authentik.get('account/verify_credentials.json')
    # resp.raise_for_status()
    # profile = resp.json()
    # do something with the token and profile
    return redirect('/')

