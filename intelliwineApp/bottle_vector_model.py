from django.db import models


class Bottle(models.Model):
    bottle_name = models.CharField(max_length=256)


class BottleVectorCharacteristics(models.Model):
    bottle_foreign_key = models.ForeignKey(Bottle, related_name='charac', default=0)
    bottle_foreign_id = models.IntegerField(default=0)
    intensity = models.IntegerField()
    sweetness = models.IntegerField()
    acidity = models.IntegerField()
    tannin = models.IntegerField()
    alcohol = models.IntegerField()
    body = models.IntegerField()
    flavour_intensity = models.IntegerField()
    finish = models.IntegerField()
    quality_level = models.IntegerField()


class BottleVectorFlavourAndAroma(models.Model):
    bottle_foreign_key = models.ForeignKey(Bottle, related_name='flav_aroma', default=0)
    bottle_foreign_id = models.IntegerField(default=0)
    # flavour list
    floral = models.IntegerField()
    # acacia = models.IntegerField()
    # honeysuckle = models.IntegerField()
    # chamomile = models.IntegerField()
    # elderflower = models.IntegerField()
    # geranium = models.IntegerField()
    # blossom = models.IntegerField()
    # rose = models.IntegerField()
    # violet = models.IntegerField()
    # iris = models.IntegerField()
    # neroli = models.IntegerField()
    green_fruit = models.IntegerField()
    # green_apple = models.IntegerField()
    # red_apple = models.IntegerField()
    # gooseberry = models.IntegerField()
    # pear = models.IntegerField()
    # amylic = models.IntegerField()
    # custard_apple = models.IntegerField()
    # quice = models.IntegerField()
    # grape = models.IntegerField()
    citrus_fruit = models.IntegerField()
    # grapefruit = models.IntegerField()
    # lemon = models.IntegerField()
    # lime = models.IntegerField()
    # juice = models.IntegerField()
    # zest = models.IntegerField()
    # orange_peel = models.IntegerField()
    # lemon_peel = models.IntegerField()
    stone_fruit = models.IntegerField()
    # peach = models.IntegerField()
    # apricot = models.IntegerField()
    # nectarine = models.IntegerField()
    tropical_fruit = models.IntegerField()
    # banana = models.IntegerField()
    # lychee = models.IntegerField()
    # mango = models.IntegerField()
    # melon = models.IntegerField()
    # passion_fruit = models.IntegerField()
    # pineapple = models.IntegerField()
    red_fruit = models.IntegerField()
    # redcurrant = models.IntegerField()
    # cranberry = models.IntegerField()
    # raspberry = models.IntegerField()
    # strawberry = models.IntegerField()
    # red_cherry = models.IntegerField()
    # plum = models.IntegerField()
    black_fruit = models.IntegerField()
    # blackcurrant = models.IntegerField()
    # blackberry = models.IntegerField()
    # bramble = models.IntegerField()
    # blueberry = models.IntegerField()
    # black_cherry = models.IntegerField()
    dried_cooked_fruit = models.IntegerField()
    # fig = models.IntegerField()
    # prune = models.IntegerField()
    # raisin = models.IntegerField()
    # sultana = models.IntegerField()
    # kirsch = models.IntegerField()
    # jamminess = models.IntegerField()
    # cooked = models.IntegerField()
    # baked = models.IntegerField()
    # stewed_fruits = models.IntegerField()
    # preserved_fruits = models.IntegerField()
    under_ripeness = models.IntegerField()
    # green_bell_pepper_capsicum = models.IntegerField()
    # under_ripeness_grass = models.IntegerField()
    # white_pepper = models.IntegerField()
    # leafiness = models.IntegerField()
    # tomato = models.IntegerField()
    # potato = models.IntegerField()
    herbaceous = models.IntegerField()
    # herbaceous_grass = models.IntegerField()
    # asparagus = models.IntegerField()
    # blackcurrant_leaf = models.IntegerField()
    # pyrazine = models.IntegerField()
    herbal = models.IntegerField()
    # eucalyptus = models.IntegerField()
    # mint = models.IntegerField()
    # medicinal = models.IntegerField()
    # lavender = models.IntegerField()
    # fennel = models.IntegerField()
    # dill = models.IntegerField()
    vegetable = models.IntegerField()
    # cabbage = models.IntegerField()
    # peas = models.IntegerField()
    # beans = models.IntegerField()
    # black_olive = models.IntegerField()
    # green_olive = models.IntegerField()
    sweet_spice = models.IntegerField()
    # cinnamon = models.IntegerField()
    # cloves = models.IntegerField()
    # ginger = models.IntegerField()
    # nutmeg = models.IntegerField()
    # sweet_spice_vanilla = models.IntegerField()
    pungent_spice = models.IntegerField()
    # black_white_pepper = models.IntegerField()
    # liquorice = models.IntegerField()
    # juniper = models.IntegerField()
    simplicity_neutrality = models.IntegerField()
    # simple = models.IntegerField()
    # neutral = models.IntegerField()
    # indistinct = models.IntegerField()
    autolytic = models.IntegerField()
    # yeast = models.IntegerField()
    # biscuit = models.IntegerField()
    # bread = models.IntegerField()
    # autolytic_toast = models.IntegerField()
    # pastry = models.IntegerField()
    # brioche = models.IntegerField()
    # lees = models.IntegerField()
    dairy_mlf = models.IntegerField()
    # butter = models.IntegerField()
    # cheese = models.IntegerField()
    # cream = models.IntegerField()
    # yoghurt = models.IntegerField()
    oak = models.IntegerField()
    # oak_vanilla = models.IntegerField()
    # butterscotch = models.IntegerField()
    # oak_toast = models.IntegerField()
    # oak_cedar = models.IntegerField()
    # charred_wood = models.IntegerField()
    # oak_smoke = models.IntegerField()
    # acrid = models.IntegerField()
    # resinous = models.IntegerField()
    kernel = models.IntegerField()
    # almond = models.IntegerField()
    # marzipan = models.IntegerField()
    # coconut = models.IntegerField()
    # hazelnut = models.IntegerField()
    # walnut = models.IntegerField()
    # chocolat = models.IntegerField()
    # coffee = models.IntegerField()
    animal = models.IntegerField()
    # animal_leather = models.IntegerField()
    # meat = models.IntegerField()
    # animal_farmyard = models.IntegerField()
    maturity = models.IntegerField()
    # vegetal = models.IntegerField()
    # mushroom = models.IntegerField()
    # hay = models.IntegerField()
    # wet_leaves = models.IntegerField()
    # forest_floor = models.IntegerField()
    # game = models.IntegerField()
    # savoury = models.IntegerField()
    # tobacco = models.IntegerField()
    # maturity_cedar = models.IntegerField()
    # honey = models.IntegerField()
    # cereal = models.IntegerField()
    mineral = models.IntegerField()
    # mineral_earth = models.IntegerField()
    # petrol = models.IntegerField()
    # kerosene = models.IntegerField()
    # mineral_rubber = models.IntegerField()
    # tar = models.IntegerField()
    # mineral_smoke = models.IntegerField()
    # stony_steely = models.IntegerField()
    # wet_wool = models.IntegerField()
    anisoles = models.IntegerField()
    # mustiness = models.IntegerField()
    # wet_cardboard = models.IntegerField()
    # tca = models.IntegerField()
    brettanomyces = models.IntegerField()
    # brettanomyces_animal = models.IntegerField()
    # leather = models.IntegerField()
    # meaty = models.IntegerField()
    # sticking_plaster = models.IntegerField()
    # vinyl = models.IntegerField()
    # farmyard = models.IntegerField()
    oxidation = models.IntegerField()
    # caramel = models.IntegerField()
    # toffee = models.IntegerField()
    # staleness = models.IntegerField()
    # sherry_aromas = models.IntegerField()
    # aidehydes = models.IntegerField()
    volatile_acidity = models.IntegerField()
    # vinegar = models.IntegerField()
    # solvents = models.IntegerField()
    # nail_varnish_remover = models.IntegerField()
    # lifted = models.IntegerField()
    reduction = models.IntegerField()
    # mercaptans = models.IntegerField()
    # cabbag = models.IntegerField()
    # eggs = models.IntegerField()
    # sweat = models.IntegerField()
    # reduction_rubber = models.IntegerField()
    # onion = models.IntegerField()
    # garlic = models.IntegerField()
    # blocked_drains = models.IntegerField()
    other = models.IntegerField()
    # beetroot = models.IntegerField()
    # earth = models.IntegerField()
    # geosmin = models.IntegerField()
    # rot = models.IntegerField()
    # mould = models.IntegerField()

    # aroma list
    # floral_aroma = models.IntegerField()
    # acacia_aroma = models.IntegerField()
    # honeysuckle_aroma = models.IntegerField()
    # chamomile_aroma = models.IntegerField()
    # elderflower_aroma = models.IntegerField()
    # geranium_aroma = models.IntegerField()
    # blossom_aroma = models.IntegerField()
    # rose_aroma = models.IntegerField()
    # violet_aroma = models.IntegerField()
    # iris_aroma = models.IntegerField()
    # neroli_aroma = models.IntegerField()
    # green_fruit_aroma = models.IntegerField()
    # green_apple_aroma = models.IntegerField()
    # red_apple_aroma = models.IntegerField()
    # gooseberry_aroma = models.IntegerField()
    # pear_aroma = models.IntegerField()
    # amylic_aroma = models.IntegerField()
    # custard_apple_aroma = models.IntegerField()
    # quice_aroma = models.IntegerField()
    # grape_aroma = models.IntegerField()
    # citrus_fruit_aroma = models.IntegerField()
    # grapefruit_aroma = models.IntegerField()
    # lemon_aroma = models.IntegerField()
    # lime_aroma = models.IntegerField()
    # juice_aroma = models.IntegerField()
    # zest_aroma = models.IntegerField()
    # orange_peel_aroma = models.IntegerField()
    # lemon_peel_aroma = models.IntegerField()
    # stone_fruit_aroma = models.IntegerField()
    # peach_aroma = models.IntegerField()
    # apricot_aroma = models.IntegerField()
    # nectarine_aroma = models.IntegerField()
    # tropical_fruit_aroma = models.IntegerField()
    # banana_aroma = models.IntegerField()
    # lychee_aroma = models.IntegerField()
    # mango_aroma = models.IntegerField()
    # melon_aroma = models.IntegerField()
    # passion_fruit_aroma = models.IntegerField()
    # pineapple_aroma = models.IntegerField()
    # red_fruit_aroma = models.IntegerField()
    # redcurrant_aroma = models.IntegerField()
    # cranberry_aroma = models.IntegerField()
    # raspberry_aroma = models.IntegerField()
    # strawberry_aroma = models.IntegerField()
    # red_cherry_aroma = models.IntegerField()
    # plum_aroma = models.IntegerField()
    # black_fruit_aroma = models.IntegerField()
    # blackcurrant_aroma = models.IntegerField()
    # blackberry_aroma = models.IntegerField()
    # bramble_aroma = models.IntegerField()
    # blueberry_aroma = models.IntegerField()
    # black_cherry_aroma = models.IntegerField()
    # dried_cooked_fruit_aroma = models.IntegerField()
    # fig_aroma = models.IntegerField()
    # prune_aroma = models.IntegerField()
    # raisin_aroma = models.IntegerField()
    # sultana_aroma = models.IntegerField()
    # kirsch_aroma = models.IntegerField()
    # jamminess_aroma = models.IntegerField()
    # cooked_aroma = models.IntegerField()
    # baked_aroma = models.IntegerField()
    # stewed_fruits_aroma = models.IntegerField()
    # preserved_fruits_aroma = models.IntegerField()
    # under_ripeness_aroma = models.IntegerField()
    # green_bell_pepper_capsicum_aroma = models.IntegerField()
    # under_ripeness_grass_aroma = models.IntegerField()
    # white_pepper_aroma = models.IntegerField()
    # leafiness_aroma = models.IntegerField()
    # tomato_aroma = models.IntegerField()
    # potato_aroma = models.IntegerField()
    # herbaceous_aroma = models.IntegerField()
    # herbaceous_grass_aroma = models.IntegerField()
    # asparagus_aroma = models.IntegerField()
    # blackcurrant_leaf_aroma = models.IntegerField()
    # pyrazine_aroma = models.IntegerField()
    # herbal_aroma = models.IntegerField()
    # eucalyptus_aroma = models.IntegerField()
    # mint_aroma = models.IntegerField()
    # medicinal_aroma = models.IntegerField()
    # lavender_aroma = models.IntegerField()
    # fennel_aroma = models.IntegerField()
    # dill_aroma = models.IntegerField()
    # vegetable_aroma = models.IntegerField()
    # cabbage_aroma = models.IntegerField()
    # peas_aroma = models.IntegerField()
    # beans_aroma = models.IntegerField()
    # black_olive_aroma = models.IntegerField()
    # green_olive_aroma = models.IntegerField()
    # sweet_spice_aroma = models.IntegerField()
    # cinnamon_aroma = models.IntegerField()
    # cloves_aroma = models.IntegerField()
    # ginger_aroma = models.IntegerField()
    # nutmeg_aroma = models.IntegerField()
    # sweet_spice_vanilla_aroma = models.IntegerField()
    # pungent_spice_aroma = models.IntegerField()
    # black_white_pepper_aroma = models.IntegerField()
    # liquorice_aroma = models.IntegerField()
    # juniper_aroma = models.IntegerField()
    # simplicity_neutrality_aroma = models.IntegerField()
    # simple_aroma = models.IntegerField()
    # neutral_aroma = models.IntegerField()
    # indistinct_aroma = models.IntegerField()
    # autolytic_aroma = models.IntegerField()
    # yeast_aroma = models.IntegerField()
    # biscuit_aroma = models.IntegerField()
    # bread_aroma = models.IntegerField()
    # autolytic_toast_aroma = models.IntegerField()
    # pastry_aroma = models.IntegerField()
    # brioche_aroma = models.IntegerField()
    # lees_aroma = models.IntegerField()
    # dairy_mlf_aroma = models.IntegerField()
    # butter_aroma = models.IntegerField()
    # cheese_aroma = models.IntegerField()
    # cream_aroma = models.IntegerField()
    # yoghurt_aroma = models.IntegerField()
    # oak_aroma = models.IntegerField()
    # oak_vanilla_aroma = models.IntegerField()
    # butterscotch_aroma = models.IntegerField()
    # oak_toast_aroma = models.IntegerField()
    # oak_cedar_aroma = models.IntegerField()
    # charred_wood_aroma = models.IntegerField()
    # oak_smoke_aroma = models.IntegerField()
    # acrid_aroma = models.IntegerField()
    # resinous_aroma = models.IntegerField()
    # kernel_aroma = models.IntegerField()
    # almond_aroma = models.IntegerField()
    # marzipan_aroma = models.IntegerField()
    # coconut_aroma = models.IntegerField()
    # hazelnut_aroma = models.IntegerField()
    # walnut_aroma = models.IntegerField()
    # chocolat_aroma = models.IntegerField()
    # coffee_aroma = models.IntegerField()
    # animal_aroma = models.IntegerField()
    # animal_leather_aroma = models.IntegerField()
    # meat_aroma = models.IntegerField()
    # animal_farmyard_aroma = models.IntegerField()
    # maturity_aroma = models.IntegerField()
    # vegetal_aroma = models.IntegerField()
    # mushroom_aroma = models.IntegerField()
    # hay_aroma = models.IntegerField()
    # wet_leaves_aroma = models.IntegerField()
    # forest_floor_aroma = models.IntegerField()
    # game_aroma = models.IntegerField()
    # savoury_aroma = models.IntegerField()
    # tobacco_aroma = models.IntegerField()
    # maturity_cedar_aroma = models.IntegerField()
    # honey_aroma = models.IntegerField()
    # cereal_aroma = models.IntegerField()
    # mineral_aroma = models.IntegerField()
    # mineral_earth_aroma = models.IntegerField()
    # petrol_aroma = models.IntegerField()
    # kerosene_aroma = models.IntegerField()
    # mineral_rubber_aroma = models.IntegerField()
    # tar_aroma = models.IntegerField()
    # mineral_smoke_aroma = models.IntegerField()
    # stony_steely_aroma = models.IntegerField()
    # wet_wool_aroma = models.IntegerField()
    # anisoles_aroma = models.IntegerField()
    # mustiness_aroma = models.IntegerField()
    # wet_cardboard_aroma = models.IntegerField()
    # tca_aroma = models.IntegerField()
    # brettanomyces_aroma = models.IntegerField()
    # brettanomyces_animal_aroma = models.IntegerField()
    # leather_aroma = models.IntegerField()
    # meaty_aroma = models.IntegerField()
    # sticking_plaster_aroma = models.IntegerField()
    # vinyl_aroma = models.IntegerField()
    # farmyard_aroma = models.IntegerField()
    # oxidation_aroma = models.IntegerField()
    # caramel_aroma = models.IntegerField()
    # toffee_aroma = models.IntegerField()
    # staleness_aroma = models.IntegerField()
    # sherry_aromas_aroma = models.IntegerField()
    # aidehydes_aroma = models.IntegerField()
    # volatile_acidity_aroma = models.IntegerField()
    # vinegar_aroma = models.IntegerField()
    # solvents_aroma = models.IntegerField()
    # nail_varnish_remover_aroma = models.IntegerField()
    # lifted_aroma = models.IntegerField()
    # reduction_aroma = models.IntegerField()
    # mercaptans_aroma = models.IntegerField()
    # cabbag_aroma = models.IntegerField()
    # eggs_aroma = models.IntegerField()
    # sweat_aroma = models.IntegerField()
    # reduction_rubber_aroma = models.IntegerField()
    # onion_aroma = models.IntegerField()
    # garlic_aroma = models.IntegerField()
    # blocked_drains_aroma = models.IntegerField()
    # other_aroma = models.IntegerField()
    # beetroot_aroma = models.IntegerField()
    # earth_aroma = models.IntegerField()
    # geosmin_aroma = models.IntegerField()
    # rot_aroma = models.IntegerField()
    # mould_aroma = models.IntegerField()
