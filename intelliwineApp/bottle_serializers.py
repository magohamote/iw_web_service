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
        fields = ('id', 'bottle_foreign_id', 'bottle_foreign_key', 'floral_flavour', 'green_fruit_flavour', 'citrus_fruit_flavour', 'stone_fruit_flavour', 'tropical_fruit_flavour', 'red_fruit_flavour', 'black_fruit_flavour', 'dried_cooked_fruit_flavour', 'under_ripeness_flavour', 'herbaceous_flavour', 'herbal_flavour', 'vegetable_flavour', 'sweet_spice_flavour', 'pungent_spice_flavour', 'simplicity_neutrality_flavour', 'autolytic_flavour', 'dairy_mlf_flavour', 'oak_flavour', 'kernel_flavour', 'animal_flavour', 'maturity_flavour', 'mineral_flavour', 'anisoles_flavour', 'brettanomyces_flavour', 'oxidation_flavour', 'volatile_acidity_flavour', 'reduction_flavour', 'other_flavour', 'floral_aroma', 'green_fruit_aroma', 'citrus_fruit_aroma', 'stone_fruit_aroma', 'tropical_fruit_aroma', 'red_fruit_aroma', 'black_fruit_aroma', 'dried_cooked_fruit_aroma', 'under_ripeness_aroma', 'herbaceous_aroma', 'herbal_aroma', 'vegetable_aroma', 'sweet_spice_aroma', 'pungent_spice_aroma', 'simplicity_neutrality_aroma', 'autolytic_aroma', 'dairy_mlf_aroma', 'oak_aroma', 'kernel_aroma', 'animal_aroma', 'maturity_aroma', 'mineral_aroma', 'anisoles_aroma', 'brettanomyces_aroma', 'oxidation_aroma', 'volatile_acidity_aroma', 'reduction_aroma', 'other_aroma')
