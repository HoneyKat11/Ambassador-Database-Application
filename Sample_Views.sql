--CREATE VIEW ambassador_view AS
SELECT a.UIN, a.first_name, a.last_name, a.major, a.is_ambassador, a.grad_year
FROM Ambassador a;

--CREATE VIEW event_view AS
SELECT e.event_ID, e.name, e.date, e.academic_year
FROM Event e;

--CREATE VIEW position_view AS
