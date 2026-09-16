from django.urls import path

from .views.accommodation import (
    AccommodationCreateView,
    AccommodationDeleteView,
    AccommodationUpdateView,
)
from .views.destinations import (
    DestinationDeleteView,
    DestinationDetailView,
    DestinationUpdateView,
)
from .views.holiday_destinations import (
    HolidayDestinationCreateView,
    HolidayDestinationDeleteView,
    HolidayDestinationUpdateView,
)
from .views.holidays import (
    HolidayCreateView,
    HolidayDeleteView,
    HolidayDetailView,
    HolidayListView,
    HolidayUpdateView,
)

urlpatterns = [
    # Holiday
    path('', HolidayListView.as_view(), name='holiday-list'),
    path('view/<slug:slug>/', HolidayDetailView.as_view(), name='holiday-detail'),
    path('create/', HolidayCreateView.as_view(), name='holiday-create'),
    path('update-<slug:slug>/', HolidayUpdateView.as_view(), name='holiday-update'),
    path('delete-<slug:slug>/', HolidayDeleteView.as_view(), name='holiday-delete'),

    # Destination
    path('destination/<int:id>/', DestinationDetailView.as_view(), name='destination-detail'),
    path('destination/update/<int:pk>/', DestinationUpdateView.as_view(), name='destination-update'),
    path('destination/delete/<int:pk>/', DestinationDeleteView.as_view(), name='destination-delete'),

    # Holiday Destination
    path('destination/<slug:holiday>/add-destination/', HolidayDestinationCreateView.as_view(), name='holiday-destination-create'),
    path('holiday-destination/update/<int:pk>/', HolidayDestinationUpdateView.as_view(), name='holiday-destination-update'),
    path('holiday-destination/delete/<int:pk>/', HolidayDestinationDeleteView.as_view(), name='holiday-destination-delete'),

    # Accommodation
    path(
        'holiday-destination/<int:holiday_destination>/add-accommodation/',
        AccommodationCreateView.as_view(),
        name='accommodation-create',
    ),
    path(
        'holiday-destination/<int:holiday_destination>/accommodation/update/',
        AccommodationUpdateView.as_view(),
        name='accommodation-update',
    ),
    path(
        'holiday-destination/<int:holiday_destination>/accommodation/delete/',
        AccommodationDeleteView.as_view(),
        name='accommodation-delete',
    ),
]