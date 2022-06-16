------- Constraint hinzufügen --------------------
-- damit wird sichergestellt, dass keine Dubletten 
-- hochgeladen werden
ALTER TABLE capstone.aviation_jobs
ADD CONSTRAINT job_id_unique UNIQUE(job_id);
--------------------------------------------------

DELETE FROM capstone.aviation_jobs
WHERE id > 250;

ALTER TABLE capstone.aviation_jobs
DROP COLUMN recruiter_nam;



ALTER TABLE capstone.aviation_jobs 
ADD COLUMN country TEXT;
-------
UPDATE capstone.aviation_jobs  
SET country = SPLIT_PART(job_location,',' ,3);
-----

SELECT SPLIT_PART(job_location,',' ,1) AS city,
	   SPLIT_PART(job_location,',' ,2) AS region,
	   SPLIT_PART(job_location,',' ,3) AS country
FROM capstone.aviation_jobs;

-------

SELECT *
FROM capstone.aviation_jobs;  

UPDATE capstone.aviation_jobs
SET country = 'France'
WHERE id = 339;
----------------------------------

SELECT TRIM(BOTH ' ' FROM country) AS country2
FROM capstone.aviation_jobs;            
 
UPDATE capstone.aviation_jobs  
SET job_id = CONCAT(posted_date,'_',city,'_',job_title);

ALTER TABLE capstone.aviation_jobs 
DROP COLUMN job_location;

SELECT *
FROM capstone.aviation_jobs
WHERE city = 'Langenhagen';

SELECT CONCAT(posted_date,'_',city,'_',job_title) AS job_id2
FROM capstone.aviation_jobs;
------------------------------


SELECT count(DISTINCT job_title) 
FROM capstone.aviation_jobs;

ALTER TABLE capstone.aviation_jobs
ADD COLUMN full_text_en TEXT;

ALTER TABLE capstone.aviation_jobs
ADD COLUMN job_title_en TEXT;

ALTER TABLE capstone.aviation_jobs
ADD COLUMN us_state TEXT;

SELECT *
FROM jobs_translated
WHERE id > 2500;

SELECT *
FROM jobs_translated
WHERE country = 'Germany';

UPDATE jobs_translated 
SET us_state = 'Germany'
WHERE id = 583;

ALTER TABLE jobs_translated 
RENAME COLUMN us_state TO state;

UPDATE jobs_translated 
SET state = 'Bayern'
WHERE id = 583;

SELECT *
FROM capstone.jobs_translated
LIMIT 15;
--------------------

SELECT TRIM(BOTH ' ' FROM city) AS trimmed
FROM jobs_translated;

SELECT *
FROM jobs_translated
WHERE country = 'Germany';

UPDATE jobs_translated 
SET country = 'United States'
WHERE country = 'USA';

UPDATE jobs_translated 
SET state = 'North Rhine-Westphalia'
WHERE city = 'Aachen';

SELECT DISTINCT city
FROM jobs_translated
WHERE country = 'Germany';

SELECT *
FROM jobs_translated
WHERE city = 'Wessling';

SELECT COUNT(*)
FROM jobs_translated;
-------------------------------------

