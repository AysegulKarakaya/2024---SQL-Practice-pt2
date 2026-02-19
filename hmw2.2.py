from mysql import connector

my_connection = connector.connect(
    host="localhost",
    user="root",
    password="4d?2N5qJ",
    database="banking" )
my_cursor = my_connection.cursor()
""" Task  2:Write  the  DML  statements  to  insert  sample  data  to  every  table. """

my_cursor.execute("""
INSERT INTO Doctor (dr_code, Name, Fname, Gender, Address, Designation)
VALUES 
    (1, 'Some', 'Guy', 'Male', 'Some Adress', 'Designation1');

INSERT INTO Staff (staff_id, Name, Dept, Gender, Address, Cell, dr_code)
VALUES 
    (1, 'Someone', 'Deaprtment', 'Female', 'Another adress', '05000000000', 2);

INSERT INTO Patient (pat_id, Name, Fname, Gender, Address, Tell, dr_code)
VALUES 
    (1, 'Another', 'Guy', 'Male', 'Wow Adress', '05000000001', 3);

INSERT INTO PatientDiagnosis (DiagNo, Diagdetails, Remark, Diagdate, Other, pat_id)
VALUES 
    (1, 'Tummyache', 'Details', '2024-11-27', 'Other text', 1);

INSERT INTO Bill (Billno, Patname, Drname, Datetime, Amount, pat_id)
VALUES 
    (1, 'Patient Guy', 'Dr. John Smith', '2024-11-27', 20000, 1);
""")