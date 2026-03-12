import argparse
import csv
import os
import sys

# Get the actual data from CSV amd put it into a giant nested dictionary
def get_courses(filepath):
    #check for existence
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    
    # The big main dictionary containing everything
    courses = {}
    # This dictionary will contain 3 layers:
    #The section, course number, and whatever element desired

    with open(fileppath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        #for each row, do this
        for row in reader:
            section = row["section"].upper()
            number = row["number"]

            #check if section is already in courses dictionary. if not, add
            if section not in courses:
                courses[section] = {}
            
            #split up prerequisites into a list
            prereqs = row["prerequisites"]
            if prereqs.strip().lower() == "none" or prereqs.strip() == "":
                prereqs = []
            else:
                prereqs = [prereq.strip() for prereq in prereqs.split(";")]

            # Within the section dictionary, nest a number dictionary who
            # has the key value pairs of all the elements

            courses[section][number] = {
                "name" : row["name"]
                "credits" : row["credits"]
                "prerequisites" : row["prerequisites"]
                "instructor" : row["instructor"]
            }
    return courses

# Give back the specific course needed, and also
# used to validate user input, ensure it's in the dictionary
def get_courses(courses, section, number):

    # If section not found, raise exceptions and list avaliable sections
    if section not in courses:
        raise Exception(
            f"Section {section} not found in courses."
            f"Available sections: {', '.join(courses.keys())}"
        )
    
    # If course number not found, list avaliable course numbers within that section
    if number not in courses[section]:
        raise Exception(
            f"Course {number} not found in section {section}."
            f"Available courses: {', '.join(courses[section].keys())}"
        )
    return courses[section][number]


        