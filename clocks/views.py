from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import CategoryWatch,Review,Watch
from .forms import AddReviewForm,UpdateReviewForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
from django.contrib import messages

class WatchListView(View):
    def get(self, request):
        watchs = Watch.objects.all().order_by('-pk')
        context = {
            'watchs': watchs
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
        watchs = Watch.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'watchs': watchs,
            'add_review_form': add_review_form
        }
        return render(request, 'watch/add_review.html', context=context)

    def post(self, request, pk):
        watchs = Watch.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                watch=watchs,
                user=request.user,
                rating=add_review_form.cleaned_data['rating']
            )

            review.save()
            messages.success(request, "Comment qo'shildi.")
            return redirect('products:watch_detail', pk=pk) 

class ReviewDeleteView(View):
    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        watch_pk = review.watch.pk
        review.delete()
        messages.success(request, "Comment o'chirildi.")
        return HttpResponseRedirect(reverse_lazy('products:watch_detail', kwargs={'pk': watch_pk}))

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
            return redirect('products:watch_detail', pk=update.watch_id) 
        else:
            messages.error(request, "Comment o'zgartirilmadi.")
            return render(request, 'watch/update_review.html', {'form': update_form}) 