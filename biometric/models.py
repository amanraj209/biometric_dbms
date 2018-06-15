from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password

class NonAcademicStaff(models.Model):
    staff_id = models.AutoField(primary_key=True, null=False, unique=True)
    staff_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    phone_no = models.CharField(max_length=10, null=False, validators=[MinLengthValidator(10)])
    enrolment_date = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return str(self.staff_id)

class Administrator(models.Model):
    staff_id = models.ForeignKey(NonAcademicStaff, on_delete=models.CASCADE, null=False)
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=200, null=False)

    def save(self, *args, **kwargs):
        if not self.pk:
                self.password = make_password(self.password)
        super(Administrator, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class AttendanceStation(models.Model):
    staff_id = models.ForeignKey(NonAcademicStaff, on_delete=models.CASCADE, null=False)
    num_hours = models.PositiveIntegerField(null=False)
    attendance_date_time = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return str(self.staff_id)

class Department(models.Model):
    staff_id = models.ForeignKey(NonAcademicStaff, on_delete=models.CASCADE, null=False)
    dept_id = models.PositiveIntegerField(null=False)
    dept_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.dept_name

class Designation(models.Model):
    staff_id = models.ForeignKey(NonAcademicStaff, on_delete=models.CASCADE, null=False)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    job_id = models.PositiveIntegerField(null=False)
    job_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.job_name

class Fingerprint(models.Model):
    staff_id = models.ForeignKey(NonAcademicStaff, on_delete=models.CASCADE, null=False)
    hash = models.CharField(max_length=200, null=False)
    x_cord = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    y_cord = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    angle = models.DecimalField(max_digits=4, decimal_places=2, null=False)

    def save(self, *args, **kwargs):
        if not self.pk:
                self.hash = make_password(self.hash)
        super(Fingerprint, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.staff_id)

class Server(models.Model):
    staff_id = models.ForeignKey(NonAcademicStaff, on_delete=models.CASCADE, null=False)
    report = models.PositiveIntegerField(null=False)

    def __str__(self):
        return str(self.staff_id)
