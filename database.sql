DROP DATABASE IF EXISTS JiDB;
CREATE DATABASE JiDB;
USE JiDB;
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
    WID INT AUTO_INCREMENT NOT NULL,  -- Wallet ID is unique
    WName VARCHAR(255) NOT NULL,
    LedgerSum INT DEFAULT 0 NOT NULL,
    PRIMARY KEY (WID)
);

-- 一個goal可以有多個ledger
CREATE TABLE Goals(
    -- UID INT NOT NULL, -- 應該不需要 if we have WID we know the user
    WID INT NOT NULL,
    GName VARCHAR(255) NOT NULL,
    GTargetAmount INT DEFAULT 0 NOT NULL,
    GCurrentAmount INT DEFAULT 0 NOT NULL,
    GDate DATE NOT NULL,
    PRIMARY KEY (WID, GName)
);

CREATE TABLE Ledgers(
    -- UID INT NOT NULL,
    WID INT NOT NULL,
    LedgerSum INT DEFAULT 0 NOT NULL,
    LName VARCHAR(255) NOT NULL,
    PRIMARY KEY (WID ,LName)
);


CREATE TABLE LedgersOfGoal(
    -- UID INT NOT NULL,
    WID INT NOT NULL,
    GName VARCHAR(255) NOT NULL,
    LName VARCHAR(255) NOT NULL,
    PRIMARY KEY (WID, GName, LName)
);

CREATE TABLE Datas(
UID INT NOT NULL,
    WID INT NOT NULL,
    LName VARCHAR(255) NOT NULL,
DID INT AUTO_INCREMENT NOT NULL,
    Price INT DEFAULT 0 NOT NULL,
    DName VARCHAR(255) NOT NULL,
    DType VARCHAR(255) NOT NULL,
    DDate DATE NOT NULL, -- Front-end should provide current date
    PRIMARY KEY (DID)
);


ALTER TABLE Wallets -- a user can have multiple wallets, so add UID to know wallet's owner
ADD CONSTRAINT `fk_Wallets_to_Users_UID` FOREIGN KEY (UID) REFERENCES Users(UID)ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Goals -- a wallet can have multiple goals, so add WID to know which wallet the goal belongs to 
ADD CONSTRAINT `fk_Goal_to_Wallets_UID_WName` FOREIGN KEY (WID) REFERENCES Wallets(WID)ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Ledgers -- a wallet can have multiple ledgers, so add WID to know which wallet the ledger belongs to
ADD CONSTRAINT `fk_Ledgers_to_Users_UID` FOREIGN KEY (WID) REFERENCES Wallets(WID)ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE LedgersOfGoal -- a goal can have multiple ledgers, so add WID and GName to know which goal the ledger belongs to
ADD CONSTRAINT `fk_LedgersOfGoal_to_Goal_WID_GName` FOREIGN KEY (WID, GName) REFERENCES Goals(WID, GName)ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE LedgersOfGoal -- a ledger can belong to multiple goals, so add LName to know which ledger the goal belongs to
ADD CONSTRAINT `fk_LedgersOfGoal_to_Ledgers_LName` FOREIGN KEY (WID,LName) REFERENCES Ledgers(WID,LName)ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Datas
ADD CONSTRAINT `fk_Datas_to_Ledgers_LID` FOREIGN KEY (WID, LName) REFERENCES Ledgers(WID, LName) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Datas -- a user can have multiple wallets, so add UID to know wallet's owner
ADD CONSTRAINT `fk_Data_to_Users_UID` FOREIGN KEY (UID) REFERENCES Users(UID)ON DELETE CASCADE ON UPDATE CASCADE