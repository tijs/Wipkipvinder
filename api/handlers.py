from piston.handler import BaseHandler
from playthings.models import Plaything

class PlaythingsHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Plaything
    fields = ('distance', 'reference', 'lat', 'lng', 'address', 'neighbourhood', 'city', 'type', 'category')

    @classmethod
    def type(self, plaything):
        return plaything.type.name

    @classmethod
    def category(self, plaything):
        return str(plaything.type.category.name).lower()

    @classmethod
    def neighbourhood(self, plaything):
        return plaything.neighbourhood.name

    @classmethod
    def city(self, plaything):
        return plaything.city.name

    def read(self, request, lat, lng, km):
        """
        Returns all play equipment within a certain range
        """
        return Plaything.objects.nearby(lat, lng, km, 50) # limit to 50 results
