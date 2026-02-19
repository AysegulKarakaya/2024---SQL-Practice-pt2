from mysql import connector

my_connection = connector.connect(
    host="localhost",
    user="root",
    password="4d?2N5qJ",
    database="banking" )
my_cursor = my_connection.cursor()
""" create tables 
"""
my_cursor.execute("""
CREATE TABLE Doctor (
dr_code INTEGER,
Name VARCHAR(32),
Fname VARCHAR(32),
Gender ENUM('Male', 'Female', 'Other'),
Address VARCHAR(260),
designation VARCHAR(64),
PRIMARY KEY (dr_code));

CREATE TABLE staff (
staff_id INTEGER,
Name VARCHAR(32),
Dept VARCHAR(32),
Gender ENUM('Male', 'Female', 'Other'),
Address VARCHAR(260),
Cell VARCHAR(11),
dr_code INTEGER,
PRIMARY KEY (staff_id),
FOREIGN KEY (dr_code) REFERENCES Doctor(dr_code));

CREATE TABLE Patient (
pat_id INTEGER,
Name VARCHAR(32),
Fname VARCHAR(32),
Gender ENUM('Male', 'Female', 'Other'),
Address VARCHAR(260),
Tell VARCHAR(11),
dr_code INTEGER,
PRIMARY KEY (pat_id),
FOREIGN KEY (dr_code) REFERENCES Doctor(dr_code));

CREATE TABLE PatientDiagnosis (
DiagNo INTEGER,
Diagdetails VARCHAR(260),
Remark TEXT,
Diagdate DATE,
Other TEXT,
pat_id INTEGER,
PRIMARY KEY (DiagNo),
FOREIGN KEY (pat_id) REFERENCES Patient(pat_id));

CREATE TABLE Bill (
Billno INTEGER,
Patname VARCHAR(64),
Drname VARCHAR(64),
Datetime DATE,
Amount INTEGER,
pat_id INTEGER,
PRIMARY KEY (Billno),
FOREIGN KEY (pat_id) REFERENCES Patient(pat_id));
""")