UPDATE jobs_translated SET state = 'Rhineland Palatinate' WHERE city = 'Hahn';
UPDATE jobs_translated SET state = 'Baden Wurttemberg' WHERE city = 'Schwäbisch Hall';
UPDATE jobs_translated SET state = 'Brandenburg' WHERE city = 'Dahlewitz';
UPDATE jobs_translated SET state = 'Lower Saxony' WHERE city = 'Langenhagen';
UPDATE jobs_translated SET state = 'Saxony-Anhalt' WHERE city = 'Silberhütte';
UPDATE jobs_translated SET state = 'North Rhine-Westphalia' WHERE city = 'Radevormwald';
UPDATE jobs_translated SET state = 'Saxony' WHERE city = 'Radebeul';
UPDATE jobs_translated SET state = 'Baden Wurttemberg' WHERE city = 'Stuttgart';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Augsburg';
UPDATE jobs_translated SET state = 'North Rhine-Westphalia' WHERE city = 'Weeze';
UPDATE jobs_translated SET state = 'Lower Saxony' WHERE city = 'Brunswick';
UPDATE jobs_translated SET state = 'Saxony' WHERE city = 'Leipzig';
UPDATE jobs_translated SET state = 'Baden Wurttemberg' WHERE city = 'Dettingen an der Erms';
UPDATE jobs_translated SET state = 'Hesse' WHERE city = 'Bensheim';
UPDATE jobs_translated SET state = 'Lower Saxony' WHERE city = 'Nordenham';
UPDATE jobs_translated SET state = 'Schleswig-Holstein' WHERE city = 'Kiel';
UPDATE jobs_translated SET state = 'Baden Wurttemberg' WHERE city = 'Friedrichshafen';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Röthenbach an der Pegnitz';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Erlangen';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Penzberg';
UPDATE jobs_translated SET state = 'Hesse' WHERE city = 'Raunheim';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Taufkirchen';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Gilching';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Vilshofen';
UPDATE jobs_translated SET state = 'Lower Saxony' WHERE city = 'Hildesheim';
UPDATE jobs_translated SET state = 'North Rhine-Westphalia' WHERE city = 'Neuss';
UPDATE jobs_translated SET state = 'Rhineland Palatinate' WHERE city = 'Ingelheim am Rhein';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Feucht';
UPDATE jobs_translated SET state = 'Lower Saxony' WHERE city = 'Göttingen';
UPDATE jobs_translated SET state = 'Hesse' WHERE city = 'Frankfurt';
UPDATE jobs_translated SET state = 'Hesse' WHERE city = 'Darmstadt';
UPDATE jobs_translated SET state = 'Saxony' WHERE city = 'Schkeuditz';
UPDATE jobs_translated SET state = 'Hesse' WHERE city = 'Neu-Isenburg';
UPDATE jobs_translated SET state = 'Hesse' WHERE city = 'Frankfurt am Main';
UPDATE jobs_translated SET state = 'Lower Saxony' WHERE city = 'Buxtehude';
UPDATE jobs_translated SET state = 'Lower Saxony' WHERE city = 'Unterlüß';
UPDATE jobs_translated SET state = 'Schleswig-Holstein' WHERE city = 'Kaltenkirchen';
UPDATE jobs_translated SET state = 'Saxony' WHERE city = 'Dresden';
UPDATE jobs_translated SET state = 'Rhineland Palatinate' WHERE city = 'Mainz';
UPDATE jobs_translated SET state = 'Baden Wurttemberg' WHERE city = 'Mengen';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Nuremberg';
UPDATE jobs_translated SET state = 'Saarland' WHERE city = 'Saarbrücken';
UPDATE jobs_translated SET state = 'Baden Wurttemberg' WHERE city = 'Trossingen';
UPDATE jobs_translated SET state = 'Baden Wurttemberg' WHERE city = 'Bruchsal';
UPDATE jobs_translated SET state = 'North Rhine-Westphalia' WHERE city = 'Krefeld';
UPDATE jobs_translated SET state = 'Baden Wurttemberg' WHERE city = 'Ehningen';
UPDATE jobs_translated SET state = 'North Rhine-Westphalia' WHERE city = 'Bielefeld';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Unterföhring';
UPDATE jobs_translated SET state = 'Rhineland Palatinate' WHERE city = 'Zweibrücken';
UPDATE jobs_translated SET state = 'Brandenburg' WHERE city = 'Schönefeld';
UPDATE jobs_translated SET state = 'Saxony' WHERE city = 'Chemnitz';
UPDATE jobs_translated SET state = 'Lower Saxony' WHERE city = 'Hannover';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Wendelstein';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Donauwörth';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Ottobrunn';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Landshut';
UPDATE jobs_translated SET state = 'Bavaria' WHERE city = 'Manching';

SELECT *
FROM jobs_translated
WHERE country = 'Germany';


SELECT *
FROM capstone.jobs_translated
WHERE country = 'France' AND state ISNULL ;
------------------------------------

SELECT *
FROM capstone.jobs_translated
WHERE country = 'United States';
----
------------------------------

DELETE FROM capstone.jobs  
WHERE id < 50;

SELECT *
FROM capstone.jobs
WHERE world_region ISNULL ;

UPDATE capstone.jobs 
SET world_region  = 'North America'
WHERE country = 'United States' OR search_country = 'United States';

SELECT *
FROM capstone.jobs
LIMIT 15;

SELECT *
FROM capstone.jobs
WHERE city = 'Bordeaux' AND state ISNULL  ;

UPDATE capstone.jobs SET state = 'Nouvelle-Aquitaine' WHERE city = 'Bordeaux';

SELECT *
FROM capstone.jobs
WHERE country = 'United Kingdom';

UPDATE capstone.jobs SET state = 'England' WHERE city = 'Bridgwater';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Leeds';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Birmingham';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Portsmouth';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Stevenage';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Slough';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Newport';
UPDATE capstone.jobs SET state = 'Wales' WHERE city = 'Cwmbrân';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Shawbury';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Leicester';
UPDATE capstone.jobs SET state = 'Wales' WHERE city = 'Cardiff';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Braintree';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'London Area';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Stafford';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Gloucester';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Brize Norton';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Broughton';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Greater Bristol Area';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Oxford';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'York';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Burnley';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Derby';
UPDATE capstone.jobs SET state = 'Wales' WHERE city = 'Cwmbran Central';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Solihull';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Blandford Forum';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Manchester';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'London';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Nottingham';
UPDATE capstone.jobs SET state = 'Scotland' WHERE city = 'Glasgow';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Pitstone';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Fareham';
UPDATE capstone.jobs SET state = 'England' WHERE city = 'Bristol';

SELECT DISTINCT(state)
FROM capstone.jobs
WHERE state ILIKE '%Engla%' ;

SELECT DISTINCT(state)
FROM capstone.world_cities_state
WHERE country = 'United Kingdom';


SELECT count(city)
FROM capstone.jobs
WHERE country = 'United States';

