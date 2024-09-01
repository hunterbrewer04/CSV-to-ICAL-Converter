import pandas as pd
from icalendar import Calendar, Event
from datetime import timedelta
import pytz

# Load the CSV file (replace 'your_file.csv' with your actual CSV file name)
df = pd.read_csv('college_course_schedule.csv')

# Create a new calendar
cal = Calendar()

# Define a timezone (change to your timezone if necessary)
timezone = pytz.timezone("America/Chicago")

# Iterate over the DataFrame and add events to the calendar
for index, row in df.iterrows():
    event = Event()
    event.add('summary', row['Event'])  # Event description
    event.add('dtstart', timezone.localize(pd.to_datetime(row['Date'])))  # Start date
    event.add('dtend', timezone.localize(pd.to_datetime(row['Date']) + timedelta(hours=1)))  # End date (1 hour later)
    cal.add_component(event)

# Save the calendar to an .ics file
with open('output_schedule.ics', 'wb') as f:
    f.write(cal.to_ical())

print("iCal file has been created successfully!")
