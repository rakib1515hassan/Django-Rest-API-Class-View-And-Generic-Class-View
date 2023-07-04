from rest_framework import serializers
from FilterObj.models import Author, Publisher, Book, Store
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['id', 'user', 'phone', 'age']


class UserSerializer(serializers.ModelSerializer): # User Create করা মধ্যমে আমরা Author Creat করতে পারবো।
    author    = AuthorSerializer(many=False)

    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password], style={'input_type':'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type':'password'})

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'password2','author')


        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True, 'required': True},
            'password2': {'write_only': True, 'required': True},
            }
        

    def validate(self, attrs): # attrs means data
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        return attrs 
        

    def create(self, validated_data):
        author_data = validated_data.pop('author')

        user = User.objects.create(
            username   = validated_data.get('username'),
            first_name = validated_data.get('first_name'),
            last_name  = validated_data.get('last_name'),
            email      = validated_data.get('email'),
            )
        
        user.set_password(validated_data.get('password'))
        user.save()

        Author.objects.create(user=user, **author_data)

        return user
    
    """NOTE এই ভাবেও save করা যেতো যদি password2 টাকে আমরা না নিতাম।

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        user = User.objects.create_user(**validated_data)
        Author.objects.create(user=user, **author_data)
        return user

    """
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ('id', 'username', 'first_name', 'last_name', 'email')







class PublisherSerializer(serializers.ModelSerializer):
# class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.StringRelatedField(many =True, read_only = True) # এর মাধ্যমে দেখাজবে এই Publisher এর কি কি Book আছে ।
    # book = serializers.HyperlinkedIdentityField(
    #     many=True,
    #     read_only=True,
    #     view_name='book-detail'  # Replace 'book-detail' with the actual view name for retrieving a book detail
    # )

    class Meta:                                                                                                                                                                                                                                                                                                                                                                                                                        
        model = Publisher
        # fields = '__all__'
        # fields = ['id', 'name']
        fields = ['id', 'name', 'book']       
        # fields = ['id', 'name', 'book', 'url']       








class BookSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(many=True)
    authors = serializers.StringRelatedField(many =True, read_only = True)     # এটি করলে 1,2,3 id পরিবর্তে author name দেখাবে।
    # authors = serializers.PrimaryKeyRelatedField(many =True, read_only = True) # এটি করলে 1,2,3 id  দেখাবে name দেখাবে না।


    # publisher = PublisherSerializer()
    publisher = serializers.StringRelatedField(read_only=True)
    # publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['id', 'name', 'authors', 'publisher', 'pages', 'price', 'rating', 'pubdate']


""" NOTE POST request এই ভাবে দিতে হবে।
{
    "name": "Easy Python",
    "authors": [1, 2, 5],     ## ManyToMany Relationship Data Insurt
    "publisher": 2,           ## ForeignKey Relationship Data Insurt
    "pages": 561,
    "price": 458.50,
    "rating": 7.5,
    "pubdate": "2023-02-26"
}
"""
""" NOTE যদি authors = AuthorSerializer(many=True)  publisher = PublisherSerializer()
         serializer create করি তবে Data এই ভাবে POST request করতে হবে। 
{
    "name": "Easy Python",
    "authors": [
        {"id": 1, "name": "....", "others_info": "...."}, 
        {"id": 2},
        {"id": 5}
    ],
    "publisher": {"id": 2},
    "pages": 561,
    "price": 458.50,
    "rating": 7.5,
    "pubdate": "2023-02-26"
}
"""




class StoreSerializer(serializers.ModelSerializer):
    # books = BookSerializer(many=True)

    class Meta:
        model = Store
        # fields = '__all__'
        fields = ['id', 'name', 'books']


""" NOTE POST request এই ভাবে দিতে হবে।
{
    "name": "Banglabazer Store",
    "books": [2, 3, 4]      ## ManyToMany Relationship Data Insurt
}
"""
