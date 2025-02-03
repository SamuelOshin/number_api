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
        if not number or not number.isdigit():
            return Response(
                {
                    "number": "alphabet",
                    "error": True
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Convert to integer
        num = int(number)
        
        # Create classifier instance
        classifier = NumberClassifier()
        
        # Get number properties
        response_data = {
            "number": num,
            "is_prime": classifier.is_prime(num),
            "is_perfect": classifier.is_perfect(num),
            "properties": classifier.get_properties(num),
            "digit_sum": classifier.digit_sum(num),
            "fun_fact": classifier.get_fun_fact(num)
        }
        
        return Response(response_data)
        
    except Exception as e:
        return Response(
            {
                "number": number if 'number' in locals() else None,
                "error": True
            },
            status=status.HTTP_400_BAD_REQUEST
        )