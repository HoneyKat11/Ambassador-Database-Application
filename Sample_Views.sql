--served_hours
--   Prerequisite for position_view, shows hours served rather than base + modifier
CREATE VIEW served_hours AS
SELECT Part.UIN,
       Pos.position_ID,
       (Pos.base_hours + Part.hour_modifier) served
FROM Participated Part
    INNER JOIN Position Pos on Part.position_ID = Pos.position_ID;



--position_view
--   Shows a modified version of "participated", showing hours served rather
--   than base + modifier in two tables
CREATE VIEW position_view AS
SELECT A.UIN,
       A.first_name || ' ' || A.last_name,
       Pos.pos_name,
       Pos.position_ID,
       E.name,
       served_hours.served
FROM Participated Part
    INNER JOIN Ambassador A ON Part.UIN = A.UIN
    INNER JOIN Position Pos ON Part.position_ID = Pos.position_ID
    INNER JOIN served_hours on Pos.position_ID = served_hours.position_ID
    INNER JOIN Event E ON Pos.event_ID = E.event_ID;



--ambassador_hours_view
--   Shows ambassador's cumulative hours served
CREATE VIEW ambassador_hours_view AS
SELECT A.UIN,
       A.first_name,
       A.last_name,
       SUM(Psv.served) cumulative_hours
FROM Ambassador A
    INNER JOIN Participated Part ON A.UIN = Part.UIN
    INNER JOIN position_view Psv ON Part.position_ID = Psv.position_ID
GROUP BY A.UIN;
