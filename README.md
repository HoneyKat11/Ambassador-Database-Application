# Ambassador-Database-Application
The purpose of this repository is to store code for an engineering ambassador database application created as a project for Intro to Data Engineering (COP 3710) during the Spring 2023 semester.

# Schema Diagram
![image](database_schema.png)

# Entity-Relationship (ER) Diagram 
![image](database_entity_relation_diagram.png)

# Tables
- Ambassador 
   - **UIN** (primary)
   - First Name
   - Last Name
   - Major
   - Graduation Year
   - Ambassador
- Participated 
   - **UIN** (foreign)
   - **Position ID** (primary)
   - Hour Modifier
- Position 
   - **Event ID** (foreign)
   - **Position ID** (primary)
   - Position Name
   - Scheduled Hours
- Event 
   - **Event ID** (primary)
   - Event Name
   - Date
   - Academic Year

## Pending Changes
- Ambassador table needs "graduation year" integer attribute
   - Diagrams need to be updated with this information 

## Inserts
- Insert new ambassador
- Insert new event
- Insert new position given an event

## Updates
- Update total hours for a position given an event
- Update hour modifier given an ambassador and position

## Deletes
- Delete an ambassador
- Delete an event

## Queries
- All ambassadors graduating a given year
- All ambassadors helping at a specific event 
- All ambassadors helping in a certain positon (during a specific event) 




