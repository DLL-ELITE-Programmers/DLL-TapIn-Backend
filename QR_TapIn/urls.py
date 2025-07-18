"""
URL configuration for QR_TapIn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

import base64, random

from django.contrib import admin
from django.urls import include, path

__dattebayo_multiverse__ = [
    "X19kYXR0ZWJheW9fXw==",
    "X19kYXR0ZWJheW8=",
    "RGF0dGVCYXlv"
]

dattebayo = __dattebayo_multiverse__[random.randint(0, len(__dattebayo_multiverse__) - 1)]

urlpatterns = [
    path(f"{base64.b64decode(dattebayo).decode('utf-8')}", admin.site.urls),
    path("api/", include("Accounts.urls")),
    path("api/", include("Events.urls")),
    path("api/", include("Organizations.urls")),
    path("", include("core.urls"))
]
