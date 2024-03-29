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
        fields = ('id', 'user_foreign_key', 'sweetness1', 'sweetness2', 'sweetness3', 'sweetness4', 'sweetness5', 'sweetness6', 'acidity1', 'acidity2', 'acidity3', 'acidity4', 'acidity5', 'tannin1', 'tannin2', 'tannin3', 'tannin4', 'tannin5', 'alcohol1', 'alcohol2', 'alcohol3', 'alcohol4', 'alcohol5', 'body1', 'body2', 'body3', 'body4', 'body5', 'flavour_intensity1', 'flavour_intensity2', 'flavour_intensity3', 'flavour_intensity4', 'flavour_intensity5', 'quality_level1', 'quality_level2', 'quality_level3', 'quality_level4', 'quality_level5', 'quality_level6')


class UserAromaSerializer(serializers.HyperlinkedModelSerializer):
    user_foreign_key = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserVectorFlavourAndAroma
        fields = (
            'id', 'user_foreign_key', 'floral', 'green_fruit', 'citrus_fruit', 'stone_fruit', 'tropical_fruit',
            'red_fruit', 'black_fruit', 'dried_cooked_fruit', 'under_ripeness', 'herbaceous', 'herbal', 'vegetable',
            'sweet_spice', 'pungent_spice', 'simplicity_neutrality', 'autolytic', 'dairy_mlf', 'oak', 'kernel',
            'animal', 'maturity', 'mineral', 'anisoles', 'brettanomyces', 'oxidation', 'volatile_acidity', 'reduction',
            'other')
