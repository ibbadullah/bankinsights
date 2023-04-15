from django.urls import path, include
from django.views.generic import TemplateView
from .views import *
from .reportParameters import *
from .graphs import SingleBankGraph
from .filtersLogic import filterReportView
from .singleBankReport import singleBankReport

urlpatterns = [
    # General views
    path('',HomeView,name="Home"),
    path('data-testing',DataTesting,name="testdata"),
    # Ajax views for returning banks search
    path('singleusbank/<str:q>',SingleUsBankSearch,name="singleusbank"),
    path('datagridbank/',DataGridBankSearch,name="DataGridBank"),
    # Report parameters view
    path('report/',reportParametersView,name="ReportParametersView"),
    path('report-filters/',filterReportView,name="FilterReportView"),
    path('report-single/',singleBankReport,name="SingleBankReport"),
    # Single bank graph
    path('bank-graphs-report/',SingleBankGraph.as_view(),name='SingleBankGraph'),
    # PDF report routings
    path('pdf-report/',PDFReportView,name="PDFReportView"),
]


