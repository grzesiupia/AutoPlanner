# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# pylint: disable=R0903, C0115, C0114, C0301
from django.db import models


class Classrooms(models.Model):
    '''This class represents tables that hold information about classrooms '''
    classroomid = models.CharField(db_column='classroomId', primary_key=True, max_length=255)  # Field name made lowercase.
    preferredsubject = models.CharField(db_column='preferredSubject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    planneremail = models.CharField(db_column='plannerEmail', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Classrooms'
        unique_together = (('classroomid', 'planneremail'),)


class Lessons(models.Model):
    '''This class represents a table containing all information about the lesson units'''
    planneremail = models.CharField(db_column='plannerEmail', primary_key=True, max_length=255)  # Field name made lowercase.
    classname = models.CharField(db_column='className', max_length=255)  # Field name made lowercase.
    lessonname = models.CharField(db_column='lessonName', max_length=255)  # Field name made lowercase.
    teacheremail = models.CharField(db_column='teacherEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classroomname = models.CharField(db_column='classroomName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lessoncount = models.IntegerField(db_column='lessonCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lessons'
        unique_together = (('planneremail', 'classname', 'lessonname'),)


class Planners(models.Model):
    '''This class represents tables that hold information about schedulers '''
    planneremail = models.CharField(db_column='plannerEmail', primary_key=True, max_length=255)  # Field name made lowercase.
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Planners'


class Polls(models.Model):
    '''This class represents tables that hold survey data'''
    pollid = models.IntegerField(db_column='pollId', primary_key=True)  # Field name made lowercase.
    teacheremail = models.CharField(db_column='teacherEmail', max_length=255)  # Field name made lowercase.
    teacherpref = models.JSONField(db_column='teacherPref')  # Field name made lowercase.
    planneremail = models.CharField(db_column='plannerEmail', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Polls'


class Subjects(models.Model):
    '''This class represents tables that hold information about subjects '''
    subjectname = models.CharField(db_column='subjectName', primary_key=True, max_length=255)  # Field name made lowercase.
    planneremail = models.CharField(db_column='plannerEmail', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subjects'
        unique_together = (('subjectname', 'planneremail'),)


class Teachers(models.Model):
    '''This class represents tables that hold information about teachers '''
    teacheremail = models.CharField(db_column='teacherEmail', primary_key=True, max_length=255)  # Field name made lowercase.
    teachername = models.CharField(db_column='teacherName', max_length=255)  # Field name made lowercase.
    teachsubject = models.CharField(db_column='teachSubject', max_length=255)  # Field name made lowercase.
    planneremail = models.CharField(db_column='plannerEmail', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teachers'


class Timetables(models.Model):
    '''This class represents the tables that hold the timetable '''
    timetableid = models.IntegerField(db_column='timetableId', primary_key=True)  # Field name made lowercase.
    data = models.JSONField()
    planneremail = models.CharField(db_column='plannerEmail', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Timetables'