from django.db import models
from django.utils import timezone


# ==============================================================================================================
class Author(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام')
    family = models.CharField(max_length=20, verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=200, verbose_name='ایمیل', null=True, blank=True)
    mobile = models.CharField(max_length=12, verbose_name='شماره موبایل', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='وضعیت')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name + " " + self.family

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'
        db_table = "t-authors"


# ==============================================================================================================
class ArticleGroup(models.Model):
    group_title = models.CharField(max_length=100, verbose_name='عنوان گروه مقالات')

    def __str__(self):
        return self.group_title

    class Meta:
        verbose_name = 'گروه مقالات'
        verbose_name_plural = 'گروه های مقالات'
        db_table = "t-article_groups"


# ==============================================================================================================
class Article(models.Model):
    group = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE, verbose_name='گروه مقاله')
    author = models.ManyToManyField(Author, verbose_name='نویسنده')
    title = models.CharField(max_length=30, verbose_name='عنوان مقاله')
    image = models.ImageField(upload_to="images/articles/", verbose_name='تصویر اصلی مقاله')
    short_text = models.TextField(verbose_name='متن خلاصه مقاله')
    text = models.TextField(default='متن مقاله', verbose_name='متن مقاله')
    key_words = models.CharField(max_length=200, verbose_name='کلمات کلیدی')
    register_date = models.DateField(auto_now_add=True, verbose_name='تاریخ درج مقاله')
    publish_date = models.DateField(default=timezone.now, verbose_name='تاریخ انتشار')
    updated_date = models.DateField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')
    is_active = models.BooleanField(default=False, verbose_name='وضعیت')
    view_number = models.PositiveSmallIntegerField(verbose_name='تعداد بازدید')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        db_table = "t-articles"


# ==============================================================================================================
def get_member_upload_to(instance, filename):
    return f"images/articles/article-{instance.article.id}/{filename}"


class ArticleGallery(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    image = models.ImageField(upload_to=get_member_upload_to, verbose_name='تصویر', )

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'
        db_table = "t-articles_gallery"
