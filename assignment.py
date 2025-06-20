#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""

import sqlite3
import datetime


dbase = 'vet_records.db'




def create_table():
   connection = sqlite3.connect(dbase)
   cursor = connection.cursor()


   cursor.execute("""
   CREATE TABLE IF NOT EXISTS vet_records (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       pet_name TEXT,
       pet_species TEXT,
       pet_breed TEXT,
       owner_name TEXT,
       owner_phone TEXT,
       owner_email TEXT,
       balance REAL,
       first_visit_date TEXT
   )
   """)


   connection.commit()
   connection.close()




def insert_record():


   print("\n=== store new information ===")
   pet_name = input("enter pet name: ")
   pet_species = input("enter pet species (cat, dog, bird, etc): ")
   pet_breed = input("enter pet breed (persian, beagle, canary, etc): ")
   owner_name = input("enter owner name: ")
   owner_phone = input("enter owner phone number: ")
   owner_email = input("enter owner email: ")


   while True:
       try:
           balance = float(input("enter owner balance: "))
           break
       except ValueError:
           print("enter a valid number!")


   first_visit_date = datetime.date.today().isoformat()


   connection = sqlite3.connect(dbase)
   cursor = connection.cursor()


   cursor.execute("""
   INSERT INTO vet_records
   (pet_name, pet_species, pet_breed, owner_name, owner_phone, owner_email, balance, first_visit_date)
   VALUES (?, ?, ?, ?, ?, ?, ?, ?)
   """, (pet_name, pet_species, pet_breed, owner_name, owner_phone, owner_email, balance, first_visit_date))


   connection.commit()


   new_id = cursor.lastrowid
   connection.close()


   print(f"\n record added successfully! record ID: {new_id}")




def search_by_id():
   print("\n=== Retrieve record by ID ===")


   while True:
       try:
           record_id = int(input("enter record ID: "))
           break
       except ValueError:
           print("enter an integer for ID!")


   connection = sqlite3.connect(dbase)
   cursor = connection.cursor()


   cursor.execute("SELECT * FROM vet_records WHERE id = ?", (record_id,))
   record = cursor.fetchone()


   connection.close()


   if record:
       display_record(record)
   else:
       print(f"didn't find the record of the ID {record_id}")




def search_by_email():
   print("\n=== retrieve record by email ===")


   email = input("Enter email: ")


   connection = sqlite3.connect(dbase)
   cursor = connection.cursor()


   cursor.execute("SELECT * FROM vet_records WHERE owner_email = ?", (email,))
   records = cursor.fetchall()


   connection.close()


   if records:
       for record in records:
           display_record(record)
           print("-" * 30)
   else:
       print(f"Didn't find record for the email: {email} ")




def search_by_phone():
   print("\n=== retrieve a record by phone number ===")


   phone = input("enter phone number: ")


   connection = sqlite3.connect(dbase)
   cursor = connection.cursor()


   cursor.execute("SELECT * FROM vet_records WHERE owner_phone = ?", (phone,))
   records = cursor.fetchall()


   connection.close()


   if records:
       for record in records:
           display_record(record)
           print("-" * 30)
   else:
       print(f"Didn't find record for the phone number{phone}")




def display_record(record):
   print("\n information:")
   print(f"ID: {record[0]}")
   print(f"Pet name: {record[1]}")
   print(f"Pet species: {record[2]}")
   print(f"Pet breed: {record[3]}")
   print(f"owner name: {record[4]}")
   print(f"owner phone number: {record[5]}")
   print(f"owner email: {record[6]}")
   print(f"owner balance: {record[7]}")
   print(f"Date of first visit: {record[8]}")




while True:
   print("1. Add new record")
   print("2. Retrieve record by ID")
   print("3. Retrieve record by Email")
   print("4. Retrieve record by phone number")


   choice = input("Please choose what you want to do(1-4): ")


   if choice == '1':
       insert_record()
   elif choice == '2':
       search_by_id()
   elif choice == '3':
       search_by_email()
   elif choice == '4':
       search_by_phone()
   else:
       print("Invalid input, try again!")


