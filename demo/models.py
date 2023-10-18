from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify 



def webp(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename

class FAQDetail(models.Model):
    title       = models.CharField(max_length=150)
    description = models.TextField()

class ShopByCategory(models.Model):
    title       = models.CharField(max_length=150)
    description = models.TextField()

class QualityMatters(models.Model):
    CHOICETYPE      = (('HomePage','HomePage'),('About','About'))
    quality_choice  = models.CharField(max_length=50,choices=CHOICETYPE)
    title           = models.CharField(max_length=150)
    description     = models.TextField()
    image           = models.ImageField(upload_to=webp,blank=True)
    image1          = models.ImageField(upload_to=webp,blank=True)

class QualityMattersCards(models.Model):
    title       = models.CharField(max_length=150)
    image       = models.ImageField(upload_to=webp)
    description = models.TextField()

class OneStopShop(models.Model):
    title       = models.CharField(max_length=150)
    image       = models.ImageField(upload_to=webp)
    description = models.TextField()

class Testmonials(models.Model):
    name        = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    description = models.TextField()
    image       = models.ImageField(upload_to=webp)

class FAQCategory(models.Model):
    title = models.CharField(max_length=150)
    slug  = models.SlugField(unique=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(FAQCategory, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class FAQ(models.Model):
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, related_name='category')
    question = models.CharField(max_length=150)
    answer   = models.TextField()

class Contacts(models.Model):
    title       = models.CharField(max_length=150)
    description = models.TextField()
    address     = models.CharField(max_length=150)
    google_map  = models.URLField(max_length=300)
    email       = models.EmailField(max_length=254)
    email1      = models.EmailField(max_length=254, blank=True)
    mobile      = models.CharField(max_length=15)
    facebook    = models.URLField(max_length=200,blank=True)
    instagram   = models.URLField(max_length=200,blank=True)
    twitter     =  models.URLField(max_length=200,blank=True)

class Banner(models.Model):
    TYPESOFBANNER = (('Home','Home'),('Blog','Blog'),('About','About'),('Catalogs','Catalogs'),('GetInTouch','GetInTouch'),('FAQ','FAQ'))
    banner_type = models.CharField(max_length=150,choices=TYPESOFBANNER)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to=webp)

class WhyChoiceUs(models.Model):
    description = models.TextField()
    video       = models.FileField(upload_to='media')

class SolutionAllLighting(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to=webp)

class OurAchievements(models.Model):
    happy_clients       = models.CharField(max_length=20)
    project_completed   = models.CharField(max_length=20)
    phone_support       = models.CharField(max_length=20)
    hard_workers        = models.CharField(max_length=20)

class OurTeams(models.Model):
    name        = models.CharField(max_length=150)
    designation = models.CharField(max_length=50)
    image       = models.ImageField(upload_to=webp)
    linkedin    = models.URLField(max_length=200,blank=True)
    instagram   = models.URLField(max_length=200,blank=True)
    twitter     =  models.URLField(max_length=200,blank=True)

class BlogTag(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    

class Blog(models.Model):
    title            = models.CharField(max_length=150)
    description      = RichTextField()
    tags             = models.ManyToManyField(BlogTag, related_name='tags')
    is_popular_post  = models.BooleanField(default=False)
    is_trending_post = models.BooleanField(default=False)
    slug             = models.SlugField(unique=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

class TermsAndConditions(models.Model):
    title            = models.CharField(max_length=150)
    description      = RichTextField()
    slug             = models.SlugField(unique=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TermsAndConditions, self).save(*args, **kwargs)