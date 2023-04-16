-- Delete an ambassador
DELETE FROM Ambassador
      WHERE UIN = {UIN};
	  
DELETE FROM Ambassador
	  WHERE first_name = {firstName}
	    AND last_name = {lastName};


-- Delete an ambassador and all associated records (unnecessary if relations set up correctly)
DELETE FROM Participated
      WHERE UIN = {UIN};
DELETE FROM Ambassador
      WHERE UIN = {UIN};

DELETE FROM Participated
      WHERE EXISTS (SELECT 1
	                  FROM Ambassador
				     WHERE Participated.UIN = Ambassador.UIN
					   AND first_name = {firstName}
					   AND last_name = {lastName});
DELETE FROM Ambassador
	  WHERE first_name = {firstName}
	    AND last_name = {lastName};


-- Delete an event and associated positions
DELETE FROM Participated
      WHERE EXISTS (SELECT 1
	                  FROM Position
					 WHERE Participated.position_ID = Position.position_ID
					   AND event_ID = {eventID});
DELETE FROM Position
      WHERE event_ID = {eventID};
DELETE FROM Event
      WHERE event_ID = {eventID};


-- Delete all ambassadors who graduated before a given year
DELETE FROM Participated
      WHERE EXISTS (SELECT 1
	                  FROM Ambassador
				     WHERE grad_year < {year});
DELETE FROM Ambassador
      WHERE grad_year < {year};
	  
	  
-- Delete all Events with no participation records
DELETE FROM Position
	  WHERE NOT EXISTS (SELECT 1
						  FROM Participated
						 WHERE Position.position_ID = Participated.position_ID);
DELETE FROM Event
	  WHERE NOT EXISTS (SELECT 1
						  FROM Position
						 WHERE Position.event_ID = Event.event_ID);


-- Delete all Events with no participation records before a given year
DELETE FROM Position
	  WHERE NOT EXISTS (SELECT 1
						  FROM Participated
						 WHERE Position.position_ID = Participated.position_ID)
		AND EXISTS (SELECT 1
		              FROM Event
					 WHERE academic_year < {year});
DELETE FROM Event
	  WHERE NOT EXISTS (SELECT 1
						  FROM Position
						 WHERE Position.event_ID = Event.event_ID)
		AND academic_year < {year};