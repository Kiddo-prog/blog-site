from django.urls import path

from articles import views as article_view

app_name = "articles"

urlpatterns = [
    path("", article_view.HomePageView.as_view(), name="article-list"),
    path("create/", article_view.ArticleCreateView.as_view(), name="article-create"),
    path(
        "<slug:slug>", article_view.ArticleDetailView.as_view(), name="article-detail"
    ),
    path("about/", article_view.about_me, name="about"),
    path("contact/", article_view.contact, name="contact"),
    path("contact/success/", article_view.success_page, name="success"),
]