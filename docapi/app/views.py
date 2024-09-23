from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Doctor

from .serializers import DoctorSerializer
from rest_framework import status
import os 

class DoctoresView(APIView):

    def post(self, request):
        # Extract data from the request

        symptoms = request.data
        
     
     
        os.environ["GOOGLE_API_KEY"] = "AIzaSyC7Z9xyqpMofKgYsNXYNXw6AzJ65O1kdlk"
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")



        departments = Doctor.objects.values_list('department', flat=True).distinct()
        
        # Generate a response from the model
        try:
            prompt = (
                    f"Answer in one word; given the symptoms '{symptoms}', "
                    f"determine the most suitable type of doctor from the following list to consult: "
                    f"{departments}. The response should be only one doctor."
                )

            # Generate the response
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(prompt)
            department = response.text.strip()

            doctors = Doctor.objects.filter(department=department)
            # Serialize the data
            serializer = DoctorSerializer(doctors, many=True)
            
        except Exception as e:
            return Response({"error": f"Error generating response: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Return a response indicating that the data was received
        return Response({"doctores": serializer.data}, status=status.HTTP_200_OK)
