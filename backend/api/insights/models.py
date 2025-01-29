from django.db import models

# insights/models.py

from django.db import models

class Insight(models.Model):
    end_year = models.CharField(max_length=4, blank=True)
    intensity = models.IntegerField(default=0)
    sector = models.CharField(max_length=100, blank=True)
    topic = models.CharField(max_length=100, blank=True)
    insight = models.TextField()
    url = models.URLField(max_length=500,blank=True)
    region = models.CharField(max_length=100,blank=True)
    start_year = models.CharField(max_length=4, blank=True)
    impact = models.TextField(max_length=500,blank=True)
    added = models.DateTimeField()
    published = models.DateTimeField(null=True,blank=True)
    country = models.CharField(max_length=100, blank=True)
    relevance = models.IntegerField(default=0)
    pestle = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=500, blank=True)
    title = models.TextField()
    likelihood = models.IntegerField(default=0)

    def __str__(self):
        return self.title

