-- Group 91
-- John Biersdorf, Jooyoung Yu
-- Law Firm Marketing and Schedule App

-- Fetch details of a municipality
SELECT municipalityName, website, stateName, fileLocation
 FROM Municipalities WHERE municipalityID = :municipalityID;

--Fetch details of a Project
SELECT * FROM Projects WHERE projectID = :projectID

--Fetch details of an Owner
SELECT ownerName, address, phoneNumber, email
 FROM Owners WHERE ownerID = :ownerID;

 --Fetch details of a Lawyer
SELECT lawyerName, stateLicensed
 FROM Lawyers WHERE LawyerID = :LawyerID;

 --Fetch details of a Case
SELECT * FROM Cases WHERE caseID = :caseID


-- Add a new Municipality
INSERT INTO Municipalities (municipalityName, website, stateName, fileLocation) 
VALUES (:municipalityName, :website, :stateName, :fileLocation);

-- Add a new Project
INSERT INTO Projects (platMap, startingDate) 
VALUES (:platMap, :startingDate);

-- Add a new Owner
INSERT INTO Owners (ownerName, address, phoneNumber, email) 
VALUES (:ownerName, :address, :phoneNumber, :email);

-- Add a new Lawyers
INSERT INTO Lawyers (lawyerName, stateLicensed) 
VALUES (:lawyerName, :stateLicensed);


-- Update the status of caseNumber when it assigned by courts
UPDATE Cases SET caseNumber = :caseNumber WHERE caseID = :caseID;

-- Update the status of deadlineDate when next deadline is known
UPDATE Cases SET deadlineDate = :deadlineDate WHERE caseID = :caseID;

-- Update an Municipality's data
UPDATE Municipalities 
SET municipalityName = :municipalityName, website = :website, 
	stateName = :stateName, fileLocation = :fileLocation
WHERE municipalityID = :municipalityID;

-- Update an Owner's data
UPDATE Owners 
SET ownerName = :ownerName, address = :address, phoneNumber = :phoneNumber, email = :email
WHERE ownerID = :ownerID;

-- Update an Lawyer's data
UPDATE Lawyers 
SET firstName = :firstName, lastName = :lastName, email = :email, role = :role
WHERE employeeID = :employeeID;


-- Delete a record of a municipality if it no longer needs to be tracked
DELETE FROM Municipalities WHERE municipalityID = :municipalityID;

-- Delete a record of a project if it no longer needs to be tracked
DELETE FROM Projects WHERE projectID = :projectID;

-- Delete a record of an onwer if it no longer needs to be tracked
DELETE FROM Owners WHERE ownerID = :ownerID;

-- Delete a record of a Lawyer if it no longer needs to be tracked
DELETE FROM Lawyers WHERE lawyerID = :lawyerID;

-- Delete a record of a case if it no longer needs to be tracked
DELETE FROM Case WHERE caseID = :caseID;
