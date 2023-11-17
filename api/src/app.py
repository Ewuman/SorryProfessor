from fastapi import FastAPI
from text_generation import TextGenerator
import os
import sqlite3
from collections import namedtuple

# provide your own api key
PALM_API_KEY = 'AIzaSyBYZnbTdqa-rByKbOFWPMF10ZveCxdKDJA'
DB_FILENAME = "excuses.db"
DB_PATH = os.path.join("..", "db", DB_FILENAME) # path should work on any OS

app = FastAPI()

# create data model for items
Item = namedtuple('Item', ['professor', 'excuse', 'assignment'])

def insert_data(item: Item):
    # insert data into db
    conn = sqlite3.connect(DB_PATH) # implicitly creates db if it doesn't exist already 
    cursor = conn.cursor()

    # create table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS Record(professor TEXT PRIMARY KEY, excuse TEXT, assignment TEXT);")

    # check if current professor in db
    res = list(cursor.execute("SELECT professor FROM Record WHERE professor = (?);", (item.professor,)))
    
    if len(res) != 0:
        conn.commit()
        conn.close()
        return False

    cursor.execute("""INSERT INTO Record (professor, excuse, assignment)
                    VALUES (?, ?, ?);""", (item.professor, item.excuse, item.assignment))
    
    conn.commit()
    conn.close()

    return True


@app.on_event("startup")
def on_startup() -> None:
    """Initialize database when starting API server."""
    pass


@app.on_event("shutdown")
def on_shutdown() -> None:
    pass


@app.post("/placeholder") # change this to proper route
def get_text(item: Item):
    # set parameters for PALM generation and update db
    
    # update db
    success = insert_data(item)

    if (not success):
        return {"message" : "Excuse already generated for this professor!"}

    # generate text
    text_gen = TextGenerator(PALM_API_KEY)
    text_gen.set_prompt(item.assignment, item.excuse)
    res = text_gen.generate_text()

    return {"message" : res}
