from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Memory(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان خاطره')
    text = models.TextField(verbose_name='متن خاطره')
    register_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=False, verbose_name='وضعیت')
    user_registered = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر ثبت کننده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خاطره'
        verbose_name_plural = 'خاطرات'
        db_table = 't_memories'

# ============================================================================================================
def uploade_gallery(instance, filename):
    return f"images/memory/gallery_{instance.memory.id}/{filename}"

class Memory_Gallery(models.Model):
    image_name = models.ImageField(upload_to=uploade_gallery, verbose_name='تصویر')
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, related_name='images')
# =============================================================================================================
class LikeMemory(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, null=True)
    user_liked = models.ForeignKey(User, on_delete=models.CASCADE, null=True)