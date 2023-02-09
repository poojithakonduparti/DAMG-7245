import os
import sqlite3
import pandas as pd
from pathlib import Path


database_file_name = 'assignment1.db'
database_file_path = os.path.join(os.path.dirname(__file__),database_file_name)
print("File path", database_file_path)

#query year from nexrad
def get_year():
     db = sqlite3.connect(database_file_path)
     query = "SELECT DISTINCT year from nexrad " 
     df_year = pd.read_sql_query(query, db)
     years = df_year['year'].tolist()
     return years

#query months from selected year 
def get_month_in_year(selected_year):
    db = sqlite3.connect(database_file_path)
    query = "SELECT DISTINCT month from nexrad  where year = " + selected_year
    df_month = pd.read_sql_query(query, db)
    months = df_month['month'].tolist()
    return months

#query days recorded in a selected month
def get_day_in_month(selected_month):
     db = sqlite3.connect(database_file_path)
     query = "SELECT DISTINCT day from nexrad where month = " + selected_month
     df_day = pd.read_sql_query(query, db)
     days = df_day['month'].tolist()
     return days


#query ground stations for a selected day
def get_stations_for_day(selected_day):
      db = sqlite3.connect(database_file_path)
      query = "SELECT DISTINCT ground_station from nexrad where day = " + selected_day
      df_station = pd.read_sql_query(query, db)
      stations = df_station['ground_station'].tolist() 
      return stations

      
