from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', ProjectsAPIView.as_view(), name='projects'),
    path('pageonedetails/', PageOneDetailsAPIView.as_view(), name='pageonedetails'),
    path('aesdetails/', AESDetailsAPIView.as_view(), name='aesdetails'),
    path('pagetwodetails/', PageTwoDetailsAPIView.as_view(), name='pagetwodetails'),
    path('corrigendumtable/', CorrigendumTableAPIView.as_view(), name='corrigendumtable'),
    path('addendum/', AddendumAPIView.as_view(), name='addendum'),
    path('prebiddetails/', PreBidDetailsView.as_view(), name='prebiddetails'),
    path('technicalbiddetails/', TechnicalBidDetailsView.as_view(), name='technicalbiddetails'),
    path('technicalbidcontractordetails/', TechnicalBidContractorDetailsView.as_view(), name='technicalbidcontractordetails'),
    path('financialbiddetails/', FinancialBidDetailsView.as_view(), name='financialbiddetails'),
    path('financialcontractordetails/', FinancialContractorDetailsView.as_view(), name='financialcontractordetails'),
    path('letter-of-intent-details/', LetterOfIntentDetailsAPIView.as_view(), name='letter_of_intent_details'),
    path('work-order-form/', WorkOrderFormAPIView.as_view(), name='work_order_form'),
    path('agreements/', AgreementAPIView.as_view(), name='agreements'),
    path('milestones/', MilestonesAPIView.as_view(), name='milestones'),
    path('page-three-details/', PageThreeDetailsAPIView.as_view(), name='page_three_details'),
    path('extension-of-time-details/<int:project_id>/', ExtensionOfTimeDetailsView.as_view(), name='extension_of_time_details'),
    path('no-of-technical-bid-times/<int:project_id>/', NoOfTechnicalBidTimesView.as_view(), name='no_of_technical_bid_times'),
]
