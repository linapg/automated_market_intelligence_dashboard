from math import isnan
import pandas as pd
import numpy as np
import os
from googletrans import Translator, constants
############################################
def clean_location(jobs):

    location_list = pd.Series([])

    for row in range(len(jobs)):
        value = jobs.loc[row, 'job_location']          # assigning/taking value for every field in column job_location
        location_list[row] = value.split(", ")

    jobs.insert(4, "location_list", location_list)

    return jobs

#############################################
def create_city_state_country(jobs):

    city = pd.Series([])
    state = pd.Series([])
    country = pd.Series([])

    forbidden_words = {'Area','Greater','Metropolitan', 'region', 'Region', 'area', 
                    'greater', 'metropolitan', 'Bay Area', 'bay area', 'Greater ', ' Area', ' area'}

    us_list = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 
            'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 
            'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 
            'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 
            'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

    for row in range(len(jobs)):

        if len(jobs.loc[row,'location_list']) == 3:
            city[row] = jobs.loc[row, 'location_list'][0]
            state[row] = jobs.loc[row, 'location_list'][1]
            country[row] = jobs.loc[row, 'location_list'][2]
            
        elif len(jobs.loc[row,'location_list']) == 2:  ## Washington, D.C. noch als Ausnahme hinzufügen

            if jobs.loc[row, 'location_list'][1] in us_list:
                city[row] = jobs.loc[row, 'location_list'][0]
                state[row] = jobs.loc[row, 'location_list'][1]
                country[row] = 'United States'
            else:
                city[row] = jobs.loc[row, 'location_list'][0]       
                country[row] = jobs.loc[row, 'location_list'][1]   

        else:
            if jobs.loc[row,'location_list'] == jobs.loc[row, 'search_country']:
                country[row] = jobs.loc[row, 'location_list'][0]
            else:
                xx = jobs.loc[row,'location_list'][0].split(' ')
                if len(xx) > 1:
               
                    for word in xx:
                        if word not in forbidden_words:
                            city[row] = ''.join(word)
                else:
                    city[row] = str(xx)
                    
                country[row] = jobs.loc[row, 'search_country']

    jobs.insert(6, "city", city)
    jobs.insert(7, "state", state)
    jobs.insert(8, "country", country)

    return jobs

