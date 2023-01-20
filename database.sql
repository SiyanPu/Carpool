DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS ride_offering;
DROP TABLE IF EXISTS ride_request;
DROP TABLE IF EXISTS success_ride;

CREATE TABLE users (user_id INTEGER PRIMARY KEY,
                    user_name TEXT,
                    password TEXT,
                    email TEXT,
                    gender TEXT,
                    age INTEGER,
                    major TEXT,
                    bestline TEXT);

INSERT INTO users (user_id, user_name, password, email, gender, age, major, bestline)
   VALUES (1,'hello1', '123password', 'hello1@yale.edu', 'female', 18, 'Computer Science', 'I offer you lean streets, desperate sunsets, the moon of the jagged suburbs.');
INSERT INTO users (user_id, user_name, password, email, gender, age, major, bestline)
   VALUES (2,'hello2', '123password', 'hello2@yale.edu', 'female', 20, 'Animal Science', 'I offer you the loyalty of a man who has never been loyal.');
INSERT INTO users (user_id, user_name, password, email, gender, age, major, bestline)
   VALUES (3,'hello3', '123password', 'hello3@yale.edu', 'male', 19, 'Undeclared', 'I offer you whatever insight my books may hold.');
INSERT INTO users (user_name, password, email, gender, age, major, bestline)
   VALUES ('hello4', '123password', 'hello4@yale.edu', 'male', 22, 'Computer Science', 'I can give you my loneliness, my darkness, the hunger of my heart.');

CREATE TABLE ride_offering (offer_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    destination TEXT,
                    departure TEXT,
                    date_time TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(user_id));

CREATE TABLE ride_request (request_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    destination TEXT,
                    departure TEXT,
                    date_time TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(user_id));
INSERT INTO ride_offering (offer_id, user_id, destination, departure, date_time)
   VALUES (1, 1, "BDL", "Yale", "2022-11-03 19:00:00");
INSERT INTO ride_offering (offer_id, user_id, destination, departure, date_time)
   VALUES (2, 1, "EWR", "Yale", "2022-11-04 19:00:00");
INSERT INTO ride_offering (offer_id, user_id, destination, departure, date_time)
   VALUES (3, 1, "LGA", "Yale", "2022-11-05 19:00:00");
INSERT INTO ride_offering (offer_id, user_id, destination, departure, date_time)
   VALUES (4, 2, "BDL", "Yale", "2022-11-03 20:00:00");

INSERT INTO ride_request (request_id, user_id, destination, departure, date_time)
   VALUES (1, 2, "BDL", "Yale", "2022-11-03 19:00:00");

CREATE TABLE success_ride (ride_id INTEGER PRIMARY KEY,
                           offer_id INTEGER,
                           offer_user_id INTEGER,
                           request_id INTEGER,
                           request_user_id INTEGER,
                           destination TEXT,
                           departure TEXT,
                           date_time TEXT,
                           FOREIGN KEY(offer_id) REFERENCES ride_offering(offer_id),
                           FOREIGN KEY(request_id) REFERENCES ride_request(request_id),
                           FOREIGN KEY(offer_user_id) REFERENCES users(user_id),
                           FOREIGN KEY(request_user_id) REFERENCES users(user_id));

INSERT INTO success_ride (offer_id, offer_user_id, request_id, request_user_id, destination, departure, date_time)
   VALUES (1, 1, 1, 1, "BDL", "Yale", "2022-11-03 19:00:00");