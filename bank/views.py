from django.shortcuts import render
from rest_framework.views import APIView

class BankView(APIView):

    def get(self):
        pass

    def post(self, bank_details):
        pass

    def patch(self, bank_details):
        pass

    def delete(self,bank_id):
        pass