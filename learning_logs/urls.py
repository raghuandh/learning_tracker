""" Defines URL patterns for learning_logs """
from django.urls import re_path as url2
from . import views

urlpatterns = [
    #Home page
    url2(r'^$', views.index, name='index'),
    url2(r'^topics/$', views.topics, name='topics'),
    url2(r'^Diary/$', views.Diary, name='Diary'),
    url2(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url2(r'^new_topic/$', views.new_topic, name='new_topic'),
    url2(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url2(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
    url2(r'^new_diary_entry/$',views.new_diary_entry, name='new_diary_entry'),
    url2(r'^diary_entry_edit/(?P<entry_id>\d+)/$', views.diary_entry_edit, name='diary_entry_edit'),
]