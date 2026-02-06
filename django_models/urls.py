from django.urls import path
from .views import admin_view, librarian_view, member_view
from django.urls import path, include

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('', include('django-models.urls')),

]
