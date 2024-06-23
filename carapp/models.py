from django.db import models

# Create your models here.

class coursemodule(models.Model):
    department = models.CharField(max_length= 255)
    program = models.CharField(max_length= 255)
    yearofstudy = models.IntegerField()
    modulename= models.CharField(max_length= 255)
    modulecode = models.CharField(max_length= 50,unique= True)

    def _str_(self):
        return self.modulename

class questions(models.Model):
    question = models.TextField(max_length=5000)
    modulecode = models.ForeignKey("coursemodule",on_delete= models.CASCADE)
    choice_1= models.TextField(max_length= 1000,null=True)
    choice_2= models.TextField(max_length= 1000,null=True)
    choice_3= models.TextField(max_length= 1000,null=True)
    choice_4= models.TextField(max_length= 1000,null=True)
    choice_5= models.TextField(max_length= 1000,null=True)
    choice_6= models.TextField(max_length= 1000,null=True)
    wrong_7= models.TextField(max_length= 1000,null=True)
    wrong_8= models.TextField(max_length= 1000,null=True)
    wrong_9= models.TextField(max_length= 1000,null=True)
    wrong_10= models.TextField(max_length= 1000,null=True)
    def _str_(self):
        return self.question
    
