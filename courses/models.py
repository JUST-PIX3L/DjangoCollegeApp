#from uuid import _FieldsType
from django.db import models


# Model for Course Info table
class Course(models.Model):

    # Course Info Database Design
    cou_name = models.CharField(unique=True, primary_key=True, max_length=60)  # This will become primary key and foreign key in other tables
    cou_building = models.CharField(max_length=60)
    cou_room = models.CharField(max_length=60)

    # Set Varaibles to be used in multi choice field DeviceStatus
    YEAR1 = '1 Year'
    YEAR2 = '2 Years'
    YEAR3 = '3 Years'
    YEAR4 = '4 Years'
    TERM_LENGTH = [
        (YEAR1, '1 Year'),
        (YEAR2, '2 Years'),
        (YEAR3, '3 Years'),
        (YEAR4, '4 Years'),
        ]
    cou_term = models.CharField(choices=TERM_LENGTH,default=YEAR2,max_length=10)

    # Setup admin verbose names, more friendly to read
    class Meta:
        verbose_name = ("Course")

    # When querying object in Course table set it to use Course Name
    def __str__(self):
        return str(self.cou_name)



# Model for Student Info table
class Student(models.Model):

    # Student Info Database Design
    stu_name = models.CharField(unique=True, primary_key=True, max_length=60)  # This will become primary key and foreign key in other tables
    stu_dob = models.DateField(max_length=60)
    stu_email = models.CharField(max_length=60)
    stu_phone = models.CharField(max_length=60)
    stu_address = models.CharField(max_length=60)
    stu_city = models.CharField(max_length=60)
    stu_postcode = models.CharField(max_length=60)
    stu_course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='cou_name', max_length=60)

    YEAR1 = '1st Year'
    YEAR2 = '2nd Year'
    YEAR3 = '3rd Year'
    YEAR4 = '4th Year'
    TERM_ENROLL = [
        (YEAR1, '1st Year'),
        (YEAR2, '2nd Year'),
        (YEAR3, '3rd Year'),
        (YEAR4, '4th Year'),
        ]
    stu_term = models.CharField(choices=TERM_ENROLL,default=YEAR2,max_length=10)

    # Setup admin verbose names, more friendly to read
    class Meta:
        verbose_name = ("Student")

    # When querying object in Student table set it to use Student Name
    def __str__(self):
        return str(self.stu_name)



# Model for Lecturer Info table
class Lecturer(models.Model):

    # Lecturer Info Database Design
    lec_name = models.CharField(unique=True, primary_key=True, max_length=60)  # This will become primary key and foreign key in other tables
    lec_dob = models.DateField(max_length=60)
    lec_email = models.CharField(max_length=60)
    lec_phone = models.CharField(max_length=60)
    lec_address = models.CharField(max_length=60)
    lec_city = models.CharField(max_length=60)
    lec_postcode = models.CharField(max_length=60)
    lec_course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='cou_name', max_length=60)

    # Setup admin verbose names, more friendly to read
    class Meta:
        verbose_name = ("Lecturer")

    # When querying object in Lecturer table set it to use Lecturer Name
    def __str__(self):
        return str(self.lec_name)






