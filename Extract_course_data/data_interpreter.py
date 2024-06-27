from datetime import datetime
import pandas as pd
from tqdm import tqdm
from datetime import datetime

#### CODE TO CALCULATE CLASS DURATION ####
def calculate_duration(start_time, end_time):
    """Calculate the duration between start and end times."""
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    duration = end - start
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{int(hours)}.{int(minutes / 60*10)}"  # Rounded to nearest quarter-hour

# Function to recover combinations
def recover_combinations(combination):
    # days_char = [
    #     'M', 'T', 'W', 'Th', 'F'
    # ]
    recovered_combinations = []
    i = 0
    while i < len(combination):
        if combination[i:i+2] == 'Th':  # Check for 'Th'
            recovered_combinations.append('Th')
            i += 2  # Skip the next character since 'Th' is two characters long
        else:
            recovered_combinations.append(combination[i])
            i += 1  # Move to the next character
    
    return recovered_combinations

def clean_time_entry(entry):        ## THANKS RAGHAV(daddy2002)
    if pd.isna(entry) or entry.lower() == 'nan':
        return 'null'
    # Split the entry by spaces and process each part
    try:
        parts =  entry.split(',')
    except:
        parts = parts
    
    daytime = {'M':'null', 'T':'null', 'W':'null', 'Th':'null', 'F':'null'}
    days_char = [
    'M', 'T', 'W', 'Th', 'F',
    'MT', 'MW', 'MTh', 'MF',
    'TW', 'TTh', 'TF',
    'WTh', 'WF',
    'ThF',
    'MTW', 'MTTh', 'MTF',
    'MWTh', 'MWF',
    'MThF',
    'TWTh', 'TWF',
    'TThF',
    'WThF',
    'MTWTh', 'MTWF',
    'MTThF', 'MWThF',
    'TWThF',
    'MTWThF']

    for part in parts:
        cont = part.split()
        time_range = cont[-1]
        if '-' in time_range:
            start_time, end_time = time_range.split('-')
            duration = calculate_duration(start_time, end_time)
        for day in days_char:
            if (day in cont):
                # print(day)
                day = recover_combinations(day)
                # print(day)
                for daisy in day:
                    daytime[daisy] = ([time_range,duration])
    # print(daytime)
    return daytime

def get_time_segment_in_binary(stri):
    # Define the start and end times
    if stri == 'n':
        stri = "08:00-08:00"
    classt = stri.split('-')
    ref_time = datetime.strptime("08:00", "%H:%M")
    start_time = datetime.strptime(classt[0], "%H:%M") - ref_time
    end_time = datetime.strptime(classt[1], "%H:%M") - ref_time
    start_time = int(start_time.total_seconds() / (60*15))
    end_time = int(end_time.total_seconds() / (60*15))
    bin_val = 2**end_time - 2**start_time # 10-11 class answer: 1111 0000 0000
    return bin_val
    

def add_day_binaries(row):
    lec_time = row['lec']
    tut_time = row['tut'] 
    lab_time = row['lab']
    if (lec_time == "null"):
        lec_time = {'M':'null', 'T':'null', 'W':'null', 'Th':'null', 'F':'null'}
    if (tut_time == "null"):
        tut_time = {'M':'null', 'T':'null', 'W':'null', 'Th':'null', 'F':'null'}
    if (lab_time == "null"):
        lab_time = {'M':'null', 'T':'null', 'W':'null', 'Th':'null', 'F':'null'}
    
    days = ['M', 'T', 'W', 'Th', 'F']
    for day in days:
        arr_lec = lec_time[day]
        arr_tut = tut_time[day]
        arr_lab = lab_time[day]
        arr_lec = get_time_segment_in_binary(arr_lec[0])
        arr_tut = get_time_segment_in_binary(arr_tut[0])
        arr_lab = get_time_segment_in_binary(arr_lab[0])
        row[day] = arr_lab | arr_lec | arr_tut


def process_times(row):
    lec_time = clean_time_entry(row['Time'])
    # print(lec_time)
    tut_time = clean_time_entry(row['Time.1'])
    # print(tut_time)
    lab_time = clean_time_entry(row['Time.2'])
    # print(lab_time)
    row['lec'] = lec_time
    row['tut'] = tut_time
    row['lab'] = lab_time
    add_day_binaries(row)
    return row

def interpret_data(df):
    #### Managing Credits Column in Data Frame ####
    # Drop rows with any missing values
    df = df.drop_duplicates()  # Remove duplicate rows
    # Extract Credits as integers from the format '0-0-0-0(3)'

    df['Credits'] = df['Credits'].str.extract(r'\((\d+)\)')
    # Handle NaN values before conversion
    df['Credits'] = df['Credits'].fillna(0)  # Replace NaN with 0
    df['Credits'] = df['Credits'].astype(int)  # Convert to integer

    # Apply the processing function to each row
    tqdm.pandas() 
    df = df.progress_apply(process_times, axis=1)
    # Drop original columns if needed
    df = df.drop(columns=['Time', 'Time.1', 'Time.2'])
    #### Managing Credits Column in Data Frame ####
    return df

if __name__ == "__main__":
    print("NOT FOR THIS PURPOSE")
    ## DEV TOOLS
    # data = {
    # 'Course Name/Group Name': ['Test Course'],
    # 'Credits': ['0-0-0-0(3)'],
    # 'Time': ['M (EEM117) W (EEM117) F (EEM117) 17:00-18:30'],
    # # 'Time':['TF (boobies) 9:00-10:00'], 
    # 'Time.1': ['TF (EEM117) 09:00-10:00, M (EEM117) 09:45-10:45'],
    # 'Time.2': ['nan']
    # }

    # data = {
    # 'Course Name/Group Name': ['Test Course', 'Test Course 2', 'Test Course 3'],
    # 'Credits': ['0-0-0-0(3)', '0-0-0-0(3)', '0-0-0-0(3)'],
    # 'Time': ['MWTh (EEM117) 09:00-10:00, M (EEM117) 09:45-10:45', 'TF (EEM118) 10:00-11:00', 'M (EEM119) 11:15-12:15'],
    # 'Time.1': ['TF (EEM117) 09:00-10:00, M (EEM117) 09:45-10:45','nan','nan'],
    # 'Time.2': ['nan','nan','nan']
    # }
    # df = pd.DataFrame(data)
    # print(df)
    # output = interpret_data(df)
    # # pd.set_option("display.max_columns", None)
    # print(output)
    # print('..............................')
    # print(output['lec'][0])