import sqlite3

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect('pets.db')
cur = conn.cursor()

# Create tables
cur.execute('''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER,
    pet_id INTEGER,
    FOREIGN KEY(person_id) REFERENCES person(id),
    FOREIGN KEY(pet_id) REFERENCES pet(id)
)''')

# Insert data
persons = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

person_pet = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

cur.executemany('INSERT INTO person VALUES (?, ?, ?, ?)', persons)
cur.executemany('INSERT INTO pet VALUES (?, ?, ?, ?, ?)', pets)
cur.executemany('INSERT INTO person_pet VALUES (?, ?)', person_pet)

# Commit the changes and close the connection
conn.commit()
conn.close()
