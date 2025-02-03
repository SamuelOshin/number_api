from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import NumberClassifier

@api_view(['GET'])
def classify_number(request):
    """
    API endpoint to classify a number and return its properties.
    """
    try:
        # Get number from query params
        number = request.GET.get('number')
        
        # Validate input
        if number is None:
            return Response(
                {
                    "error": True,
                    "message": "No number provided."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Convert to integer safely
        try:
            num = int(number)  # Allows negative numbers
        except ValueError:
            return Response(
                {
                    "error": True,
                    "message": "Invalid input. Please enter a valid integer."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get number properties
        response_data = {
            "number": num,
            "is_prime": NumberClassifier.is_prime(num),
            "is_perfect": NumberClassifier.is_perfect(num),
            "properties": NumberClassifier.get_properties(num),
            "digit_sum": NumberClassifier.digit_sum(num),
            "fun_fact": NumberClassifier.get_fun_fact(num)
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {
                "error": True,
                "message": "An unexpected error occurred."
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )