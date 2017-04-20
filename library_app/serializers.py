from rest_framework import serializers
from library_app.models import Author,Book

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255,required=True)
    last_name = serializers.CharField(max_length=255,required=True)
    birth_date = serializers.DateField()

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'birth_date')

    def create(self, validated_data):
        """
        Create and return a new Author, given the validated data
        """
        return Author.objects.create(**validated_data)

    def update(self,instance,validated_data):
        """
        Update and return an existing Author instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()           
        return instance

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255,required=True)
    author = AuthorSerializer()
    isbn = serializers.CharField(max_length=13)
    year_published = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=6,decimal_places=2)
    
    class Meta:
        model = Book
        fields = ('id','title','author', 'isbn', 'year_published','price')

    def create(self,validated_data):
        """
        Create and return a new Book and its Author (if the Author does not already exist),
        given the validated data
        """
        author_data = validated_data.pop('author')
        author_exists = Author.objects.filter(first_name=author_data['first_name'], last_name=author_data['last_name'], birth_date=author_data['birth_date'])
        if (author_exists.count() > 0):
            new_author = Author.objects.get(first_name=author_data['first_name'], last_name=author_data['last_name'], birth_date=author_data['birth_date'])
        else:
            new_author = Author.objects.create(**author_data)
            new_author.save()
        book = Book.objects.create(author=new_author,**validated_data)          
        return book

    def update(self,instance,validated_data):
        """
        Update and return an existing Book instance, given the validated data.
        """
        author_data = validated_data.pop('author')
        author = instance.author

        author.first_name = author_data.get('first_name',author.first_name)
        author.last_name = author_data.get('last_name',author.last_name)
        author.birth_date = author_data.get('birth_date',author.birth_date)
        author.save()
        
        instance.title = validated_data.get('title')
        instance.isbn = validated_data.get('isbn')
        instance.year_published = validated_data.get('year_published')
        instance.price = validated_data.get('price')
        instance.save()

        return instance
        

    
    
