from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


from movies_app.models import Peliculas, Sala, Promociones, Schedule
#from movies_project.movies_app.models import Sala
from .forms import MoviesForm, PromocionesForm, SalaForm, ScheduleForm

# Create your views here.

# def get_movie(request, code):
#     if not code:
#         movies = Peliculas.objects.all()
#         context = []
#         for record in movies:
#             context.append({"name": record.name, "code": record.code, "sala": record.sala })
#         render(request, 'index.html', context=context)
#     else: 
#         movies = Peliculas.objects.get(code = code)
#         context["name"] = movies.name
#         context["code"] = movies.code
#         context["sala"] = movies.sala
#         render(request, 'index.html', context=[context])
#url https://www.misitio.com/movies/code:int
# Create your views here.

def get_all_movies(request):
    movies = Peliculas.objects.all()
    context = {"movies": movies}
    return render(request, "all_movies.html", context=context)

def get_all_rooms(request):
    rooms = Sala.objects.all()
    context = {"rooms": rooms}
    return render(request, "all_rooms.html" , context=context)

# Create your views here.

def get_all_promotions(request):
    promotions = Promociones.objects.all()
    context = {"promotions": promotions}
    return render(request, "all_promotions.html" , context=context)

def get_all_schedule(request):
    calendario= Schedule.objects.all()
    context = {"calendario": calendario}
    return render(request, "all_calendario.html" , context=context)

#yo estoy aca

def post_movie(request):
    if request.method == "POST":
        form = MoviesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            movie = Peliculas(name=data['name'], code=data['code'], sala=data['sala'])
            movie.save()
            return HttpResponseRedirect('/movies')
    else:
        form = MoviesForm()
    return render(request, 'movies_form.html', {'form': form})


def post_sala(request):
    if request.method =="POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            sala = Sala(number=data['number'], code=data['code'])
            sala.save()
            return HttpResponseRedirect('/movies/rooms')
    else:
        form = SalaForm()
    return render(request, 'salas_form.html', {'form': form})

def post_schedule(request):
    if request.method =="POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            schedule = Schedule(horario=data['horario'],pelicula=data["pelicula"],sala=data["sala"], code=data['code'])
            schedule.save()
            return HttpResponseRedirect('/movies/schedule')
    else:
        form = ScheduleForm()
    return render(request, 'schedule_form.html', {'form': form})

def post_promociones(request):
    if request.method =="POST":
        form = PromocionesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            promociones = Promociones(precio=data['precio'],code=data["code"],descripcion=data["descripcion"])
            promociones.save()
            return HttpResponseRedirect('/movies/promotions')
    else:
        form = PromocionesForm()
    return render(request, 'promociones_form.html', {'form': form})


def search(request):
    context_dict = dict()
    if request.GET['movies_search']:
        search_param = request.GET['movies_search']
        peliculas = Peliculas.objects.filter(name__contains=search_param)
        context_dict = {
            'movies': peliculas
        }

    return render(
        request=request,
        context=context_dict,
        template_name="home.html",
    )