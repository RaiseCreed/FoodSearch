from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(blank=False,null=False,max_length=200)
    image = models.ImageField(blank=True,null=True,upload_to="recipes/",default="recipes/default-profile.jpg")
    email = models.EmailField(blank=False,null=False,max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)

    def __str__(self) -> str:
        return str(self.username)


class Recipe(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    owner = models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True,null=True,related_name='recipes')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(blank=False,null=False,max_length=200)
    image = models.ImageField(blank=True,null=True,upload_to="recipes/",default="recipes/default-recipe.jpg")
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0,null=True,blank=True)
    intro = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    tags = models.ManyToManyField('Tag',blank=True)

    def __str__(self) -> str:
        return str(self.name)
    
    @property
    def reviewers(self):
        querySet = self.review_set.all().values_list('owner__id',flat=True)
        return querySet
    
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes/totalVotes) * 100 

        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()
        
    class Meta:
        ordering = ['vote_ratio','vote_total']


class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE,blank=False,null=False,default='')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    class Meta:
        unique_together = [['owner','recipe']]
        
    def __str__(self) -> str:
        return self.value
    
class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.name
    