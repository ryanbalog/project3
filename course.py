'''
Project 3
CS2420
Ryan Balog
'''


class Course:
    '''Node class that stores course data and next pointer'''

    def __init__(self, course_number=0, course_name="", \
        course_credit_hr=0.0, course_grade=0.0, next=None):
        if not isinstance(course_number, int) or course_number < 0:
            raise ValueError("error")

        if not isinstance(course_name, str):
            raise ValueError("error")

        if not isinstance(course_credit_hr, float) or course_credit_hr < 0:
            raise ValueError("error")

        if not isinstance(course_grade, float) or course_grade < 0:
            raise ValueError("error")
        self.course_number = course_number
        self.course_name = course_name
        self.course_credit_hr = course_credit_hr
        self.course_grade = course_grade
        self.next = next

    def number(self):
        '''returns course number'''
        return self.course_number

    def name(self):
        '''returns course name'''
        return self.course_name

    def credit_hr(self):
        '''returns credit hours of course'''
        return self.course_credit_hr

    def grade(self):
        '''returns grade for the course'''
        return self.course_grade

    def __str__(self):
        '''returns a string of the course information'''
        return f"cs{self.course_number} {self.course_name} Grade:{self.course_grade}Credit Hours: {self.course_credit_hr}"