#############################################
def assign_world_regions(jobs):

    region_category = {
                'Europe' : ['Ukraine', 'France', 'Spain', 'Sweden', 'Norway', 'Germany', 'Finland', 'Poland', 'Italy', 'United Kingdom', 
                            'Romania', 'Belarus', 'Kazakhstan', 'Greece', 'Bulgaria', 'Iceland', 'Hungary', 'Portugal', 'Serbia', 'Austria', 
                            'Czech Republic', 'Ireland', 'Lithuania', 'Latvia', 'Croatia', 'Bosnia and Herzegovina', 'Slovakia', 'Estonia', 
                            'Denmark', 'Switzerland', 'Netherlands', 'Moldova', 'Belgium', 'Albania', 'North Macedonia', 'Slovenia', 
                            'Montenegro', 'Kosovo', 'Azerbaijan', 'Luxembourg', 'Andorra', 'Malta', 'Liechtenstein', 'San Marino', 
                            'Monaco', 'Vatican City', 'Cyprus',  'Czechia', 'Czech Republic'],

                'Africa' : ['Nigeria', 'Ethiopia', 'Egypt', 'DR Congo', 'Tanzania', 'South Africa', 'Kenya', 'Uganda', 'Algeria', 
                            'Sudan', 'Morocco', 'Angola', 'Mozambique', 'Ghana', 'Madagascar', 'Cameroon', 'Niger', 'Burkina Faso', 'Mali', 
                            'Malawi', 'Zambia', 'Senegal', 'Chad', 'Somalia', 'Zimbabwe', 'Guinea', 'Rwanda', 'Benin', 'Burundi', 'Tunisia', 
                            'South Sudan', 'Togo', 'Sierra Leone', 'Libya', 'Congo', 'Liberia', 'Central African Republic', 'Mauritania', 'Eritrea', 
                            'Namibia', 'Gambia', 'Botswana', 'Gabon', 'Lesotho', 'Guinea-Bissau', 'Equatorial Guinea', 'Mauritius', 'Eswatini', 'Djibouti'],

                'Middle East' : ['Turkey', 'Bahrain', 'Kuwait', 'Oman', 'Qatar', 'Saudi Arabia', 'United Arab Emirates', 'Yemen', 'Abkhazia', 'Armenia', 
                            'Artsakh', 'Azerbaijan', 'Georgia', 'South Ossetia', 'Iraq', 'Israel', 'Jordan', 'Lebanon', 'Palestine', 'Syria', 'Iran', 
                            'Akrotiri and Dhekelia', 'Cyprus'],
                            
                'North America' : ['USA', 'United States', 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 
                            'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 
                            'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 
                            'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 
                            'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 
                            'West Virginia', 'Wisconsin', 'Wyoming', 'Canada', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 
                            'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 
                            'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],

                'Central America' : ['Mexico', 'Guatemala', 'Cuba', 'Haiti', 'Dominican Republic', 'Honduras', 'Nicaragua', 'El Salvador', 'Costa Rica', 'Panama', 
                                'Jamaica', 'Trinidad and Tobago', 'Belize', 'Bahamas', 'Barbados', 'Saint Lucia', 'Grenada', 'Antigua and Barbuda', 'Dominica', 
                                'Saint Kitts and Nevis'],

                'South America' : ['Argentina', 'Bolivia', 'Bouvet Island', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Falkland Islands', 'French Guiana', 
                            'Guyana', 'Paraguay', 'Peru', 'South Georgia', 'Suriname', 'Uruguay', 'Venezuela', 'South Sandwich Islands'],

                'South Asia' : ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Nepal', 'Maldives', 'Pakistan', 'Sri Lanka'],

                'Southeast Asia' : ['Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam'],

                'Central Asia' : ['Kazakhstan', 'Kyrgyzstan', 'Tajikistan', 'Turkmenistan', 'Uzbekistan'],

                'East Asia' : ['China', 'Hong Kong', 'Macau', 'Japan', 'Mongolia', 'North Korea', 'South Korea', 'Taiwan']

    }
    world_regions = pd.Series([])

    for row in range(len(jobs)):

        for key in region_category:

            for value in region_category[key]:
                
                if jobs['country'][row] == value:
                    world_regions[row] = key
    
    jobs.insert(6, "world_region", world_regions)

    return jobs

########################################
def create_id(jobs):

    job_id = pd.Series([])

    for row in range(len(jobs)):
        if pd.api.types.is_float(jobs['city'][row]):
            value = str(jobs.loc[row, 'posted_date'] + '_' + jobs.loc[row, 'country'] + '_' + jobs.loc[row, 'job_title'] + '_' + jobs.loc[row, 'company_name']) 
            job_id[row] = value
        else:
            value = str(jobs.loc[row, 'posted_date'] + '_' + jobs.loc[row, 'city'] + '_' + jobs.loc[row, 'job_title'] + '_' + jobs.loc[row, 'company_name']) 
            job_id[row] = value

    jobs.insert(1, "job_id", job_id) 

    return jobs

######################################
def translate_job_titles(jobs):

    translator = Translator()
    job_translate = pd.Series([])

    for row in range(len(jobs)):
        value = translator.translate(jobs.loc[row, 'job_title'])
        job_translate[row] = value.text

    jobs.insert(5, "job_title_trans", job_translate) 

    return jobs

######################################    
def clean_job_titles(jobs):

    forbidden_job_titles = ['(m/f/d)', 'H/F', 'M/F', '(m/f)', 'F/M', '(d/f/m)', '(m/w/d)', '(m/f/diverse)', 'F/H', 
                    '(F/M)', '( F/M)', 'm/f', '(m/f/x)', '(M/F/D)', '(all genders)', '(M/F)', '(d/m/f)', '(m / w / d)', 
                    '(D/W/M)', '(f/m/d)', '(f/m/x)', '(f/m/diverse)', '(F / H)', '(He/She/They)', '(She/He/They)', 
                    'F / H', '(H/F)', '(w/m/d)', '(3rd Shift)', '(1st Shift)','(On-Site', '( F/M)', '(Direct Hire)', 'REMOTE', 
                    '(gn)', '[German speaking]', 'Remote', 'remote', '(Flex/Hybrid Options)', 'Freelance', '(flex/hybrid options)', 
                    '(all genders)', '(m/w/d)-', '(REMOTE - US)', '(m / w / d)', 'Entry-Level', 'Entry-Level ', 'Sr. ', 'Sr.', 
                    ' H / F ',  'F / H', '()', 'F/HF/H', 'm/w/d']
                    
    clean_job_title = pd.Series([])  

    for row in range(len(jobs)):  
        clean_job_title[row] = jobs.loc[row, 'job_title_trans']

        for word in forbidden_job_titles:
            if word in jobs.loc[row, 'job_title_trans']:
                clean_job_title[row] = clean_job_title[row].replace(word, '')
            
    jobs.insert(5, "job_title_en", clean_job_title) 
    
    return jobs

######################################
def clean_text(jobs):

    jobs['full_text'] = jobs['full_text'].astype('string')

    for row in range(len(jobs)):
        rows = jobs.loc[row, 'full_text']
        jobs.loc[row, 'full_text'] = rows.replace("\n","")

    jobs['full_text'] = jobs['full_text'].str.strip()

    return jobs

############################
def translate_job_description(jobs):

    translator = Translator()
    description_translate = pd.Series([])

    for row in range(len(jobs)):
        value = translator.translate(jobs.loc[row, 'full_text'])
        description_translate[row] = value.text.replace("'","''")
        
    jobs.insert(5, "job_description", description_translate) 
    
    return jobs

###############################   
def delete_columns(jobs):

    jobs = jobs.drop(columns='job_title_trans',axis=1)
    jobs = jobs.drop(columns='location_list',axis=1)
    jobs = jobs.drop(columns='job_location',axis=1)
    jobs = jobs.drop(columns='full_text',axis=1)
    jobs = jobs.drop(columns='job_title',axis=1)

    return jobs
               
####################################
def upload_competitor_db(jobs):

    schema = os.getenv('schema')
    from sql import engine
    for row in range(len(jobs)):
        try:
            jobs.iloc[row:row+1, :].to_sql(name='jobs',         # Name of DataFrame
                                            con=engine,         # Engine or connection
                                            if_exists='append', # Just add new values in existing table
                                            schema=schema,      # Use schema that was defined earlier in .sql
                                            index=False,        # Write DataFrame index as a column
                                            chunksize=1,        # Specify the number of rows in each batch to be written at a time
                                            method='multi')     # Pass multiple values in a single INSERT clause
            print(f"row {row} of jobs was inserted successfully.")
        except:
            print(f"row {row} of jobs was ignored.")
            continue
        
####################################