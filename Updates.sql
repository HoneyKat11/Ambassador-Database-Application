-- Update hour modifier given an ambassador and position
UPDATE Participated
   SET hour_modifier = {hourModifier}
 WHERE position_ID = {positionID}
   AND UIN = {UIN};
   
UPDATE Participated
   SET hour_modifier = {hourModifier}
 WHERE position_ID = {positionID}
   AND EXISTS (SELECT 1
			     FROM Ambassador
				WHERE Ambassador.UIN = Participated.UIN
				  AND first_name = {firstName}
				  AND last_name = {lastName});


-- Update name for a given ambassador
UPDATE Ambassador
   SET first_name = {firstName},last_name ={lastName},
 WHERE UIN = {UIN};


-- Update major for a given ambassador
UPDATE Ambassador
   SET major = {givenMajor}
 WHERE first_name = {firstName}
   AND last_name = {lastName};
   
UPDATE Ambassador
   SET major = {givenMajor}
 WHERE UIN = {UIN};


-- Update ambassador status for a given ambassador
UPDATE Ambassador
   SET is_ambassador = {givenStatus}
 WHERE first_name = {firstName}
   AND last_name = {lastName}
   AND UIN = {UIN};


-- Update graduation year for a given ambassador
UPDATE Ambassador
   SET grad_year = {givenYear}
 WHERE first_name = {firstName}
   AND last_name = {lastName};

UPDATE Ambassador
   SET grad_year = {givenYear}
 WHERE UIN = {UIN};


-- Update scheduled hours for a given position
UPDATE Position
   SET base_hours = {positionHours}
 WHERE position_ID = {positionID}
   AND event_ID = {eventID};

