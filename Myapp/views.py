from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie
from .forms import MovieForm, RegistrationForm
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import error as error_message
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import uuid


def movie_list(request):
    if not request.user.is_authenticated:
        return redirect('Myapp:user_login')
    """Displays a list of all movies."""
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'Myapp/movie_list.html', context)

def movie_create(request):
  """Creates a new movie."""
  if request.method == 'POST':
    form = MovieForm(request.POST)
    if form.is_valid():
            movie_instance = form.save(commit=False)  # Save without committing to database
            movie_instance.id = uuid.uuid4()  # Assign a UUID to the movie instance
            movie_instance.save()  # Save the movie instance with the UUID
            messages.success(request, 'Movie created successfully!')
            return redirect('Myapp:movie_list')
  else:
    form = MovieForm()
  context = {'form': form}
  return render(request, 'Myapp/movie_create.html', context)
 
#update  
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)  # Populate form with movie data
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie updated successfully!')
            return redirect('Myapp:movie_list')  # Redirect to list view after successful update
    else:
        context = {'movie': movie, 'form': form}

    return render(request, 'Myapp/movie_update.html', context)
    
  
#delete
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        movie.delete()
        messages.success(request, 'Movie deleted successfully!')
        return redirect('Myapp:movie_list')  # Redirect to list view after successful deletion
    else:
        # If not a POST request (GET request), display confirmation prompt
        return render(request, 'Myapp/movie_delete.html', {'movie': movie})
        
#registeration view

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Myapp:user_login')
    else:
        form = UserCreationForm()
    return render(request, 'Myapp/register.html', {'form': form})
    
#login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Myapp:movie_list')
    else:
        form = AuthenticationForm()
    return render(request, 'Myapp/login.html', {'form': form})

#ogout view

@login_required
def user_logout(request):
    logout(request)
    # Redirect to desired page after successful logout
    return redirect('Myapp:user_login') 

 
 