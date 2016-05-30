# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-30 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intelliwineApp', '0005_bottlevector_testclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottleVectorCharacteristics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity1', models.IntegerField()),
                ('intensity2', models.IntegerField()),
                ('intensity3', models.IntegerField()),
                ('intensity4', models.IntegerField()),
                ('intensity5', models.IntegerField()),
                ('sweetness1', models.IntegerField()),
                ('sweetness2', models.IntegerField()),
                ('sweetness3', models.IntegerField()),
                ('sweetness4', models.IntegerField()),
                ('sweetness5', models.IntegerField()),
                ('sweetness6', models.IntegerField()),
                ('acidity1', models.IntegerField()),
                ('acidity2', models.IntegerField()),
                ('acidity3', models.IntegerField()),
                ('acidity4', models.IntegerField()),
                ('acidity5', models.IntegerField()),
                ('tannin1', models.IntegerField()),
                ('tannin2', models.IntegerField()),
                ('tannin3', models.IntegerField()),
                ('tannin4', models.IntegerField()),
                ('tannin5', models.IntegerField()),
                ('alcohol1', models.IntegerField()),
                ('alcohol2', models.IntegerField()),
                ('alcohol3', models.IntegerField()),
                ('alcohol4', models.IntegerField()),
                ('alcohol5', models.IntegerField()),
                ('body1', models.IntegerField()),
                ('body2', models.IntegerField()),
                ('body3', models.IntegerField()),
                ('body4', models.IntegerField()),
                ('body5', models.IntegerField()),
                ('flavour_intensity1', models.IntegerField()),
                ('flavour_intensity2', models.IntegerField()),
                ('flavour_intensity3', models.IntegerField()),
                ('flavour_intensity4', models.IntegerField()),
                ('flavour_intensity5', models.IntegerField()),
                ('finish1', models.IntegerField()),
                ('finish2', models.IntegerField()),
                ('finish3', models.IntegerField()),
                ('finish4', models.IntegerField()),
                ('finish5', models.IntegerField()),
                ('qualityLevel1', models.IntegerField()),
                ('qualityLevel2', models.IntegerField()),
                ('qualityLevel3', models.IntegerField()),
                ('qualityLevel4', models.IntegerField()),
                ('qualityLevel5', models.IntegerField()),
                ('qualityLevel6', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BottleVectorFlavourAndAroma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floral_flavour', models.IntegerField()),
                ('acacia_flavour', models.IntegerField()),
                ('honeysuckle_flavour', models.IntegerField()),
                ('chamomile_flavour', models.IntegerField()),
                ('elderflower_flavour', models.IntegerField()),
                ('geranium_flavour', models.IntegerField()),
                ('blossom_flavour', models.IntegerField()),
                ('rose_flavour', models.IntegerField()),
                ('violet_flavour', models.IntegerField()),
                ('iris_flavour', models.IntegerField()),
                ('neroli_flavour', models.IntegerField()),
                ('green_fruit_flavour', models.IntegerField()),
                ('green_apple_flavour', models.IntegerField()),
                ('red_apple_flavour', models.IntegerField()),
                ('gooseberry_flavour', models.IntegerField()),
                ('pear_flavour', models.IntegerField()),
                ('amylic_flavour', models.IntegerField()),
                ('custard_apple_flavour', models.IntegerField()),
                ('quice_flavour', models.IntegerField()),
                ('grape_flavour', models.IntegerField()),
                ('citrus_fruit_flavour', models.IntegerField()),
                ('grapefruit_flavour', models.IntegerField()),
                ('lemon_flavour', models.IntegerField()),
                ('lime_flavour', models.IntegerField()),
                ('juice_flavour', models.IntegerField()),
                ('zest_flavour', models.IntegerField()),
                ('orange_peel_flavour', models.IntegerField()),
                ('lemon_peel_flavour', models.IntegerField()),
                ('stone_fruit_flavour', models.IntegerField()),
                ('peach_flavour', models.IntegerField()),
                ('apricot_flavour', models.IntegerField()),
                ('nectarine_flavour', models.IntegerField()),
                ('tropical_fruit_flavour', models.IntegerField()),
                ('banana_flavour', models.IntegerField()),
                ('lychee_flavour', models.IntegerField()),
                ('mango_flavour', models.IntegerField()),
                ('melon_flavour', models.IntegerField()),
                ('passion_fruit_flavour', models.IntegerField()),
                ('pineapple_flavour', models.IntegerField()),
                ('red_fruit_flavour', models.IntegerField()),
                ('redcurrant_flavour', models.IntegerField()),
                ('cranberry_flavour', models.IntegerField()),
                ('raspberry_flavour', models.IntegerField()),
                ('strawberry_flavour', models.IntegerField()),
                ('red_cherry_flavour', models.IntegerField()),
                ('plum_flavour', models.IntegerField()),
                ('black_fruit_flavour', models.IntegerField()),
                ('blackcurrant_flavour', models.IntegerField()),
                ('blackberry_flavour', models.IntegerField()),
                ('bramble_flavour', models.IntegerField()),
                ('blueberry_flavour', models.IntegerField()),
                ('black_cherry_flavour', models.IntegerField()),
                ('dried_cooked_fruit_flavour', models.IntegerField()),
                ('fig_flavour', models.IntegerField()),
                ('prune_flavour', models.IntegerField()),
                ('raisin_flavour', models.IntegerField()),
                ('sultana_flavour', models.IntegerField()),
                ('kirsch_flavour', models.IntegerField()),
                ('jamminess_flavour', models.IntegerField()),
                ('cooked_flavour', models.IntegerField()),
                ('baked_flavour', models.IntegerField()),
                ('stewed_fruits_flavour', models.IntegerField()),
                ('preserved_fruits_flavour', models.IntegerField()),
                ('under_ripeness_flavour', models.IntegerField()),
                ('green_bell_pepper_capsicum_flavour', models.IntegerField()),
                ('under_ripeness_grass_flavour', models.IntegerField()),
                ('white_pepper_flavour', models.IntegerField()),
                ('leafiness_flavour', models.IntegerField()),
                ('tomato_flavour', models.IntegerField()),
                ('potato_flavour', models.IntegerField()),
                ('herbaceous_flavour', models.IntegerField()),
                ('herbaceous_grass_flavour', models.IntegerField()),
                ('asparagus_flavour', models.IntegerField()),
                ('blackcurrant_leaf_flavour', models.IntegerField()),
                ('pyrazine_flavour', models.IntegerField()),
                ('herbal_flavour', models.IntegerField()),
                ('eucalyptus_flavour', models.IntegerField()),
                ('mint_flavour', models.IntegerField()),
                ('medicinal_flavour', models.IntegerField()),
                ('lavender_flavour', models.IntegerField()),
                ('fennel_flavour', models.IntegerField()),
                ('dill_flavour', models.IntegerField()),
                ('vegetable_flavour', models.IntegerField()),
                ('cabbage_flavour', models.IntegerField()),
                ('peas_flavour', models.IntegerField()),
                ('beans_flavour', models.IntegerField()),
                ('black_olive_flavour', models.IntegerField()),
                ('green_olive_flavour', models.IntegerField()),
                ('sweet_spice_flavour', models.IntegerField()),
                ('cinnamon_flavour', models.IntegerField()),
                ('cloves_flavour', models.IntegerField()),
                ('ginger_flavour', models.IntegerField()),
                ('nutmeg_flavour', models.IntegerField()),
                ('sweet_spice_vanilla_flavour', models.IntegerField()),
                ('pungent_spice_flavour', models.IntegerField()),
                ('black_white_pepper_flavour', models.IntegerField()),
                ('liquorice_flavour', models.IntegerField()),
                ('juniper_flavour', models.IntegerField()),
                ('simplicity_neutrality_flavour', models.IntegerField()),
                ('simple_flavour', models.IntegerField()),
                ('neutral_flavour', models.IntegerField()),
                ('indistinct_flavour', models.IntegerField()),
                ('autolytic_flavour', models.IntegerField()),
                ('yeast_flavour', models.IntegerField()),
                ('biscuit_flavour', models.IntegerField()),
                ('bread_flavour', models.IntegerField()),
                ('autolytic_toast_flavour', models.IntegerField()),
                ('pastry_flavour', models.IntegerField()),
                ('brioche_flavour', models.IntegerField()),
                ('lees_flavour', models.IntegerField()),
                ('dairy_mlf_flavour', models.IntegerField()),
                ('butter_flavour', models.IntegerField()),
                ('cheese_flavour', models.IntegerField()),
                ('cream_flavour', models.IntegerField()),
                ('yoghurt_flavour', models.IntegerField()),
                ('oak_flavour', models.IntegerField()),
                ('oak_vanilla_flavour', models.IntegerField()),
                ('butterscotch_flavour', models.IntegerField()),
                ('oak_toast_flavour', models.IntegerField()),
                ('oak_cedar_flavour', models.IntegerField()),
                ('charred_wood_flavour', models.IntegerField()),
                ('oak_smoke_flavour', models.IntegerField()),
                ('acrid_flavour', models.IntegerField()),
                ('resinous_flavour', models.IntegerField()),
                ('kernel_flavour', models.IntegerField()),
                ('almond_flavour', models.IntegerField()),
                ('marzipan_flavour', models.IntegerField()),
                ('coconut_flavour', models.IntegerField()),
                ('hazelnut_flavour', models.IntegerField()),
                ('walnut_flavour', models.IntegerField()),
                ('chocolat_flavour', models.IntegerField()),
                ('coffee_flavour', models.IntegerField()),
                ('animal_flavour', models.IntegerField()),
                ('animal_leather_flavour', models.IntegerField()),
                ('meat_flavour', models.IntegerField()),
                ('animal_farmyard_flavour', models.IntegerField()),
                ('maturity_flavour', models.IntegerField()),
                ('vegetal_flavour', models.IntegerField()),
                ('mushroom_flavour', models.IntegerField()),
                ('hay_flavour', models.IntegerField()),
                ('wet_leaves_flavour', models.IntegerField()),
                ('forest_floor_flavour', models.IntegerField()),
                ('game_flavour', models.IntegerField()),
                ('savoury_flavour', models.IntegerField()),
                ('tobacco_flavour', models.IntegerField()),
                ('maturity_cedar_flavour', models.IntegerField()),
                ('honey_flavour', models.IntegerField()),
                ('cereal_flavour', models.IntegerField()),
                ('mineral_flavour', models.IntegerField()),
                ('mineral_earth_flavour', models.IntegerField()),
                ('petrol_flavour', models.IntegerField()),
                ('kerosene_flavour', models.IntegerField()),
                ('mineral_rubber_flavour', models.IntegerField()),
                ('tar_flavour', models.IntegerField()),
                ('mineral_smoke_flavour', models.IntegerField()),
                ('stony_steely_flavour', models.IntegerField()),
                ('wet_wool_flavour', models.IntegerField()),
                ('anisoles_flavour', models.IntegerField()),
                ('mustiness_flavour', models.IntegerField()),
                ('wet_cardboard_flavour', models.IntegerField()),
                ('tca_flavour', models.IntegerField()),
                ('brettanomyces_flavour', models.IntegerField()),
                ('brettanomyces_animal_flavour', models.IntegerField()),
                ('leather_flavour', models.IntegerField()),
                ('meaty_flavour', models.IntegerField()),
                ('sticking_plaster_flavour', models.IntegerField()),
                ('vinyl_flavour', models.IntegerField()),
                ('farmyard_flavour', models.IntegerField()),
                ('oxidation_flavour', models.IntegerField()),
                ('caramel_flavour', models.IntegerField()),
                ('toffee_flavour', models.IntegerField()),
                ('staleness_flavour', models.IntegerField()),
                ('sherry_aromas_flavour', models.IntegerField()),
                ('aidehydes_flavour', models.IntegerField()),
                ('volatile_acidity_flavour', models.IntegerField()),
                ('vinegar_flavour', models.IntegerField()),
                ('solvents_flavour', models.IntegerField()),
                ('nail_varnish_remover_flavour', models.IntegerField()),
                ('lifted_flavour', models.IntegerField()),
                ('reduction_flavour', models.IntegerField()),
                ('mercaptans_flavour', models.IntegerField()),
                ('cabbag_flavour', models.IntegerField()),
                ('eggs_flavour', models.IntegerField()),
                ('sweat_flavour', models.IntegerField()),
                ('reduction_rubber_flavour', models.IntegerField()),
                ('onion_flavour', models.IntegerField()),
                ('garlic_flavour', models.IntegerField()),
                ('blocked_drains_flavour', models.IntegerField()),
                ('other_flavour', models.IntegerField()),
                ('beetroot_flavour', models.IntegerField()),
                ('earth_flavour', models.IntegerField()),
                ('geosmin_flavour', models.IntegerField()),
                ('rot_flavour', models.IntegerField()),
                ('mould_flavour', models.IntegerField()),
                ('floral_aroma', models.IntegerField()),
                ('acacia_aroma', models.IntegerField()),
                ('honeysuckle_aroma', models.IntegerField()),
                ('chamomile_aroma', models.IntegerField()),
                ('elderflower_aroma', models.IntegerField()),
                ('geranium_aroma', models.IntegerField()),
                ('blossom_aroma', models.IntegerField()),
                ('rose_aroma', models.IntegerField()),
                ('violet_aroma', models.IntegerField()),
                ('iris_aroma', models.IntegerField()),
                ('neroli_aroma', models.IntegerField()),
                ('green_fruit_aroma', models.IntegerField()),
                ('green_apple_aroma', models.IntegerField()),
                ('red_apple_aroma', models.IntegerField()),
                ('gooseberry_aroma', models.IntegerField()),
                ('pear_aroma', models.IntegerField()),
                ('amylic_aroma', models.IntegerField()),
                ('custard_apple_aroma', models.IntegerField()),
                ('quice_aroma', models.IntegerField()),
                ('grape_aroma', models.IntegerField()),
                ('citrus_fruit_aroma', models.IntegerField()),
                ('grapefruit_aroma', models.IntegerField()),
                ('lemon_aroma', models.IntegerField()),
                ('lime_aroma', models.IntegerField()),
                ('juice_aroma', models.IntegerField()),
                ('zest_aroma', models.IntegerField()),
                ('orange_peel_aroma', models.IntegerField()),
                ('lemon_peel_aroma', models.IntegerField()),
                ('stone_fruit_aroma', models.IntegerField()),
                ('peach_aroma', models.IntegerField()),
                ('apricot_aroma', models.IntegerField()),
                ('nectarine_aroma', models.IntegerField()),
                ('tropical_fruit_aroma', models.IntegerField()),
                ('banana_aroma', models.IntegerField()),
                ('lychee_aroma', models.IntegerField()),
                ('mango_aroma', models.IntegerField()),
                ('melon_aroma', models.IntegerField()),
                ('passion_fruit_aroma', models.IntegerField()),
                ('pineapple_aroma', models.IntegerField()),
                ('red_fruit_aroma', models.IntegerField()),
                ('redcurrant_aroma', models.IntegerField()),
                ('cranberry_aroma', models.IntegerField()),
                ('raspberry_aroma', models.IntegerField()),
                ('strawberry_aroma', models.IntegerField()),
                ('red_cherry_aroma', models.IntegerField()),
                ('plum_aroma', models.IntegerField()),
                ('black_fruit_aroma', models.IntegerField()),
                ('blackcurrant_aroma', models.IntegerField()),
                ('blackberry_aroma', models.IntegerField()),
                ('bramble_aroma', models.IntegerField()),
                ('blueberry_aroma', models.IntegerField()),
                ('black_cherry_aroma', models.IntegerField()),
                ('dried_cooked_fruit_aroma', models.IntegerField()),
                ('fig_aroma', models.IntegerField()),
                ('prune_aroma', models.IntegerField()),
                ('raisin_aroma', models.IntegerField()),
                ('sultana_aroma', models.IntegerField()),
                ('kirsch_aroma', models.IntegerField()),
                ('jamminess_aroma', models.IntegerField()),
                ('cooked_aroma', models.IntegerField()),
                ('baked_aroma', models.IntegerField()),
                ('stewed_fruits_aroma', models.IntegerField()),
                ('preserved_fruits_aroma', models.IntegerField()),
                ('under_ripeness_aroma', models.IntegerField()),
                ('green_bell_pepper_capsicum_aroma', models.IntegerField()),
                ('under_ripeness_grass_aroma', models.IntegerField()),
                ('white_pepper_aroma', models.IntegerField()),
                ('leafiness_aroma', models.IntegerField()),
                ('tomato_aroma', models.IntegerField()),
                ('potato_aroma', models.IntegerField()),
                ('herbaceous_aroma', models.IntegerField()),
                ('herbaceous_grass_aroma', models.IntegerField()),
                ('asparagus_aroma', models.IntegerField()),
                ('blackcurrant_leaf_aroma', models.IntegerField()),
                ('pyrazine_aroma', models.IntegerField()),
                ('herbal_aroma', models.IntegerField()),
                ('eucalyptus_aroma', models.IntegerField()),
                ('mint_aroma', models.IntegerField()),
                ('medicinal_aroma', models.IntegerField()),
                ('lavender_aroma', models.IntegerField()),
                ('fennel_aroma', models.IntegerField()),
                ('dill_aroma', models.IntegerField()),
                ('vegetable_aroma', models.IntegerField()),
                ('cabbage_aroma', models.IntegerField()),
                ('peas_aroma', models.IntegerField()),
                ('beans_aroma', models.IntegerField()),
                ('black_olive_aroma', models.IntegerField()),
                ('green_olive_aroma', models.IntegerField()),
                ('sweet_spice_aroma', models.IntegerField()),
                ('cinnamon_aroma', models.IntegerField()),
                ('cloves_aroma', models.IntegerField()),
                ('ginger_aroma', models.IntegerField()),
                ('nutmeg_aroma', models.IntegerField()),
                ('sweet_spice_vanilla_aroma', models.IntegerField()),
                ('pungent_spice_aroma', models.IntegerField()),
                ('black_white_pepper_aroma', models.IntegerField()),
                ('liquorice_aroma', models.IntegerField()),
                ('juniper_aroma', models.IntegerField()),
                ('simplicity_neutrality_aroma', models.IntegerField()),
                ('simple_aroma', models.IntegerField()),
                ('neutral_aroma', models.IntegerField()),
                ('indistinct_aroma', models.IntegerField()),
                ('autolytic_aroma', models.IntegerField()),
                ('yeast_aroma', models.IntegerField()),
                ('biscuit_aroma', models.IntegerField()),
                ('bread_aroma', models.IntegerField()),
                ('autolytic_toast_aroma', models.IntegerField()),
                ('pastry_aroma', models.IntegerField()),
                ('brioche_aroma', models.IntegerField()),
                ('lees_aroma', models.IntegerField()),
                ('dairy_mlf_aroma', models.IntegerField()),
                ('butter_aroma', models.IntegerField()),
                ('cheese_aroma', models.IntegerField()),
                ('cream_aroma', models.IntegerField()),
                ('yoghurt_aroma', models.IntegerField()),
                ('oak_aroma', models.IntegerField()),
                ('oak_vanilla_aroma', models.IntegerField()),
                ('butterscotch_aroma', models.IntegerField()),
                ('oak_toast_aroma', models.IntegerField()),
                ('oak_cedar_aroma', models.IntegerField()),
                ('charred_wood_aroma', models.IntegerField()),
                ('oak_smoke_aroma', models.IntegerField()),
                ('acrid_aroma', models.IntegerField()),
                ('resinous_aroma', models.IntegerField()),
                ('kernel_aroma', models.IntegerField()),
                ('almond_aroma', models.IntegerField()),
                ('marzipan_aroma', models.IntegerField()),
                ('coconut_aroma', models.IntegerField()),
                ('hazelnut_aroma', models.IntegerField()),
                ('walnut_aroma', models.IntegerField()),
                ('chocolat_aroma', models.IntegerField()),
                ('coffee_aroma', models.IntegerField()),
                ('animal_aroma', models.IntegerField()),
                ('animal_leather_aroma', models.IntegerField()),
                ('meat_aroma', models.IntegerField()),
                ('animal_farmyard_aroma', models.IntegerField()),
                ('maturity_aroma', models.IntegerField()),
                ('vegetal_aroma', models.IntegerField()),
                ('mushroom_aroma', models.IntegerField()),
                ('hay_aroma', models.IntegerField()),
                ('wet_leaves_aroma', models.IntegerField()),
                ('forest_floor_aroma', models.IntegerField()),
                ('game_aroma', models.IntegerField()),
                ('savoury_aroma', models.IntegerField()),
                ('tobacco_aroma', models.IntegerField()),
                ('maturity_cedar_aroma', models.IntegerField()),
                ('honey_aroma', models.IntegerField()),
                ('cereal_aroma', models.IntegerField()),
                ('mineral_aroma', models.IntegerField()),
                ('mineral_earth_aroma', models.IntegerField()),
                ('petrol_aroma', models.IntegerField()),
                ('kerosene_aroma', models.IntegerField()),
                ('mineral_rubber_aroma', models.IntegerField()),
                ('tar_aroma', models.IntegerField()),
                ('mineral_smoke_aroma', models.IntegerField()),
                ('stony_steely_aroma', models.IntegerField()),
                ('wet_wool_aroma', models.IntegerField()),
                ('anisoles_aroma', models.IntegerField()),
                ('mustiness_aroma', models.IntegerField()),
                ('wet_cardboard_aroma', models.IntegerField()),
                ('tca_aroma', models.IntegerField()),
                ('brettanomyces_aroma', models.IntegerField()),
                ('brettanomyces_animal_aroma', models.IntegerField()),
                ('leather_aroma', models.IntegerField()),
                ('meaty_aroma', models.IntegerField()),
                ('sticking_plaster_aroma', models.IntegerField()),
                ('vinyl_aroma', models.IntegerField()),
                ('farmyard_aroma', models.IntegerField()),
                ('oxidation_aroma', models.IntegerField()),
                ('caramel_aroma', models.IntegerField()),
                ('toffee_aroma', models.IntegerField()),
                ('staleness_aroma', models.IntegerField()),
                ('sherry_aromas_aroma', models.IntegerField()),
                ('aidehydes_aroma', models.IntegerField()),
                ('volatile_acidity_aroma', models.IntegerField()),
                ('vinegar_aroma', models.IntegerField()),
                ('solvents_aroma', models.IntegerField()),
                ('nail_varnish_remover_aroma', models.IntegerField()),
                ('lifted_aroma', models.IntegerField()),
                ('reduction_aroma', models.IntegerField()),
                ('mercaptans_aroma', models.IntegerField()),
                ('cabbag_aroma', models.IntegerField()),
                ('eggs_aroma', models.IntegerField()),
                ('sweat_aroma', models.IntegerField()),
                ('reduction_rubber_aroma', models.IntegerField()),
                ('onion_aroma', models.IntegerField()),
                ('garlic_aroma', models.IntegerField()),
                ('blocked_drains_aroma', models.IntegerField()),
                ('other_aroma', models.IntegerField()),
                ('beetroot_aroma', models.IntegerField()),
                ('earth_aroma', models.IntegerField()),
                ('geosmin_aroma', models.IntegerField()),
                ('rot_aroma', models.IntegerField()),
                ('mould_aroma', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='BottleVector',
        ),
    ]
