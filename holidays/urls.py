from django.urls import path

from .views import HolidayListView, HolidayDetailView, HolidayCreateView, HolidayUpdateView, HolidayDeleteView

urlpatterns = [
    path('', HolidayListView.as_view(), name='holiday-list'),
    path('view/<slug:slug>/', HolidayDetailView.as_view(), name='holiday-detail'),
    path('create/', HolidayCreateView.as_view(), name='holiday-create'),
    path('update-<slug:slug>/', HolidayUpdateView.as_view(), name='holiday-update'),
    path('delete-<slug:slug>/', HolidayDeleteView.as_view(), name='holiday-delete'),
]