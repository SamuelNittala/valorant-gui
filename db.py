import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv('URI'))

def insert_into_table(agent,ability,side,map,area,url):
    area_tags = area.split(',')
    insert_query = f"insert into {agent}(ability,side,map,area,url)values({ability},{side},{map},Array{area_tags},{url})"
    try:
        pd.read_sql(insert_query,engine)
    except:
        print('Insertion success')



