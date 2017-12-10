# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from .serializers import Hot_News_Serializer
from .models import Hot_News
from rest_framework import viewsets
# rest_framework 中以 viewsets 取代原本 views 方法

from rest_framework.permissions import IsAuthenticated

 
class Hot_NewsViewSet(viewsets.ModelViewSet):
    queryset = Hot_News.objects.all()
    serializer_class = Hot_News_Serializer 
    # 複寫 attribute in GenericAPIView
    # 上面三行使得 model 俱備 CRUD 功能,因 viewsets.ModelViewSet 裡面幫你定義了這些功能
    
    #permission_classes = (IsAuthenticated,)
    # 替 API 設定基本權限 (有授權的使用者才能用此 API) 

def scraping(request):

    import os
    import sys
    from pprint import pprint
    import requests
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    #______________抓取焦點新聞網址_____________

    root_url = r'https://nba.udn.com/nba/index?gr=www'
    root_html = requests.get(root_url)
    root_html_text = root_html.text.encode('cp950', 'ignore').decode('cp950')
    # 重新編碼解碼過濾編碼有問題字元

    root_sp_obj = BeautifulSoup(root_html_text, 'html.parser')
    # 利用 'html.parser' 方法解析原始碼, 建立 soup 物件

    news_links_block = root_sp_obj.select('#news_body')
    # 利用 soup 選擇器標定 id = 'news_body' 內所有 <a>

    news_url_tags = news_links_block[0].find_all('a')
    news_img_tags = news_links_block[0].find_all('img')

    # 分別搜尋 id = 'news_body' 內所有 <a></a>,<img>

    news_urls = []
    img_urls = []
    # 建立串列儲存焦點'新聞網址' & '圖片網址'

    for url_tag in news_url_tags:
      news_urls.append( 'https://nba.udn.com/'+ url_tag.get('href'))

    for img_tag in news_img_tags:
            img_urls.append(img_tag.get('src'))
    
    # 判斷焦點新聞是否已存在
    duplicate_index = []

    for news_url in news_urls:
        try:
            Hot_News.objects.get(news_url = news_url)
            duplicate_index.append(news_urls.index(news_url))   # 記下重複的 index
        except:
            pass
    
    if len(duplicate_index) == len(news_urls):   # 全部重複則不動作
        pass

    else:
        if duplicate_index:                      # 若部分重複則刪除重複部分
            for i in reversed(duplicate_index):  # 倒過來刪除以免破壞 index 結構
                del news_urls[i]
                del img_urls[i]

        #_____________繼續分析抓取到的每個焦點新聞網址_____________

        headlines = []
        contents = []
        #建立串列儲存'新聞標題'與'新聞內容'

        publish_times = []
        repoters = []
        #建立串列儲存'發布時間'與'記者資訊'

        for news_url in news_urls:
            news_html = requests.get(news_url)
            news_html_text = news_html.text.encode('cp950', 'ignore').decode('cp950')
            news_sp_obj = BeautifulSoup(news_html_text, 'html.parser')
    
            main_block = news_sp_obj.select('#story_body_content')
            headlines.append(main_block[0].find('h1').text)
            # 儲存新聞標題

            paragraph_tags = main_block[0].find('p')
            contents.append(paragraph_tags.text[0:-34])
            # 儲存新聞內容 (切字串去掉最後面粉絲團訊息)

            info_block = news_sp_obj.select('.shareBar__info--author')
            publish_times.append(info_block[0].text[:16])
            repoters.append(info_block[0].text[16:])
            # 儲存發布時間與作者資訊 (切字串分開兩者)

        news_list = list(zip(news_urls,publish_times, repoters, headlines, contents, img_urls))
        # 整合所有資料至一串列

        for news in news_list:
            news_url = news[0]
            publish_time = news[1]
            repoter = news[2]
            headline = news[3]
            content = news[4]
            img_url = news[5]
            video_dir = ''

            data_unit = Hot_News.objects.create (news_url = news_url, publish_time = publish_time, repoter = repoter, headline = headline, content = content, img_dir = img_url, video_dir = video_dir)
            # 新增一筆新聞資料
            data_unit.save()
            # 將資料存入資料庫

    return render(request, 'scraping.html', locals())

def detail(request, id):
    page = id
    return render(request, 'detail.html', locals())

    
