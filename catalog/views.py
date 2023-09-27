from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Category, Product, Article


class CategoryListView(ListView):
    model = Category


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        if self.request.method == "POST":
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}, phone: {phone} message: {message}')

        # Для добавления информации из БД в отображение контактов.
        # context_data['object_list'] = Some_data_for_contacts.objects.all()

        return context_data


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ArticleListView(ListView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview', 'is_published',)
    success_url = reverse_lazy('catalog:articles')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview', 'is_published',)
    success_url = reverse_lazy('catalog:articles')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('catalog:articles')
