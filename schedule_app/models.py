from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    position = models.ForeignKey(
        Position, null=True, on_delete=models.SET_NULL)
    company = models.CharField(max_length=200, null=True)
    date_hired = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    # STATUS = (
    #     ('Assigned', 'Assigned'),
    #     ('In Progress', 'In Progress'),
    #     ('Complete', 'Complete')
    # )
    PRIORITY = (
        ('Not Important', 'Not Important'),
        ('Important', 'Important'),
        ('Very Important', 'Very Important')
    )
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_assigned = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField(null=True)
    status = models.CharField(max_length=200, null=True, choices=PRIORITY)
    # status = models.CharField(max_length=200, null=True, choices=STATUS)
    employee = models.ForeignKey(
        Employee, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
