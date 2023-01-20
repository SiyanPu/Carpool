from flask import Flask
from flask import render_template, url_for, flash, request, redirect, Response
# import sqlite3
from flask_login import UserMixin

# _DATABASE_URL = 'file:database.sqlite?mode=rw'

class User_login(UserMixin):
    def __init__(self, id, username, password, email, gender, age, major, bestline):
         self.id = id
         self.username = username
         self.email = email
         self.password = password
         self.authenticated = False
         self.gender = gender
         self.age = age
         self.major = major
         self.bestline = bestline

    def is_active(self):
         return self.is_active()
    def is_anonymous(self):
         return False
    def is_authenticated(self):
         return self.authenticated
    def is_active(self):
         return True
    def get_id(self):
         return self.id

    