from django.urls import path
from .views import PagesListView,PageDetailView

urlpatterns = [
    path('', PagesListView.as_view(), name="pages"),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
]