#import csv file
import os
import csv

dirname = os.path.dirname(__file__)
employee_csv = os.path.join(dirname,"..", "Resources", "employee_data.csv")

emp_id = []
full_name = []
dob = []
new_dob_format = []
ssn = []
state = []
first_name = []
last_name = []
new_ssn = []
state_abv = []

# Dictionary containing states names as keys and abbreviations as values (provided) 
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(employee_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

    for row in csvreader:
        #employee ID list
        emp_id.append(row[0])

        #names list
        full_name = row[1].split(" ")
        first_name.append(full_name[0])
        last_name.append(full_name[1])

        #date of birth conversion by adjusting order
        dob = row[2].split("-")
        new_dob_format.append(f'{dob[2]}/{dob[1]}/{dob[0]}')

        #split ssn and convert to ***-** format
        ssn = row[3].split("-")
        new_ssn.append(f'***-**-{ssn[2]}')

        #match state list to dictionary and if matched, append dictionary list
        state_abv.append(us_state_abbrev[row[4]])

new_employee_csv = zip(emp_id, first_name, last_name, new_dob_format, new_ssn, state_abv)

output_file = os.path.join(dirname,"..","Resources","employee_data_final.csv")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    writer.writerows(new_employee_csv)
