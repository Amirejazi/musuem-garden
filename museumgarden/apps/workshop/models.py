from django.db import models


# ================================================================================
class WorkShopStatus(models.Model):
    status_code = models.IntegerField(primary_key=True, verbose_name='کد وضعیت')
    status_title = models.CharField(max_length=100, verbose_name='عنوان وضعیت')

    def __str__(self):
        return self.status_title

    class Meta:
        verbose_name = 'وضعیت کارگاه'
        verbose_name_plural = 'وضعیت کارگاه ها'
        db_table = 't_workshop_status'


def upload_workShop_images(instance, filename):
    return f"images/workshops/{filename}"


# ================================================================================
class WorkShop(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image_name = models.ImageField(upload_to=upload_workShop_images, verbose_name='عکس اصلی')
    date_time = models.DateTimeField(verbose_name='تاریخ و زمان برگزاری')
    place = models.CharField(max_length=150, verbose_name='مکان برگزاری')
    teacher = models.CharField(max_length=150, verbose_name='مدرس')
    information = models.TextField(verbose_name='اطلاعات')
    report_text = models.TextField( verbose_name='متن گزارش', blank=True, null=True)
    viewNumber = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    register_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')
    status = models.ForeignKey(WorkShopStatus, on_delete=models.CASCADE, verbose_name='وضعیت کارگاه')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کارگاه'
        verbose_name_plural = 'کارگاه ها'
        db_table = 't_workshop'


#================================================================================
def upload_workShop_gallery(instance,filename):
    return f"images/workshops/gallery/{instance.WorkShop.id}/{filename}"


class WorkShop_gallery(models.Model):
    workshop = models.ForeignKey(WorkShop, on_delete=models.CASCADE, verbose_name='کارگاه')
    image = models.ImageField(upload_to= upload_workShop_gallery, verbose_name='تصویر')

    def __str__(self):
        return self.workshop
    class Meta:
        verbose_name = 'گالری کارگاه'
        verbose_name_plural = 'گالری کارگاه ها'
        db_table = 't_workshop_gallery'