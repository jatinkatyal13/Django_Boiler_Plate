from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from .models import *

from django.views.generic import *

# Create your views here.

def index(request):

    # feedBackForm = FeedBackForm(initial= {
    #     'rating' : 1
    # })

    if request.method == "GET":
        feedBackForm = FeedBackForm(initial={
            'some_num' : 5
        })

    elif request.method == "POST":
        feedBackForm = FeedBackForm(request.POST)
        if feedBackForm.is_valid():

            # print(request.POST['name'])

            # print(feedBackForm.cleaned_data['name'])

            # f = Feedback(
            #     name = feedBackForm.cleaned_data['name'],
            #     rating = feedBackForm.cleaned_data['rating'],
            #     remarks = feedBackForm.cleaned_data['remarks']
            # )
            # f.save()
            Feedback.objects.create(
                name = feedBackForm.cleaned_data['name'],
                rating = feedBackForm.cleaned_data['rating'],
                remarks = feedBackForm.cleaned_data['remarks']
            )

            print(feedBackForm.cleaned_data['some_num'])

            # go to success url
            return HttpResponseRedirect('success')

    # common to both get and post
    context = {
        'form' : feedBackForm
    }

    return render(request, 'form_learn/index.html', context)

def feedback(request):
    if request.method == "GET":
        feedBackForm = FeedBackModelForm()
    elif request.method == "POST":
        feedBackForm = FeedBackModelForm(request.POST)
        if feedBackForm.is_valid():
            feedBackForm.save()
            return HttpResponseRedirect('success')
    
    context = {
        'form' : feedBackForm
    }

    return render(request, 'form_learn/index.html', context)

def feedback_edit(request, pk):
    feedback = get_object_or_404(Feedback, pk = pk)
    if request.method == "GET":
        feedBackForm = FeedBackModelForm(instance=feedback)
    elif request.method == "POST":
        feedBackForm = FeedBackModelForm(request.POST, instance=feedback)
        if feedBackForm.is_valid():
            feedBackForm.save()
            return HttpResponseRedirect('/form/success')
    
    context = {
        'form' : feedBackForm
    }

    return render(request, 'form_learn/index.html', context)

class GenericFormView(FormView):
    template_name = 'generic_form_view.html'
    form_class = FeedBackForm
    success_url = '/form/success'

    def form_valid(self, form):
        Feedback.objects.create(
                name = form.cleaned_data['name'],
                rating = form.cleaned_data['rating'],
                remarks = form.cleaned_data['remarks']
            )
        
        return super().form_valid(form)

class GenericAddView(CreateView):
    model = Feedback
    fields = '__all__'
    template_name = 'generic_form_view.html'
    success_url = '/form/success'

class GenericUpdateView(UpdateView):
    model = Feedback
    fields = '__all__'
    template_name = 'generic_form_view.html'
    success_url = '/form/success'

class GenericDeleteView(DeleteView):
    model = Feedback
    template_name = 'delete_view.html'
    success_url = '/form/success'