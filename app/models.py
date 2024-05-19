from django.db import models

# Create your models here.


class Candidate(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    summary = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    def __str__(self):
        return self.name
    
class Language(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    level = models.CharField(max_length=2)
    def __str__(self):
        return self.name

class SoftSkills(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name


class SocialNetworks(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    link = models.TextField()
    def __str__(self):
        return self.name


class Experience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    years = models.CharField(max_length=300)
    company_name  = models.CharField(max_length=300)
    position  = models.CharField(max_length=300)
    describtion = models.TextField()
    def __str__(self):
        return self.years



class Studies(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    years = models.CharField(max_length=300, null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name











