import os
import subprocess
from datetime import datetime

def calculate_progress():
    now = datetime.now()
    # Define start and end dates for year, month
    start_of_year = datetime(now.year, 1, 1)
    end_of_year = datetime(now.year + 1, 1, 1)
    start_of_month = datetime(now.year, now.month, 1)
    next_month = now.month % 12 + 1
    start_of_next_month = datetime(now.year + (now.month // 12), next_month, 1)
 
    
    # Calculate percentage progress
    year_progress = (now - start_of_year) / (end_of_year - start_of_year) * 100
    month_progress = (now - start_of_month) / (start_of_next_month - start_of_month) * 100
    life_progress = ((now.year - 1993) / 80) * 100  # Using 1993 as birth year and 80 as lifespan
    return year_progress, month_progress, life_progress

def daily_commit():
    # Calculate progress metrics
    year_progress, month_progress, life_progress = calculate_progress()
    
    # Define the message and house rules
    message = """
    Be good, and be good at it - 1.01^365

    Daily reminder of house rules:
    - Hard Thing Rule
    - Fun Thing Rule
    - Be early
    - No whining
    - No complaining
    - No excuses

    Time Metrics:
    - Year: {:.2f}%
    - Month: {:.2f}%
    - Life: {:.2f}%
    """.format(year_progress, month_progress, life_progress)
    
    # Make sure the daily_files directory exists
    os.makedirs('daily_files', exist_ok=True)
    
    # Create a new log file for each day in the 'daily_files' folder
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_filename = os.path.join('daily_files', f"log-{date_str}.txt")
    
    with open(log_filename, 'w') as file:
        file.write(f"Date: {datetime.now()}\n")
        file.write(message)

if __name__ == '__main__':
    daily_commit()