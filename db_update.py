from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import select, update, text
import pytz, time
import os
from sqlalchemy.sql import func
from src import db
from sqlalchemy.orm import sessionmaker

#run every 15 minutes
# Function to run the update logic
class update_db():
	def update_box_script(self):
		engine = create_engine(os.getenv("DATABASE_URL"))
		metadata = MetaData()
    
	# Create a session factory bound to the engine
		Session = sessionmaker(bind=engine)

		# Instantiate a session
		session = Session()
		# Assuming 'boxes' is the table name
		box_tbl = Table('boxes', metadata, autoload_with=engine)
		# Get the current time in UTC
		#fixit get curr timezone SELECT CURRENT_TIMEZONE(), datetime.utcnow().replace(tzinfo=pytz.utc)
		# current_time = select([func.current_timestamp()])
		server_time_all = session.execute(text("SELECT CURRENT_TIMESTAMP"))
		server_time = server_time_all.fetchone()[0]
		print(f"\nserver_time from db {server_time}\n")
		# print(f"\ncurrent_time from db {server_time}\n")
		# Build a query to select all rows where 'in_use' is True and 'booked_until_interval15' is in the past
		query = select(box_tbl).where(
				(box_tbl.c.in_use == True) &
				(box_tbl.c.booked_until_interval15 < server_time)
		)
		
		# Execute the query
		results = session.execute(query).fetchall()

		# Update the 'in_use' status for rows where 'booked_until_interval15' is in the past
		for row in results:
				update_query = update(box_tbl).where(box_tbl.c.id == row.id).values(in_use=False, booked_until_interval15=None, user_id=None)
				session.execute(update_query)
		
		# Commit the changes
		session.commit()

    # Close the session
		session.close()


	# Run the update logic every 15 minutes
	def update_db_infinite(self):
		while (1):
			self.update_box_script()
			print("Updated box statuses in 15 minutes loop")
			time.sleep(900)