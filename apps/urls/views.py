from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from apps.urls.forms import UrlForm
from apps.urls.models import Urls
from apps.urls.utils import generate_unique_key
from short_url.settings import BASE_LOCAL_URL


def slug(request, slug):
    url = Urls.objects.filter(slug=slug).first()
    if slug[0] == '!':
        url = Urls.objects.filter(slug=slug[1:]).first()
        return render(request, 'info.html',
                      {'short_url': BASE_LOCAL_URL + str(slug[1:]), 'main_url': url.url, 'seen_count': url.seen_count,
                       "user": url.user})
    if url:
        url.seen_count += 1
        url.save()
        return redirect(url.url)
    else:
        return HttpResponse("something is wrong")


def home(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(urls=None).order_by("?").first()
            url = Urls.objects.filter(url=request.POST['url']).first()
            if url:
                return render(request, 'home.html', {'form': form, 'short_link': BASE_LOCAL_URL + str(url.slug),
                                                     "main_link": request.POST['url']})
            else:
                unique_key = generate_unique_key()
                url = Urls(url=request.POST['url'], user=user, slug=unique_key)
                url.save()
                return render(request, 'home.html', {'form': form, 'short_link': BASE_LOCAL_URL + str(unique_key),
                                                     'main_link': request.POST['url']})
    else:
        form = UrlForm()
    return render(request, 'home.html', {'form': form})