SELECT DISTINCT(city)
FROM capstone.world_cities_state wcs 
WHERE country = 'United Kingdom'

SELECT COUNT(*)
FROM capstone.world_cities_state;

SELECT * 
FROM capstone.jobs
Where city = 'München';

SELECT *
FROM jobs j 
WHERE country = 'United States' AND state = 'GA' ;

UPDATE jobs 
SET city = 'Atlanta'
WHERE city = 'Atlanta, GA';

SELECT *
FROM jobs j 
WHERE world_region = 'Central America' ;


SELECT * 
FROM jobs
WHERE world_region = 'Africa';

SELECT *
FROM jobs
WHERE id > 1500
ORDER BY id desc;

SELECT *
FROM competitors c 
ORDER BY name;

SELECT *
FROM jobs j 
WHERE job_title_en = 'Aircraft maintenance team manager';

DELETE FROM jobs 
WHERE id = 1017;

SELECT *
FROM jobs j 
WHERE country = 'Germany' AND posted_date = '2022-06-1'
ORDER BY id;

DELETE FROM jobs 
WHERE id = 511;

SELECT *
FROM jobs j 
WHERE job_title_en ILIKE '%MTU M%'
ORDER BY id;

SELECT *
FROM jobs j 
WHERE company_name ILIKE '%Air France%' OR job_description ilike '%KLM' OR job_description ILIKE '%AFI' OR job_description ILIKE '%E&M%';

SELECT COUNT(*)
FROM jobs j 
WHERE job_description ilike '%AERO%' OR job_title_en  ILIKE '%AEROSTAR%';

CREATE TABLE jobs_provider AS
SELECT *
FROM jobs_jcat;

DELETE FROM jobs_provider 
WHERE competitor_id < 17;

INSERT INTO competitors VALUES
(15, 'Air France', )

SELECT *
FROM jobs j 
WHERE id = 860;

SELECT *
FROM jobs_provider 
WHERE jobs_id = 860;

SELECT *
FROM world_locations wl 
WHERE city = 'Suzhou';

DELETE FROM world_locations 
WHERE city = 'Suzhou' AND state = 'Anhui';

SELECT DISTINCT(jobs_id)
FROM jobs_provider jp ;

SELECT jobs_id , competitor_id , matching_keyword 
FROM jobs_provider jp ;

SELECT Count(DISTINCT(jobs_id))
FROM jobs_provider jp ;

SELECT *
FROM jobs j 
WHERE id IN (1991, 1992, 2005, 1837, 1841, 1961, 1964, 1329, 1408, 1334, 234, 309, 413, 419, 860, 421, 459, 624, 
			640, 675, 676, 700, 711, 722,758, 802, 835,854, 861, 895, 948, 956, 967, 986, 1029);
		
SELECT *
FROM jobs
WHERE id IN (SELECT jobs_id AS jobs_id
				FROM jobs_provider jp);
			
SELECT *
FROM jobs_provider jp
WHERE jobs_id = 1455;

SELECT *
FROM world_locations wl 
WHERE country ILIKE '%Neth%';

INSERT INTO world_locations VALUES
('Schiphol', 'Noord-Holland', 'Netherlands');

SELECT *
FROM jobs j 
WHERE country ilike '%Netherlands%';

SELECT *
FROM jobs j 
WHERE company_name ILIKE '%Lufth%'

INSERT INTO competitors VALUES
(18, 'Lufthansa', 'Germany, Hungary, Bulgaria', 'MRO (Airline MRO)');

SELECT *
FROM jobs j 
WHERE id > 2000;

SELECT *
FROM jobs j WHERE job_description ILIKE '%Milita%';
-----------------------------------------------------

UPDATE jobs_categories 
SET keywords = 'Engineer, Engineering, F&E, CAD, Service Engineer, Repair Development, Certification Engineer, Design Engineer, 
				Ingénieur, Entwicklungsingenieur, Ingenieur, Test Engineer, Weight & Balance, Computational, Avionics Engineer, 
				Mechanical Engineer, Electrical Engineer'
WHERE id = 14;

--------------------------
DELETE FROM jobs_jcat  
WHERE jcat_id < 17;
-------------------------

SELECT *
FROM jobs j 
WHERE id = 802;
----------------------

SELECT 
 j.company_name,
 j.id,
 jc.name,
 count(job_title_en) AS number_of_jobs,
 job_title_en,
 job_description 
FROM capstone.jobs j
LEFT JOIN 
capstone.jobs_jcat jj 
ON 
CAST(j.id AS int4) = CAST(jj.jobs_id AS int4)
JOIN
capstone.jobs_categories jc 
ON
jj.jcat_id = jc.id 
GROUP BY 1, 2, 3,5,6
HAVING company_name ilike '%Safran%';
-------------------------------------------
SELECT *
FROM jobs_categories jc 
ORDER BY id ;
------
SELECT COUNT(*)
FROM jobs_provider jp 
WHERE competitor_id = 16;
------------

SELECT *
FROM jobs_provider jp 
WHERE competitor_id = 19;
