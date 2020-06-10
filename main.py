'''
Project 3
CS2420
Ryan Balog
'''

from course import Course
from courselist import CourseList


def main():
    '''driver function'''
    course_list = CourseList()
    with open('data.txt', 'r') as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            course_list.insert(Course(int(line[0]), line[1], float(line[2]), float(line[3])))


    print(f"Current List: ({course_list.size()})")
    print(course_list)
    print(f"\n\n\n\nCumulative GPA: {round(course_list.calculate_gpa(),3)}\n\n")


if __name__ == "__main__":
    main()
