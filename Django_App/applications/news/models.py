from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True, default=timezone.now,
                                  verbose_name=_('Birthday Date'))
    avatar = models.ImageField(upload_to='images/avatars/', null=True,
                               default='images/avatars/defavatar.jpg', verbose_name=_('Avatar'))

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

    news_author = models.ForeignKey(User, on_delete=models.CASCADE, default=True, verbose_name=_('Author of the news'))
    news_title = models.CharField(verbose_name=_('Title of the news'), max_length=200)
    news_sh_description = models.CharField(verbose_name=_('Short description of the news'),
                                           max_length=800)
    news_content = RichTextUploadingField()
    news_tag = models.CharField(max_length=100, choices=TAG_TYPES, default=ANOTHER)
    publication_date = models.DateTimeField(verbose_name=_('Date of publication of the news'))
    count_of_views = models.IntegerField(verbose_name=_('Count of views'))
    img = models.ImageField(upload_to='images/', verbose_name=_('Title photo'))
    likes = models.IntegerField(default=0, verbose_name=_('Count of likes'))

    def __str__(self):
        return self.news_title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news:one_by_one', args=[str(self.id)])


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_('News'))
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author of the news'))
    comment_text = models.TextField(verbose_name=_('Text of the comment'))
    comment_date = models.DateTimeField(verbose_name=_('Date of publication of the comment'), default=timezone.now)

    def __str__(self):
        return self.comment_author.username + ' ' + str(self.news.id) + ' ' + str(self.comment_date)


class UserFavourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_ID')
    fav_news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='Fav_news_ID')


class UserLiked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_ID_Liked')
    liked_post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='Liked_post_ID')
