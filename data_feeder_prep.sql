DROP DATABASE eNursery;
CREATE DATABASE eNursery;
USE eNursery;

CREATE TABLE Login_Details (
    Username VARCHAR(255) NOT NULL,
    Password TEXT NOT NULL,
    PRIMARY KEY(Username)
);

CREATE TABLE Customer_Details (
    Username VARCHAR(255) NOT NULL,
    Password TEXT NOT NULL,
    Contact TEXT NOT NULL,
    eMail TEXT NOT NULL,
    Address_1 TEXT NOT NULL,
    Address_2 TEXT NOT NULL,
    Address_3 TEXT,
    Pincode INT NOT NULL,
    PRIMARY KEY(Username)
);

CREATE TABLE Plant_Details (
    Serial INT NOT NULL,
    Name TEXT NOT NULL,
    Stock INT DEFAULT 0,
    Price INT DEFAULT 100,
    Botanical_Name TEXT NOT NULL,
    Tree INT DEFAULT 0,
    Flower INT DEFAULT 0,
    Edible INT DEFAULT 0,
    Descp TEXT NOT NULL,
    PRIMARY KEY(Serial)
);

CREATE TABLE Orders (
    Username VARCHAR(255) NOT NULL,
    Contact TEXT NOT NULL,
    Status VARCHAR(100) DEFAULT 'Pending',
    Date_Time TIMESTAMP NOT NULL,
    Serial INT NOT NULL,
    Quantity INT DEFAULT 1
);

COMMIT;
