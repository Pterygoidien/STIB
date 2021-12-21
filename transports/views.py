from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .forms import StationForm
from .models import Station, Line


def SearchItinary(request):
    context = {}
    if request.method == 'GET':
        form = StationForm(request.GET)
        context['form'] = form

        if form.is_valid():
            if form['departure'].value() != form['arrival'].value():
                departure_station = Station.objects.get(pk=form['departure'].value())
                arrival_station = Station.objects.get(pk=form['arrival'].value())
                departure_lines = departure_station.line_set.all()
                context['message'] = 'Pas de résultat trouvé'
                direct_path, connexion_path = [], []
                context['departure_lines'] = departure_lines
                context['arrival_lines']=[]

                for departure_line_instance  in departure_lines:
                    departure_line_instance_stations = departure_line_instance.Line_stations.all()
                    if arrival_station in departure_line_instance_stations:
                        direct_path.append(departure_line_instance)
                        context['message'] = f'Pas besoin de correspondance, la ligne {departure_line_instance.Line_number} contient la station de départ et la station d\'arrivée'
                        break ####break si on tolère qu'il n'y ait qu'un résultat de ligne direct: on sort de la loop, on gagne du temps en faisant moins de calculs au serveur.

                    context['message'] = f'Instances trouvées contenant à la fois station_instance et {arrival_station}'
                    for station_instance in departure_line_instance_stations:
                        try:
                            arrival_line = Line.objects.filter(Line_stations = arrival_station).filter(Line_stations=station_instance).exclude(Line_number=departure_line_instance.Line_number)
                            if (len(arrival_line)>0):
                                connexion_path.append((departure_line_instance, arrival_line, station_instance))
                                context['arrival_lines'].extend(arrival_line)
                                context['message']=f'Correspondance trouvée (départ : Ligne {departure_line_instance} à {departure_station}, correspondance à l\'arrêt {station_instance} pour la ligne {arrival_line.first()}'
                        except ObjectDoesNotExist:
                            context['message']='error'
                if len(direct_path)==0 and len(connexion_path)==0:
                    context['message'] = 'Aucun résultat trouvé (pas de correspondances)'



                context['direct_path'] = direct_path
            else:
                context['message'] = 'Merci de choisir une arrivée différente du départ'



    else:
        context['form'] = StationForm()
    return render(request, 'transports/search.html', context)

