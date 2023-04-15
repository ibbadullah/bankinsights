from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from .models import *
from django.db.models import Q, Avg
from django.http import JsonResponse
from django.template.loader import render_to_string
from django_xhtml2pdf.utils import generate_pdf
import itertools
from .locationGeocoding import securityCheck

# Create your views here.
def HomeView(request):
    if securityCheck(request) == False:
        #return render(request,'invalid-request.html')
        return HttpResponse(f"<script>location.replace('https://bankinsights.io/');</script>")
    # Drop down menus
    dm1 = itertools.chain(DropdownMenuState.objects.all())
    dm2 = itertools.chain(BankBranch.objects.all())
    dm3 = itertools.chain(DropdownMenuDistance.objects.all())
    dm4 = itertools.chain(DropdownMenuPeerGroup.objects.all())
    p1 = itertools.chain(DropdownMenu4Quarters.objects.all())
    p2 = itertools.chain(DropdownMenu4Years.objects.all())
    # Data Drop down menu
    ddm1 = itertools.chain(NavigationMenuData.objects.filter(parent_id=0))
    # Data Sub drop down menu
    sm1 = itertools.chain(NavigationMenuData.objects.filter(parent_id=1))
    sm2 = itertools.chain(NavigationMenuData.objects.filter(parent_id=2))
    sm3 = itertools.chain(NavigationMenuData.objects.filter(parent_id=3))
    sm4 = itertools.chain(NavigationMenuData.objects.filter(parent_id=4))
    sm5 = itertools.chain(NavigationMenuData.objects.filter(parent_id=5))
    sm6 = itertools.chain(NavigationMenuData.objects.filter(parent_id=6))
    sm7 = itertools.chain(NavigationMenuData.objects.filter(parent_id=7))
    # Data sub in drop down menu
    sim1 = itertools.chain(NavigationMenuData.objects.filter(parent_id=10))
    sim2 = itertools.chain(NavigationMenuData.objects.filter(parent_id=11))
    sim3 = itertools.chain(NavigationMenuData.objects.filter(parent_id=12))
    sim4 = itertools.chain(NavigationMenuData.objects.filter(parent_id=13))
    sim5 = itertools.chain(NavigationMenuData.objects.filter(parent_id=15))
    sim6 = itertools.chain(NavigationMenuData.objects.filter(parent_id=16))
    sim7 = itertools.chain(NavigationMenuData.objects.filter(parent_id=17))
    sim8 = itertools.chain(NavigationMenuData.objects.filter(parent_id=18))
    sim9 = itertools.chain(NavigationMenuData.objects.filter(parent_id=19))
    sim10 = itertools.chain(NavigationMenuData.objects.filter(parent_id=20))
    sim11 = itertools.chain(NavigationMenuData.objects.filter(parent_id=21))
    sim12 = itertools.chain(NavigationMenuData.objects.filter(parent_id=22))
    sim13 = itertools.chain(NavigationMenuData.objects.filter(parent_id=23))
    sim14 = itertools.chain(NavigationMenuData.objects.filter(parent_id=24))
    sim15 = itertools.chain(NavigationMenuData.objects.filter(parent_id=25))
    sim16 = itertools.chain(NavigationMenuData.objects.filter(parent_id=26))
    sim17 = itertools.chain(NavigationMenuData.objects.filter(parent_id=26))
    sim18 = itertools.chain(NavigationMenuData.objects.filter(parent_id=28))
    sim19 = itertools.chain(NavigationMenuData.objects.filter(parent_id=29))
    sim20 = itertools.chain(NavigationMenuData.objects.filter(parent_id=30))
    sim21 = itertools.chain(NavigationMenuData.objects.filter(parent_id=31))
    sim22 = itertools.chain(NavigationMenuData.objects.filter(parent_id=32))
    return render(request,'home.html',{"dm1":dm1,"dm2":dm2,"dm3":dm3,"dm4":dm4,"p1":p1,"p2":p2,"ddm":ddm1,"sm1":sm1,
                                       "sm2":sm2,"sm3":sm3,"sm4":sm4,"sm5":sm5,"sm6":sm6,"sm7":sm7,"sim1":sim1,"sim2":sim2,
                                       "sim3":sim3,"sim4":sim4,"sim5":sim5,"sim6":sim6,"sim7":sim7,"sim8":sim8,"sim9":sim9,
                                       "sim10":sim10,"sim11":sim11,"sim12":sim12,"sim13":sim13,"sim14":sim14,"sim15":sim15,"sim16":sim16,
                                       "sim17":sim17,"sim18":sim18,"sim19":sim19,"sim20":sim20,"sim21":sim21,"sim22":sim22})



