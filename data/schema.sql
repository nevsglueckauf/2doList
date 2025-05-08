
BEGIN TRANSACTION;
CREATE TABLE category (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
    
);
INSERT INTO category VALUES(1,'Normal');
INSERT INTO category VALUES(2,'Gartenarbeit');
INSERT INTO category VALUES(3,'Hobbykeller');
INSERT INTO category VALUES(4,'Plattenkauf');
INSERT INTO category VALUES(6,'Namentanzen');
INSERT INTO category VALUES(12,'Foo_Bar');
CREATE TABLE task (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    priority INTEGER NULL DEFAULT 0,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT CHECK( status IN ('PENDING', 'DONE', 'IN_PROGRESS', 'CANCELLED', 'PAUSED') )   NOT NULL DEFAULT 'PENDING',
    created TEXT NOT NULL DEFAULT current_timestamp,
    start_dt TEXT NULL,
    end_dt TEXT NULL,
    category_id INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY(category_id) REFERENCES category(id)
);
INSERT INTO task VALUES(1,0,'Foo_BAr_baz','New description under the block','PENDING','2025-05-08 08:47:18','2025-12-09','2025-12-09',2);
INSERT INTO task VALUES(2,0,'foo','Do foo with bar','PENDING','2025-05-08 08:57:25',NULL,NULL,2);
INSERT INTO task VALUES(3,0,'Kim Wilde - Cambodia','Höchstens 55€!!','PENDING','2025-05-08 10:43:28','2025-09-01','2025-09-11',4);
INSERT INTO task VALUES(5,0,'Skinny Puppy - Remission & Bites','Höchstens 1000€!!','DONE','2025-05-08 10:45:01','2025-09-01','2025-09-11',4);
INSERT INTO task VALUES(7,0,'Legendary Pink Dots - Shadow weaver','Höchstens 1000€!!','PENDING','2025-05-08 11:27:20','2025-09-01','2025-09-11',4);
INSERT INTO task VALUES(8,0,'Legendary Pink Dots - Shadow weaver','Höchstens 1000€!!','PENDING','2025-05-08 11:32:59','2025-09-01','2025-09-11',4);
INSERT INTO task VALUES(9,0,'Beatles - White Album','Höchstens 1100€!!','PENDING','2025-05-08 11:34:18','2025-09-01','2025-09-11',4);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('category',12);
INSERT INTO sqlite_sequence VALUES('task',9);
COMMIT;
