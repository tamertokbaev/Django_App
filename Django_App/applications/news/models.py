from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


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
    news_content = models.TextField('Content of the news')
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
