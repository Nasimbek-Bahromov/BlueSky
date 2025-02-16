"""
URL configuration for Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""Config loyihasi uchun URL konfiguratsiyasi.

`urlpatterns` royxati URL manzillarini krishlarga yonaltiradi. Qo'shimcha ma'lumot uchun qarang:
 https://docs.djangoproject.com/en/5.0/topics/http/urls/
Misollar:
Funktsiya ko'rinishlari
 1. Import qoshing: my_app import korinishlaridan
 2. URL namunalariga URL qoshing: path('', views.home, name='home')
Sinfga asoslangan ko'rinishlar
 1. Import qoshing: from other_app.views import Home
 2. Urlpatternsga URL qoshing: path('', Home.as_view(), name='home')
Shu jumladan boshqa URLconf
 1. include() funksiyasini import qiling: django.urls dan import include, path
 2. URL namunalariga URL qoshing: path('blog/', include('blog.urls'))"""


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
