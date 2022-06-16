import pandas as pd
import numpy as np
import os
import re

####################################################################
subcategory = {
'Customer Support' : ['Field Support Engineer', 'Field Service Support Engineer', 'Product Support Engineering Lead', 'In-Service Solution Design Engineer', 
                                        'Repair Design Engineer - Back office', 'Product Support Engineer (Electrical System)'],

'Development' : ['Aviation Systems Engineer', 'Analog Electronics Engineer Energy Conversion', 'Principal Validation Verification (V&V) Engineer', 
                'EMC Senior Specialist Engineer', 'Design Engineer', 'Aerospace Data & Process Engineer', 'Performance Dynamics Engineer', 
                'Aero equipment environmental qualification test engineer', 'Engineer-Expert-e Sauvegarde F / H', 
                'System Engineer', 'Functional Engineer Industrial Systems & Data', 'Work-study engineer electrical engineer', 
                'General Aerothermal Engineer', 'Hydraulic Control Systems Engineer', 'Ingenieur conception amelioration LEAP', 
                'Operational Safety Engineer', 'Calculation Methods Engineer - Bearings & Seals', 'Engineer-Usage Methods & Equipment F / H', 
                'Inertial physical modeling engineer', 'MdP densification modeling engineer', 'Structural Calculation Methods Engineer -', 
                'Calculation Tools & Methods Engineer - Tribology', 'PLM Engineer (Product Lifecycle Management)', 'Experienced EMC engineer', 
                'Electronic Board Development Engineer', 'Senior Product Engineer', 'Reliability, Availability. Maintainability Safety (RAMS) Engineer', 
                'Performance Dynamics Engineer', 'CAM PROJECT ENGINEER', 'Tooling Engineer', 'Systems Engineer - Safety & Reliability', 
                'Senior Industrial Innovation Engineer', 'Lead BoM Integration Engineer', 'Tooling Engineer', 'Senior Assembly Methods Engineer', 
                'Principal Electronics Engineer', 'Senior Simulation Means Engineer', 'Senior V&V Engineer', 'Senior Principal Validation Verification (V&V) Engineer', 
                'Senior Electronics Engineer', 'Methods Engineer Rotating Parts', 'Calculation Tools & Methods Engineer', 'AASM Product Engineer', 'Engineer BE / MOA H / F', 
                'Functional Safety Study Engineer', 'HP turbine thermal engineer in-service support', 'Functional pilot PLM/CAD Industrialization Methods', 
                'Engineer-e specialized machining method costs', 'Engineer Development C optronic models', 'CEPI M&P Patents Engineer', 
                'Functional System Missile Test Engineer', 'Inertial Equipment System Engineer', 'Patent Engineer EED Pole CEPI', 'Optronic Observation Systems Engineer', 
                'Optronics System Engineer', 'Airborne Sights System Engineer', 'System Engineer - Combatant Digitization', 'Chemical Engineer', 'Design Engineer', 
                'Design Engineer - Composites', 'Design Engineer II'],

'Managing' : ['Project Engineer', 'Principal Product Engineer', 'Engineering Project Lead', 'SENIOR PRODUCT ENGINEER', 'Senior Configuration Engineer', 'Configuration Management Engineer'],

'Process & Improvement' : ['IS industrial Engineer / Analyst', 'Continuous Improvement Engineer', 'Process Development Engineer', 'Process Development Investment Engineer', 
            'Production industrial performance engineerM/F', 'Process methods engineer', 'Methodist engineer, PLM animator', 'Industrial Methods Engineer', 'Industrial Methods Engineer', 
            'Aerospace Data & Process Engineer', 'External industrialization pilot engineer', 'IS industrial Engineer / Analyst', 'Facilities Engineer', 
            'Pilot Support Shop Visit- Industrial Engineering', 'Industrial Engineer', 'Production Engineer', 'Production Engineer', 'Production Engineer'],

'Testing' : ['Average test reliability performance engineer', 'Electrical Test Engineer', 'Test & Means Engineer', 'Senior Test & Means Engineer', 
            'Engineer responsible test benches means testing']
}
####################################################################
def find_job_keyword(subcat_df):
    #job_cat = pd.Series([])

    for row in range(len(subcat_df)):
        for key in subcategory:
            for subcat in subcategory[key]:
                job_title_low = subcat_df['job_title_en'][row].lower()
                subcat_low = subcat.lower()
                jobs_id = subcat_df['id'][row]

                if re.search(subcat_low, job_title_low):
                    save_subcategories(subcat_df['id'][row], key)

###################################################################
def save_subcategories(subcat, jobs_id):
    connection = psycopg2.connect(user="postgres",
                                    password="]+Dr\DXm()`o=L:+",
                                    host="35.234.81.23",
                                    port="5432",
                                    database="postgres")
    
    try:
        
        cursor = connection.cursor()

        postgres_insert_query = f"UPDATE capstone.jobs_jcat (subcategory) VALUES ('{subcat}') WHERE jobs_id = {jobs_id}"
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
###########################################################