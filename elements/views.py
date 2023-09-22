from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from elements.serializers import AttributeNameSerializer
from elements.serializers import get_serializer
from elements.models import *
 

@api_view(['POST'])
def import_element(request): 

    # Accept either single element (dictionary) or list of elements

    if type(request.data) == dict:
        data = [request.data]   
    elif type(request.data) == list:
        data = request.data
    else:
        return Response({"error":"Wrong data type"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Iterate through data one element at a time
    for element in data:

        # Get element name and data
        try:
            element_name = list(element.keys())[0]
            element_data = list(element.values())[0]
        except (IndexError) as e: #AttributeError # in case that json is not in correct format, or empty
            return Response({"error" : "Wrong Json format"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get serializer based on element name
        try:
            serializer = get_serializer(element_name)
        except (NameError) as e:
            return Response({"error" : f"Wrong element name {element_name}"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Try to get element if already exists
        try:
            # Get correct model based on element name
            model = get_model(element_name)
            # Get element from DB
            element = model.objects.get(id=element_data["id"])
            serializer = serializer(element,data=element_data)
        except (NameError,KeyError, model.DoesNotExist) as e:
            serializer = serializer(data=element_data)

        try:

            # Save the data
            if serializer.is_valid(raise_exception=True):
                try:
                    serializer.save()
                except (Exception) as e:
                    return Response({"error" : "Error occured while saving data", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except (KeyError) as e:
            return Response({"error" : "Wrong Json format"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"success" : data}, status=status.HTTP_201_CREATED)




@api_view(['GET'])
def detail(request,element_name,element_id = None): 

    # Get model and serializer based on element name
    try:
        model = get_model(element_name)
        serializer = get_serializer(element_name)
    except (NameError) as e:
        return Response({"error" : f"Wrong element name {element_name}"}, status=status.HTTP_400_BAD_REQUEST)
    

    # Get all elements of a model
    if element_id == None:
        elements = model.objects.all()
        serializer = serializer(elements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Get one element of a model
    else:
        try:
            element = model.objects.get(id=element_id)
        except (model.DoesNotExist) as e:
            return Response({"error" : "Element does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = serializer(element)
        return Response(serializer.data, status=status.HTTP_200_OK)





@api_view(['GET'])
def reset_db(request):
    """ Deletes all tables in DB but does not reset it completely
        (for example ID auto increment is not reseted)
    """
    Catalog.objects.all().delete()
    ProductAttributes.objects.all().delete()
    ProductImage.objects.all().delete()
    Product.objects.all().delete()
    Attribute.objects.all().delete()
    AttributeValue.objects.all().delete()
    AttributeName.objects.all().delete()
    Image.objects.all().delete()

    return Response({"Response": "Database was reseted"}, status=status.HTTP_200_OK)


