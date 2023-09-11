from django.shortcuts import get_object_or_404, redirect, render
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def index(request):
    treatments = Treatment.objects.all()
    staffs = Staff.objects.all()
    bg_image = Background_image.objects.all()
    bg_image2 = Background_image2.objects.all()
    bg_image3 = Background_image3.objects.all()
    reviews = Review.objects.all()
    context = {'treatments':treatments, 'staffs':staffs, 'bg_image':bg_image, 'bg_image2':bg_image2, 'bg_image3':bg_image3, 'reviews':reviews}
    return render(request, 'general/index.html', context)

def nechupadam_history(request):
    return render(request, 'general/nechupadam_history.html')

def nechupadam_process(request):
    return render(request, 'general/nechupadam_process.html')

def team(request):
    staffs = Staff.objects.all()
    context = {'staffs':staffs}
    return render(request, 'general/team.html', context)

def doctor_profile(request):
    return render(request, 'general/doctor_profile.html')

def testimonials(request):
    reviews = Review.objects.all()
    context = {'reviews':reviews}
    return render(request, 'general/testimonials.html', context)

def nechupadam_contact(request):
    return render(request, 'general/nechupadam_contact.html')

def nechupadam_location(request):
    return render(request, 'general/nechupadam_location.html')


def general_info(request):
    treatments = Treatment.objects.all()
    context = {'treatments':treatments}
    return render(request, 'general/general_info.html', context)

def nechupadam_images(request):
    categories = Image_category.objects.all()
    images = Images.objects.all()
    context = {'images':images, 'categories':categories}
    return render(request, 'general/nechupadam_images.html', context)


def nechupadam_treatments(request):
    treatments = Treatment.objects.all()
    context = {'treatments':treatments}
    return render(request, 'general/nechupadam_treatments.html', context)


def more_about_treatment(request, pk):
    get_treatment = get_object_or_404(Treatment, pk=pk)
    if request.method == "POST":
        return
    else:
        context = {
            'get_treatment':get_treatment,
        }
    return render(request, 'general/more_about_treatment.html', context)



def nechupadam_youtube(request):
    categories = Youtube_category.objects.all()
    youtube = Youtube.objects.all()
    context = {'categories':categories, 'youtube':youtube}
    return render(request, 'general/nechupadam_youtube.html', context)


def nechupadam_articles(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'general/nechupadam_articles.html', context)


def more_about_article(request, pk):
    get_article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        return
    else:
        context = {
            'get_article':get_article,
        }
    return render(request, 'general/more_about_article.html', context)


def booking(request):
    a = request.POST.get("name")
    c = request.POST.get("phone")
    d = request.POST.get("doctor")
    e = request.POST.get("date")
    booking = Booking.objects.create(name=a, phone=c, doctor=d, date=e)
    return render(request, 'general/bookingsuccess.html')
        

# from django.shortcuts import render,redirect
# from .models import *
# from django.conf import settings
# from django.core.mail import EmailMessage
# # from django.core.mail.backends import EmailMessage



# # Create your views here.
# def medical_report(request):
#     if request.method == "POST":
#         name=request.POST.get('name')
#         address=request.POST.get('address')
#         city=request.POST.get('city')
#         code=request.POST.get('code')
#         phone=request.POST.get('phone')
#         email=request.POST.get('email')
#         file = request.FILES.get('orufile')

#         obj =Medical_report(name=name, address=address,city=city,post=code,phone=phone,email=email,document_name=file)
#         obj.save()
#         # if file is not None:
#         message = 'Patient Name: {}\nAddress: {}\nCity: {}\nPincode: {}\nPhone Number: {}\nEmail: {}\n '.format(name,address,city,code,phone,email)
#         email = EmailMessage(
#             "Medical Report From Patient",
#             message,
#             settings.EMAIL_HOST_USER,
#             ['nihalonline24@gmail.com']
            
#         )
#         email.attach(
#             file.name,
#             file.read(),
#             file.content_type
                
#         )
#         email.send()
#     return render(request,'general/report_success.html')

        
   
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from django.shortcuts import render, redirect
from .models import Medical_report
from django.conf import settings
from django.core.mail import EmailMessage

# Define a function to generate a temporary file path
def get_temp_file_path(filename):
    temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
    os.makedirs(temp_dir, exist_ok=True)  # Create the 'temp' directory if it doesn't exist
    return os.path.join(temp_dir, filename)

