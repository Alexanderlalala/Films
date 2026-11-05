from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Rating(models.Model):
    IMDB_score = models.IntegerField(70)
    Rotten_Tomatoes_score = models.IntegerField(60)
    Audience_score = models.IntegerField(80)

    Cinema = models.OneToOneField(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return f"Rating for {self.Cinema.name}"

class Director(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateTimeField(auto_now_add=True)

    connection_to_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} {self.surname} - Director of {self.connection_to_movie.name}"

class Actors(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateTimeField(auto_now_add=True)

    Movie_actors = models.ManyToManyField(Movie, related_name='actors')
    def __str__(self):
        return f"{self.name} {self.surname} - Actor in {', '.join(movie.name for movie in self.Movie_actors.all())}"

class Tickets(models.Model):
    price = models.IntegerField()
    seat_number = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket for {self.movie.name} - Seat {self.seat_number}"

class MovieTheater(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    tickets_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name