'''This module contains classes that represent tables in the database '''
# pylint: disable=R0903, C0115
from django.db import models





class Lessons(models.Model):
    '''This class represents a table containing all information about the lesson units'''
    lesson_id = models.IntegerField(primary_key=True)
    lesson_name = models.CharField(max_length=50, blank=True, null=True)
    teacher_email = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='teacher_email', blank=True, null=True)
    email = models.ForeignKey('Planners', models.DO_NOTHING, db_column='email', blank=True, null=True)
    classroom = models.CharField(max_length=50, blank=True, null=True)
    lesson_pref = models.JSONField(blank=True, null=True)
    numbers_of_lesson = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Lessons'


class Planners(models.Model):
    '''This class represents tables that hold information about schedulers '''
    email = models.CharField(primary_key=True, max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Planners'


class Polls(models.Model):
    '''This class represents tables that hold survey data'''
    pool_id = models.IntegerField(primary_key=True)
    email = models.ForeignKey(Planners, models.DO_NOTHING, db_column='email', blank=True, null=True)
    teacher_email = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='teacher_email', blank=True, null=True)
    teacher_pref = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Polls'


class Teachers(models.Model):
    '''This class represents tables that hold information about teachers '''
    teacher_email = models.CharField(primary_key=True, max_length=50)
    teacher_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Teachers'


class Timetables(models.Model):
    '''This class represents the tables that hold the timetable '''
    timetable_id = models.IntegerField(primary_key=True)
    data = models.JSONField(blank=True, null=True)
    email = models.ForeignKey(Planners, models.DO_NOTHING, db_column='email', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Timetables'


class DjangoContentType(models.Model):
    '''Default django table'''
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    ''' Default django table'''
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'