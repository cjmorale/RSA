
CREATE TABLE User_info
(
ID int PRIMARY KEY AUTO_INCREMENT,
Name varchar(255),
Login varchar (255),
Email_Address varchar(255),
Password varchar(2550),
Modulas varchar(2550),
Exp varchar(2550)
)

SELECT * FROM users.User_info;

INSERT INTO User_info (Name, Login, Email_Address, Password)
VALUES ("Carlo Morales","cjmorale","cjmorale2004@gmail.com","Overland04");
