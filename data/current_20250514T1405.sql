PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE category (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
    
);
INSERT INTO category VALUES(1,'NormalGibtEsNicht');
INSERT INTO category VALUES(2,'Gartenarbeit');
INSERT INTO category VALUES(3,'Hobbykeller');
INSERT INTO category VALUES(4,'Plattenkauf');
INSERT INTO category VALUES(6,'Namentanzen');
INSERT INTO category VALUES(12,'Mambabaumkletterkabbelei');
INSERT INTO category VALUES(13,'Training für Olympia');
INSERT INTO category VALUES(14,'Kreativer Umgang mit Technik - aka H@xX');
INSERT INTO category VALUES(15,'BlueboxingSavesMoney');
INSERT INTO category VALUES(16,'Formulartest');
INSERT INTO category VALUES(17,'Siebengebirgsjägerlatin');
INSERT INTO category VALUES(18,'Disneyworld (Marvel, Star Wars, Mickey etc.)');
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
INSERT INTO task VALUES(1,0,'Foo_BAr_baz','New description under the block','DONE','2025-05-08 08:47:18','2025-12-09','2025-12-09',2);
INSERT INTO task VALUES(2,0,'Neverland Journey','Walk with Peter Pan','PENDING','2025-05-08 08:57:25','None','None',18);
INSERT INTO task VALUES(3,0,'Kim Wilde - Cambodia','Höchstens 55€!!','DONE','2025-05-08 10:43:28','2025-09-01','2025-09-11',4);
INSERT INTO task VALUES(5,0,'Skinny Puppy - Remission & Bites','Höchstens 1000€!!','DONE','2025-05-08 10:45:01','2025-09-01','2025-09-11',4);
INSERT INTO task VALUES(7,0,'Foyer des Arts: 1989: Was ist super? (live)','Sehr schwierig zu bekommen - auf Vinyl, oder CD. Digital - z.B. YT: kein Problem','PENDING','2025-05-08 11:27:20','2025-12-09','2075-12-09',4);
INSERT INTO task VALUES(8,0,'Legendary Pink Dots - Shadow weaver','Höchstens 1000€!!','PENDING','2025-05-08 11:32:59','2025-09-01','2025-09-11',4);
INSERT INTO task VALUES(9,0,'Beatles - White Album','Höchstens 1100€!!','PENDING','2025-05-08 11:34:18','2025-09-01','2025-09-11',4);
INSERT INTO task VALUES(10,0,'Bluewalk Aug. 2025','Wandertag mit den Schlümpfen','IN_PROGRESS','2025-05-12 10:07:10','2025-08-12','2025-08-29',4);
INSERT INTO task VALUES(11,0,'EESF H@xX','Europäischen Einlagensicherungsfonds sicherheitstechnisch vor Anforderungen stellen','PENDING','2025-05-13 09:19:28','2025-05-22','2025-05-31',2);
INSERT INTO task VALUES(12,0,'Fotosafari Mars mit Musk','Nikon UND Canon einpacken','DONE','2025-05-13 11:41:52','2025-05-13','2025-05-20',4);
INSERT INTO task VALUES(13,0,'Foo','kdhjsdk','DONE','2025-05-13 11:42:32','2025-05-13','2025-05-13',4);
INSERT INTO task VALUES(14,0,'Bar','Locker bleiben','PENDING','2025-05-13 11:55:18','2025-05-13','2025-05-13',1);
INSERT INTO task VALUES(16,0,'TestFoo','bar -> baz(24.33) * 0.666','PENDING','2025-05-13 12:13:26','2025-05-19','2025-05-31',2);
INSERT INTO task VALUES(17,0,'Lala','In Richtung NNW','PENDING','2025-05-13 12:14:24','2025-05-19','2025-05-22',14);
INSERT INTO task VALUES(18,0,'Foo','Bar tech.','PENDING','2025-05-14 11:05:21','2025-05-14','2025-05-28',3);
INSERT INTO task VALUES(19,0,'Testeintrag','Nach Umstellung auf Controller()','PENDING','2025-05-14 11:10:03','2025-05-14','2025-05-27',6);
INSERT INTO task VALUES(20,0,'Essen mit Godot','So lamgsam bekomme ich hunger ....','PENDING','2025-05-14 11:59:18','2035-05-08','2035-05-14',12);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('category',18);
INSERT INTO sqlite_sequence VALUES('task',20);
COMMIT;
