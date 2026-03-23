# CLI College Course Catalog
#### Video Demo: https://www.youtube.com/watch?v=3PeOz1bd2wg
#### Description:
 This command-line tool lets you quickly look up information about college courses from a CSV file. Instead of manually searching, you can type a simple command followed by options of choice to instatnly retrieve details about any course in the database, including the course name, number of credits, prerequisites, and instructor.
 #### How to use:
 To look up a course, run the program with a section and course number, along with any flags for the information you want:
```
python courses.py [section] [number] [-n] [-c] [-p] [-i]
```
The available flags are:
- `-n` — show the course name
- `-c` — show the number of credits
- `-p` — show prerequisites
- `-i` — show the instructor

You can also combine flags, for example `-nci` instead of typing `-n -c -i` separately. If you run the program withno arguments, or with the `--help` flag, it will display a help menu explaining all available options.


#### File Descriptions
**courses.py** — The main program file. It contains all the logic for loading course data, looking up courses, displaying results, and handling command line arguments. It is broken into several functions to keep the code organized and easy to read. Each function has a single clear responsibility rather than putting everything into one large block of code.

**courses.csv** — The data file that stores all the course information. Each row represents one course with columns for section, number, name, credits, prerequisites, and instructor. Prerequisites are separated by semicolons when a course has more than one, and the program handles splitting these automatically when loading the data.

**test_courses.py** — Contains all the pytest tests for the project. It tests that courses load correctly from the CSV, that valid courses can be looked up, that invalid sections and course numbers raise proper errors, and that the argument parser works as expected with different combinations of flags.

**README.md** — This file. Documents the project, its files, and the design choices made along the way.

#### Design Chocies:
One of the first decisions was how to store the course data. A CSV file made the most sense because it's simple, easy to edit, and does not require any external software. Anyone can open and edit a CSV in a spreadsheet application like Excel or Google Sheets, making it easy to add or update courses without touching the code at all.

The course data is loaded into a nested dictionary, organized first by section and then by course number. This makes lookups fast and clean since any course can be accessed directly with courses[section][number] rather than looping through a list every time.

The program is split into several separate functions rather than writing everything in one place. This makes the code easier to read, test, and modify. For example, get_course handles both looking up a course and validating that it exists, returning clear error messages if the section or number is not found instead of crashing with a confusing Python error.

Finally, argparse was chosen to handle command line arguments rather than manually reading from sys.argv. Argparse automatically generates a help menu, handles missing argument errors, and supports combining short flags like -nci, all without any extra code needed.

The goal of this project was to build something practical and useful while learning how to work with command line arguments, file I/O, argparse, and data structures in Python.


