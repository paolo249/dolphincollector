from django.shortcuts import render, redirect
from .models import Dolphin, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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
  toys_dolphin_doesnt_have = Toy.objects.exclude(id__in=dolphin.toys.all().values_list('id'))
  return render(request, 'dolphins/detail.html', {
    # include the cat and feeding_form in the context
    'dolphin': dolphin, 
    'feeding_form': feeding_form,
     'toys': toys_dolphin_doesnt_have
  })

def add_feeding(request, dolphin_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dolphin_id = dolphin_id
    new_feeding.save()
  return redirect('detail', dolphin_id=dolphin_id)



class DolphinCreate(CreateView):
  model = Dolphin
  fields = ['name', 'region', 'description', 'status']

  def form_valid(self, form):
     form.instance.user = self.request.user
     return super().form_valid(form)

class DolphinUpdate(UpdateView):
  model = Dolphin
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['region', 'description', 'status']

class DolphinDelete(DeleteView):
  model = Dolphin
  success_url = '/dolphins/'



class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, dolphin_id, toy_id):
  Dolphin.objects.get(id=dolphin_id).toys.add(toy_id)
  return redirect('detail', dolphin_id=dolphin_id)

def unassoc_toy(request, dolphin_id, toy_id):
  Dolphin.objects.get(id=dolphin_id).toys.remove(toy_id)
  return redirect('detail', dolphin_id=dolphin_id)

