import pandas as pd
import numpy as np
import requests
import os
from sql import get_data
import psycopg2 # Needed to get database errors when uploading dataframe
import sql
import sqlalchemy
# hides warning messages
import warnings
warnings.filterwarnings("ignore")
import re

############################################
def match_company_name(df):
    competitor_name = { 1 : 'Air France Industrie KLM Engineering & Maintenance', 
                    2 : 'Delta TechOps', 
                    3 : 'Singapore Airlines Engineering Company', 
                    4 : 'Turkish Technic', 
                    5 : 'AJ Walter', 
                    6 : 'SR Technics', 
                    7 : 'ST Aerospace', 
                    8 : 'StandardAero', 
                    9 : 'AAR', 
                    10 : 'Airbus', 
                    11 : 'Boeing', 
                    12 : 'MTU', 
                    13 : 'GE Aviation', 
                    14 : 'Rolls-Royce', 
                    15 : 'Raytheon Technologies', 
                    16 : 'SAFRAN', 
                    17 : 'Nayak',
                    18 : 'Lufthansa Technik',
                    19 : 'Aerostar'
                    }

    provider_keywords = {
    1 : [r'\bAFI\b', 'AFI KLM E&M', 'KLM E&M', 'Prognos', 'Barfield', 'EPCOR', 'Spairliners'],
    2 : ['Delta', r'\bDTO\b', 'Delta Services', 'Delta Material Services (DMS)', 'Digital Alliance'],
    3 : ['SIAEC', 'SIAECo', 'SIA Engineering Company', 'SAESL', 'BAPAS', r'\bHMS\b', 'Eagle Services'],
    4 : [r'\bTHY\b', 'Turkish Airlines Technic', 'Habom', 'Habom MRO Center'],
    5 : ['AJW', 'AJ Walter Technique'],
    6 : [r'\bSRT\b', 'SRT Malta'],
    7 : [r'\bSTA\b', 'ST Engineering', 'STENG', 'VT Aerospace'],
    8 : ['Carlyle', 'Carlyle Group', 'Standard Aero'],
    9 : ['AAR Corp', 'StAAR* (Strategic Tools by AAR) ', 'IMOPS* (Inventory Management and Order Processing System)', 
        'APRISe* (AAR Performance Reporting Information System)'],
    10 : ['Services by Airbus', 'Skywise', 'FHS Services', 'Flight Hour Services', 'SATAIR'],
    11 : ['Boeing Global Services', r'\BGS\b', 'AnalytX', r'\bCSP\b'],
    12 : ['MTU Hannover', 'MTU Maintenance', 'MTU Zhuhai', 'MTU Canada', 'MTU Brandenburg', 'MTU Dallas', 'EME Aero', 
        'EME.Aero', 'MTU Maintenance Serbia'],
    13 : ['GE Engine Services', 'GEES', r'\bCFM\b', 'CFMI', 'LEAP', r'\bGE\b', 'GE Celma', 'GE Wales', 'PHB', 'TRUEngines'],
    14 : [r'\bRR\b', 'Rolls', 'Trent', r'\bTAY\b', 'SPEY', 'RB211', 'Total Care', 'PBH Total Care'],
    15 : ['Pratt&Whitney', 'Pratt & Whitney', 'Collins Aerospace', r'\bPW\b', 'P&W', 'Pratt', 'Hamilton Sundstrand', r'\bUTC\b', 'UTAS', 
        'United Technologies', 'Rockwell-Collins', 'Goodrich', 'Raytheon'],
    16 : ['CFMI', r'\bCFM\b', 'Messier', 'Dowty', 'Zodiac', 'LEAP', 'SNECMA', 'Messier-Bugatti-Dowty', 'Safran Engineering Services'],
    17 : ['Nayak'],
    18 : ['Lufthansa Technik'],
    19 : ['Aerostar', 'Aerostar S.A', 'Group Industrial Aeronautic Bacau']
}
    
    for row in range(len(df)):
        print(row)
        xyz = 0
        for key in competitor_name:
            
            if df['company_name'][row].lower() in competitor_name[key].lower():
                save_provider(df['id'][row], key, competitor_name[key])
                xyz = 1
                break
        if xyz != 1:
            print('hab nix gefunden')
            for item in provider_keywords:
                for word in provider_keywords[item]:
                    print(f'else-loop {word}')

                    provider_low = provider['job_title_en'][row].lower()
                    keyword_low = word.lower()

                    if provider_low.find(keyword_low) != -1:
                        save_provider(df['id'][row], item, word)
                    else:
                        provider_low = provider['job_description'][row].lower()
                        keyword_low = word.lower()
                        if provider_low.find(keyword_low) != -1:
                            save_provider(df['id'][row], item, word)

############################################
def save_provider(jobs_id, competitor_id, keyword):
    connection = psycopg2.connect(user="postgres",
                                    password="]+Dr\DXm()`o=L:+",
                                    host="35.234.81.23",
                                    port="5432",
                                    database="postgres")
    
    try:
        cursor = connection.cursor()

        postgres_insert_query = f"INSERT INTO capstone.jobs_provider (jobs_id, competitor_id, matching_keyword) VALUES ({jobs_id}, {competitor_id}, '{keyword}')"
        print(postgres_insert_query)
        cursor.execute(postgres_insert_query)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

############################################