DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS data_point;
DROP TABLE IF EXISTS news;
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
CREATE TABLE data_point (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  total INTEGER NOT NULL,
  sentiment REAL NOT NULL,
  point_date DATETIME NOT NULL,
  created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE news (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  statement_date DATETIME NOT NULL,
  created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "data_point" (
    "id",
    "total",
    "sentiment",
    "point_date",
    "created"
  )
VALUES (
    '1',
    '0',
    '0.091926',
    '01.15.20',
    '2021-03-11 15:52:52'
  ),
  (
    '2',
    '0',
    '0.045407',
    '02.15.20',
    '2021-03-11 15:52:52'
  ),
  (
    '3',
    '0',
    '0.113407',
    '03.15.20',
    '2021-03-12 00:56:32'
  ),
  (
    '4',
    '0',
    '0.075429',
    '04.15.20',
    '2021-03-12 00:56:51'
  ),
  (
    '5',
    '0',
    '0.039759',
    '05.15.20',
    '2021-03-12 00:57:13'
  ),
  (
    '6',
    '0',
    '0.018538',
    '06.15.20',
    '2021-03-12 01:55:42'
  ),
  (
    '7',
    '0',
    '0.015846',
    '07.15.20',
    '2021-03-12 01:55:42'
  ),
  (
    '8',
    '0',
    '0.050964',
    '08.15.20',
    '2021-03-12 01:55:42'
  ),
  (
    '9',
    '0',
    '0.027433',
    '09.15.20',
    '2021-03-12 01:55:42'
  ),
  (
    '10',
    '0',
    '0.018138',
    '10.15.20',
    '2021-03-12 01:55:42'
  ),
  (
    '11',
    '0',
    '0.010034',
    '11.15.20',
    '2021-03-12 01:55:42'
  ),
  (
    '12',
    '0',
    '0.031875',
    '12.15.20',
    '2021-03-12 01:55:42'
  );