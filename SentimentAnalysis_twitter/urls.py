from django.conf.urls import url
from django.contrib import admin
from search import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #Home page
    url(r'^$', views.index, name='index'),

    #Search results
    url(r'^search/', views.get_name, name='search-results'),

    #Instagram Dataset 1 results
    url(r'^map/', views.instagram_data, name='map'),

    #Instagram Dataset April Week-end results
    url(r'^map-we/', views.instagram_we_data, name='map-we'),


    #download csv
    url(r'^download/', views.download_csv, name='download'),
    
] 