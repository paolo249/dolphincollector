from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dolphin, Toy
from .forms import FeedingForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dolphins_index(request):
  dolphins = Dolphin.objects.all()
  return render(request, 'dolphins/index.html', { 'dolphins': dolphins })



def dolphins_detail(request, dolphin_id):
  dolphin = Dolphin.objects.get(id=dolphin_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'dolphins/detail.html', {
    # include the cat and feeding_form in the context
    'dolphin': dolphin, 'feeding_form': feeding_form
  })

def add_feeding(request, dolphin_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.dolphin_id = dolphin_id
    new_feeding.save()
  return redirect('detail', dolphin_id=dolphin_id)

class DolphinCreate(CreateView):
  model = Dolphin
  fields = '__all__'
  success_url = '/dolphins/'


class DolphinUpdate(UpdateView):
  model = Dolphin
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['region', 'description', 'status']

class DolphinDelete(DeleteView):
  model = Dolphin
  success_url = '/dolphins/'

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'