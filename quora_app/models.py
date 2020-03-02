from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s "% self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=12)
    profile_pic = models.ImageField(upload_to='profile_pics', max_length=100 )
    topics = models.ManyToManyField(Topic)
    def __str__(self):
        return "%s " % self.user.username

class Activity(models.Model):
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )
    activity_type = models.CharField(max_length=6, choices=ACTIVITY_TYPES)
    user = models.ForeignKey(Profile, null=True , on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return "%s "% self.activity_type

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    topic =models.ManyToManyField(Topic)
    description = models.CharField(max_length = 100, null= True ,blank =True)
    vote = GenericRelation(Activity)

    def down_vote_count(self):
        return self.vote.filter(activity_type='D').count()

    def up_vote_count(self):
        return self.vote.filter(activity_type='U').count()

    def __str__(self):
        return "%s " % self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    reply_date = models.DateField(auto_now_add=True)
    vote = GenericRelation(Activity)

    def down_vote_count(self):
        return self.vote.filter(activity_type='D').count()

    def up_vote_count(self):
        return self.vote.filter(activity_type='U').count()

    def __str__(self):
        return "%s" % self.content

class Follow(models.Model):
    following = models.ForeignKey(User, default="",on_delete=models.CASCADE,related_name='following')
    follower = models.ForeignKey(User,  default="",on_delete=models.CASCADE ,related_name='followers')
    class Meta:
        unique_together = ('follower', 'following')

class Comment(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=200)
    answer = models.ForeignKey(Answer ,on_delete=models.CASCADE ,related_name="comments")
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return self.comment