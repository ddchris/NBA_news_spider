# -*- coding: utf-8 -*-

# 做序列化 ( 其他人呼叫 API 時將 python 資料轉成其他格式(ex:JSON,HTML,XML...) 送出)
from rest_framework import serializers
from myapp.models import Hot_News

class Hot_News_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hot_News            # 指出序列化哪個 model
        fields = '__all__'          # 序列化全部欄位寫法
        #fields = ('id', 'news_url', 'publish_time', 'repoter', 'headline', 'content', 'img_dir', 'video_dir')   # 序列化特定欄位寫法