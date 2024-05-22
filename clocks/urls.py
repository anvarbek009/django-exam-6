from django.urls import path
from .views import ReviewDeleteView,ReviewUpdateView, WatchListView, WatchDetailView,AddReviewView,SearchResultsView

app_name = 'clocks'
urlpatterns = [
    path('watchs/',WatchListView.as_view(),name='watch_list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('deatail/<int:pk>',WatchDetailView.as_view(),name='watch_detail'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add_review'),  
    path('review_delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('review_update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
]