def send_email(subject, body, send_to_email, pdf_file_path=None):
    try:
        email = 'retrohubmusic@gmail.com'
        password = 'howktwkhtnmmokgq'

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if pdf_file_path:
            with open(pdf_file_path, 'rb') as pdf_file:
                pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
                pdf_attachment.add_header('Content-Disposition', f'attachment; filename=report.pdf')
                msg.attach(pdf_attachment)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

def medical_report(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        code = request.POST.get('code')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        file = request.FILES.get('orufile')

        obj = Medical_report(name=name, address=address, city=city, post=code, phone=phone, email=email, document_name=file)
        obj.save()

        # Check if a file was uploaded
        if file is not None:
            message = f'Patient Name: {name}\nAddress: {address}\nCity: {city}\nPincode: {code}\nPhone Number: {phone}\nEmail: {email}\n'

            # Generate a temporary file path for the PDF file
            pdf_file_path = get_temp_file_path('report.pdf')

            # Save the uploaded PDF file to the temporary location
            with open(pdf_file_path, 'wb') as pdf_file:
                for chunk in file.chunks():
                    pdf_file.write(chunk)

            # Send the email using the send_email function and attach the PDF file
            send_email("Medical Report From Patient", message, 'nihalonline24@gmail.com', pdf_file_path)

    return render(request, 'general/report_success.html')

################################################################################################################################
#Admin_Interface


def nechulogin(request):
    return render(request, 'nechuadmin/nechulogin.html')

def nechuadminhome(request):
    return render(request, 'nechuadmin/nechuadminhome.html')


def imagecategory(request):
    category = Image_category.objects.all()
    context = {'categories':category}
    return render(request, 'nechuadmin/imagecategory.html', context)

def youtubecategory(request):
    category = Youtube_category.objects.all()
    context = {'categories':category}
    return render(request, 'nechuadmin/youtubecategory.html', context)

def articles(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'nechuadmin/articles.html', context)

def staffs(request):
    staffs = Staff.objects.all()
    context = {'staffs':staffs}
    return render(request, 'nechuadmin/staffs.html', context)

def bg(request):
    bg = Background_image.objects.all()
    bg2 = Background_image2.objects.all()
    bg3 = Background_image3.objects.all()
    context = {'bg':bg, 'bg2':bg2, 'bg3':bg3}
    return render(request, 'nechuadmin/bg.html', context)

def treatments(request):
    treatments = Treatment.objects.all()
    context = {'treatments':treatments}
    return render(request, 'nechuadmin/treatments.html', context)

def images(request):
    categories = Image_category.objects.all()
    images = Images.objects.all()
    context = {'images':images, 'categories':categories}
    return render(request, 'nechuadmin/images.html', context)

def youtube(request):
    categories = Youtube_category.objects.all()
    youtube = Youtube.objects.all()
    context = {'categories':categories, 'youtube':youtube}
    return render(request, 'nechuadmin/youtube.html', context)

def bookings(request):
    bookings = Booking.objects.all().order_by('-submitted_on')
    context = {'booking':bookings}
    return render(request, 'nechuadmin/bookings.html', context)

def medicalreports(request):
    reports = Medical_report.objects.all().order_by('-submitted_on')
    context = {'reports':reports}
    return render(request, 'nechuadmin/medicalreports.html', context)

def reviews(request):
    reviews = Review.objects.all()
    context = {'reviews':reviews}
    return render(request, 'nechuadmin/reviews.html', context)

def singlearticle(request, pk):
    get_article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        return
    else:
        context = {
            'get_article':get_article,
        }
    return render(request, 'nechuadmin/singlearticle.html', context)

def singletreatment(request, pk):
    get_treatment = get_object_or_404(Treatment, pk=pk)
    if request.method == "POST":
        return
    else:
        context = {
            'get_treatment':get_treatment,
        }
    return render(request, 'nechuadmin/singletreatment.html', context)



def addTreatment(request):
    a = request.POST.get("title")
    b = request.FILES["image"]
    c = request.POST.get("description")
    d = request.POST.get("know_more")
    e = request.POST.get("youtube")
    treatments = Treatment.objects.create(title=a, image=b, description=c, know_more_link=d, youtube_link=e)
    return redirect('treatments')

def add_image(request):
    a = request.POST.get("title")
    b = request.FILES["image"]
    c = request.POST.get("description")
    d = request.POST.get("category")
    images = Images.objects.create(title=a, image=b, description=c, category=d)
    return redirect('images')

def add_youtube_category(request):
    a = request.POST.get("category")
    categories = Youtube_category.objects.create(category=a)
    return redirect('youtube')

def add_image_category(request):
    a = request.POST.get("category")
    categories = Image_category.objects.create(category=a)
    return redirect('images')


def add_youtube(request):
    a = request.POST.get("title")
    b = request.POST.get("youtube")
    c = request.POST.get("category")
    youtube = Youtube.objects.create(title=a, youtube_link=b, category=c)
    return redirect('youtube')

def add_article(request):
    a = request.POST.get("title")
    b = request.FILES["image"]
    c = request.POST.get("content")
    d = request.POST.get("author")
    artcles = Article.objects.create(title=a, image=b, content=c, author=d)
    return redirect('articles')

def add_review(request):
    a = request.POST.get("name")
    b = request.FILES["image"]
    c = request.POST.get("review")
    review = Review.objects.create(name=a, image=b, review=c)
    return redirect('reviews')

def addStaff(request):
    a = request.POST.get("name")
    b = request.FILES["image"]
    c = request.POST.get("description")
    d = request.POST.get('position')
    staffs = Staff.objects.create(name=a, image=b, description=c, position=d)
    return redirect('staffs')

def add_bg(request):
    a = request.POST.get("title1")
    b = request.FILES["image"]
    c = request.POST.get("title2")
    bg = Background_image.objects.create(title1=a, image=b, title2=c)
    return redirect('bg')

def add_bg2(request):
    a = request.POST.get("title1")
    b = request.FILES["image"]
    c = request.POST.get("title2")
    bg = Background_image2.objects.create(title1=a, image=b, title2=c)
    return redirect('bg')

def add_bg3(request):
    a = request.POST.get("title1")
    b = request.FILES["image"]
    c = request.POST.get("title2")
    bg = Background_image3.objects.create(title1=a, image=b, title2=c)
    return redirect('bg')

def edittreatment(request, pk):
    get_treatment = get_object_or_404(Treatment, pk=pk)
    if request.method == "POST":
        new_title = request.POST['title']
        new_description = request.POST['description']
        new_link = request.POST['know_more']
        new_youtube_link = request.POST['youtube']

        # Check if a new image was provided
        new_image = request.FILES.get('image')
        if new_image:
            get_treatment.image = new_image

        get_treatment.title = new_title
        get_treatment.description = new_description
        get_treatment.know_more_link = new_link
        get_treatment.youtube_link = new_youtube_link
        get_treatment.save()
        return redirect('treatments')
    else:
        context = {
            'get_treatment': get_treatment,
        }
        return render(request, 'nechuadmin/edittreatment.html', context)

def edit_image(request, pk):
    get_image = get_object_or_404(Images, pk=pk)
    if request.method == "POST":
        new_title = request.POST['title']
        new_description = request.POST['description']
        new_category = request.POST['category']

        # Check if a new image was provided
        new_image = request.FILES.get('image')
        if new_image:
            get_image.image = new_image

        get_image.title = new_title
        get_image.description = new_description
        get_image.category = new_category
        get_image.save()
        return redirect('images')
    else:
        context = {
            'get_image': get_image,
        }
        return render(request, 'nechuadmin/edit_image.html', context)

def edit_imagecategory(request, pk):
    get_category = get_object_or_404(Image_category, pk=pk)
    if request.method == "POST":
        new_category = request.POST['task']
        get_category.category = new_category
        get_category.save()
        return redirect('imagecategory')
    else:
        context = {
            'get_category':get_category,
        }
        return render(request, 'nechuadmin/edit_imagecategory.html', context)


def edit_youtubecategory(request, pk):
    get_category = get_object_or_404(Youtube_category, pk=pk)
    if request.method == "POST":
        new_category = request.POST['task']
        get_category.category = new_category
        get_category.save()
        return redirect('youtubecategory')
    else:
        context = {
            'get_category':get_category,
        }
        return render(request, 'nechuadmin/edit_youtubecategory.html', context)



def edit_article(request, pk):
    get_article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        new_title = request.POST['title']
        new_content = request.POST['content']
        new_author = request.POST['author']

        # Check if a new image was provided
        new_image = request.FILES.get('image')
        if new_image:
            get_article.image = new_image

        get_article.title = new_title
        get_article.content = new_content
        get_article.author = new_author
        get_article.save()
        return redirect('articles')
    else:
        context = {
            'get_article': get_article,
        }
        return render(request, 'nechuadmin/edit_article.html', context)



def edit_review(request, pk):
    get_treatment = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        new_title = request.POST['name']
        new_description = request.POST['review']

        # Check if a new image was provided
        new_image = request.FILES.get('image')
        if new_image:
            get_treatment.image = new_image

        get_treatment.name = new_title
        get_treatment.review = new_description
        get_treatment.save()
        return redirect('reviews')
    else:
        context = {
            'get_treatment': get_treatment,
        }
        return render(request, 'nechuadmin/edit_review.html', context)


def edit_staff(request, pk):
    get_staff = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        new_name = request.POST['name']
        new_position = request.POST['position']
        new_description = request.POST['description']

        # Check if a new image was provided
        new_image = request.FILES.get('image')
        if new_image:
            get_staff.image = new_image

        get_staff.name = new_name
        get_staff.position = new_position
        get_staff.description = new_description
        get_staff.save()
        return redirect('staffs')
    else:
        context = {
            'get_staff': get_staff,
        }
        return render(request, 'nechuadmin/edit_staff.html', context)


def edit_bg(request, pk):
    get_bg = get_object_or_404(Background_image, pk=pk)
    if request.method == "POST":
        new_title1 = request.POST['title1']
        new_title2 = request.POST['title2']

        # Check if a new image was provided
        new_image = request.FILES.get('image')
        if new_image:
            get_bg.image = new_image

        get_bg.title1 = new_title1
        get_bg.title2 = new_title2
        get_bg.save()
        return redirect('bg')
    else:
        context = {
            'get_bg': get_bg,
        }
        return render(request, 'nechuadmin/edit_bg.html', context)


def edit_bg2(request, pk):
    get_bg = get_object_or_404(Background_image2, pk=pk)
    if request.method == "POST":
        new_title1 = request.POST['title1']
        new_title2 = request.POST['title2']

        # Check if a new image was provided
        new_image = request.FILES.get('image')
        if new_image:
            get_bg.image = new_image

        get_bg.title1 = new_title1
        get_bg.title2 = new_title2
        get_bg.save()
        return redirect('bg')
    else:
        context = {
            'get_bg': get_bg,
        }
        return render(request, 'nechuadmin/edit_bg2.html', context)


def edit_bg3(request, pk):
    get_bg = get_object_or_404(Background_image3, pk=pk)
    if request.method == "POST":
        new_title1 = request.POST['title1']
        new_title2 = request.POST['title2']

        # Check if a new image was provided
        new_image = request.FILES.get('image')
        if new_image:
            get_bg.image = new_image

        get_bg.title1 = new_title1
        get_bg.title2 = new_title2
        get_bg.save()
        return redirect('bg')
    else:
        context = {
            'get_bg': get_bg,
        }
        return render(request, 'nechuadmin/edit_bg3.html', context)

def delete_treatment(request, pk):
    treatment = get_object_or_404(Treatment, pk=pk)
    treatment.delete()
    return redirect('treatments')


def delete_image(request, pk):
    images = get_object_or_404(Images, pk=pk)
    images.delete()
    return redirect('images')  


def delete_imagecategory(request, pk):
    category = get_object_or_404(Image_category, pk=pk)
    category.delete()
    return redirect('imagecategory')

def delete_youtubecategory(request, pk):
    category = get_object_or_404(Youtube_category, pk=pk)
    category.delete()
    return redirect('youtubecategory')

def delete_article(request, pk):
    articles = get_object_or_404(Article, pk=pk)
    articles.delete()
    return redirect('articles')  


def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('reviews')  

def delete_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    staff.delete()
    return redirect('staffs')


def delete_bg(request, pk):
    bg = get_object_or_404(Background_image, pk=pk)
    bg.delete()
    return redirect('bg')

# def nechulogin(request):
#     return render(request, 'nechuadmin/nechulogin.html')

def nechulogin(request):
     if request.method == "POST":
          username = request.POST['uname']
          password = request.POST['pswd']
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request,user)
               return redirect("nechuadminhome")
          else:
               messages.info(request,'Username or password incorrect')
               return redirect('nechulogin')


     return render(request,'nechuadmin/nechulogin.html')


def SignOut(request):
     logout(request)
     return redirect('nechulogin')

######################################################################################################################################




