## @brief Models for the instructor app.

from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


## @brief This class represents the instructors enrolled in the website.
class Instructor(models.Model):
    ## The user associated with the instructor
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    ## The name of the instructor
    name = models.CharField(max_length=100)

    ## The information about the instructor
    information = models.CharField(max_length=1000)

    ## @brief This function returns the string representation of the instructor class.
    #
    # Used by Django admin website to represent the instructor objects.
    # @param self The object pointer.
    def __str__(self):
        return self.name


## @brief This class represents the courses.
class Course(models.Model):
    ## The name of the course
    name = models.CharField(max_length=100)

    ## The course code
    code = models.CharField(max_length=10)

    ## The instructor of the course
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    ## The course logo
    course_logo = models.FileField(default=1, upload_to='course_pic')

    credits = models.IntegerField(blank=True, default=1)

    ## @brief This function returns the string representation of the course class.
    #
    # Used by Django admin website to represent the course objects.
    def __str__(self):
        return self.name


## @brief This class represents the assignments in a course.
class Assignment(models.Model):

    ##The short title of the assignment
    title = models.CharField(max_length=100, default='')

    ## The description of the assignment
    description = models.CharField(default='', blank=True, max_length=1000)

    ## The file containing the problems for the assignment
    file = models.FileField(default='', upload_to='assignments')

    ## The course associated with the assignment
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    ## The date,time of posting the assignment
    post_time = models.DateTimeField(auto_now=True)

    ## The deadline to complete the assignment for the students
    deadline = models.CharField(blank=True, max_length= 100)

    def __str__(self):
        return self.title
        


## @brief This class represents the submissions for an assignment.
class Submission(models.Model):
    ## The file submitted by student
    file_submitted = models.FileField(default='', upload_to='submissions')

    ## The date,time of uploading the submission
    time_submitted = models.CharField(max_length=100)

    ## The user associated with the submission(who uploaded the submission)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    ## The assignment associated with the submission
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE, default=1)

    remarks = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.user
        




