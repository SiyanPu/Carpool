from sqlite3 import connect
from contextlib import closing
from offer import Offer, Request
from user_login import User_login
from sys import stderr, exit
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask import flash, redirect, url_for

_DATABASE_URL = 'file:database.sqlite?mode=rw'


def get_user(id):
    user = None
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                query_str = "SELECT * FROM users WHERE user_id = ?;"
                
                cursor.execute(query_str, [id])


                row = cursor.fetchone()
                if row is not None:
                    user = User_login(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]))
                return user
    except IndexError:
        print("index error",file = stderr)
        exit(1)

def get_offers(Filter):
    From, to, date, time = Filter

    offers = []
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stmt = "SELECT * FROM ride_offering WHERE departure like '%" + From + "%' "\
                "AND destination like '%" + to + "%' "\
                "AND date_time like '%" + date + "%' "\
                "AND date_time like '%" + time + "%' "\
                ";"
                cursor.execute(stmt)

                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    offers.append(Offer(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
                    row = cursor.fetchone()
                print(offers)
    
                return offers
    except IndexError:
        print("index error",file = stderr)
        exit(1)

def get_requests(Filter):
    From, to, date, time = Filter

    requests = []
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stmt = "SELECT * FROM ride_request WHERE departure like '%" + From + "%' "\
                "AND destination like '%" + to + "%' "\
                "AND date_time like '%" + date + "%' "\
                "AND date_time like '%" + time + "%' "\
                ";"
                cursor.execute(stmt)

                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    requests.append(Offer(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
                    row = cursor.fetchone()
                print(requests)
    
                return requests
    except IndexError:
        print("index error",file = stderr)
        exit(1)

def get_user_offers(user_id):
    offers = []
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stmt = "SELECT * FROM ride_offering WHERE user_id = " + str(user_id) + ";"
                cursor.execute(stmt)

                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    offers.append(Offer(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
                    row = cursor.fetchone()
                print(offers)
    
                return offers
    except IndexError:
        print("index error",file = stderr)
        exit(1)

def get_user_requests(user_id):
    requests = []
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stmt = "SELECT * FROM ride_request WHERE user_id = ?;"
                cursor.execute(stmt, [str(user_id)])

                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    requests.append(Request(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
                    row = cursor.fetchone()
                print(requests)
    
                return requests
    except IndexError:
        print("index error",file = stderr)
        exit(1)


def get_match_requests(user_id):
    offers = []
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stmt = "SELECT * FROM ride_offering WHERE user_id = " + str(user_id) + ";"
                cursor.execute(stmt)

                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    offers.append(Offer(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
                    row = cursor.fetchone()
                print(offers)
    except IndexError:
        print("index error",file = stderr)
        exit(1)
    match_requests = []
    for offer in offers:
        to = offer.destination
        From = offer.departure
        date = offer.date_time[:10]
        hour = int(offer.date_time[11:13])
        try:
            with connect(_DATABASE_URL, isolation_level=None,
                uri=True) as connection:
                with closing(connection.cursor()) as cursor:
                    stmt = "SELECT * FROM ride_request WHERE departure like '%" + From + "%' "\
                    "AND destination like '%" + to + "%' "\
                    "AND date_time like '%" + date + "%' "\
                    ";"
                    cursor.execute(stmt)
                    print(stmt)
                    row = cursor.fetchone()
                    while row is not None:
                        print(row)
                        request_hour = int(row[4][11:13])
                        if request_hour < hour + 3 and request_hour > hour - 3:
                            match_requests.append(Offer(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
                        row = cursor.fetchone()
                    print(match_requests)
        
        except IndexError:
            print("index error",file = stderr)
            exit(1)
    return match_requests

def get_match_offers(user_id):
    requests = []
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stmt = "SELECT * FROM ride_request WHERE user_id = " + str(user_id) + ";"
                cursor.execute(stmt)

                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    requests.append(Offer(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
                    row = cursor.fetchone()
                print(requests)
    except IndexError:
        print("index error",file = stderr)
        exit(1)

    match_offers = []
    for request in requests:
        to = request.destination
        From = request.departure
        date = request.date_time[:10]
        hour = int(request.date_time[11:13])
        try:
            with connect(_DATABASE_URL, isolation_level=None,
                uri=True) as connection:
                with closing(connection.cursor()) as cursor:
                    stmt = "SELECT * FROM ride_offering WHERE departure like '%" + From + "%' "\
                    "AND destination like '%" + to + "%' "\
                    "AND date_time like '%" + date + "%' "\
                    ";"
                    cursor.execute(stmt)
                    print(stmt)
                    row = cursor.fetchone()
                    while row is not None:
                        print(row)
                        offer_hour = int(row[4][11:13])
                        if offer_hour < hour + 3 and offer_hour > hour - 3:
                            match_offers.append(Offer(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
                        row = cursor.fetchone()
                    print(match_offers)
        
        except IndexError:
            print("index error",file = stderr)
            exit(1)
    return match_offers



def create_offer_db(offer_info):
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stat_str = "INSERT INTO ride_offering (user_id, destination, departure, date_time) VALUES "
                stat_str += str(offer_info)
                stat_str += ";"
                print(stat_str)
                cursor.execute(stat_str)
                
    except IndexError:
        print("index error",file = stderr)
        exit(1)


def complete_offer(offer_id):
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stat_str = "DELETE FROM ride_offering WHERE offer_id = "
                stat_str += str(offer_id)
                stat_str += ";"
                print(stat_str)
                cursor.execute(stat_str)
                
    except IndexError:
        print("index error",file = stderr)
        exit(1)
    
def create_request_db(request_info):
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stat_str = "INSERT INTO ride_request (user_id, destination, departure, date_time) VALUES "
                stat_str += str(request_info)
                stat_str += ";"
                print(stat_str)
                cursor.execute(stat_str)
    except IndexError:
        print("index error",file = stderr)
        exit(1)

def complete_request(request_id):
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stat_str = "DELETE FROM ride_request WHERE request_id = "
                stat_str += str(request_id)
                stat_str += ";"
                print(stat_str)
                cursor.execute(stat_str)
                
    except IndexError:
        print("index error",file = stderr)
        exit(1)

def create_user(user_info):
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stat_str = "INSERT INTO users (user_name, password, email, gender, age, major, bestline) VALUES "
                stat_str += str(user_info)
                stat_str += ";"
                print(stat_str)
                cursor.execute(stat_str)
                
    except IndexError:
        print("index error",file = stderr)
        exit(1)

def loading_user(user_id):
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stat_str = "SELECT * from users where user_id = "
                stat_str += str(user_id)
                stat_str += ";"
                print(stat_str)
                cursor.execute(stat_str)
                lu = cursor.fetchone()
                if lu is None:
                    return None
                else:
                    return User_login(int(lu[0]), lu[1], lu[2], lu[3], lu[4], lu[5], lu[6], lu[7])
    except IndexError:
        print("index error",file = stderr)
        exit(1)

def validate_email(email):

    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stat_str = 'SELECT user_id, email FROM users where email = "'
                print(email)
                stat_str += str(email)
                stat_str += '";'
                print(stat_str)
                cursor.execute(stat_str)
                valemail = cursor.fetchone()
                print(valemail)
                if valemail is None:
                    return False
                else:
                    print(valemail)
                    return valemail[0]   
    except IndexError:
        print("index error",file = stderr)
        exit(1)

def validate_password(user_id, email, password):
    try:
        with connect(_DATABASE_URL, isolation_level=None,
            uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                stat_str = "SELECT * from users where user_id = "
                stat_str += str(user_id)
                stat_str += ";"
                print(stat_str)
                cursor.execute(stat_str)
                lu = cursor.fetchone()

                Us = User_login(int(lu[0]), lu[1], lu[2], lu[3], lu[4], lu[5], lu[6], lu[7])
                print(Us.email, Us.password)
                if email == Us.email and password == Us.password:
                    print(Us.email, Us.password)
                    print(111)
                    login_user(Us)
                    # Umail = list({email})[0].split('@')[0]
                    # # flash('Logged in successfully '+Umail)
                    # # redirect(url_for('profile'))
                    return True
                else:
                    # flash('Login Unsuccessfull.')
                    return False

    except IndexError:
        print("index error",file = stderr)
        exit(1)
