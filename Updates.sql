-- Update total hours for a position given an event
UPDATE


-- Update hour modifier given an ambassador and position
UPDATE

-- Update name for a given ambassador
UPDATE Ambassador
	set first_name = {givenfirstName},last_name ={givenLastName}
	WHERE in (SELECT *
				FROM Ambassador
				WHERE UIN = {UIN})


-- Update major for a given ambassador
UPDATE Ambassador
	set major = {givenMajor}
	WHERE in (SELECT *
			  FROM Ambassador
			 WHERE first_name = {firstName}
			   AND last_name = {lastName}
			   
			SELECT *
			  FROM Ambassador
			 WHERE UIN = {UIN});


-- Update ambassador status for a given ambassador
UPDATE Ambassador
	set ambassadorStatus = {givenStaus}
	WHERE in (SELECT *
			  FROM Ambassador
			 WHERE first_name = {firstName}
			   AND last_name = {lastName}
			   
			SELECT *
			  FROM Ambassador
			 WHERE UIN = {UIN});


-- Update graduation year for a given ambassador
UPDATE Ambassador
	set grad_year = {givenYear}
	WHERE in (SELECT *
			  FROM Ambassador
			 WHERE first_name = {firstName}
			   AND last_name = {lastName}
			   
			SELECT *
			  FROM Ambassador
			 WHERE UIN = {UIN});


-- Update scheduled hours for a given position
UPDATE


-- Update hour modifier for a given participated record
UPDATE

