from mysql import connector

my_connection = connector.connect(
    host="localhost",
    user="root",
    password="4d?2N5qJ",
    database="banking" )
my_cursor = my_connection.cursor()
""" Write  the  SQL  statement  to  find  the  total  number  of  patients  treated  by  each  doctor, including 
doctors who have not treated any patients. """

my_cursor.execute("""
SELECT 
    CONCAT(Doctor.Name, ' ', Doctor.Fname) AS DoctorFullName,
    COUNT(Patient.pat_id) AS TotalPatients
FROM Doctor
LEFT JOIN Patient ON Doctor.dr_code = Patient.dr_code
GROUP BY Doctor.dr_code
ORDER BY DoctorFullName;
""")