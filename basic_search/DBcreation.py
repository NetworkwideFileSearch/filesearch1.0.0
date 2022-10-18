
import sqlite3

conn = sqlite3.connect('file_search.db') 
c = conn.cursor()

c.execute('''
            CREATE TABLE  metadata(
                file_id integer primary key autoincrement,
                file_name text,
                file_type text,
                file_size integer,
                creation_date text, 
                accessed_date text,
                modification_date text,
                file_location text,
                keywords text default "not yet"
            )
          ''')
          
 
                     
conn.commit()

