from django.db import models

class Computer(models.Model):
    name=models.TextField()
    existingApps=models.TextField()
    runningApp=models.TextField()
    lastUpdated=models.DateTimeField(auto_now=True)
    action=models.TextField()

    def __str__(self):
        return "%s -- last updated on %s" %(self.name, self.lastUpdated)
    
    def listApps(self):
        return self.existingApps.split(",")
