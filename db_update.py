from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import select, update, text
import pytz, time
import os
from sqlalchemy.sql import func
from src import db
from sqlalchemy.orm import sessionmaker

#This is run in its own thread, initiated in src/__init__.py, and runs every 15 minutes to update the db. It checks if a box is in use, and if the booked_until_interval15 is in the past, and if so, sets in_use to false, booked_until_interval15 to None and user_id to None.
class update_db():
	def update_box_script(self):
		engine = create_engine(os.getenv("DATABASE_URL"))
		metadata = MetaData()
    
		Session = sessionmaker(bind=engine)

		session = Session()
		box_tbl = Table('boxes', metadata, autoload_with=engine)
		# Get the current time in server time --> UTC
		server_time_all = session.execute(text("SELECT CURRENT_TIMESTAMP"))
		server_time = server_time_all.fetchone()[0]
  
		query = select(box_tbl).where(
				(box_tbl.c.in_use == True) &
				(box_tbl.c.booked_until_interval15 < server_time)
		)
  
		results = session.execute(query).fetchall()

		# Update in_use and booked..
		for row in results:
				update_query = update(box_tbl).where(box_tbl.c.id == row.id).values(in_use=False, booked_until_interval15=None, user_id=None)
				session.execute(update_query)
		
		session.commit()

		session.close()

	# Run the update logic every 15 minutes
	def update_db_infinite(self):
		while (1):
			self.update_box_script()
			time.sleep(900)