from django.db import models

# Create your models here.

#用户
class Users(models.Model):
    uname=models.CharField(max_length=20,)
    upwd=models.CharField(max_length=20)
    #学院
    ucollege=models.CharField(max_length=20)
    unum=models.CharField(max_length=10)
    uemail=models.EmailField()

    def __str__(self):
        return self.uname


#图书表
class Books(models.Model):
    bname=models.CharField(max_length=30)
    bauthor=models.CharField(max_length=20)
    bpublish_com=models.CharField(max_length=30)
    bpublish_date=models.DateField()

    def __str__(self):
        return self.bname

#借阅历史表
class Histroys(models.Model):
    hbookid=models.ForeignKey('Books',on_delete=models.CASCADE)
    huserid=models.ForeignKey('Users',on_delete=models.CASCADE)
    hdate=models.DateTimeField(auto_now=True)
    hreturn=models.DateTimeField()
    hstatus=models.BooleanField(default=False)