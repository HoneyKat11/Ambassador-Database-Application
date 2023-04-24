--Create position view, which is a log of all ambassador's service
CREATE VIEW position_view AS
SELECT A.UIN,
       A.first_name || ' ' || A.last_name,
       Pos.pos_name,
       Pos.position_ID,
       E.name,
       Pos.base_hours + Part.hour_modifier as served_hours
FROM Participated Part
    INNER JOIN Ambassador A ON Part.UIN = A.UIN
    INNER JOIN Position Pos ON Part.position_ID = Pos.position_ID
    INNER JOIN Event E ON Pos.event_ID = E.event_ID;



--Creates ambassador hours, which shows cumulative hours per ambassador
CREATE VIEW ambassador_hours_view AS
SELECT A.UIN,
       A.first_name,
       A.last_name,
       SUM(Psv.served_hours)
FROM Ambassador A
    INNER JOIN Participated Part ON A.UIN = Part.UIN
    INNER JOIN position_view Psv ON Part.position_ID = Psv.position_ID
GROUP BY A.UIN;



CREATE VIEW event_view AS
SELECT E.event_ID,
       E.name,
       E.date,
       E.academic_year
FROM Event E;