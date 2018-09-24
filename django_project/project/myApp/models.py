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


class Children(models.Model):
    pname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    ssummary = models.CharField(max_length=20)
    isDeleted = models.BooleanField(default=False)
    sgrade = models.ForeignKey(Grades, on_delete=models.CASCADE)
