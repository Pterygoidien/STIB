from django.shortcuts import render
from .forms import StationForm
from .models import Station, Line


def SearchItinary(request):
    context = {
        'form':StationForm(),
    }
    if request.method == 'GET':
        form = StationForm(request.GET)
        if form.is_valid():
            if form['departure'].value() != form['arrival'].value():
                departure_station = Station.objects.get(id=form['departure'].value()) #pk=form(...) à éviter, la requête par 'pk' prend plus de temps !
                arrival_station = Station.objects.get(id=form['arrival'].value())
                departure_lines = departure_station.line_set.all()

                context = {
                    'form':form,
                    'departure_station':departure_station,
                    'arrival_station':arrival_station,
                    'direct_path':[],
                    'connexion_path':[],
                }

                for departure_line_instance  in departure_lines:
                    departure_line_instance_stations = departure_line_instance.Line_stations.all()
                    if arrival_station in departure_line_instance_stations:
                        context['direct_path'].append(departure_line_instance)
                        #break
                    else:
                        for station_instance in departure_line_instance_stations:
                            arrival_lines = Line.objects.filter(
                                Line_stations=arrival_station
                            ).filter(
                                Line_stations=station_instance
                            ).exclude(
                                Line_number=departure_line_instance.Line_number
                            ).exclude(
                                Line_stations=departure_station
                            )
                            if arrival_lines:
                                context['connexion_path'].append((departure_line_instance, arrival_lines, station_instance))
            else:
                context['message'] = 'Merci de choisir une arrivée différente du départ'
    else:
        context['message']='faites votre recherche'
    return render(request, 'transports/search.html', context)

