from mysql import connector

my_connection = connector.connect(
    host="localhost",
    user="root",
    password="4d?2N5qJ",
    database="banking" )
my_cursor = my_connection.cursor()
""" Task 3: Write the SQL statement to find the Doctor names and all of their patients  """

my_cursor.execute("""
SELECT 
    CONCAT(Doctor.Name, ' ', Doctor.Fname) AS DoctorFullName,
    CONCAT(Patient.Name, ' ', Patient.Fname) AS PatientFullName
FROM Doctor
LEFT JOIN Patient ON Doctor.dr_code = Patient.dr_code
ORDER BY Doctor.Name, Patient.Name;
""")