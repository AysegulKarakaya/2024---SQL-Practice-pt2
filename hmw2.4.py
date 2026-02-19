from mysql import connector

my_connection = connector.connect(
    host="localhost",
    user="root",
    password="4d?2N5qJ",
    database="banking" )
my_cursor = my_connection.cursor()
""" Task 4: Write the SQL statement that will return the patient’s name, doctor name the total debt for each patient 
where they patient fee is over 100. The total order value for a Patient debt is the sum of all the bills related to the 
patient.   """

my_cursor.execute("""
SELECT 
    CONCAT(Patient.Name, ' ', Patient.Fname) AS PatientFullName,
    CONCAT(Doctor.Name, ' ', Doctor.Fname) AS DoctorFullName,
    SUM(Bill.Amount) AS TotalDebt
FROM Patient
JOIN Bill ON Patient.pat_id = Bill.pat_id
JOIN Doctor ON Patient.dr_code = Doctor.dr_code
GROUP BY Patient.pat_id, Doctor.dr_code
HAVING SUM(CAST(Bill.Amount AS DECIMAL(10,2))) > 100
ORDER BY TotalDebt DESC;
""")