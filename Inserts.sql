-- Insert new ambassador
INSERT INTO Ambassador (first_name, last_name, UIN, major, is_ambassador, grad_year) -- Can trim anything but UIN as needed
     VALUES ({firstName}, {lastName}, {UIN}, {major}, {ambassadorStatus}, {gradYear},);


-- Insert new event
INSERT INTO Event (name, date, academic_year, event_ID) -- Can trim anything but event_ID as needed
     VALUES ({eventName}, {eventDate}, {eventAcademicYear}, {eventUniqueID});


-- Insert new position given an event
INSERT INTO Position (pos_name, base_hours, event_ID, position_ID) -- Can trim anything but event_ID and position_ID as needed
     VALUES ({positionName}, {positionHours}, {positionsEventID}, {positionID});


-- Insert new record for ambassador participating in an event
INSERT INTO Participated (position_ID, UIN, hour_modifier) -- Can trim hour_modifier as needed
     VALUES ({positionID}, {UIN}, {hourModifier});