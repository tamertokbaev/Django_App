from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    avatar = models.ImageField(upload_to='images/avatars/', null=True, default='images/avatars/defavatar.jpg')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class News(models.Model):
    # Defines which tag is used to a particular news. For example, for the news about KPL will be used KPL tag.
    KPL = 'Казахстанская-премьер лига'  # Kazakhstan premier league
    NAT_TEAM = 'Национальная сборная по футболу'  # National team of Kazakhstan
    UCL = 'Лига чемпионов УЕФА'  # UEFA Champions League
    UEL = 'Лига Европы УЕФА'  # UEFA Europe League
    ANOTHER = 'Другое'  # Another

    TAG_TYPES = [
        (ANOTHER, 'Другое'),
        (KPL, 'Казахстанская-премьер лига'),
        (NAT_TEAM, 'Национальная сборная по футболу'),
        (UCL, 'Лига чемпионов УЕФА'),
        (UEL, 'Лига Европы УЕФА'),
    ]

    news_title = models.CharField('Title of the news', max_length=200)
    news_sh_description = models.CharField('Short description of the news', max_length=800)
    news_content = RichTextUploadingField()
    news_tag = models.CharField(max_length=100, choices=TAG_TYPES, default=ANOTHER)
    publication_date = models.DateTimeField('Date of publication of the news')
    count_of_views = models.IntegerField('Count of views of the news')
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.news_title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField('Content of comment')
    comment_date = models.DateTimeField('Date of publication of the comment', default=timezone.now)

    def __str__(self):
        return self.comment_author.username + ' ' + str(self.news.id) + ' ' + str(self.comment_date)


class UserFavourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_ID')
    fav_news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='Fav_news_ID')
