-- All ambassadors graduating a given year
SELECT first_name, last_name
  FROM Ambassador
 WHERE grad_year = {givenYear};


-- All ambassadors of a given major
SELECT first_name "First", last_name "Last"
  FROM Ambassador
 WHERE major = {givenMajor};


-- A specific ambassador's information (UIN, major, graduation year, ambassador status)
SELECT *
  FROM Ambassador
 WHERE first_name = {firstName}
   AND last_name = {lastName};
   
SELECT *
  FROM Ambassador
 WHERE UIN = {UIN};


-- A specific ambassador's hour count for a given year
SELECT SUM(base_hours + hour_modifier)
  FROM Participated
  JOIN Ambassador ON Participated.UIN = Ambassador.UIN
  JOIN Position ON Participated.position_ID = Position.position_ID
 WHERE first_name = {firstName}
   AND last_name = {lastName};
 
 SELECT SUM(base_hours + hour_modifier)
  FROM Participated
  JOIN Position ON Participated.position_ID = Position.position_ID
 WHERE UIN = {UIN};
  
  
-- A specific ambassador's cumulative record of positions/events
SELECT name "Event", pos_name "Position"
  FROM Participated
  JOIN Ambassador ON Participated.UIN = Ambassador.UIN
  JOIN Position ON Participated.position_ID = Position.position_ID
  JOIN Event ON Position.event_ID Event.event_ID
 WHERE first_name = {firstName}
   AND last_name = {lastName};

SELECT name "Event", pos_name "Position"
  FROM Participated
  JOIN Position ON Participated.position_ID = Position.position_ID
  JOIN Event ON Position.event_ID Event.event_ID
 WHERE UIN = {UIN};


-- List of ambassadors and their respective positions at a specific event
SELECT first_name, last_name, pos_name
  FROM Participated
  JOIN Position ON Participated.position_ID = Position.position_ID
  JOIN Event ON Position.event_ID Event.event_ID
 WHERE name = {eventName};  
 
SELECT first_name, last_name, pos_name
  FROM Participated
  JOIN Position ON Participated.position_ID = Position.position_ID
 WHERE event_ID = {eventID}; 


-- List of ambassadors in a given position at a specifc event
SELECT first_name, last_name
  FROM Participated
  JOIN Position ON Participated.position_ID = Position.position_ID
  JOIN Event ON Position.event_ID Event.event_ID
 WHERE name = {eventName}
   AND pos_name = {positionName};  
 
SELECT first_name, last_name
  FROM Participated
  JOIN Position ON Participated.position_ID = Position.position_ID
 WHERE event_ID = {eventID}
   AND position_ID = {positionID}; 
   
SELECT first_name, last_name
  FROM Participated
  JOIN Position ON Participated.position_ID = Position.position_ID
  JOIN Event ON Position.event_ID Event.event_ID
 WHERE name = {eventName}
   AND position_ID = {positionID};
 
SELECT first_name, last_name
  FROM Participated
  JOIN Position ON Participated.position_ID = Position.position_ID
 WHERE event_ID = {eventID}
   AND pos_name = {positionName};  