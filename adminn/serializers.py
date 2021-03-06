from rest_framework.serializers import ModelSerializer, SerializerMethodField
from adminn.models import *


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    product_count = SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'product_count': {'read_only': True}
        }

    def get_product_count(self, instance):
        return instance.product_set.count()

class SubCategorySerializer(ModelSerializer):
    product_count = SerializerMethodField()
    class Meta:
        model = SubCategory
        fields = '__all__'
        extra_kwargs = {
            'product_count': {'read_only': True}
        }

    def get_product_count(self, instance):
        return instance.product_set.count()

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class GenderSerializer(ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ["user"]

class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class ImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    name = SerializerMethodField()
    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def get_name(self, instance):
        return instance.user.name

