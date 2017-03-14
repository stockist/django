from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Song

class IndexView(generic.ListView):
	"""docstring for IndexView"""
	template_name = 'music/index.html'
	context_object_name = "all_album"
	def get_queryset(self):
		return Album.objects.all()


class DetailView(generic.DetailView):
	"""docstring for DetailView"""
	model = Album
	template_name = 'music/detailPage.html'






class AlbumCreate(CreateView):
	"""docstring for AlbumCreate"""
	model = Album
	fields = ['artist', 'album_title', 'genere']
		