from flask import Flask, request, Response, render_template, make_response
import random

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/csp/')
def csp():
    name = request.args.get("name", default=None, type=str)
    description = request.args.get("description", default=None, type=str)
    
    if not name:
        name = 'Anonymous'    
    return render_template('csp.html', name=name, description=description)

@app.route('/test/')
def test():
    name = request.args.get("name", default=None, type=str)
    
    if not name:
        name = 'Anonymous'    
    return render_template('test.html', name=name)

# Used for setting HTTP headers
@app.after_request
def after(response):

    # Set some random cookie
    hash = random.getrandbits(128)
    privkey = '%032x' % hash
    response.set_cookie('your_special_privatekey', privkey)
    
    ## Set your HTTP Response headers below
    #response.headers['<header>'] = "<header_value(s)>"
    csp_policy = "default-src 'none';"
    script_policy = " script-src 'none';"
    style_policy = " style-src 'none';"
    font_policy = " font-src 'none';"
    img_policy = " img-src 'none';"

    csp_policy += script_policy + style_policy + font_policy + img_policy
    response.headers['Content-Security-Policy-Report-Only'] = csp_policy

    return response
