from django.db import models
from django.utils import timezone


##===========================================================================================

class Place(models.Model):
    place_name = models.CharField(max_length=20, verbose_name='نام مکان')
    information = models.TextField(default='توضیحات', verbose_name='توضیحات')
    place_image = models.ImageField(upload_to='images/places/', verbose_name="تصویر")
    visiting_day = models.CharField(max_length=20, verbose_name='روز های بازدید')
    visiting_hour = models.CharField(max_length=20, verbose_name='ساعت های بازدید')
    rules = models.TextField(blank=True, verbose_name='قوانین')
    register_date = models.DateField(default=timezone.now, verbose_name='تاریخ ثبت نام')

    def __str__(self):
        return self.place_name

    class Meta:
        verbose_name = 'مکان '
        verbose_name_plural = 'مکان ها'
        db_table = 't_place'


##===========================================================================================
class VisitorType(models.Model):
    type_name = models.CharField(max_length=20, verbose_name='نوع بازدید کننده')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'نوع بازدید کننده '
        verbose_name_plural = 'نوع بازدید کننده ها'
        db_table = 't_visitor_type'


##===========================================================================================
class TicketPrice(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='مکان مورد نظر')
    visitor = models.ForeignKey(VisitorType, on_delete=models.CASCADE, verbose_name='نوع بازدید کننده')
    price = models.IntegerField(verbose_name='قیمت')

    def __str__(self):
        return f"{self.place} {self.visitor} {self.price}"

    class Meta:
        verbose_name = 'بهای بلیت'
        verbose_name_plural = 'بهای بلیت ها'
        db_table = 't_ticket_prices'


##===========================================================================================
class Message(models.Model):
    full_name = models.CharField(max_length=40, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=80, verbose_name='ایمیل')
    subject = models.CharField(max_length=100, verbose_name='عنوان')
    message = models.TextField(verbose_name='پیام')
    is_seen = models.BooleanField(default=False, verbose_name='وضعیت مشاهده توسط مدیر')
    register_date = models.DateField(default=timezone.now, verbose_name='تاریخ ثبت پیام')

    def __str__(self):
        return self.full_name + ' ' + self.subject

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
        db_table = 't_messages'
