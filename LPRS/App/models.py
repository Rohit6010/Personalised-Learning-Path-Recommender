from django.db import models

# Create your models here.
class SignUp(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    phone = models.IntegerField(default=0)

class Array(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return '(' + str(self.id) + ') ' + self.level

class LinkedList(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return self.question
    
class Tree(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return self.question

class Recursion(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return self.question

class DP(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return self.question

class Graph(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return self.question
    
class Stack(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return self.question

class Queue(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return self.question

class String(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return self.question

class Heap(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__ (self):
        return self.question

class Student(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    textual_trait = models.IntegerField(default=0)
    visual_trait = models.IntegerField(default=0)
    curr_topic = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)

    def __str__ (self):
        return self.username

class AssessDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    topic = models.CharField(max_length=30)
    scoreBeg = models.IntegerField(default=0)
    scoreImd = models.IntegerField(default=0)
    scoreExp = models.IntegerField(default=0) 
    level = models.CharField(max_length=20, blank=True, null=True)

    def __str__ (self):
        return self.student.username + "_" + self.topic 

class Content(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subtopic = models.CharField(max_length=30)

    text1 = models.CharField(max_length=5000,blank=True, null=True)
    text2 = models.CharField(max_length=5000,blank=True, null=True)
    text3 = models.CharField(max_length=5000,blank=True, null=True)
    text4 = models.CharField(max_length=5000,blank=True, null=True)

    video1 = models.CharField(max_length=5000, blank=True, null=True)
    video2 = models.CharField(max_length=5000, blank=True, null=True)
    video3 = models.CharField(max_length=5000, blank=True, null=True)
    video4 = models.CharField(max_length=5000, blank=True, null=True)
   
    def __str__ (self):
        return self.subtopic

class TopicId(models.Model):
     id = models.IntegerField(default=0, primary_key=True)
     topic = models.CharField(max_length=50, blank=True, null=True)
     

     def __str__ (self):
        return self.topic
  
class Cognitive(models.Model):
    question = models.CharField(max_length=1000)
    option_text = models.CharField(max_length=100)
    option_visual = models.CharField(max_length=100)

    def __str__ (self):
        return self.question

class Practice(models.Model):
    topic = models.CharField(max_length=50)
    question = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    level = models.CharField(max_length=50)

    def __str__ (self):
        return "("+self.topic+") ("+self.level+") "+ self.question
