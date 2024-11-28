CREATE TABLE 'langs' (
    'lang_id' INTEGER NOT NULL,
    'lang_name' TEXT NOT NULL,
    PRIMARY KEY("lang_id" AUTOINCREMENT)
)

INSERT INTO 'langs' ('lang_id', 'lang_name') VALUES (1, 'Arabic')

INSERT INTO 'langs' ('lang_name') VALUES ('Arabic')
INSERT INTO 'langs' ('lang_name') VALUES ('English')


SELECT * FROM "table_name"
SELECT "id" FROM "table_name"
SELECT "id", "colume_1" FROM "table_name"

SELECT * FROM "table_name" WHERE "id" = 1
SELECT * FROM "table_name" LIMIT 1

SELECT * FROM "table_name" ORDER BY "id" DESC
SELECT * FROM "table_name" ORDER BY "id" DESC LIMIT 1

