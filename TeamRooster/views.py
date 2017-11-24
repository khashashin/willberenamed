from django.shortcuts import render
from . models import TeamRooster, Staff

# Create your views here.
def base_page(request):
    staff = Staff.objects.all()
    return render(request, 'base.html')

# def home_page(request):
#     staff = Staff.objects.all()
#     return render(request, 'home.html', {'staff': staff})

# def team_rooster_page(request):
#     team_rooster = TeamRooster.objects.all()
#     return render(request, 'teamrooster.html', {'team_rooster': team_rooster})



# teams = [
#     Teams('Jungadler Mannheim', 'Calce', 'Luigi', 'Headcoach', 'https://vignette.wikia.nocookie.net/adventuretimewithfinnandjake/images/8/82/Piq_21633_400x400.png'),
#     Teams('HC Wisle', 'Christen', 'Markus', 'Headcoach', 'https://vignette.wikia.nocookie.net/wiiu/images/5/5e/New-Super-Mario-Bros-Art-21-400x400.jpg'),
#     Teams('Genève Hockey Futur', 'Foliot', 'Andy', 'Headcoach', 'https://www.isupportcause.com/uploads/overlay/isupportimg_1502860790663.png'),
#     Teams('EHC Bern 96', 'Guggenheim', 'Fabian', 'Headcoach', 'https://static1.squarespace.com/static/512e6d67e4b0e0699d1444d6/512f7c17e4b012cdc28b802a/5134d3eae4b066ad5331805b/1362416619556/pirate_mickey-400x400.jpg'),
#     Teams('HC Innerschwyz Future', 'Bissig', 'Roman', 'Headcoach', 'http://www.fpcbp.com/wp-content/gallery/tkGallery/OYIaJ1KK.png'),
    # Teams('SC Bern Future'),
    # Teams('Dijon Hockey'),
    # Teams('Kellenberger'),
    # Teams('HC Dragon Thun'),
    # Teams('SC Langenthal')
# ]

# team_rooster = [
#     TeamRooster(1, 'Roth', 'Justus', 'TH', 2004),
#     TeamRooster(3, 'Yamak', 'Emre', 'ST', 2004)
# ]
