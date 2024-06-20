DROP DATABASE IF EXISTS DBMS;
CREATE DATABASE DBMS;
USE DBMS;
CREATE TABLE Users(
	UID INT NOT NULL AUTO_INCREMENT,
    BUDGET INT DEFAULT 0,
    UName VARCHAR(255) NOT NULL,
    UPassword VARCHAR(255) NOT NULL,
    UAccount VARCHAR(255) NOT NULL,
    UNickname VARCHAR(255) DEFAULT 'Nickname',
    isrightHander BOOLEAN DEFAULT TRUE,
    isDarkMode BOOLEAN DEFAULT FALSE,
    NoticeTime TIME DEFAULT '21:00:00', -- NULL/None indicates that users do not want to have a specific notice time
    PRIMARY KEY (UID)
);

-- 一個wallet可以有多個goal goal of wallet
-- 一個wallet可以有多個ledger ledger of wallet
CREATE TABLE Wallets(
    UID INT NOT NULL,
    WID INT AUTO_INCREMENT NOT NULL,  -- Wallet ID is unique wid =0
    WName VARCHAR(255) NOT NULL,
    -- LedgerSum INT DEFAULT 0 NOT NULL,
    PRIMARY KEY (WID)
);

-- 一個goal可以有多個ledger
CREATE TABLE Goals(
    UID INT NOT NULL,
    GID INT AUTO_INCREMENT NOT NULL,
    GName VARCHAR(255) NOT NULL,
    GTargetAmount INT DEFAULT 0 NOT NULL,
    GCurrentAmount INT DEFAULT 0 NOT NULL,
    GDate DATE NOT NULL,
    PRIMARY KEY (GID)
);

CREATE TABLE Ledgers(
    -- UID INT NOT NULL,
    WID INT NOT NULL, -- wid =0 
    LID INT AUTO_INCREMENT NOT NULL,
    -- LedgerSum INT DEFAULT 0 NOT NULL,
    LName VARCHAR(255) NOT NULL,
    PRIMARY KEY (LID)
);

CREATE TABLE Datas(
	UID INT NOT NULL,
    LName VARCHAR(255) DEFAULT NULL,
	DID INT AUTO_INCREMENT NOT NULL,
    Price INT DEFAULT 0 NOT NULL,
    DName VARCHAR(255) NOT NULL,
    DType VARCHAR(255) NOT NULL,
    DDate DATE NOT NULL, -- Front-end should provide current date
    PRIMARY KEY (DID)
);

CREATE TABLE DataToGoal(
    DID INT NOT NULL,
    GID INT NOT NULL,
    PRIMARY KEY (DID, GID)
);

CREATE TABLE DataToLedger(
    DID INT NOT NULL,
    LID INT NOT NULL,
    PRIMARY KEY (DID, LID)
);

ALTER TABLE Wallets -- a user can have multiple wallets, so add UID to know wallet's owner
ADD CONSTRAINT `fk_Wallets_to_Users_UID` FOREIGN KEY (UID) REFERENCES Users(UID)ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Ledgers -- a wallet can have multiple ledgers, so add WID to know which wallet the ledger belongs to
ADD CONSTRAINT `fk_Ledgers_to_Wallets_WID` FOREIGN KEY (WID) REFERENCES Wallets(WID)ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Datas -- a user can have multiple wallets, so add UID to know wallet's owner
ADD CONSTRAINT `fk_Data_to_Users_UID` FOREIGN KEY (UID) REFERENCES Users(UID)ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Goals
ADD CONSTRAINT `fk_Goals_to_Users_UID` FOREIGN KEY (UID) REFERENCES Users(UID)ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE DataToGoal
ADD CONSTRAINT `fk_DataToGoal_to_Datas_DID` FOREIGN KEY (DID) REFERENCES Datas(DID)ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE DataToGoal
ADD CONSTRAINT `fk_DataToGoal_to_Goals_GID` FOREIGN KEY (GID) REFERENCES Goals(GID)ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE DataToLedger
ADD CONSTRAINT `fk_DataToLedger_to_Datas_DID` FOREIGN KEY (DID) REFERENCES Datas(DID)ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE DataToLedger
ADD CONSTRAINT `fk_DataToLedger_to_Ledgers_LID` FOREIGN KEY (LID) REFERENCES Ledgers(LID)ON DELETE CASCADE ON UPDATE CASCADE;