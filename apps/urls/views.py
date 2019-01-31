from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from apps.urls.forms import UrlForm
from apps.urls.models import Urls
from apps.urls.utils import generate_unique_key
from short_url.settings import BASE_LOCAL_URL


class HomelView(View):
    form_class = Urls
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = UrlForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(urls=None).order_by("?").first()
            url = Urls.objects.filter(url=request.POST['url']).first()
            if url:
                return render(request, 'home.html', {'form': form, 'short_link': BASE_LOCAL_URL + str(url.slug),
                                                     "main_link": request.POST['url']})
            unique_key = generate_unique_key()
            url = Urls(url=request.POST['url'], user=user, slug=unique_key)
            url.save()
            return render(request, 'home.html', {'form': form, 'short_link': BASE_LOCAL_URL + str(unique_key),
                                                 'main_link': request.POST['url']})


class SlugView(View):
    def get(self, request, *args, **kwargs):
        url = Urls.objects.filter(slug=self.kwargs['slug']).first()
        if self.kwargs['slug'][0] == '!':
            url = Urls.objects.filter(slug=self.kwargs['slug'][1:]).first()
            return render(request, 'info.html',
                          {'short_url': BASE_LOCAL_URL + str(self.kwargs['slug'][1:]), 'main_url': url.url,
                           'seen_count': url.seen_count,
                           "user": url.user})
        if url:
            url.seen_count += 1
            url.save()
            return redirect(url.url)
        else:
            return HttpResponse("something is wrong")
