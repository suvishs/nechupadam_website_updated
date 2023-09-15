from django.db import models
from django.utils import timezone

class Treatment(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='myimages/', null=True, blank=True)
    description = models.TextField(blank=True)
    know_more_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    uploaded_date = models.DateTimeField(default=timezone.now, editable=False)
    edited_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url


class Images(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='myimages/', null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=200, blank=True)
    uploaded_date = models.DateTimeField(default=timezone.now, editable=False)
    edited_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url


class Image_category(models.Model):
    category = models.CharField(max_length=200)
    uploaded_date = models.DateTimeField(default=timezone.now, editable=False)
    edited_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.category


class Youtube_category(models.Model):
    category = models.CharField(max_length=200)
    uploaded_date = models.DateTimeField(default=timezone.now, editable=False)
    edited_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.category
    

class Youtube(models.Model):
    title = models.CharField(max_length=200)
    youtube_link = models.URLField(blank=True)
    category = models.CharField(max_length=200)
    uploaded_date = models.DateTimeField(default=timezone.now, editable=False)
    edited_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title
    


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='myimages/', null=True, blank=True)
    author = models.CharField(max_length=200)
    content = models.TextField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url


class Review(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='myimages/')
    review = models.TextField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    

class Booking(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, blank=True) 
    doctor = models.CharField(max_length=200, blank=True)  
    date = models.DateField(blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Medical_report(models.Model):
    name=models.CharField(max_length=100,null=False,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100 ,null=True,blank=True)
    post=models.IntegerField(50,null=True,blank=True)
    phone=models.IntegerField(60,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    document_name=models.FileField(upload_to="upload/",null=True,blank=True)
    image = models.ImageField(upload_to='upload/',null=True,blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    

    

class Staff(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='mystaffs/')
    description = models.TextField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    

class Background_image(models.Model):
    image = models.ImageField(upload_to='mybg/')
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    

class Background_image2(models.Model):
    image = models.ImageField(upload_to='mybg/')
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url

class Background_image3(models.Model):
    image = models.ImageField(upload_to='mybg/')
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    
class History(models.Model):
    year = models.IntegerField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='history_images/', null=True)

    def __str__(self):
        return str(self.year) 

    class Meta:
        ordering = ['year']
        
class DentalSurgeryStep(models.Model):
    step_number = models.IntegerField(null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='surgery_images/', null=True)

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"