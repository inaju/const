from django.db import models

# Create your models here.
DISPLAY = [
('Done', 'Done'),
("Didn't do", "Didn't do"),
]


class GoalsList(models.Model):
    Goal=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Goal

class GoalModel(models.Model):
    Date=models.DateField(auto_now=False)
    Goals=models.ForeignKey(GoalsList, on_delete=models.CASCADE)
    Check=models.CharField( max_length=50, choices=DISPLAY, default='some')
    

    def __str__(self):
        return  str(self.Goals)

class DateModel(models.Model):
    Date=models.ForeignKey(GoalsList,on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.Goals)




class Check(models.Model):
    Check=models.CharField( max_length=50, choices=DISPLAY, default='some')

    def __str__(self):
        return  str(self.Check)

class Date(models.Model):
    Date=models.DateField(auto_now=False)
    Check=models.ForeignKey(Check, on_delete=models.CASCADE)


    def __str__(self):
        return  str(self.Date)


class Goals(models.Model):
    Goal=models.CharField(max_length=50)
    Date=models.ForeignKey(Date, on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.Goal)


class JoinModel(models.Model):
    GoalList=models.ForeignKey(Goals, on_delete=models.CASCADE)

