from rest_framework import serializers

from intelliwineApp.user_model import User, UserVectorCharacteristics, UserVectorFlavourAndAroma


class UserSerializer(serializers.HyperlinkedModelSerializer):
    charac = serializers.StringRelatedField(many=False)
    flav_aroma = serializers.StringRelatedField(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'charac', 'flav_aroma')


class UserCharacSerializer(serializers.HyperlinkedModelSerializer):
    user_foreign_key = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserVectorCharacteristics
        fields = ('id', 'user_foreign_key', 'intensity1', 'intensity2', 'intensity3', 'intensity4', 'intensity5', 'sweetness1', 'sweetness2', 'sweetness3', 'sweetness4', 'sweetness5', 'sweetness6', 'acidity1', 'acidity2', 'acidity3', 'acidity4', 'acidity5', 'tannin1', 'tannin2', 'tannin3', 'tannin4', 'tannin5', 'alcohol1', 'alcohol2', 'alcohol3', 'alcohol4', 'alcohol5', 'body1', 'body2', 'body3', 'body4', 'body5', 'flavour_intensity1', 'flavour_intensity2', 'flavour_intensity3', 'flavour_intensity4', 'flavour_intensity5', 'finish1', 'finish2', 'finish3', 'finish4', 'finish5', 'quality_level1', 'quality_level2', 'quality_level3', 'quality_level4', 'quality_level5', 'quality_level6')


class UserAromaSerializer(serializers.HyperlinkedModelSerializer):
    user_foreign_key = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserVectorFlavourAndAroma
        fields = ('id', 'user_foreign_key', 'floral_flavour', 'green_fruit_flavour', 'citrus_fruit_flavour', 'stone_fruit_flavour', 'tropical_fruit_flavour', 'red_fruit_flavour', 'black_fruit_flavour', 'dried_cooked_fruit_flavour', 'under_ripeness_flavour', 'herbaceous_flavour', 'herbal_flavour', 'vegetable_flavour', 'sweet_spice_flavour', 'pungent_spice_flavour', 'simplicity_neutrality_flavour', 'autolytic_flavour', 'dairy_mlf_flavour', 'oak_flavour', 'kernel_flavour', 'animal_flavour', 'maturity_flavour', 'mineral_flavour', 'anisoles_flavour', 'brettanomyces_flavour', 'oxidation_flavour', 'volatile_acidity_flavour', 'reduction_flavour', 'other_flavour', 'floral_aroma', 'green_fruit_aroma', 'citrus_fruit_aroma', 'stone_fruit_aroma', 'tropical_fruit_aroma', 'red_fruit_aroma', 'black_fruit_aroma', 'dried_cooked_fruit_aroma', 'under_ripeness_aroma', 'herbaceous_aroma', 'herbal_aroma', 'vegetable_aroma', 'sweet_spice_aroma', 'pungent_spice_aroma', 'simplicity_neutrality_aroma', 'autolytic_aroma', 'dairy_mlf_aroma', 'oak_aroma', 'kernel_aroma', 'animal_aroma', 'maturity_aroma', 'mineral_aroma', 'anisoles_aroma', 'brettanomyces_aroma', 'oxidation_aroma', 'volatile_acidity_aroma', 'reduction_aroma', 'other_aroma')
