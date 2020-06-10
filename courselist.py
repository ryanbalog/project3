'''
Project 3
CS2420
Ryan Balog
'''

from recursioncounter import RecursionCounter
from course import Course


class CourseList:
    '''controls courses in a linked list structure'''

    def __init__(self):
        self.head = None

    def insert(self, course):
        '''inserts course to list'''
        if self.head == None:
            self.head = course
        elif self.head.course_number > course.course_number:
            course.next = self.head
            self.head = course
        else:
            self.insert_helper(self.head, self.head.next, course)

    def insert_helper(self, previous, current, course):
        '''recursively finds correct location for insertion'''
        RecursionCounter()

        if current is None:
            previous.next = course
        elif course.course_number < current.course_number:
            previous.next = course
            course.next = current
        else:
            self.insert_helper(current, current.next, course)

    def remove(self, number):
        '''removes a class node from list'''
        if self.head is None:
            return None
        if self.head.course_number == number:
            self.head = self.head.next
            return True
            
        return self.remove_helper(self.head, self.head.next, number)

    def remove_helper(self, prev, current, number):
        '''recursively checks list for class node'''
        RecursionCounter()

        if not current is None:
            if current.course_number == number:
                prev.next = current.next
                return True
            return  self.remove_helper(current, current.next, number)
        return False


    def remove_all(self, number):
        '''removes all class nodes of a specific class ID'''
        RecursionCounter()
        if self.head is None:
            return None
        if self.head.course_number == number:
            self.head = self.head.next
            return self.remove_all(number)
        return self.remove_all_helper(self.head, self.head.next, number)

    def remove_all_helper(self, prev, current, number):
        '''recursively iterates nodes looking for classID for removal'''
        RecursionCounter()

        if not current is None:
            if current.course_number == number:
                prev.next = current.next
                if not prev.next.next is None:
                    return self.remove_all_helper(prev, prev.next, number)
                return True
            return  self.remove_all_helper(current, current.next, number)
        return False

    def find(self, number):
        '''finds a class node'''
        return self.find_helper(self.head, number)

    def find_helper(self, current, number):
        '''returns class node if found'''
        RecursionCounter()
        if current is None:
            return False
        if current.course_number == number:
            return current
        return self.find_helper(current.next, number)
        

    def size(self):
        '''returns size of course list'''
        if self.head == None:
            return 0
        return self.size_helper(self.head)

    def size_helper(self, current):
        '''recursively iterates course list to count size'''
        RecursionCounter()
        if current is None:
            return 0
        return 1 + self.size_helper(current.next)

    def calculate_gpa(self):
        '''calculates GPA'''
        vals = [0.0, 0.0]
        if self.head is None:
            return 0.0
        vals = self.calculate_gpa_helper(self.head, vals)
        num = vals[0]
        den = vals[1]
        gpa = num / den

        return gpa

    def calculate_gpa_helper(self, current, val):
        '''recursively iterates linked list for gpa calculation'''
        RecursionCounter()
        val[0] += (current.course_credit_hr * current.course_grade)
        val[1] += current.course_credit_hr

        if current.next is None:
            return val
        return self.calculate_gpa_helper(current.next, val)

    def is_sorted(self):
        '''checks if list is sorted by class ID'''
        if self.head == None:
            return True
        return self.is_sorted_helper(self.head)

    def is_sorted_helper(self, current):
        RecursionCounter()

        if current.next is None:
            return True
        if current.course_number > current.next.course_number:
            return False
        return self.is_sorted_helper(current.next)

    def __str__(self):
        '''returns string representation of course list'''
        if self.head is None:
            return

        return self.str_helper(self.head)

    def str_helper(self, current):
        RecursionCounter()
        if current.next is None:
            return current.__str__()
        return current.__str__() +"\n"+ self.str_helper(current.next)

    def __iter__(self):
        self.cursor = self.head
        return self

    def __next__(self):
        if self.cursor is None:
            raise StopIteration
        else:
            course = self.cursor
            self.cursor = self.cursor.next
            return course