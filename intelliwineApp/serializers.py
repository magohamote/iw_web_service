# ModelSerializer classes don't do anything particularly magical,
# they are simply a shortcut for creating serializer classes:
#   - An automatically determined set of fields.
#   - Simple default implementations for the create() and update() methods.
from math import sqrt

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import BottleDNA, TestClass
from .bottleModel.bottle_vector_model import BottleVectorCharacteristics, BottleVectorFlavourAndAroma


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BottleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BottleDNA
        fields = ('clarity', 'colorSimple', 'color', 'observations1', 'condition', 'intensity', 'aromaCharacteristic',
                  'development', 'sweetness', 'acidity', 'tanning', 'alcohol', 'body', 'flavourIntensity',
                  'flavourCharacteristic', 'observations2', 'finish', 'qualityLevel', 'structure', 'balance',
                  'concentration', 'complexity', 'length', 'typicity', 'levelOfReadiness', 'appellation', 'region',
                  'country', 'variety', 'vintage', 'productionMethod', 'climaticInfluences', 'nameOfTheWine',
                  'nameOfTheWinery', 'typeOfSweetness', 'typeOfCarbonDioxide', 'typeOfViscosity', 'typeOfAlcohol',
                  'typeOfAcid', 'typeOfFruit', 'typeOfTannin', 'ripeness', 'freshness', 'harmony')

    @staticmethod
    def cosine_similarity(x, y):
        numerator = sum(a * b for a, b in zip(x, y))
        denominator = sqrt(sum([a * a for a in x])) * sqrt(sum([a * a for a in y]))
        return numerator / float(denominator)


class TestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TestClass
        fields = ('test',)


class BottleVectorCharacSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BottleVectorCharacteristics
        fields = ('intensity1', 'intensity2', 'intensity3', 'intensity4', 'intensity5',
                  'sweetness1', 'sweetness2','sweetness3', 'sweetness4', 'sweetness5', 'sweetness6',
                  'acidity1', 'acidity2', 'acidity3', 'acidity4', 'acidity5',
                  'tannin1', 'tannin2', 'tannin3', 'tannin4', 'tannin5',
                  'alcohol1', 'alcohol2', 'alcohol3', 'alcohol4', 'alcohol5',
                  'body1', 'body2', 'body3', 'body4', 'body5',
                  'flavour_intensity1', 'flavour_intensity2', 'flavour_intensity3', 'flavour_intensity4', 'flavour_intensity5',
                  'finish1', 'finish2', 'finish3', 'finish4', 'finish5',
                  'qualityLevel1', 'qualityLevel2', 'qualityLevel3', 'qualityLevel4', 'qualityLevel5', 'qualityLevel6')


class BottleVectorFlavAromaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BottleVectorFlavourAndAroma
        fields = ('floral_flavour', 'acacia_flavour', 'honeysuckle_flavour', 'chamomile_flavour', 'elderflower_flavour', 'geranium_flavour', 'blossom_flavour', 'rose_flavour', 'violet_flavour', 'iris_flavour', 'neroli_flavour', 'green_fruit_flavour', 'green_apple_flavour', 'red_apple_flavour', 'gooseberry_flavour', 'pear_flavour', 'amylic_flavour', 'custard_apple_flavour', 'quice_flavour', 'grape_flavour', 'citrus_fruit_flavour', 'grapefruit_flavour', 'lemon_flavour', 'lime_flavour', 'juice_flavour', 'zest_flavour', 'orange_peel_flavour', 'lemon_peel_flavour', 'stone_fruit_flavour', 'peach_flavour', 'apricot_flavour', 'nectarine_flavour', 'tropical_fruit_flavour', 'banana_flavour', 'lychee_flavour', 'mango_flavour', 'melon_flavour', 'passion_fruit_flavour', 'pineapple_flavour', 'red_fruit_flavour', 'redcurrant_flavour', 'cranberry_flavour', 'raspberry_flavour', 'strawberry_flavour', 'red_cherry_flavour', 'plum_flavour', 'black_fruit_flavour', 'blackcurrant_flavour', 'blackberry_flavour', 'bramble_flavour', 'blueberry_flavour', 'black_cherry_flavour', 'dried_cooked_fruit_flavour', 'fig_flavour', 'prune_flavour', 'raisin_flavour', 'sultana_flavour', 'kirsch_flavour', 'jamminess_flavour', 'cooked_flavour', 'baked_flavour', 'stewed_fruits_flavour', 'preserved_fruits_flavour', 'under_ripeness_flavour', 'green_bell_pepper_capsicum_flavour', 'under_ripeness_grass_flavour', 'white_pepper_flavour', 'leafiness_flavour', 'tomato_flavour', 'potato_flavour', 'herbaceous_flavour', 'herbaceous_grass_flavour', 'asparagus_flavour', 'blackcurrant_leaf_flavour', 'pyrazine_flavour', 'herbal_flavour', 'eucalyptus_flavour', 'mint_flavour', 'medicinal_flavour', 'lavender_flavour', 'fennel_flavour', 'dill_flavour', 'vegetable_flavour', 'cabbage_flavour', 'peas_flavour', 'beans_flavour', 'black_olive_flavour', 'green_olive_flavour', 'sweet_spice_flavour', 'cinnamon_flavour', 'cloves_flavour', 'ginger_flavour', 'nutmeg_flavour', 'sweet_spice_vanilla_flavour', 'pungent_spice_flavour', 'black_white_pepper_flavour', 'liquorice_flavour', 'juniper_flavour', 'simplicity_neutrality_flavour', 'simple_flavour', 'neutral_flavour', 'indistinct_flavour', 'autolytic_flavour', 'yeast_flavour', 'biscuit_flavour', 'bread_flavour', 'autolytic_toast_flavour', 'pastry_flavour', 'brioche_flavour', 'lees_flavour', 'dairy_mlf_flavour', 'butter_flavour', 'cheese_flavour', 'cream_flavour', 'yoghurt_flavour', 'oak_flavour', 'oak_vanilla_flavour', 'butterscotch_flavour', 'oak_toast_flavour', 'oak_cedar_flavour', 'charred_wood_flavour', 'oak_smoke_flavour', 'acrid_flavour', 'resinous_flavour', 'kernel_flavour', 'almond_flavour', 'marzipan_flavour', 'coconut_flavour', 'hazelnut_flavour', 'walnut_flavour', 'chocolat_flavour', 'coffee_flavour', 'animal_flavour', 'animal_leather_flavour', 'meat_flavour', 'animal_farmyard_flavour', 'maturity_flavour', 'vegetal_flavour', 'mushroom_flavour', 'hay_flavour', 'wet_leaves_flavour', 'forest_floor_flavour', 'game_flavour', 'savoury_flavour', 'tobacco_flavour', 'maturity_cedar_flavour', 'honey_flavour', 'cereal_flavour', 'mineral_flavour', 'mineral_earth_flavour', 'petrol_flavour', 'kerosene_flavour', 'mineral_rubber_flavour', 'tar_flavour', 'mineral_smoke_flavour', 'stony_steely_flavour', 'wet_wool_flavour', 'anisoles_flavour', 'mustiness_flavour', 'wet_cardboard_flavour', 'tca_flavour', 'brettanomyces_flavour', 'brettanomyces_animal_flavour', 'leather_flavour', 'meaty_flavour', 'sticking_plaster_flavour', 'vinyl_flavour', 'farmyard_flavour', 'oxidation_flavour', 'caramel_flavour', 'toffee_flavour', 'staleness_flavour', 'sherry_aromas_flavour', 'aidehydes_flavour', 'volatile_acidity_flavour', 'vinegar_flavour', 'solvents_flavour', 'nail_varnish_remover_flavour', 'lifted_flavour', 'reduction_flavour', 'mercaptans_flavour', 'cabbag_flavour', 'eggs_flavour', 'sweat_flavour', 'reduction_rubber_flavour', 'onion_flavour', 'garlic_flavour', 'blocked_drains_flavour', 'other_flavour', 'beetroot_flavour', 'earth_flavour', 'geosmin_flavour', 'rot_flavour', 'mould_flavour', 'floral_aroma', 'acacia_aroma', 'honeysuckle_aroma', 'chamomile_aroma', 'elderflower_aroma', 'geranium_aroma', 'blossom_aroma', 'rose_aroma', 'violet_aroma', 'iris_aroma', 'neroli_aroma', 'green_fruit_aroma', 'green_apple_aroma', 'red_apple_aroma', 'gooseberry_aroma', 'pear_aroma', 'amylic_aroma', 'custard_apple_aroma', 'quice_aroma', 'grape_aroma', 'citrus_fruit_aroma', 'grapefruit_aroma', 'lemon_aroma', 'lime_aroma', 'juice_aroma', 'zest_aroma', 'orange_peel_aroma', 'lemon_peel_aroma', 'stone_fruit_aroma', 'peach_aroma', 'apricot_aroma', 'nectarine_aroma', 'tropical_fruit_aroma', 'banana_aroma', 'lychee_aroma', 'mango_aroma', 'melon_aroma', 'passion_fruit_aroma', 'pineapple_aroma', 'red_fruit_aroma', 'redcurrant_aroma', 'cranberry_aroma', 'raspberry_aroma', 'strawberry_aroma', 'red_cherry_aroma', 'plum_aroma', 'black_fruit_aroma', 'blackcurrant_aroma', 'blackberry_aroma', 'bramble_aroma', 'blueberry_aroma', 'black_cherry_aroma', 'dried_cooked_fruit_aroma', 'fig_aroma', 'prune_aroma', 'raisin_aroma', 'sultana_aroma', 'kirsch_aroma', 'jamminess_aroma', 'cooked_aroma', 'baked_aroma', 'stewed_fruits_aroma', 'preserved_fruits_aroma', 'under_ripeness_aroma', 'green_bell_pepper_capsicum_aroma', 'under_ripeness_grass_aroma', 'white_pepper_aroma', 'leafiness_aroma', 'tomato_aroma', 'potato_aroma', 'herbaceous_aroma', 'herbaceous_grass_aroma', 'asparagus_aroma', 'blackcurrant_leaf_aroma', 'pyrazine_aroma', 'herbal_aroma', 'eucalyptus_aroma', 'mint_aroma', 'medicinal_aroma', 'lavender_aroma', 'fennel_aroma', 'dill_aroma', 'vegetable_aroma', 'cabbage_aroma', 'peas_aroma', 'beans_aroma', 'black_olive_aroma', 'green_olive_aroma', 'sweet_spice_aroma', 'cinnamon_aroma', 'cloves_aroma', 'ginger_aroma', 'nutmeg_aroma', 'sweet_spice_vanilla_aroma', 'pungent_spice_aroma', 'black_white_pepper_aroma', 'liquorice_aroma', 'juniper_aroma', 'simplicity_neutrality_aroma', 'simple_aroma', 'neutral_aroma', 'indistinct_aroma', 'autolytic_aroma', 'yeast_aroma', 'biscuit_aroma', 'bread_aroma', 'autolytic_toast_aroma', 'pastry_aroma', 'brioche_aroma', 'lees_aroma', 'dairy_mlf_aroma', 'butter_aroma', 'cheese_aroma', 'cream_aroma', 'yoghurt_aroma', 'oak_aroma', 'oak_vanilla_aroma', 'butterscotch_aroma', 'oak_toast_aroma', 'oak_cedar_aroma', 'charred_wood_aroma', 'oak_smoke_aroma', 'acrid_aroma', 'resinous_aroma', 'kernel_aroma', 'almond_aroma', 'marzipan_aroma', 'coconut_aroma', 'hazelnut_aroma', 'walnut_aroma', 'chocolat_aroma', 'coffee_aroma', 'animal_aroma', 'animal_leather_aroma', 'meat_aroma', 'animal_farmyard_aroma', 'maturity_aroma', 'vegetal_aroma', 'mushroom_aroma', 'hay_aroma', 'wet_leaves_aroma', 'forest_floor_aroma', 'game_aroma', 'savoury_aroma', 'tobacco_aroma', 'maturity_cedar_aroma', 'honey_aroma', 'cereal_aroma', 'mineral_aroma', 'mineral_earth_aroma', 'petrol_aroma', 'kerosene_aroma', 'mineral_rubber_aroma', 'tar_aroma', 'mineral_smoke_aroma', 'stony_steely_aroma', 'wet_wool_aroma', 'anisoles_aroma', 'mustiness_aroma', 'wet_cardboard_aroma', 'tca_aroma', 'brettanomyces_aroma', 'brettanomyces_animal_aroma', 'leather_aroma', 'meaty_aroma', 'sticking_plaster_aroma', 'vinyl_aroma', 'farmyard_aroma', 'oxidation_aroma', 'caramel_aroma', 'toffee_aroma', 'staleness_aroma', 'sherry_aromas_aroma', 'aidehydes_aroma', 'volatile_acidity_aroma', 'vinegar_aroma', 'solvents_aroma', 'nail_varnish_remover_aroma', 'lifted_aroma', 'reduction_aroma', 'mercaptans_aroma', 'cabbag_aroma', 'eggs_aroma', 'sweat_aroma', 'reduction_rubber_aroma', 'onion_aroma', 'garlic_aroma', 'blocked_drains_aroma', 'other_aroma', 'beetroot_aroma', 'earth_aroma', 'geosmin_aroma', 'rot_aroma', 'mould_aroma')
