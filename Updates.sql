-- Update total hours for a position given an event



-- Update hour modifier given an ambassador and position


-- Update name for a given ambassador
UPDATE Ambassador
	set first_name = {givenfirstName},last_name ={givenLastName},
	WHERE UIN = {UIN};


-- Update major for a given ambassador
UPDATE Ambassador
	set major = {givenMajor}
	WHERE first_name = {firstName}
	AND last_name = {lastName}
	AND UIN = {UIN});


-- Update ambassador status for a given ambassador
UPDATE Ambassador
	set ambassadorStatus = {givenStaus}
	WHERE first_name = {firstName}
	AND last_name = {lastName}
	AND UIN = {UIN});


-- Update graduation year for a given ambassador
UPDATE Ambassador
	set grad_year = {givenYear}
	WHERE first_name = {firstName}
	AND last_name = {lastName}
	AND UIN = {UIN});



-- Update scheduled hours for a given position



-- Update hour modifier for a given participated record


