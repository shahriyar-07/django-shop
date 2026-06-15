from django.db import models


# Create your models here.


class SiteSettings(models.Model):
    site_name = models.CharField(verbose_name='نام سایت', max_length=200)
    site_url = models.CharField(verbose_name='دامنه سایت', max_length=200)
    address = models.CharField(verbose_name='آدرس سایت', max_length=200)
    phone = models.CharField(verbose_name='تلفن', blank=True, null=True, max_length=200)
    fax = models.CharField(verbose_name='فکس', blank=True, null=True, max_length=200)
    email = models.CharField(verbose_name='ایمیل', blank=True, null=True, max_length=200)
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(verbose_name='لوگوی سایت', upload_to='images/site-settings/')
    is_main_settings = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=200)

    class Meta:
        verbose_name = 'دسته بندی لینک فوتر'
        verbose_name_plural = 'دسته بندی های لینک فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=200)
    url = models.CharField()
    footer_link_box = models.ForeignKey(FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=200, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        product_list = 'product_list', 'صفحه لیست محصولات'
        product_detail = 'product_detail' ,'صفحه جزئیات محصولات'
        about_us = 'about_us' , 'صفحه درباره ما'


    title = models.CharField(max_length=200 , verbose_name='عنوان بنر')
    url = models.URLField(max_length=400 ,blank=True , null = True, verbose_name='آدرس بنر')
    image = models.ImageField(upload_to='images/banner' , verbose_name='تصویر بنر')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    position = models.CharField(max_length=200 ,choices=SiteBannerPositions.choices , verbose_name='جایگاه نمایشی')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'بنر تبلیفاتی'
        verbose_name_plural = 'بنر تبلیفاتی های تبلیغاتی'