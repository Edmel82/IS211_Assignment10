import sqlite3

def get_person_data(person_id):
    conn = sqlite3.connect('pets.db')
    cur = conn.cursor()

    cur.execute('SELECT first_name, last_name, age FROM person WHERE id = ?', (person_id,))
    person = cur.fetchone()

    if person:
        print(f"{person[0]} {person[1]}, {person[2]} years old")

        cur.execute('''
            SELECT pet.name, pet.breed, pet.age 
            FROM pet 
            JOIN person_pet ON pet.id = person_pet.pet_id 
            WHERE person_pet.person_id = ?
        ''', (person_id,))
        
        pets = cur.fetchall()
        for pet in pets:
            print(f"  {pet[0]}, a {pet[1]}, that was {pet[2]} years old")
    else:
        print("Person not found.")

    conn.close()

def main():
    while True:
        person_id = int(input("Enter person ID (or 1 to exit): "))
        if person_id == 1:
            break
        get_person_data(person_id)

if __name__ == '__main__':
    main()
