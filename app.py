from flask import Flask, url_for, request, make_response, render_template, redirect
from markupsafe import escape

app = Flask(__name__)

# Main Route --> enroutment is used for adding a function to the url
@app.route("/")
def index():
    return f"""
    <ul>
        <li><a href="{url_for('hello', string = "Juan Andres")}">/escape</a></li>

        <li><a href="{url_for('show_user_profile', username='Juan Pedrito')}">/Converter String</a></li>

        <li><a href="{url_for('int_function', id=21)}">Converter Int</a></li>

        <li><a href="{url_for('float_function', float = 2.2)}">/Converter Float</a></li>

        <li><a href="{url_for('show_subpath', subpath='converter_path/https://github.com')}">/Converter Path</a></li>

        <li><a href="{url_for('uuid_function', uuid = "989C6E5C-2CC1-11CA-A044-08002B1BB4F5")}">/Converter UUID</a></li>

        <li><a href="{url_for('projects')}">/proyects</a></li>

        <li><a href="http://127.0.0.1:5000/about/">/about/ (throws error)</a></li>

        <li><a href="{url_for('about', next= "/")}">/about/ (using url_for)</a></li>

        <li><a href="{url_for('methods_http_function')}">Methods HTTP</a></li>

        <li><a href="{url_for('get_decorator_function')}">Using get decorator</a></li>

        <li><a href="{url_for('redirection_function')}">Redirection</a></li>
    </ul>
"""

# Escape HTML
@app.route("/<string>", methods=["GET"])
def hello(string):
    return f"Hello, {escape(string)}!"

## Variable rules and converters
# string converter --> accept any text without "/"
@app.route('/converter_str/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

# int converter --> accepts positive int numbers
@app.route("/converter_int/<int:id>")
def int_function(id):
    return f'Converter int {id}'

# float converter --> accepts positive float numbers
@app.route("/converter_float/<float:float>")
def float_function(float):
    return f'Converter Float {float}'

# path converter --> accepts strings but with "/" included
@app.route('/converter_path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

# uuid converter --> accepts UUID strings (989C6E5C-2CC1-11CA-A044-08002B1BB4F5)
@app.route("/converter_uuid/<uuid:uuid>")
def uuid_function(uuid):
    return f'Converter uuid {(uuid)}'

## Unique URLs

@app.route('/projects/') # --> writing /projects will redirect you to /projects/
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page' # --> writing /about/ will throw 404

## URLs constructions
@app.route('/login')
def login():
    return 'login'

@app.route('/url_constructions/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_user_profile', username='Juan Pedrito'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

## Methods HTTP
# We can do it in two ways
    
# using Methods
@app.route("/methods", methods=["GET","POST"])
def methods_http_function():
    if request.method == "POST":
        return "Function for login"
    else:
        return "Show the login form function"
    
# using decorators
@app.get('/using_get_decoration')
def get_decorator_function():
    return "I am using @app.get to print this get"

@app.post('/using_get_decoration') #--> This will only work with post methods
def post_decorator_function():
    return "I am using @app.get to print this get"

################################################ PREGUNTAR A TEMIS POR ARCHIVOS ESTATICOS

## Request Object

@app.post('/using_request_object')
def request_object_function():
    content = request.json
    searchword = content.get('key', '')
    if searchword:
        return "post made succsessfully"
    
## Cookies
    
# Read Cookies
@app.route('/cookies')
def get_cookie():
    username = request.cookies.get('username')

# Set Cookies
@app.route('/cookies_two/')
def set_cookies():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

## Errors and Redirections
@app.route('/redirection')
def redirection_function():
    return redirect(url_for('hello',  string = "Juan Andres"))

