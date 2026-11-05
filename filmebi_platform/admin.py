from django.contrib import admin

from filmebi.filmebi.filmebi_platform.models import Movie, Rating, Actors, Director, Tickets, Movietheater

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Director)
admin.site.register(Actors  )
admin.site.register(Tickets)
admin.site.register(Movietheater)