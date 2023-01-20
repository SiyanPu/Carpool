
from flask import Flask, request, render_template, make_response, session, redirect, url_for
from database import get_user, get_offers, create_user, validate_email
from database import validate_password, loading_user, get_user_offers, get_user_requests
from database import get_requests, create_offer_db, create_request_db, get_match_offers, get_match_requests
from database import complete_offer, complete_request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__, template_folder='.', static_url_path='/static')
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = u"Please log in"
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        # print(request.form)
        if "offerID" in request.form.keys():
            offer_id = int(request.form["offerID"])
            complete_offer(offer_id)
        if "requestID" in request.form.keys():     
            request_id = int(request.form["requestID"])
            complete_request(request_id)

    id = current_user.id
    html = render_template('index.html',
            user = get_user(id),
            user_offers = get_user_offers(id),
            user_requests = get_user_requests(id),
            match_offers = get_match_offers(id),
            match_requests = get_match_requests(id))
    response = make_response(html)
    return response

@app.route('/all_offers', methods=['GET', 'POST'])
@login_required
def get_all_offers():
    From = request.args.get('from') or ''
    to = request.args.get('to') or ''
    date = request.args.get('date') or ''
    time = request.args.get('time') or ''

    html = render_template('all_offers.html',
            offers = get_offers([From, to, date, time]))
    response = make_response(html)
    return response

@app.route('/all_requests', methods=['GET'])
@login_required
def get_all_requests():
    From = request.args.get('from') or ''
    to = request.args.get('to') or ''
    date = request.args.get('date') or ''
    time = request.args.get('time') or ''
    html = render_template('all_requests.html',
            offers = get_requests([From, to, date, time]))
    response = make_response(html)
    return response

@app.route('/create_offer', methods=['GET'])
@login_required
def create_offer():
    origin = request.args.get('From')
    destination = request.args.get('To')
    date = request.args.get('Date')
    time = request.args.get('Time')
    html = None
    if origin and destination and date and time:
        date_time = date + ' ' + time
        offer_info = [current_user.id, destination.upper(), origin.upper(), date_time]
        create_offer_db(tuple(offer_info))
        html = render_template('create_offer.html', success="Offer created successfully!")
    if not html:
        html = render_template('create_offer.html')
    response = make_response(html)
    return response

@app.route('/create_request', methods=['GET'])
@login_required
def create_request():
    origin = request.args.get('From')
    destination = request.args.get('To')
    date = request.args.get('Date')
    time = request.args.get('Time')
    html = None
    if origin and destination and date and time:
        date_time = date + ' ' + time
        offer_info = [current_user.id, destination.upper(), origin.upper(), date_time]
        create_request_db(tuple(offer_info))
        html = render_template('create_request.html', success="Request created successfully!")
    if not html:
        html = render_template('create_request.html')
    response = make_response(html)
    return response

@app.route('/user', methods=['GET','POST'])
@login_required
def user_profile():
    if request.method == 'GET':
        if session['userID']:
            id = session['userID']
        else:
            id = current_user.id      
    else:
        id = int(request.form["userID"])
        # print(id)
        session['userID'] = id

    html = render_template('user_profile.html', user = get_user(id))
    response = make_response(html)
    return response

@app.route('/createuser', methods=['GET'])
def createuser():
    name = request.args.get('name')
    password = request.args.get('password')
    email = request.args.get('email')
    gender = request.args.get('gender')
    age = request.args.get('age')
    major = request.args.get('major')
    bestline = request.args.get('bestline')
    html = None
    if name and password and email and gender and age and major and bestline:
        user_info = [name, password, email, gender, age, major, bestline]
        if not validate_email(email):
            # user does not exist in our db. can create new user
            create_user(tuple(user_info))
            html = render_template('create_user.html', success="Registration success! Redirecting to login page...")
        else:
            html = render_template('create_user.html', error="Email already registered!")
    if not html:
        html = render_template('create_user.html')
    response = make_response(html)
    return response

@app.route('/login', methods=['GET'])
def login():
    password = request.args.get('password')
    email = request.args.get('email')
    user_id = validate_email(email)
    error = ''
    if email:
        if not user_id:
            print("no user exists")
            error = 'no user with this email exists'
        else:       
            login = validate_password(user_id, email, password)
            if login:
                print("successful")
                return redirect(url_for("index"))
            else:
                print("log in failed")
                error = 'username or password incorrect'
    html = render_template('log_in.html', error = error)

    response = make_response(html)
    return response

@login_manager.user_loader
def load_user(user_id):
   return loading_user(user_id)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))