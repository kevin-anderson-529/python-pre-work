CREATE TABLE `new_schema`.`new_table`(
	ID number INT NOT NULL,
	`Price` VARCHAR(45) NULL,
	`Item`	VARCHAR(45) NULL,
	PRIMARY KEY(`ID number`));
INSERT INTO `new_schema`.`new_table` (`ID number`, `Price`, `Item`) VALUES ('4672481', '5.99', 'Eggs');
INSERT INTO `new_schema`.`new_table` (`ID number`, `Price`, `Item`) VALUES ('4672424', '3.99', 'Milk');
SELECT * FROM new_schema.new_table;


