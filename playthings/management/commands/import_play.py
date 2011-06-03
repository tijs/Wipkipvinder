from optparse import make_option
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from playthings.models import Plaything, Hood, Category, Type
import rd2wgs84
import json
from playthings.models import City

class Command(BaseCommand):
    args = '<city input_file>'
    help = 'Imports the given json file for the given city'
    option_list = BaseCommand.option_list + (
        make_option('--force',
            action='store_true',
            dest='force',
            default=False,
            help='Always overwrite existing playthings'),
        )

    def handle(self, *args, **options):
        '''
        import the given JSON file taking into account city specific settings
        '''

        if len(args) != 2:
            raise CommandError('This commands takes exactly 2 arguments')

        city_name = args[0] # i.e. 'den haag'
        json_file = args[1] # i.e. 'export.geojson'

        city = City.objects.get(name__iexact=city_name)

        if not city:
            raise CommandError('City "%s" does not exist' % city_name)

        try:
            geofile = open(json_file)
            data = json.loads(geofile.read().decode('latin_1')) # somehow latin_1 works more reliably
        except:
            raise CommandError('Could not load: "%s"' % json_file)

        # try and add each 'feature' a.k.a. play thingie to the DB
        for i in data["features"]:
            coords = i["geometry"]["coordinates"]

            # convert from the 'dutch' coordinate system to the more common WGS84 (which Google gets)
            if type(coords[0]).__name__=='float':
                newk = rd2wgs84.convert(coords[0], coords[1])
                lat = newk[0]
                lng = newk[1]

            properties = i["properties"]

            # only add playthings with lat, lng and some properties
            if lat and lng and properties:
                create_or_update(self.stderr, self.stdout, city, properties, lat, lng, options.get('force'))
            else:
                pass

        self.stdout.write('Successfully imported playthings from JSON "%s"\n' % json_file.encode('utf-8'))

def create_or_update(stderr, stdout, city, properties, lat, lng, force):
    '''
    Create a new plaything entry based on the JSON entry.
    '''

    # load JSON mapping for given city
    mapping = settings.MAPPING[city.name]

    ref = str(properties[mapping['ref']])

    try:
        new_pt = Plaything.objects.get(reference=ref, city=city)

        if force:
            pass
        else:
            return True

    except Plaything.DoesNotExist:
        new_pt = Plaything()
        new_pt.reference = ref

    new_pt.city = city
    new_pt.lat = str(lat)
    new_pt.lng = str(lng)

    # todo: perhaps do a reverse geocode instead to get a nicer address
    full_address = "%s" % properties[mapping['street']]
    new_pt.address = full_address.lower()

    # find or create the Neighbourhood
    try:
        hood = Hood.objects.get(name__iexact=properties[mapping['neighbourhood']])
    except Hood.DoesNotExist:
        hood = Hood(name=str(properties[mapping['neighbourhood']]).lower(), city=city)
        hood.save()

    new_pt.neighbourhood = hood

    # find or create the Category
    try:
        category = Category.objects.get(name__iexact=properties[mapping['category']])
    except Category.DoesNotExist:
        category = Category(name=str(properties[mapping['category']]).lower())
        category.save()

    # find or create the Type
    try:
        type = Type.objects.get(name__iexact=properties[mapping['type']], category=category)
    except Type.DoesNotExist:
        type = Type(name=str(properties[mapping['type']]).lower(), category=category)
        type.save()

    new_pt.type = type

    new_pt.save()
    stdout.write('Saved %s: %s\n' % (ref.encode('utf-8'), type.name.encode('utf-8')))


