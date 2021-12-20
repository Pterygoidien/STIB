from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Vehicule(models.Model):
    """La classe véhicule est une classe dynamique qui englobe plusieurs moyens de transport publics de la STIB :
        B -> Bus
        T -> Tram
        M -> Metro
        N -> Noctis
        Chaque instance de classe correspond à l'enregistrement d'un véhicule, avec son type, et sa ligne.
        La ligne est un entier positif, même si certaines lignes peuvent avoir des caractères spéciaux (préfixe 'n', ou T).
        Les éventuels préfixes sont ajoutés par la suite.

        Cette classe est en réalité futile, puisque la classe "Ligne" peut exister sans la classe véhicule,
        pour peu qu'on lui spécifie le type de véhicule, puisque ce dernier est invariable à la ligne assignée. """
    class Vehicule_Type(models.TextChoices):
        BUS = 'B', _('Bus')
        TRAM = 'T', _('Tram')
        METRO = 'M', _('Metro')
        NOCTIS = 'N', _('Noctis')

    vehicule_type = models.CharField(
        max_length=1,
        choices=Vehicule_Type.choices,
        default=Vehicule_Type.BUS
    )


class Station(models.Model):
    """La classe Station correspond aux arrêts de bus/tram/n'importe quel moyen de transport public."""
    Station_name = models.CharField(max_length=200)
    Station_adress = models.CharField(max_length=300)

    def __str__(self):
        return self.Station_name


class Line(models.Model):
    Line_number = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    class Vehicule_Type(models.TextChoices):
        BUS = 'B', _('Bus')
        TRAM = 'T', _('Tram')
        METRO = 'M', _('Metro')

    vehicule_type = models.CharField(
        max_length=1,
        choices=Vehicule_Type.choices,
        default=Vehicule_Type.BUS
    )
    Line_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.vehicule_type}: {self.Line_number}'

class Route(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    route_desc = models.TextField()

    #route_stations = models.ManyToManyField(Station, through="RoutePath")


class RoutePath(models.Model):
    pass

class Ride(models.Model):
    """La classe Ride correspond à un trajet pour un véhicule X d'une ligne Y qui emprunte les différents arrêts à des temps déterminés par l'horaire.
    Elle lie donc 'line' avec une timetable"""
    pass

