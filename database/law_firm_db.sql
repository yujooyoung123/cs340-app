-- Group 91
-- John Biersdorf, Jooyoung Yu
-- Law Firm Marketing and Schedule App

-- Disabling commits and foreign key checks
SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

--Creating Table Municipalities
CREATE OR REPLACE TABLE Municipalities (
    municipalityID int NOT NULL AUTO_INCREMENT,
    municipalityName varchar(65) NOT NULL,
    website varchar(45) NOT NULL,
    stateName varchar(20) NOT NULL,
    fileLocation varchar(45) NOT NULL,
    PRIMARY KEY (municipalityID)
);

--Creating Table Projects
CREATE OR REPLACE TABLE Projects (
    projectID int NOT NULL AUTO_INCREMENT,
    platMap varchar(45) NOT NULL,
    startingDate date NOT NULL,
    PRIMARY KEY (projectID)
);

--Creating Intersection Table Municipalities_Projects
CREATE OR REPLACE TABLE Municipalities_Projects (
    municipalityID int NOT NULL,
    projectID int NOT NULL,
    FOREIGN KEY (municipalityID) REFERENCES Municipalities(municipalityID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (projectID) REFERENCES Projects(projectID) ON DELETE CASCADE ON UPDATE CASCADE
);

--Creating Table Owners
CREATE OR REPLACE TABLE Owners (
    ownerID int NOT NULL AUTO_INCREMENT,
    ownerName varchar(65) NOT NULL,
    address varchar(128) NOT NULL,
    phoneNumber varchar(20) NOT NULL,
    email varchar(45) NOT NULL,
    projectID int NOT NULL,
    caseID int,
    PRIMARY KEY (ownerID),
    FOREIGN KEY (projectID) REFERENCES Projects(projectID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (caseID) REFERENCES Cases(caseID) ON DELETE SET NULL ON UPDATE CASCADE
);

--Creating Table Lawyers
CREATE OR REPLACE TABLE Lawyers (
    lawyerID int NOT NULL AUTO_INCREMENT,
    lawyerName varchar(50) NOT NULL,
    stateLicensed varchar(50) NOT NULL,
    PRIMARY KEY (lawyerID)
);

--Creating Table Cases
CREATE OR REPLACE TABLE Cases (
    caseID int NOT NULL AUTO_INCREMENT,
    caseNumber varchar(45),
    deadlineDate varchar(45),
    projectID int NOT NULL,
    lawyerID int NOT NULL,
    PRIMARY KEY (caseID),
    FOREIGN KEY (projectID) REFERENCES Projects(projectID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (lawyerID) REFERENCES Lawyers(lawyerID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- INSERT STATEMENTS --

-- Inserting Test Data into Municipalities
INSERT INTO Municipalities (municipalityID, municipalityName, website, stateName, fileLocation)
VALUES (5214, 'Jefferson', 'jeff.com', 'Georgia', 'files/mun/5214'),
(5547, 'Jackson', 'jackie.com', 'Washington', 'files/mun/5547'),
(5784, 'Keeowee', 'keeowee.com', 'South Carolina', 'files/mun/5784'),
(5466, 'Tacoseattle', 'conjuncture.com', 'South Carolina', 'files/mun/5466'),
(5888, 'Wilkin', 'wilco.com', 'Illinois', 'files/mun/5888');

-- Inserting Test Data into Projects
INSERT INTO Projects (projectID, platMap, startingDate)
VALUES (99445, 'jackmap.pdf', 19980516),
(98744, 'map2.pdf', 20130425),
(93368, 'simpsonsmap.pdf', 19121212),
(91727, 'erealdmap.pdf', 20070708),
(99363, 'harold.pdf', 20121219);

-- Inserting Test Data into Intersection Table Municipalities_Projects
INSERT INTO Municipalities_Projects (municipalityID, projectID)
VALUES (5214, 99445),
(5466, 91727),
(5784, 98744),
(5888, 93368),
(5547, 99363);

-- Inserting Test Data into Owners
INSERT INTO Owners (ownerID, ownerName, address, phoneNumber, email, projectID, caseID)
VALUES (7415, 'J. Schmit', '95 Circle Way', '123-456-7890', 'jschmit@gmail.com', 99445, 33100),
(7841, 'A. Bond', '2354 Ruby Drive', '987-654-3210', 'BondA@hotmail.com', 93368, 32505),
(7111, 'P.Gray', '998 Mead Ave.', '888-888-8888', 'Gray123@yahoo.com', 91727, 32323),
(7265, 'J. Green', '8825 Drive Road', '999-999-9991', 'Buffgn@gmail.com', 98744, 32322),
(7896, 'Y. Song', '231 Mingle Street', '848-878-8989', 'Music@msn.com', 99363, 38841);

-- Inserting Test Data into Lawyers
INSERT INTO Lawyers (lawyerID, lawyerName, stateLicensed) VALUES
(101, 'Phoenix Wright', 'FL'),
(102, 'Tom McAfee', 'FL'),
(105, 'Jack Harlow', 'GA'),
(108, 'Langford Crossing', 'WA'),
(103, 'Alex Anuller', 'FL');

-- Inserting Test Data into Cases
INSERT INTO Cases (caseID, caseNumber, deadlineDate, projectID, lawyerID) VALUES
(33100, 1, 09082050, 99445, 101),
(32505, 2, 07052029, 98744, 102),
(32323, 3, 12032063, 99363, 105),
(32322, 5, 12252099, 93368, 108),
(38841, 6, 08122035, 91727, 103);

-- Enabling commits and foreign key checks
SET FOREIGN_KEY_CHECKS=1;
COMMIT;