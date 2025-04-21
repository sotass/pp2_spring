import psycopg2
import csv
import os

csv_filename = "\\Users\sotas\OneDrive\Рабочий стол\pp2_spring\labs\lab10\contacts.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['first_name', 'phone'])
    writer.writerow(['Alisher', '+7085208306'])
    writer.writerow(['Batyrkhan', '+77471530843'])
    writer.writerow(['Yerkesh', '+7758720564'])

print(f"CSV-файл '{csv_filename}' создан.")

try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="sotasakurai12859"
    )
    print("Подключение к базе данных успешно.")
except Exception as e:
    print("Ошибка подключения:", e)
    exit()

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    );
""")
conn.commit()
print("Таблица PhoneBook проверена/создана.")

with open(csv_filename, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            cur.execute("""
                INSERT INTO PhoneBook (first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (row['first_name'], row['phone']))
        except Exception as e:
            print(f"Ошибка при вставке: {e}")
conn.commit()
print("Данные из CSV успешно загружены в таблицу.")

def update_contact(old_phone, new_first_name=None, new_phone=None):
    if new_first_name:
        cur.execute("""
            UPDATE PhoneBook
            SET first_name = %s
            WHERE phone = %s;
        """, (new_first_name, old_phone))
    if new_phone:
        cur.execute("""
            UPDATE PhoneBook
            SET phone = %s
            WHERE phone = %s;
        """, (new_phone, old_phone))
    conn.commit()
    print("Контакт успешно обновлён.")

def search_contacts(first_name=None, phone=None):
    if first_name:
        cur.execute("SELECT * FROM PhoneBook WHERE first_name ILIKE %s;", (f"%{first_name}%",))
    elif phone:
        cur.execute("SELECT * FROM PhoneBook WHERE phone = %s;", (phone,))
    else:
        print("Не указаны фильтры для поиска.")
        return
    results = cur.fetchall()
    print("Результаты поиска:")
    for row in results:
        print(row)

def delete_contact(first_name=None, phone=None):
    if first_name:
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s;", (first_name,))
    elif phone:
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s;", (phone,))
    else:
        print("Укажите имя или номер для удаления.")
        return
    conn.commit()
    print("Контакт удалён.")

update_contact(old_phone='+7758720564', new_first_name='Baga')
'''search_contacts(first_name='Yerkesh')
delete_contact(first_name='Alisher')'''

cur.execute("SELECT * FROM PhoneBook")
rows = cur.fetchall()
print("\nДанные в таблице PhoneBook:")
for row in rows:
    print(row)

cur.close()
conn.close()
print("\nСоединение с БД закрыто.")