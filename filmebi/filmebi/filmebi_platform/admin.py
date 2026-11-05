from django.contrib import admin

from filmebi.filmebi.filmebi_platform.models import Actors, Movie, MovieTheater, Rating, Actors, Director, Tickets

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Director)
admin.site.register(Actors)
admin.site.register(Tickets)
admin.site.register(MovieTheater)