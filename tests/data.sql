INSERT INTO user (username, password)
VALUES (
    'test',
    'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'
  ),
  (
    'other',
    'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79'
  );
INSERT INTO data_point(
    total,
    sentiment,
    point_date,
    created
  )
VALUES (
    22,
    0.6,
    '2020-01-04',
    '2020-01-04 12:04:00'
  );
INSERT INTO news (
    title,
    content,
    statement_date,
    created
  )
VALUES (
    'Friseure werden geöffnet',
    'Alle Friseure in Deutschland werden geöffnet',
    '2020-02-02',
    '2020-01-04 12:04:00'
  );