import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import RegisterSerializer
from .models import OtpCode
from utils import send_otp_code

class RegisterAPIView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            cd = serializer.validated_data

            random_code = random.randint(1000, 9999)
            send_otp_code(cd['phone_number'], random_code)

            OtpCode.objects.create(phone_number=cd['phone_number'], code=random_code)

            request.session['user_registration_info'] = {
                'phone_number' : cd['phone_number'],
                'full_name'    : cd['full_name'],
                'email'        : cd['email'],
                'password'     : cd['password'],
            }
            return Response({'message': 'OTP send successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















