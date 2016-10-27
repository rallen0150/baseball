"""baseball_stat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from stats.views import MasterListCreateAPIView, MasterDetailUpdateDestroyAPIView, BattingListCreateAPIView, \
                        BattingDetailUpdateDestroyAPIView, FieldingListCreateAPIView, FieldingDetailUpdateDestroyAPIView, \
                        PitchingListCreateAPIView, PitchingDetailUpdateDestroyAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/master/$', MasterListCreateAPIView.as_view(), name="master_list_create_view"),
    url(r'^api/master/(?P<pk>\d+)/$', MasterDetailUpdateDestroyAPIView.as_view(), name="master_detail_update_destroy_view"),
    url(r'^api/batting/$', BattingListCreateAPIView.as_view(), name="batting_list_create_view"),
    url(r'^api/batting/(?P<pk>\d+)/$', BattingDetailUpdateDestroyAPIView.as_view(), name="batting_detail_update_destroy_view"),
    url(r'^api/fielding/$', FieldingListCreateAPIView.as_view(), name="fielding_list_create_view"),
    url(r'^api/fielding/(?P<pk>\d+)/$', FieldingDetailUpdateDestroyAPIView.as_view(), name="fielding_detail_update_destroy_view"),
    url(r'^api/pitching/$', PitchingListCreateAPIView.as_view(), name="pitching_list_create_view"),
    url(r'^api/pitching/(?P<pk>\d+)/$', PitchingDetailUpdateDestroyAPIView.as_view(), name="pitching_detail_update_destroy_view"),
]
