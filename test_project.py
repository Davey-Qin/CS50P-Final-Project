import pytest
import project

def test_load_courses():
    courses = project.load_courses("courses.csv")
    assert type(courses) == dict
    assert "CISS" in courses
    assert "100" in courses["CISS"]

def test_get_courses():
    courses = project.load_courses("courses.csv")
    course = project.get_courses(courses, "CISS", "100")
    assert course["name"] == "Introduction to Computer Science"
    assert course["credits"] == "4"
    assert course["prerequisites"] == []
    assert course["instructor"] == "Peter Wood"
    
def test_build_parser():
    parser = project.build_parser()
    args = parser.parse_args(["CISS", "101", "-n"])
    assert args.section == "CISS"
    assert args.number == "101"
    assert args.name == True
    assert args.credits == False