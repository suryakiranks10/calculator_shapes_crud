"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from operations.views import AdditionView
from operations.views import SubtractionView
from operations.views import MultiplicationView
from operations.views import SquareView
from operations.views import RectangleView
from operations.views import TriangleView
from operations.views import CircleView
from operations.views import ParallelogramView
from operations.views import TrapeziumView
from operations.views import RhombusView
from operations.views import EllipseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("add/",AdditionView.as_view()),
    path("sub/",SubtractionView.as_view()),
    path("mul/",MultiplicationView.as_view()),
    path("square/",SquareView.as_view()),
    path("rectangle/",RectangleView.as_view()),
    path("triangle/",TriangleView.as_view()),
    path("circle/",CircleView.as_view()),
    path("parallelogram/",ParallelogramView.as_view()),
    path("trapezium/",TrapeziumView.as_view()),
    path("rhombus/",RhombusView.as_view()),
    path("ellipse/",EllipseView.as_view()),
]
