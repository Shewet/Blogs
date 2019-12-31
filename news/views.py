from django.shortcuts import render,redirect
import requests
import os
import shutil
from django.conf import settings
requests.packages.urllib3.disable_warnings()
# Create your views here.
from bs4 import BeautifulSoup
from .models import Headline,UserProfile
from datetime import timedelta, timezone, datetime


def news_list(request):
    headlines=Headline.objects.all()
    context={
        'headlines':headlines
    }
    return render(request,'news/home.html',context)

def scrape(request):
    user_p=UserProfile.objects.filter(user=request.user).first()
    if user_p:
        user_p.last_scrape =datetime.now(timezone.utc)
    else:
        user_p=UserProfile(user=request.user,last_scrape=datetime.now(timezone.utc))
    user_p.save()
    session = requests.Session()
    session.headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/79.0.3945.79 Chrome/79.0.3945.79 Safari/537.36"}
    url="https://www.theonion.com/"
    content=session.get(url,verify=False).content
    soup=BeautifulSoup(content,"html.parser")
    posts=soup.find_all('div',{'class':'curation-module__item'})
    for post in posts:
        srcset=post.find('img',{"class":"dv4r5q-2 iaqrWM"})
        title_html = post.find('h6')
        if not title_html:
            title_html=post.find('h3')
        title=title_html.text
        image_source=srcset['srcset'].split(" 80w,")[0]
        url_html = post.find_all('a',href=True)[1]
        url=url_html['href']
        headline=Headline.objects.filter(url=url)
        if not headline:
            image_filename=image_source[image_source.rfind("/")+1:]
            r= session.get(image_source,stream=True,verify=False)
            with open(image_filename,"w+b") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
            current_file_absolute_path= os.path.abspath(image_filename)
            shutil.move(current_file_absolute_path,settings.MEDIA_ROOT+image_filename)
            
            headline=Headline(title=title,url=url,image=image_filename)
            headline.save()
        else:
            pass
        return redirect('/news/home')



