#DDL:
	#Create Database:
		CREATE DATABASE epsilon;
	#Show datases:
		show databases;
	#Connecting to perticular DB:
		use epsilon;
	
	#Create TABLE:
		create table employee (ID int, NAME varchar(100),SALARY int, AGE int, GENDER varchar(20));
	#Show tables:
		show tables;
	#dropping table
		DROP TABLE employee;
	#Drooping data base
		DROP DATABASE epsilon;
	
	
#DML:
	#Copy/Insert Operation
		insert into employee (ID,NAME,SALARY,AGE,GENDER) values (8,"Vijay",100000,23,"Male");
		insert into employee (NAME,SALARY,AGE,GENDER,ID) values ("Shreyas",100000,23,"Female",9);
		insert into employee values (10,'Faraz',100000,23,'Male');	
		insert into employee values (11,'Vivek',23,100000,'Male');	
		insert into employee values ('Dhruvi',23,100000,'Female',12);..........Column Data Type & Data Type provided is violated
	
	#Read Opration
		select * from employee;                         All COLUMNS from table
		select ID,NAME from employee;                   Selected COLUMNS from Table
		select count(*) from employee;                  Count of All Records
		select distinct SALARY from employee;           To get DISTINCT values of Column SALARY
		select count(distinct SALARY) from employee;    Count of Distinct Values of SALARY column
		SELECT DISTINCT NAME,SALARY FROM employee;      NAME|SALARY......If Name as well as Salary are same for any 2 or more records then they would be considered as duplicates as per the given columns
	#Delete
		DELETE * FROM employe WHERE AGE=23;
		DELETE * FROM employee;
		TRUNCATE TABLE employee;  #Faster than delete
		
	#Update 
		UPDATE employee SET SALARY=200000 WHERE GENDER="Female";
		UPDATE employee SET SALARY=150000, AGE=30 WHERE GENDER="Female";
		
    #Aggregate Operations: Aggregation means accumulative on the total records
	
		select count(*) from employee; .....COUNT
		select min(salary) from employee;....MIN
		select max(salary) from employee;....MAX
		select avg(salary) from employee;....AVG
		select sum(salary) from employee;....SUM
		select * from employee limit 4;
	
	#Filtering Operations: Filter the rows based on conditions that are going to be applied
		SELECT * FROM employee WHERE age<30;
		SELECT NAME,Salary FROM employee WHERE age<30;
		SELECT * FROM employee WHERE NAME ="Nandini";
		SELECT * FROM employee WHERE NAME IN ('Nandini','Akshay');
		SELECT * FROM employee WHERE Age<30 AND NAME IN ('Nandini','Akshay'); #A intersection B
		SELECT * FROM employee WHERE Age<30 OR NAME IN ('Nandini','Akshay');  #A Union B
		SELECT * FROM employee WHERE (Age<30 AND NAME IN ('Nandini','Akshay')) OR (SALARY<200000 AND GENDER="Female");  #A Union B
		SELECT * FROM employee WHERE NAME LIKE 'Nan%';   #  % Regex
		SELECT * FROM employee WHERE NAME LIKE '%an%';   #  % Regex
	
	#Grouping Operatins: Group By clause would applied when we like to grup the data based on COLUMNS
						 The result of Group By operation is always going to be aggregated output
		
		SELECT SALARY, COUNT(*) FROM employee GROUP BY SALARY;
		SELECT SALARY, AGE,COUNT(*) FROM employee GROUP BY Salary,Age;
		SELECT AGE,SUM(SALARY) FROM employee GROUP BY AGE;
		SELECT AGE, COUNT(*) FROM employee GROUP BY AGE;
	#Order By Clause : T order the resultset either in ASC or in DESC
	
		SELECT AGE AS AGE, COUNT(*) AS CNT FROM employee GROUP BY AGE ORDER BY AGE DESC;
		SELECT AGE AS AGE, COUNT(*) AS CNT FROM employee GROUP BY AGE ORDER BY CNT DESC;
		
	#Having clause
		Co clause with Group BY
		This clause is used to filter the aggregated output resulted out of Group By clause
		
		SELECT AGE AS AGE,COUNT(*) AS CNT FROM employee GROUP BY AGE HAVING AGE<40;  #GROUP BY AGE THEN FILTER 
		SELECT AGE AS AGE,COUNT(*) AS CNT FROM employee GROUP BY AGE HAVING AGE<40 ORDER BY AGE DESC;

	
	Difference between DISTINCT Vs GROUP BY
		Distinct clause is used only to get distinct values. But it will not return any Aggregated result set as output
		Group By clause is used to group the values based on column/s and it will always returns aggregated output
		
		
	#Inner Queries
		SELECT * FROM (SELECT AGE AS AGE,COUNT(*) AS CNT FROM employee GROUP BY AGE HAVING AGE<90 ORDER BY AGE DESC)A WHERE A.AGE>30 AND A.CNT>1;
	

	Indexing:
		How can I identify any record uniquely?
		Indexing n the table will help us t identify the records uniquely.
		
		Primary KEY
		Socondary Key/Foreign Key
		
	#Join Operations:
		
		SELECT s.STD_ID,s.STD_NAME,s.STD_MARKS,c.COLL_NAME,c.COLL_LOCATION FROM student s, college c WHERE s.STD_COLL_ID=c.COLL_ID; 
		SELECT s.STD_ID,s.STD_NAME,s.STD_MARKS,c.COLL_NAME,c.COLL_LOCATION FROM student s INNER JOIN college c ON s.STD_COLL_ID=c.COLL_ID; 
		SELECT * FROM student s LEFT JOIN college c ON s.STD_COLL_ID=c.COLL_ID;  #Left Join
		SELECT * FROM student s RIGHT JOIN college c ON s.STD_COLL_ID=c.COLL_ID; # Right Join
		SELECT * FROM student s CROSS JOIN college c ON s.STD_COLL_ID=c.COLL_ID; #Cross Join/Full
	
	#Stored Procedures