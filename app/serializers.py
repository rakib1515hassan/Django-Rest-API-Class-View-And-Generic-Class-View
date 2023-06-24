from rest_framework import serializers
from app.models import Student, Teacher, STUDENT_CLASS, GENDER


class StudentSerializer(serializers.Serializer):
    id            = serializers.IntegerField(read_only=True)
    name          = serializers.CharField(max_length=100, allow_blank=True, required=True)
    student_class = serializers.ChoiceField(choices=STUDENT_CLASS, default='vi')
    gender        = serializers.ChoiceField(choices=GENDER, default='Male')
    roll          = serializers.IntegerField(allow_null=True, required=True)
    picture       = serializers.ImageField(allow_null=True, required=False)
    email         = serializers.EmailField(max_length=50, required=True)
    waiver        = serializers.BooleanField(default=False)
    description   = serializers.CharField(max_length=200)
    date_of_birth = serializers.DateField()
    created_at    = serializers.DateField(read_only=True)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)


    # instance = Old data যা আমাদের Database এ আগেথেকে save আছে।
    # validated_data = New data যা user update করার জন্যে পেরন করেছে।
    def update(self, instance, validated_data):   
        instance.name          = validated_data.get('name', instance.name)
        instance.student_class = validated_data.get('student_class', instance.student_class)
        instance.gender        = validated_data.get('gender', instance.gender)
        instance.roll          = validated_data.get('roll', instance.roll)
        instance.picture       = validated_data.get('picture', instance.picture)
        instance.email         = validated_data.get('email', instance.email)
        instance.waiver        = validated_data.get('waiver', instance.waiver)
        instance.description   = validated_data.get('description', instance.description)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance

# Alter-Native Way-
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
#         # fields = ['id', 'name', 'student_class', 'gender', 'roll', 'picture', 'email', 'waiver', 'description', 'date_of_birth']




class TeacherSerializer(serializers.Serializer):
    name       = serializers.CharField(max_length=50)
    age        = serializers.IntegerField()
    salary     = serializers.IntegerField()
    experience = serializers.BooleanField()

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
    
    def update(self, instance, validated_data): 
        instance.name       = validated_data.get('name',       instance.name)
        instance.age        = validated_data.get('age',        instance.age)
        instance.salary     = validated_data.get('salary',     instance.salary)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.save()
        return instance

## Alter-Native Way 
# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         # fields = ['id', 'name', 'age', 'salary', 'experience']
#         fields = '__all__'




















# NOTE ------------------------------( Definition  of Serialization )-------------------------------
"""

    In Django REST Framework, Serializers are responsible for converting complex data such as querysets
    and model instances to native Python datatype (called serialization) that can then be easily rendered
    into JSON, XML or other content type which is understandable by Front End.

"""


# NOTE ---------------------------------( All Serialization Field)----------------------------------
"""
class AllSerializerFields(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)

    a = serializers.CharField(
        max_length=100, min_length=3, allow_blank=True, trim_whitespace=True, allow_null=True, required=True
        )

    b = serializers.IntegerField(max_length=None, min_length=None)

    c = serializers.FloatField(max_length=None, min_length=None)

    d = serializers.DecimalField(
        max_length=None, min_length=None, max_digits=10, decimal_places=None, coerce_to_string=None
        )
    
    e = serializers.SlugField(max_length=50, min_length=None, all_blank=False)

    f = serializers.EmailField(max_length=50, min_length=None, all_blank=False, required=True)

    g = serializers.BooleanField(default=False)

    h = serializers.NullBooleanField()

    i = serializers.URLField(max_length=300, min_length=None, all_blank=False)

    j = serializers.FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL)

    k = serializers.ImageField(allow_null=True, required=False)

    l = serializers.DateField(format=api_settings.DATE_FORMAT, input_formats=None)

    m = serializers.TimeField(format=api_settings.TIME_FORMAT, input_formats=None)

    n = serializers.DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None, default_timezone=None)

    o = serializers.DurationField(max_value=None, min_value=None)

    p = serializers.RegexField(regex=None, max_length=300, min_length=None, all_blank=False)

    q = serializers.UUIDField(format='hex_verbose')

    r = serializers.FilePathField(
        path=None, match=None, recursive=False, allow_files=True, allow_folders=False, required=False, **kwargs
        )
    
    s = serializers.IPAddressField(protocol='both', unpack_ipv4=False, **options)

    t = serializers.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female')))

    u = serializers.MultipleChoiceField(choices=((a,a),(b,b),(c,c)))

    v = serializers.ListField(child=<A_FIELD_INSTANCE>, allow_empty=True, max_length=None, min_length=None)

    w = serializers.DictField(child=<A_FIELD_INSTANCE>, allow_empty=True)

    x = serializers.HStoreField(child=<A_FIELD_INSTANCE>, allow_empty=True)

    y = serializers.JSONField(binary, encoder)

    z = serializers.ReadOnlyField()

    aa = serializers.HiddenField()

    ab = serializers.ModelField(model_field=<Django ModelField instance>)

    ac = serializers.SerializerMethodField(method_name=None)

"""

