import sqlite3
from _config import DATABASE_PATH


with sqlite3.connect(DATABASE_PATH) as connection:

	c = connection.cursor()

	#pro_shops
	c.execute("""CREATE TABLE pro_shops(pro_shop_id INTEGER PRIMARY KEY AUTOINCREMENT,
										golf_club_id INTEGER NOT NULL,
										opening_hours TEXT NOT NULL,
										annual_revenue INTEGER NOT NULL,
										other_shop_details TEXT,
										FOREIGN KEY(golf_club_id) REFERENCES golf_clubs(golf_club_id))""")

	#golf_clubs
	c.execute("""CREATE TABLE golf_clubs(golf_club_id INTEGER PRIMARY KEY AUTOINCREMENT,
										 club_name TEXT NOT NULL,
										 year_established TEXT NOT NULL,
										 club_address TEXT NOT NULL,
										 other_club_details TEXT)""")

	#lockers
	c.execute("""CREATE TABLE lockers(locker_number INTEGER PRIMARY KEY AUTOINCREMENT,
									  golf_club_id INTEGER NOT NULL,
									  locker_location TEXT NOT NULL,
									  locker_rental_amount INTEGER NOT NULL,
									  other_locker_details TEXT,
									  FOREIGN KEY(golf_club_id) REFERENCES golf_clubs(golf_club_id))""")

	#member_lockers
	c.execute("""CREATE TABLE member_lockers(locker_number INTEGER NOT NULL,
											 member_id INTEGER NOT NULL,
											 rented_from_date TEXT PRIMARY KEY,
											 rented_to_date TEXT,
											 FOREIGN KEY(locker_number) REFERENCES lockers(locker_number),
											 FOREIGN KEY(member_id) REFERENCES members(member_id))""")
	
	#professionals
	c.execute("""CREATE TABLE professionals(pro_id INTEGER PRIMARY KEY AUTOINCREMENT,
											employed_by_club_id INTEGER NOT NULL,
											data_of_birth TEXT NOT NULL,
											gender TEXT NOT NULL,
											handicap INTEGER NOT NULL,
											pro_first_name TEXT NOT NULL,
											pro_last_name TEXT NOT NULL,
											other_pro_details TEXT,
											FOREIGN KEY(employed_by_club_id) REFERENCES golf_clubs(golf_club_id))""")

	#ref_lesson_status
	c.execute("""CREATE TABLE ref_lesson_status(lesson_status_code INTEGER PRIMARY KEY,
												lesson_status_description TEXT)""")

	#members
	c.execute("""CREATE TABLE members(member_id INTEGER PRIMARY KEY AUTOINCREMENT,
									  golf_club_id INTEGER NOT NULL,
									  membership_type_code INTEGER NOT NULL,
									  fees_due_date TEXT NOT NULL,
									  fees_paid_uptodate_yn TEXT NOT NULL,
									  member_first_name TEXT NOT NULL,
									  member_last_name TEXT NOT NULL,
									  member_phone TEXT NOT NULL,
									  member_email TEXT NOT NULL,
									  member_address TEXT NOT NULL,
									  other_member_details TEXT,
									  FOREIGN KEY(membership_type_code) REFERENCES membership_types(membership_type_code),
									  FOREIGN KEY(golf_club_id) REFERENCES golf_clubs(golf_club))""")


	#membership_types
	c.execute("""CREATE TABLE membership_types(membership_type_code INTEGER PRIMARY KEY AUTOINCREMENT,
											   annual_fees INTEGER NOT NULL,
											   membership_type_description TEXT NOT NULL)""")
											   

	#member_lessons
	c.execute("""CREATE TABLE member_lessons(member_id INTEGER,
											 pro_id INTEGER,
											 lesson_datetime TEXT PRIMARY KEY,
											 lesson_status_code TEXT NOT NULL,
											 booking_made_datetime TEXT NOT NULL,
											 lesson_fee_amount INTEGER NOT NULL,
											 FOREIGN KEY(member_id) REFERENCES member_lesson(member_id),
											 FOREIGN KEY(pro_id) REFERENCES professionals(pro_id))""")


	#ref_payment_methods
	c.execute("""CREATE TABLE ref_payment_methods(payment_method_code TEXT PRIMARY KEY,
												  payment_method_description TEXT NOT NULL)""")


	#subscription_payment_methods
	c.execute("""CREATE TABLE subscription_payment_methods(member_id INTEGER NOT NULL,
														   payment_method_code TEXT NOT NULL,
														   valid_from_date TEXT PRIMARY KEY,
														   payment_method_details TEXT,
														   FOREIGN KEY(member_id) REFERENCES members(member_id),
														   FOREIGN KEY(payment_method_code) REFERENCES ref_payment_methods(payment_method_code))""")