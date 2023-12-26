from django.db import models
from django.contrib.auth.models import AbstractUser


class Direction(models.Model):
    name = models.CharField(max_length=250)
    duration = models.IntegerField()
    payment = models.DecimalField(decimal_places=2, max_digits=25)

    def __str__(self):
        return self.name


class User(AbstractUser):
    status = models.IntegerField(choices=(
        (1, 'mentor'),
        (2, 'reception'),
        (3, 'accountant'),
        (4, 'director')
    ), blank=True, null=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True, blank=True)


class Region(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Student(models.Model):
    status = models.IntegerField(choices=(
        (1, 'active'),
        (2, 'in_group'),
        (3, 'leave'),
        (4, 'graduated'),
        (5, 'passive')
    ), default=1)
    full_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=250)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=250)
    extra_phone = models.CharField(max_length=250)
    debt = models.DecimalField(decimal_places=2, max_digits=22, default=0)

    def __str__(self):
        return self.full_name


class Group(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    created_at = models.CharField(max_length=250)

    def __str__(self):
        return self.direction.name


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=24, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.full_name
