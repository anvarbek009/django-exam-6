from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Review,Watch,Order,Cart, CartItem
from .forms import AddReviewForm,UpdateReviewForm,OrderForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
from django.contrib import messages

# class WatchCategoryView(View):
#     def get(self, request):
#         category_watchs = CategoryWatch.objects.all()
#         context = {
#             'category_watchs': category_watchs
#         }
#         return render(request, 'base.html', context=context)

class WatchListView(View):
    def get(self, request):
        watchs = Watch.objects.all().order_by('-pk')
        context = {
            'watchs': watchs
        }
        return render(request, 'watch/watch_list.html', context=context)

class SearchResultsView(View):
    def get(self, request):
        query = request.GET.get('q')
        results = Watch.objects.filter(name__icontains=query) if query else []
        context = {
           'results': results,
            'query': query
        }
        return render(request, 'watch/watch_list.html', context=context)

class WatchDetailView(View):
    model = Watch
    template_name = 'watch/watch_detail.html'
    def get(self, request, pk):
        watch = Watch.objects.get(pk=pk)
        reviews = Review.objects.filter(watch=pk)
        context = {
            'watch': watch,
            'reviews': reviews
        }

        return render(request, 'watch/watch_detail.html', context=context)
       
class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        watch = Watch.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'watch': watch,
            'add_review_form': add_review_form
        }
        return render(request, 'watch/add_review.html', context=context)

    def post(self, request, pk):
        watch = Watch.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                watch=watch,
                user=request.user,
                rating=add_review_form.cleaned_data['rating']
            )
            review.save()
            messages.success(request, "Comment qo'shildi.")
            return redirect('clocks:watch_detail', pk=pk)
        else:
            context = {
                'watch': watch,
                'add_review_form': add_review_form
            }
            return render(request, 'watch/add_review.html', context=context)

class AddToCartView(View):
    def post(self, request, pk):
        watch = get_object_or_404(Watch, pk=pk)
        cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, watch=watch)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        messages.success(request, "Watch added to cart successfully.")
        return redirect('clocks:watch_detail', pk=pk)
    
class CartView(View):
    def get(self, request):
        cart = Cart.objects.get(user=request.user, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart)
        context = {
            'cart': cart,
            'cart_items': cart_items
        }
        return render(request, 'watch/cart.html', context)
    
class RemoveFromCartView(View):
    def post(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk)
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
        return redirect('clocks:cart')
class ReviewDeleteView(View):
    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        watch_pk = review.watch.pk
        review.delete()
        messages.success(request, "Comment o'chirildi.")
        return HttpResponseRedirect(reverse_lazy('clocks:watch_detail', kwargs={'pk': watch_pk}))     
class ReviewUpdateView(View):
    def get(self, request, pk):
        data = Review.objects.get(pk=pk)
        update_form=UpdateReviewForm(instance=data)
        return render(request, 'watch/update_review.html', {'form': update_form})    
    def post(self, request, pk):
        update = Review.objects.get(pk=pk)
        update_form = UpdateReviewForm(request.POST, instance=update)
        if update_form.is_valid():
            update_review = update_form.save(commit=False)
            update_review.watch_id = update.watch_id
            update_review.save()
            messages.success(request, "Comment o'zgartirildi.")
            return redirect('clocks:watch_detail', pk=update.watch_id) 
        else:
            messages.error(request, "Comment o'zgartirilmadi.")
            context={
                'form': update_form
            }
            return render(request, 'watch/update_review.html', context=context) 
        
class TopExpensiveWatchesView(View):
    def get(self, request):
        top_expensive_watches = Watch.objects.order_by('-price')[:3]
        context = {
            'watches': top_expensive_watches
            }
        return render(request, 'watch/top_expensive.html', context=context)

class TopCheapWatchesView(View):
    def get(self, request):
        top_cheap_watches = Watch.objects.order_by('price')[:3]
        context = {
            'watches': top_cheap_watches
            }
        return render(request, 'watch/top_cheap.html', context=context)