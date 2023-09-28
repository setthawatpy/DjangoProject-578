from django.shortcuts import render, redirect
from django.contrib import messages
from app_profile.models import *
from app_profile.forms import *

# Create your views here.


def home(request):
    return render(request, "general/home.html")


def profile(request):
    return render(request, "general/profile.html")


def educational(request):
    return render(request, "general/educational.html")


def interestingThings(request):
    return render(request, "general/interestingThings.html")


def dreamCareer(request):
    return render(request, "general/dreamCareer.html")


def modelPerson(request):
    return render(request, "general/modelPerson.html")


def lab10(request):
    sid = "xxxxxxxxxxx-0"
    name = "xxxxx xxxxx"
    nickname = 'xxx'
    gender = "ชาย"
    birthday = "xx xxx xxxx"
    height = 000
    weight = 00
    address = "xxxxxxxxxxxxxxxxx"
    number_phone = "099-999-9999"
    job = "นักศึกษา"
    status = "โสด"
    productlist = [
        ["มาม่ารสแกงเขียวหวานไก่", "7", 'images/1.png'],
        ["มาม่ารสหมูสับ", "7", 'images/2.png'],
        ["มาม่ารสตำยำกุ้ง", "7", 'images/3.png'],
        ["มาม่ารสหมูน้ำตก", "7", 'images/4.png'],
        ["มาม่ารสกระเพราแซบแห้ง", "7", 'images/5.png'],
        ["มาม่ารสตำยำกุ้งน้ำข้น", "7", "images/6.jpg"],
        ["มาม่ารสเป็ดพะโล้", "7", "images/7.jpg"],
        ["มาม่าหมูสับต้มยำน้ำข้น", "7", "images/8.jpg"],
        ["มาม่ารสหมูต้มยำ", "7", "images/9.jpg"],
        ["มาม่าคับรสหมูสับ", "18", 'images/10.png'],
        ["มาม่าคับรสต้มยำกุ้ง", "18", 'images/11.png'],
        ["มาม่าคับรสตำยำกุ้งน้ำข้น", "18", 'images/12.png'],
        ["มาม่าคับรสหมูสับตำยำน้ำข้น", "18", 'images/13.png'],
        ["มาม่าคับรสเป็ดพะโล้", "18", 'images/14.png'],
        ["มาม่าคับรสแกงเขียวหวานไก่", "18", 'images/15.png'],
        ["มาม่าคับรสหมูน้ำตก", "18", 'images/16.png'],
        ["มาม่าคับรสต้มแซบ", "18", 'images/17.png'],
        ["มาม่าคับรสเย็นตาโฟต้มยำหม้อไฟ", "18", 'images/18.png'],
        ["มาม่าครับรสสไปซี่คาโบนาร่า", "18", 'images/19.jpg'],
        ["มาม่าครับรสกระเพราแซบแห้ง", "18", 'images/20.png'],
        ["มาม่าคับรสเป็ดพะโล้และรสต้มแซบ", "18", 'images/21.png'],
    ]
    context = {
        'name': name, 
        'nickname': nickname, 
        'sid': sid, 
        'address': address, 
        'gender': gender,
        'weight': weight, 
        'height': height, 
        'number_phone': number_phone, 
        'birthday': birthday,
        'job': job, 
        'status': status, 
        'productlist': productlist
    }
    return render(request, "general/lab10.html", context)


def createProduct(request):
    if request.method == "POST":
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "บันทึกข้อมูลสำเร็จ")
            return redirect("lab11")
        else:
            messages.error(request, "บันทึกข้อมูลล้มเหลว")
            return redirect("createProduct")
    else:
        form = ProductsForm()
    context = {"form": form, }
    return render(request, "general/createProduct.html", context)


def lab11(request):
    products = Products.objects.all().order_by('id').reverse()
    count = products.count()
    context = {
        "products": products,
        "count": count,
    }
    return render(request, "general/lab11.html", context)


def lab12(request):
    return render(request, "general/lab12.html")