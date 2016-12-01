# ModelSerializer classes don't do anything particularly magical,
# they are simply a shortcut for creating serializer classes:
#   - An automatically determined set of fields.
#   - Simple default implementations for the create() and update() methods.

from rest_framework import serializers

from intelliwineApp.bottle_vector_model import BottleVectorCharacteristics, BottleVectorFlavourAndAroma, Bottle
from .bottle_dna_model import BottleDNA


class BottleDNASerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BottleDNA
        fields = ('clarity', 'colorSimple', 'color', 'observations1', 'condition', 'intensity', 'aromaCharacteristic',
                  'development', 'sweetness', 'acidity', 'tanning', 'alcohol', 'body', 'flavourIntensity',
                  'flavourCharacteristic', 'observations2', 'finish', 'quality_level', 'structure', 'balance',
                  'concentration', 'complexity', 'length', 'typicity', 'levelOfReadiness', 'appellation', 'region',
                  'country', 'variety', 'vintage', 'productionMethod', 'climaticInfluences', 'nameOfTheWine',
                  'nameOfTheWinery', 'typeOfSweetness', 'typeOfCarbonDioxide', 'typeOfViscosity', 'typeOfAlcohol',
                  'typeOfAcid', 'typeOfFruit', 'typeOfTannin', 'ripeness', 'freshness', 'harmony')


class BottleSerializer(serializers.HyperlinkedModelSerializer):
    charac = serializers.StringRelatedField(many=False)
    flav_aroma = serializers.StringRelatedField(many=False)

    class Meta:
        model = Bottle
        fields = ('id', 'bottle_name', 'charac', 'flav_aroma')


class BottleVectorCharacSerializer(serializers.HyperlinkedModelSerializer):
    bottle_foreign_key = serializers.StringRelatedField(many=False)

    class Meta:
        model = BottleVectorCharacteristics
        fields = ('id', 'bottle_foreign_id', 'bottle_foreign_key', 'intensity', 'sweetness', 'acidity', 'tannin', 'alcohol', 'body', 'flavour_intensity', 'finish', 'quality_level')


class BottleVectorFlavAromaSerializer(serializers.HyperlinkedModelSerializer):
    bottle_foreign_key = serializers.StringRelatedField(many=False)

    class Meta:
        model = BottleVectorFlavourAndAroma
        fields = (
            'id', 'bottle_foreign_id', 'bottle_foreign_key', 'floral', 'green_fruit', 'citrus_fruit', 'stone_fruit',
            'tropical_fruit', 'red_fruit', 'black_fruit', 'dried_cooked_fruit', 'under_ripeness', 'herbaceous',
            'herbal', 'vegetable', 'sweet_spice', 'pungent_spice', 'simplicity_neutrality', 'autolytic', 'dairy_mlf',
            'oak', 'kernel', 'animal', 'maturity', 'mineral', 'anisoles', 'brettanomyces', 'oxidation',
            'volatile_acidity', 'reduction', 'other')
