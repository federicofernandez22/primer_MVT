from django.urls import path
from Familia.views import papa, mama, hermana






urlpatterns = [
    
    path('papa/', papa),
    path('mama/', mama),
    path('hermana/', hermana),
    

]