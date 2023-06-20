import uuid
# Name : mohammed alothmani
# Delivery Date :20/06/2023
# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
class Course :
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

class Studant :
    total_studants = 0


    def __int__(self, student_name, student_age,student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = [...]
        Studant.total_studants +=1

    def enroll_new_course(self,course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_studant_courses(self):
        for course in self.courses_list:
            print(f'course id : {course.course_id}')
            print(f'course name : {course.course_name}')
            print(f'course id : {course.course_mark}')
            print()
            print()
    def get_studant_avareg(self):
        total_marks = 0
        for course in self.courses_list:
            total_marks += course.course_mark
        if len(self.courses_list) > 0 :
            avareg = total_marks/ len(self.courses_list)
            return avareg
        else:
            return 0









