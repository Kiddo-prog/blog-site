from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Article
from .forms import ArticleForm
from django.views.generic import ListView, DetailView, CreateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from user.forms import ContactForm


# Create your views here.


class HomePageView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()
    context_object_name = "article_list"
    paginate_by = 5


class ArticleDetailView(DetailView):
    context_object_name = "article_detail"
    template_name = "articles/article_detail.html"
    queryset = Article.objects.all()


class ArticleCreateView(CreateView):
    template_name = "forms/create_article.html"
    queryset = Article.objects.all()
    form_class = ArticleForm

    def get_success_url(self):
        return reverse("articles:article-list")


# Update Article Post
def about_me(request):
    return render(request, "about_me.html", {})


def contact(request):
    if request.method == "GET":
        form = ContactForm(request.GET)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                send_mail(
                    subject, message, email, {"admin@example.com"}, fail_silently=False
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found")
        return redirect("articles:success")

    return render(request, "contact.html", {"form": form})


def success_page(request):
    return render(request, "success.html", {})