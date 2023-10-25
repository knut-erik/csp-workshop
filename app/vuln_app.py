from flask import Flask, request, Response, render_template, make_response
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/inline/')
def inline():

    # User can set their name via the name variable
    # e.g. /?name=My Name
    param_name = request.args.get("name", default=None, type=str)
    if not param_name:
        param_name = 'Anonymous'

    # The my_html variable conatins the HTML to return from the request
    my_html = """
    <html>
    <title>CSP - inline XSS</title>
    <body>
        Hello there {name}
    </body>
    </html
    """
    my_html = my_html.replace('{name}',param_name)

    return make_response(my_html, 200)


@app.route('/csp/')
def csp():
    name = request.args.get("name", default=None, type=str)
    if not name:
        name = 'Anonymous'

    # Ex 1 - prevent XSS no. x
    response_html = "<html>"
    response_html = '<body>Hello there ' + name +'</body>'
    response_html += '</html>'
    response = make_response(response_html);

    #response.headers['Content-Security-Policy'] = <your policies>
    #response.headers['Reporting-Endpoints'] = <your endpoints>

    return response

# Creating a cookie for the examples
@app.after_request
def after(resp):
    hash = random.getrandbits(128)
    privkey = '%032x' % hash
    resp.set_cookie('your_special_privatekey', privkey)
    
    return resp
