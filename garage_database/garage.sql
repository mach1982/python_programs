--Createting the user name a password 
--Change the passwod to you own password
--Default is 'password'
--Default user is garage but you cand chane that to sutit the clients needs

CREATE USER garage IDENTIFIED by password
DEFAULT TABLESPACE users TEMPORARY TABLESPACE
temp ACCOUNT unlock;

 
--Granting permissions 
GRANT CONNECT , RESOURCE TO garage;
GRANT CREATE SESSION to garage
grant create any table to garaage;
GRANT UNLIMITED TABLESPACE TO garage;
GRANT CREATE SEQUENCE TO garage; 

CREATE TABLE emp(
emp_id NUMBER(6) CONSTRAINT emp_emp_id_pk PRIMARY KEY,
emp_lname VARCHAR2(25) CONSTRAINT emp_emp_lname_nn NOT NULL,
emp_fname VARCHAR2(25)CONSTRAINT emp_emp_fname_nn NOT NULL,
emp_address VARCHAR2(50) ,
emp_basic_salary NUMBER(6),
--departmet are S=Sale W=workshp A=Admin M=Managemnt, and VIP
emp_department VARCHAR2(3),
emp_join_date DATE DEFAULT SYSDATE CONSTRAINT emp_emp_join_date_nn NOT NULL
);

CREATE TABLE sales_person(
sp_id number (6) CONSTRAINT sp_id_pk PRIMARY KEY,
sp_emp_id NUMBER(6) CONSTRAINT sp_emp_id_fk  REFERENCES emp(emp_id),
sp_comission number(6),
sp_car_reg_no VARCHAR2(20) CONSTRAINT sp_car_reg_no_fk REFERENCES car(car_reg_no),
sp_customer_id NUMBER(6) NOT NULL,
sp_car_sale_total_price NUMBER (6),
sp_cars_sold_per_month NUMBER(3)
);

CREATE TABLE mechanic(
mech_id NUMBER(6) CONSTRAINT mech_id PRIMARy KEY,
mech_emp_id NUMBER(6)  CONSTRAINT mech_emp_id_fk  REFERENCES emp(emp_id),
mech_job_id NUMBER (6) CONSTRAINT mech_job_id REFERENCES job(job_id) ,
mech_car_reg_no VARCHAR2(20) CONSTRAINT mech_car_reg_no_fk REFERENCES car(car_reg_no),
overtime_per_month NUMBER(6)
);

CREATE TABLE customer(
cust_id NUMBER (6) CONSTRAINT customer_cust_id_pk PRIMARY KEY,
cust_lname VARCHAR2(25) NOT NULL,
cust_fname VARCHAR2(25) NOT NULL,
cust_address VARCHAR2(50),
cust_emp_id NUMBER(6) CONSTRAINT cust_emp_id_fk  REFERENCES emp(emp_id),
cust_car_reg_no VARCHAR2(20) CONSTRAINT customer_car_reg_no_fk REFERENCES car(car_reg_no),
trade_in_price NUMBER (6),
car_sale_price NUMBER (6)

);

CREATE TABLE car(
car_vin NUMBER (7) ,
car_reg_no VARCHAR2(20) CONSTRAINT car_reg_pk PRIMARY KEY ,
car_make VARCHAR2(25) NOT NULL ,
car_model VARCHAR(10) NOT NULL,
fuel VARCHAR2(1) CONSTRAINT car_fule_ck CHECK (fule IN('P','D','E','H')),
car_price NUMBER (6),
new_used VARCHAR2 (1)CONSTRAINT car_newused_ck CHECK (new_used IN('N','U')),
in_workshop VARCHAR2 (1) CONSTRAINT in_workshop_ck CHECK (in_workshop in('Y','N')),
sold VARCHAR (1) CONSTRAINT sold_ck CHECK (sold in('Y','N'))
);

CREATE TABLE job(
job_id NUMBER(6) CONSTRAINT job_id_pk PRIMARY KEY,
star_time DATE,
end_time DATE ,
job_emp_id NUMBER(6)CONSTRAINT job_emp_id_fk  REFERENCES emp(emp_id),
job_car_reg_no VARCHAR2(20)CONSTRAINT job_car_reg_no_fk REFERENCES car(car_reg_no)
);

CREATE TABLE part(
prat_no VARCHAR(20)  CONSTRAINT part_id_pk PRIMARY KEY ,
manufacture VARCHAR(50),
type VARCHAR2(15),
supplier VARCHAR2(20),
price NUMBER(6),
part_job_id NUMBER(6)CONSTRAINT part_job_id_fk REFERENCES job(job_id),
part_emp_id NUMBER(6) CONSTRAINT jobg_emp_id_fk REFERENCES emp(emp_id),
part_car_reg_no VARCHAR2(20) CONSTRAINT part_car_reg_no_fk REFERENCES car(car_reg_no)
);


drop table employess;