from django.urls import path
from terza_app.views import diff,pari
app_name="terza_app"
urlpatterns=[
    path('diff', diff, name='diff'),
    path('pari', pari, name='pari'),
     
]