# NOTE ------------------------------------( Core Argumetnts )------------------------------------
"""
1) label - A short text string that may be used as the name of the field in HTML form fields or other descriptive elements.


2) validators - A list of validator functions which should be applied to the incoming field input, and which either raise a
   validation error or simply return. Validator functions should typically raise serializers. ValidationError, but Django's
   built-in ValidationError is also supported for compatibility with validators defined in the Django codebase or third party
   Django packages.

3) error_messages - A dictionary of error codes to error messages.

4) help_text - A text string that may be used as a description of the field in HTML form field or other descriptive elements.

5) required - Normally an error will be raised if a field is not supplied during deserialization. Set to false if this field
   is not required to be present during deserialization.
   Setting this to False also allows the object attribute or dictionary key to be omitted from output when serializing the
   instance. If the key is not present it will simply not be included in the output representation.
   Defaults to True.

6) default - If set, this gives the default value that will be used for the field if no input value is supplied. If not set the
   default behaviour is to not populate the attribute at all.
   The default is not applied during partial update operations. In the partial update case only fields that are provided in the
   incoming data will have a validated value returned.
   Note that setting a default value implies that the field is not required. Including both the default and required keyword 
   arguments is invalid and will raise an error.

7) initial - A value that should be used for pre-populationg the value of HTML form fields.

8) style - A dictionary of key-value pairs that can be used to control how renderers should render the filed.
    Example:-

        password = serializers.CharField(
            max_length=100,
            style={'input_type':'password', 'placeholder': 'Enter Your Password'}
        )

9) read_only - Read-only fields are included in the API output, but should not be included in the input during create or
   update operations. Any 'read_only' fields that are incorrectly included in the serializer input will be ignored.
   Set this to True to ensure that the field is used when serializing a representation, but is not used when creating or
   updating an instance during deserialization.
   Defaults to False

10) write_only - Set this to True to ensure that the field may be used when updating or creating an instance, but is not
    included when serializing the representation.
    Defaults to False

11) allow_null - Normally an error will be raised if None is passed to a serializer field. Set this keyword argument to 
    True if None should be considered a valid value.
    Note that, without an explicit default, setting this argument to True will imply a default value of null for 
    serialization output, but does not imply a default for input deserialization.
    Defaults to False

12) source - The name of the attribute that will be used to populate the field. May be a method that only takes a self
    argument, such as URLField(source='get_absolute_url'), or may use dotted notation to traverse attributes, such as 
    EmailField(source='user.email'). When serializing fields with dotted notation, it may be necessary to provide a 
    default value if any object is not present or is empty during attribute traversal.
    The value source="*' has a special meaning, and is used to indicate that the entire object should be passed through
    to the field. This can be useful for creating nested representations, or for fields which require access to the complete
    object in order to determine the output representation.
    Defaults to the name of the field.


"""


# NOTE ------------------------------( Definition  of De-Serialization )-------------------------------
"""

Deserialization allows parsed data to be converted back into complex types, after first validating the incomimg data.

"""

