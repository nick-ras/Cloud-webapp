from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import select, update
import pytz, time


#ru nevery 15 minutes
# Function to run the update logic
def update_box_statuses():
  # Assuming the use of SQLAlchemy's declarative base
	engine = create_engine(os.getenv("DATABASE_URL"))
	metadata = MetaData(bind=engine)
	session = engine.connect()

# Assuming 'boxes' is the table name
	boxes_table = Table('boxes', metadata, autoload_with=engine)
    # Get the current time in UTC
	current_time = datetime.utcnow().replace(tzinfo=pytz.utc)
	
	# Build a query to select all rows where 'in_use' is True and 'booked_until_interval15' is in the past
	query = select([boxes_table]).where(
			(boxes_table.c.in_use == True) &
			(boxes_table.c.booked_until_interval15 < current_time)
	)
	
	# Execute the query
	results = session.execute(query).fetchall()

	# Update the 'in_use' status for rows where 'booked_until_interval15' is in the past
	for row in results:
			update_query = update(boxes_table).where(boxes_table.c.id == row.id).values(in_use=False)
			session.execute(update_query)
	
	# Commit the changes
	session.commit()
	session.close()

while (1):
	update_box_statuses()
	time.sleep(900)