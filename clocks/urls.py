from django.urls import path
from .views import ReviewDeleteView,ReviewUpdateView, WatchListView, WatchDetailView,AddReviewView,SearchResultsView,AddToCartView,RemoveFromCartView,CartView,TopCheapWatchesView,TopExpensiveWatchesView

app_name = 'clocks'
urlpatterns = [
    path('watchs/',WatchListView.as_view(),name='watch_list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('deatail/<int:pk>',WatchDetailView.as_view(),name='watch_detail'),
    path('add_to_cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add_review'),  
    path('review_delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('remove_from_cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('review_update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
    path('top_expensive/', TopExpensiveWatchesView.as_view(), name='top_expensive'),
    path('top_cheap/', TopCheapWatchesView.as_view(), name='top_cheap')
]