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

    vehicule_type = models.CharField('type de véhicule',
        max_length=1,
        choices=Vehicule_Type.choices,
        default=Vehicule_Type.BUS
    )

    def __str__(self):
        return self.vehicule_type


class Station(models.Model):
    """La classe Station correspond aux arrêts de bus/tram/n'importe quel moyen de transport public."""
    Station_name = models.CharField("Nom de l\'arrêt",max_length=200)
    Station_adress = models.CharField('Adresse de l\'arret',max_length=300)
    Station_number = models.PositiveIntegerField('Identification (facultatif)',blank=True, null=True)
    Station_desc = models.CharField('Description (ou tag Google Map)',max_length=150, blank=True, null=True)
    Station_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, verbose_name="Type de transport")

    def __str__(self):
        return f'{self.Station_name} ({self.Station_adress})'


class Line(models.Model):
    Line_number = models.PositiveIntegerField('Numéro de la ligne',validators=[MinValueValidator(1), MaxValueValidator(100)])
    Line_name = models.CharField('Nom de la ligne (départ-arrivée)',max_length=200, blank=True, null=True)
    Line_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, verbose_name="Type de transport")
    Line_stations = models.ManyToManyField(Station, through="Route", verbose_name="Arrêts associés")



    def __str__(self):
        return f'Ligne {self.Line_number}'

class Line_station(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    order = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(60)])


class Route(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE, verbose_name="Ligne associée")
    station = models.ForeignKey(Station, on_delete=models.CASCADE, verbose_name="Arrêt associé")
    order = models.IntegerField('Ordre de passage')

    def __str__(self):
        return f'{self.line} - {self.order} - {self.station}'


