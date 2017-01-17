## 2. Adding columns ##

ALTER TABLE facts
ADD leader text;

## 6. Creating a table with relations ##

create table factbook.states(
id integer,
name text,
area integer,
country,integer,
FOREIGN KEY(country) REFERENCES facts(id)
);

## 7. Querying across foreign keys ##

SELECT * from landmarks
INNER JOIN facts
ON landmarks.country == facts.id;

## 8. Types of joins ##

SELECT * from landmarks
LEFT OUTER JOIN facts
ON landmarks.country == facts.id;