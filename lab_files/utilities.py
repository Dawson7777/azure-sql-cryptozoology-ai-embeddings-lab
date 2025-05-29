import json
import os
import struct
import logging
import mssql_python
import re

from azure import identity
from dotenv import load_dotenv

from mssql_python.db_connection import connect


def get_cryptids(search_text:str) -> str:
    
    conn_str=os.environ["MSSQL_PYTHON_DRIVER_CONNECTION_STRING"]
    print(conn_str)
    conn = connect(conn_str)
    logging.info("Querying MSSQL...")
    logging.info(f"Message content: '{search_text}'")
    try:        
        cursor = conn.cursor()  
        params = (search_text, )
        cursor.execute("{CALL [dbo].[get_cryptids] (?)}", params)
        output_value = cursor.fetchall()

        logging.info(f"Found {len(output_value)} cryptids.")

        payload = ""
        for row in output_value:
            payload += f'CryptidName: {row[0]}|TimeOfDay: {row[1]}|Location: {row[2]}|Weather: {row[3]}|VideoSetting: {row[4]}|"VideoDescription: "{row[5]}|"CryptidLore: "{row[6]}|"ThreatLevel: "{row[7]}'
            payload += "\n"

        return payload    
    finally:
        cursor.close()    

if __name__ == "__main__":
    print(get_cryptids("bigfoot"))