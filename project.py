import argparse
import csv
import os
import sys

# Get the actual data from CSV amd put it into a giant nested dictionary
def load_courses(filepath):
    #check for existence
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    
    # The big main dictionary containing everything
    courses = {}
    # This dictionary will contain 3 layers:
    #The section, course number, and whatever element desired

    with open(filepath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        #for each row, do this
        for row in reader:
            section = row["section"].upper().strip()
            number = row["number"].strip()

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
                "name" : row["name"].strip(),
                "credits" : row["credits"].strip(),
                "prerequisites" : prereqs,
                "instructor" : row["instructor"].strip()
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

def build_parser():
    # Help for the users
    parser = argparse.ArgumentParser(
        prog="courses.py",
        description="Look up college course information",
        epilog="Example: python courses.py CISS 101 -ci"
    )

    # Positional arguments, which course to look up
    # If in there, set to true. This will be utilized later as condtionals
    # to decide what to display

    parser.add_argument(
        "section",
        help="Course section identifier"
    )

    parser.add_argument(
        "number",
        help="Course number"
    )

    parser.add_argument(
        "-n", "--name",
        action="store_true",
        help="Show course name"
    )

    parser.add_argument(
        "-c", "--credits",
        action="store_true",
        help="Show number of credits"
    )
    
    parser.add_argument(
        "-p", "--prerequisites",
        action="store_true",
        help="Show prerequisites"
    )

    parser.add_argument(
        "-i", "--instructors",
        action="store_true",
        help="Show intructor"
    )

    return parser

# Function to finally display all the things.
# Takes in course section, number, the actual course, and arguments
def display_course(section, number, course, args):
    print(f"\n{section} {number}")
    print("-" * 20)
    if args.name:
        print(f"  Name: {course['name']}")
    if args.credits:
        print(f"  Credits: {course['credits']}")
    if args.prerequisites:
        prereqs = course["prerequisites"]
        if prereqs:    
            prereq_str = ", ".join(prereqs) 
        else:
            prereq_str = "None"
        print(f"  Prereqs: {prereq_str}")
    if args.instructors:
        print(f"  Instructor: {course['instructor']}")

def main():
    parser = build_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    #show help if no flags given
    if not any([args.name, args.credits, args.prerequisites, args.instructors]):
        parser.print_help()
        sys.exit(0)

    courses = load_courses("courses.csv")
    try: 
        course = get_courses(courses, args.section, args.number)
    except Exception as exception:
        print(f"Exception occured: {exception}")
        sys.exit(1)

    display_course(args.section.upper(), args.number, course, args)
    print()

        



if __name__ == "__main__":
    main()



        