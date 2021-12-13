create_schema = ('''
CREATE SCHEMA IF NOT EXISTS petl3
''')

drop_table = ('''
DROP TABLE IF EXISTS petl3.viable_counties
''')

create_table = ('''
CREATE TABLE IF NOT EXISTS petl3.viable_counties (
geo_id INT NOT NULL,
state TEXT NOT NULL,
county TEXT NOT NULL,
sales_vector INT NOT NULL
)
''')

insert_data = ('''
INSERT INTO petl3.viable_counties
VALUES (%s, %s, %s, %s)
''')
