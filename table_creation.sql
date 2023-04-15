CREATE TABLE Ambassador (
	UIN INT PRIMARY KEY,
   	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	major CHAR(50),
	is_ambassador INTEGER,
	grad_year INTEGER
);

CREATE TABLE Participated (
	UIN INT,
   	position_ID INT,
	hour_modifier INT DEFAULT 0,
	PRIMARY KEY (UIN, position_ID),
	FOREIGN KEY (UIN)
		REFERENCES Ambassador (UIN)
			ON UPDATE CASCADE
	FOREIGN KEY (position_ID)
		REFERENCES Position (position_ID)
			ON UPDATE CASCADE
);

CREATE TABLE Position (
	event_ID INT,
   	position_ID INT,
	pos_name TEXT NOT NULL,
	base_hours REAL,
	PRIMARY KEY (event_ID, position_ID),
	FOREIGN KEY (event_ID)
		REFERENCES Event (event_ID)
			ON UPDATE CASCADE
);

CREATE TABLE Event (
	event_ID INT PRIMARY KEY,
   	name TEXT NOT NULL,
	date TEXT,
	academic_year TEXT
);
