from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Reviews


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Reviews
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name', read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__" 
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        extra_kwargs = {
            'url': {'view_name': 'stream-detail', 'lookup_field': 'pk'},
        }

    # add custom serializer field, doc:https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    # def get_len_name(self, obj):
    #     return len(obj.name)

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and description must be different.")
    #     return data 
    
    # def validate_name(self, value):
    #     '''Validate the name of the movie'''
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name must be at least two character long.")
    #     else:
    #         return value



# def name_length(value):
#     if len(value) < 3 :
#         raise serializers.ValidationError("Name must be at least 3 characters long.")
    

# # Serializer class for converting Movie objects into serialized data
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         '''Create and return a new `Snippet` instance, given the validated data'''
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         '''Update and return an existing `Snippet` instance, given the validated data'''
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and description must be different.")
#         return data 
    
    # def validate_name(self, value):
    #     '''Validate the name of the movie'''
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name must be at least two character long.")
    #     else:
    #         return value
