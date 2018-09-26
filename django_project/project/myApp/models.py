from django.db import models


# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s-%d-%d" % (self.gname, self.ggirlnum, self.gboynum)


class childrenManager(models.Manager):
    def get_queryset(self):
        return super(childrenManager, self).get_queryset().filter(isDeleted=False)

    def createChild(self, name, gender, age, summary, grade):
        child = self.model()
        # print(type(grade))
        child.pname = name
        child.sgender = gender
        child.sage = age
        child.ssummary = summary
        child.sgrade = grade
        return child


class Children(models.Model):
    # childObj = models.Manager()  # we can custom manage object
    childObj = childrenManager()
    pname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    ssummary = models.CharField(max_length=20)
    isDeleted = models.BooleanField(default=False)
    sgrade = models.ForeignKey(Grades, on_delete=models.CASCADE)

    def __str__(self):
        return self.pname

    # class Meta:
    #     db_table = "students"  # define data table name
    #     ordering = ['id']  # ASC order to fetch object list,desc used ['-id']
