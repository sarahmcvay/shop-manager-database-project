-- This file resets important database tables.
-- And adds any data that is needed for the tests to run.

DROP TABLE IF EXISTS test_table;

CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(255));

INSERT INTO test_table (name) VALUES ('first_record');