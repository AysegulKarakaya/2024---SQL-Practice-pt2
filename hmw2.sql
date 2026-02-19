/*Task  2:Write  the  DML  statements  to  insert  sample  data  to  every  table.*/
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


/*Task 3: Write the SQL statement to find the Doctor names and all of their patients*/
SELECT 
    CONCAT(Doctor.Name, ' ', Doctor.Fname) AS DoctorFullName,
    CONCAT(Patient.Name, ' ', Patient.Fname) AS PatientFullName
FROM Doctor
LEFT JOIN Patient ON Doctor.dr_code = Patient.dr_code
ORDER BY Doctor.Name, Patient.Name;


/*Task 4: Write the SQL statement that will return the patient’s name, doctor name the total debt for each patient where they patient fee is over 100. 
The total order value for a Patient debt is the sum of all the bills related to the patient.*/
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


/*Task  5: Write  the  SQL  statement  to  find  the  total  number  of  patients 
treated  by  each  doctor, including doctors who have not treated any patients. */
SELECT 
    CONCAT(Doctor.Name, ' ', Doctor.Fname) AS DoctorFullName,
    COUNT(Patient.pat_id) AS TotalPatients
FROM Doctor
LEFT JOIN Patient ON Doctor.dr_code = Patient.dr_code
GROUP BY Doctor.dr_code
ORDER BY DoctorFullName;








