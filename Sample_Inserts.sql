-- Insert new ambassador
INSERT INTO Ambassador values(123450000, 'John', 'Smith', 'Software', true, 2024);
INSERT INTO Ambassador values(543210000, 'Sarah', 'Williams', 'Civil', true, 2024);
INSERT INTO Ambassador values(221230000, 'Daniel', 'Hill', 'Environmental', false, 2026);
INSERT INTO Ambassador values(667790000, 'Max', 'Rock', 'Bioengineering', true, 2025);

-- Insert new event
INSERT INTO Event values(1, 'Say Yes to the Nest', 'March 18th, 2023', 'Spring 2023');
INSERT INTO Event values(2, 'Solar Go Kart Racing', 'April 1st, 2023', 'Spring 2023');

-- Insert new position given an event
INSERT INTO Position values(1, 1, 'Tour Guide', 5);
INSERT INTO Position values(1, 2, 'Activity Director', 3);
INSERT INTO Position values(2, 3, 'Coordinator', 7);
INSERT INTO Position values(2, 4, 'Driver', 4);

-- Insert new record for ambassador participating in an event
INSERT INTO Participated values(12345, 1, 0);
INSERT INTO Participated values(54321, 2, 0);
INSERT INTO Participated values(22123, 3, 2);
INSERT INTO Participated values(66779, 4, 1);
