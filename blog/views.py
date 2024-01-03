from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import New, Trandingnews, Categorynews, Singlenews, Comments, Indexnews, Products
from .forms import ContactForms, NewsletterForms, CommentForms


# Create your views here.
def index(request):
    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")
    tnews = Trandingnews.objects.all()
    news = New.objects.all()
    inews = Indexnews.objects.all()
    print(inews)
    context = {
        "form": form,
        "news": news,
        "tnews": tnews,
        "inews": inews,
    }
    return render(request, 'index.html', context=context)

# Create your views here.
def single(request):
    form = NewsletterForms(request.POST or None)
    form = CommentForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")
    tnews = Trandingnews.objects.all()
    snews = Singlenews.objects.all()
    comment = Comments.objects.all()
    context = {
        "form": form,
        "single": single,
        "tnews": tnews,
        "comment": comment,
        "snews": snews
    }
    return render(request, 'single.html', context=context)

def category(request):
    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")
    cnews = Categorynews.objects.all()
    tnews = Trandingnews.objects.all()
    context = {
        "form": form,
        "category": category,
        "tnews": tnews,
        "cnews": cnews
    }
    return render(request, 'category.html', context=context)

def contact(request):
    form = ContactForms(request.POST or None)
    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()

        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {

        "form": form,
        "contact": contact
    }
    return render(request, 'contact.html', context=context)


def newdetailview(request, id):
    try:
        new = New.objects.get(id=id)
        context = {
            "new": new
        }
    except contact.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "new_detail.html", context=context)

def products(request):
    product = Products.objects.filter(status="YR")
    context = {
        "product": product
    }
    return render(request, "product.html", context=context)

def productdetailview(request, product):
   product = get_object_or_404(Products, slug=product)
   context = {
       "product": product
   }
   return render(request, "product_detail.html", context=context)


def tnewsdetailview(request, tnews):
   tnews = get_object_or_404(Trandingnews, slug=tnews)
   context = {
       "tnews": tnews
   }
   return render(request, "tnews_detail.html", context=context)





