from django.urls import path

from .views.holidays import HolidayListView, HolidayDetailView, HolidayCreateView, HolidayUpdateView, HolidayDeleteView
from .views.destinations import DestinationDetailView, DestinationUpdateView, DestinationDeleteView
from .views.holiday_destinations import HolidayDestinationCreateView, HolidayDestinationUpdateView, HolidayDestinationDeleteView

urlpatterns = [
    path('', HolidayListView.as_view(), name='holiday-list'),
    path('view/<slug:slug>/', HolidayDetailView.as_view(), name='holiday-detail'),
    path('create/', HolidayCreateView.as_view(), name='holiday-create'),
    path('update-<slug:slug>/', HolidayUpdateView.as_view(), name='holiday-update'),
    path('delete-<slug:slug>/', HolidayDeleteView.as_view(), name='holiday-delete'),
    path('destination/<int:id>/', DestinationDetailView.as_view(), name='destination-detail'),
    path('destination/update/<int:pk>/', DestinationUpdateView.as_view(), name='destination-update'),
    path('destination/delete/<int:pk>/', DestinationDeleteView.as_view(), name='destination-delete'),
    path('destination/<slug:holiday>/add-destination/', HolidayDestinationCreateView.as_view(), name='holiday-destination-create'),
    path('holiday-destination/update/<int:pk>/', HolidayDestinationUpdateView.as_view(), name='holiday-destination-update'),
    path('holiday-destination/delete/<int:pk>/', HolidayDestinationDeleteView.as_view(), name='holiday-destination-delete'),
]