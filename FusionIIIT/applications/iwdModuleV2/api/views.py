#APIs
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404
from applications.iwdModuleV2.models import *
from django.contrib.auth.models import User
from applications.globals.models import ExtraInfo, HoldsDesignation, Designation

class ProjectsAPIView(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PageOneDetailsAPIView(APIView):
    def get(self, request):
        page_one_details = PageOneDetails.objects.all()
        serializer = PageOneDetailsSerializer(page_one_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PageOneDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AESDetailsAPIView(APIView):
    def get(self, request):
        aes_details = AESDetails.objects.all()
        serializer = AESDetailsSerializer(aes_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AESDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PageTwoDetailsAPIView(APIView):
    def get(self, request):
        page_two_details = PageTwoDetails.objects.all()
        serializer = PageTwoDetailsSerializer(page_two_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PageTwoDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CorrigendumTableAPIView(APIView):
    def get(self, request):
        corrigendum_table = CorrigendumTable.objects.all()
        serializer = CorrigendumTableSerializer(corrigendum_table, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CorrigendumTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AddendumAPIView(APIView):
    def get(self, request):
        addendum = Addendum.objects.all()
        serializer = AddendumSerializer(addendum, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddendumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class PreBidDetailsView(APIView):
    def get(self, request, format=None):
        prebid_details = PreBidDetails.objects.all()
        serializer = PreBidDetailsSerializer(prebid_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PreBidDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechnicalBidDetailsView(APIView):
    def get(self, request, format=None):
        technical_bid_details = TechnicalBidDetails.objects.all()
        serializer = TechnicalBidDetailsSerializer(technical_bid_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TechnicalBidDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechnicalBidContractorDetailsView(APIView):
    def get(self, request, format=None):
        technical_bid_contractor_details = TechnicalBidContractorDetails.objects.all()
        serializer = TechnicalBidContractorDetailsSerializer(technical_bid_contractor_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TechnicalBidContractorDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinancialBidDetailsView(APIView):
    def get(self, request, format=None):
        financial_bid_details = FinancialBidDetails.objects.all()
        serializer = FinancialBidDetailsSerializer(financial_bid_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FinancialBidDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinancialContractorDetailsView(APIView):
    def get(self, request, format=None):
        financial_contractor_details = FinancialContractorDetails.objects.all()
        serializer = FinancialContractorDetailsSerializer(financial_contractor_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FinancialContractorDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LetterOfIntentDetailsAPIView(APIView):
    def get(self, request):
        letter_of_intent_details = LetterOfIntentDetails.objects.all()
        serialized_data = LetterOfIntentDetailsSerializer(letter_of_intent_details, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serialized_data = LetterOfIntentDetailsSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkOrderFormAPIView(APIView):
    def get(self, request):
        work_order_forms = WorkOrderForm.objects.all()
        serialized_data = WorkOrderFormSerializer(work_order_forms, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serialized_data = WorkOrderFormSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class AgreementAPIView(APIView):
    def get(self, request):
        agreements = Agreement.objects.all()
        serialized_data = AgreementSerializer(agreements, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serialized_data = AgreementSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class MilestonesAPIView(APIView):
    def get(self, request):
        milestones = Milestones.objects.all()
        serialized_data = MilestonesSerializer(milestones, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serialized_data = MilestonesSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class PageThreeDetailsAPIView(APIView):
    def get(self, request):
        page_three_details = PageThreeDetails.objects.all()
        serialized_data = PageThreeDetailsSerializer(page_three_details, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serialized_data = PageThreeDetailsSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ExtensionOfTimeDetailsView(APIView):
    def get(self, request, project_id):
        extension_of_time_details = ExtensionOfTimeDetails.objects.filter(key=project_id)
        serializer = ExtensionOfTimeDetailsSerializer(extension_of_time_details, many=True)
        return Response(serializer.data)

    def post(self, request, project_id):
        serializer = ExtensionOfTimeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(key=project_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoOfTechnicalBidTimesView(APIView):
    def get(self, request, project_id):
        no_of_technical_bid_times = NoOfTechnicalBidTimes.objects.get(key=project_id)
        serializer = NoOfTechnicalBidTimesSerializer(no_of_technical_bid_times)
        return Response(serializer.data)

    def post(self, request, project_id):
        serializer = NoOfTechnicalBidTimesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(key=project_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)