def PDFReportView(request):
    if securityCheck(request) == False:
        #return render(request,'invalid-request.html')
        return HttpResponse(f"<script>location.replace('https://bankinsights.io/');</script>")
    # Getting data from url variables
    rssdID = int(request.GET.get('id'))
    periodsList = request.GET.get('period')
    periodsList = periodsList.split(",")
    # Getting bank details
    bankData = BankHq.objects.get(rssd_id=rssdID)
    peerGroupLabel = DropdownMenuPeerGroup.objects.get(value=bankData.peer_group)
    branchQuery = BankBranch.objects.filter(rssd_id_hq=rssdID).distinct()
    labelsList = request.GET.get('labels')
    labelsList = labelsList.split(',')
    bankState = DropdownMenuState.objects.get(value=bankData.state)
    # Required states of branches
    branchStatesList = []
    for s in branchQuery:
        branchStatesList.append(s.state)
    branchStatesList.append(bankState)
    branches = DropdownMenuState.objects.filter(value__in=branchStatesList).distinct().order_by('label')

    # Getting bank full data for the report
    p1 = BankData.objects.filter(period=periodsList[0],rssd_id=rssdID)
    p2 = BankData.objects.filter(period=periodsList[1], rssd_id=rssdID)
    p3 = BankData.objects.filter(period=periodsList[2], rssd_id=rssdID)
    p4 = BankData.objects.filter(period=periodsList[3], rssd_id=rssdID)
    data = {
        "P1": p1,
        "P2": p2,
        "P3": p3,
        "P4": p4,
        "Bank": bankData,
        "PeerGroupLabel": peerGroupLabel.label,
        "Branches": branches,
        "Labels": labelsList,
        "BankState": bankState
    }
    return render(request,'pdf/pdf.html',{"Data":data})


# getting report in response for pdf printing - This function is not anymore in use
def PDFReportDownload(request):
    # Getting data from url variables
    rssdID = int(request.GET.get('id'))
    periodsList = request.GET.get('period')
    periodsList = periodsList.split(",")
    # Getting bank details
    bankData = BankHq.objects.get(rssd_id=rssdID)
    # Getting bank full data for the report
    p1 = BankData.objects.filter(period=periodsList[0],rssd_id=rssdID)
    p2 = BankData.objects.filter(period=periodsList[1], rssd_id=rssdID)
    p3 = BankData.objects.filter(period=periodsList[2], rssd_id=rssdID)
    p4 = BankData.objects.filter(period=periodsList[3], rssd_id=rssdID)
    data = {
        "P1": p1,
        "P2": p2,
        "P3": p3,
        "P4": p4,
        "Bank": bankData,
    }
    pdfdata = render_to_string('pdf/pdf_download.html',{"Data":data})
    return JsonResponse({"khan":pdfdata})


# Testing view for testing different logics
def DataTesting(request):
    rssd1 = [22,33,45,67,88,65]
    return render(request, 'invalid-request.html')

# Bank branch location (Ajax)
def BanksBranchesLocation(request,q):
    if request.method == 'GET':
        res = None
        userquery = q
        query = BankBranch.objects.filter(Q(city__icontains=userquery) | Q(state__icontains=userquery) | Q(address__icontains=userquery))[0:20]
        if len(query) > 0 and len(userquery) > 0:
            data = []
            for q in query:
                item = {
                    "city": q.city,
                    "state": q.state,
                    "rssd_id_hq": q.rssd_id_hq,
                }
                data.append(item)
            res = data
        else:
            res = "Sorry, no results found."
        return JsonResponse({"data": res})



# Single US bank search (Ajax)
def SingleUsBankSearch(request,q):
    if request.method == 'GET':
        res = None
        testingQ = request.GET.get('query')
        print(testingQ)
        userquery = q
        print(userquery)
        query = BankHq.objects.filter(Q(bank__istartswith=testingQ) | Q(bank__icontains=testingQ))[0:20]
        if query.count() > 0:
            data = []
            for d in query:
                item = {
                    "bankname": d.bank,
                    "rssid": d.rssd_id,
                }
                data.append(item)
            res = data
        else:
            res = "Sorry, no result was found."
        return JsonResponse({"data": res})


# Bank data grid search (Ajax)
def DataGridBankSearch(request):
    if request.method == 'POST':
        res = None
        banks = request.POST.get('bank')
        periods = request.POST.get('periods')
        rssdIDs = request.POST.get('rssdIds')
        userquery = request.POST.get('userquery')
        periods = periods.split(',')
        if banks == "All US banks":
            rssdIDQuery = BankData.objects.filter(period=periods[0]).values_list('rssd_id',flat=True)
            query = BankHq.objects.filter(bank__icontains=userquery,rssd_id__in=rssdIDQuery)[0:20]
            if query.count() > 0:
                data = []
                for q in query:
                    item = {
                        "bankname": q.bank,
                        "rssid": q.rssd_id,
                    }
                    data.append(item)
                res = data
            else:
                res = "Sorry, no result was found."
            return JsonResponse({"data": res})
        else:
            rssdIDs = rssdIDs.replace("'","")
            rssdIDs = rssdIDs.replace("[","")
            rssdIDs = rssdIDs.replace("]","")
            rssdIDs = rssdIDs.replace(" ", "")
            rssdIDs = rssdIDs.replace("  ", "")
            rssdIDs = rssdIDs.split(",")
            myList = []
            for myid in rssdIDs:
                print(myid)
                myList.append(int(myid))
            print(type(myList))
            query = BankHq.objects.filter(bank__icontains=userquery,rssd_id__in=myList)[0:20]
            if query.count() > 0:
                data = []
                for q in query:
                    item = {
                        "bankname": q.bank,
                        "rssid": q.rssd_id,
                    }
                    data.append(item)
                res = data
            else:
                res = "Sorry, no result was found."
            return JsonResponse({"data": res})



