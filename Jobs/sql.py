# import modules to adress environment variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

# Import the Python packages for get_data() function
import pandas as pd
import psycopg2 as psy


# Insert the get_data() function definition below
def get_data(x):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # create a connection to the PostgreSQL server
        conn = psy.connect(host=os.getenv("host"),
                    port=os.getenv("port"),
                    database=os.getenv("database"),
                    options='-c search_path='+os.getenv("schema"), # this special looking parameter is for the schema
                    user=os.getenv("user"),
                    password=os.getenv("password"))

        result = pd.read_sql_query(x, conn)
        return result
    # the code below makes the function more robust, you can ignore this part
    except (Exception, psy.DatabaseError) as error:
        print('schadee')
        print(error)
    finally:
        if conn is not None:
            conn.close()


from sqlalchemy import create_engine
engine = create_engine(f'postgresql+psycopg2://{os.getenv("user")}:{os.getenv("password")}@{os.getenv("host")}:{os.getenv("port")}/{os.getenv("database")}',  
connect_args={'options': '-csearch_path={}'.format(os.getenv("schema"))})