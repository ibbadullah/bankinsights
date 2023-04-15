from django.shortcuts import render,redirect, HttpResponse
from django.http import JsonResponse
from .models import *
from .bankdataFields import *
from .locationGeocoding import *
from .smartLogics import *
from django.contrib import messages
from reports.filtersSmartLogics import getRequiredRSSDIDs
import string


# Report generating main view
def reportParametersView(request):
    # cookies stuff
    if securityCheck(request) == False:
        return render(request,'invalid-request.html')
    request.session['sort'] = 'clear'
    # declaring empty dictionaries variables & lists for storing data
    banks = ""
    allUSBanks = ""
    usbankswithbranchesinState = ""
    usbankswithbranchesnearLocation = ""
    milesDistance = ""
    usbanksinBankPeerGroup = ""
    singleUSBank = ""
    singleUSBankName = ""
    usbankswithbranchesinStateList = []
    nearLocationList = []
    usbanksinBankPeerGroupList = []
    periods = ""
    periodsList = []
    periodSingleLabel = ""
    periodsLabelsList = []
    formDataItems = 0
    dataField1 = 0
    dataField2 = 0
    dataField3 = 0
    dataField4 = 0
    dataField5 = 0
    dataField6 = 0

    if request.method == "POST":
        # Getting three main form fields value
        banks = request.POST['banks']
        formPeriodsField = request.POST['periods']
        formDataItems = request.POST['dataItemsCounter']
        dataField1 = request.POST['data1']
        dataField2 = request.POST['data2']
        dataField3 = request.POST['data3']
        dataField4 = request.POST['data4']
        dataField5 = request.POST['data5']
        dataField6 = request.POST['data6']
        # Getting RSSD IDs
        rssdIDs = None
        if banks == "US banks with branches in State":
            usbankswithbranchesinState = request.POST['USbankswithbranchesinState']
            rssdSelectedBanks = banks + " - " + getStateLabel(usbankswithbranchesinState)
            mylist = getRequiredRSSDIDs(banks, usbankswithbranchesinState, "pass")
            rssdIDs = mylist

        elif banks == "US banks with branches near Location":
            usbankswithbranchesnearLocation = request.POST['bankbranchlocation']
            milesDistance = request.POST['milesDistance']
            gl = getGeoLocation(usbankswithbranchesnearLocation)
            if gl == "Nothing found":
                messages.info(request, f'Unknown location.  Please try another location. ("{usbankswithbranchesnearLocation.upper()}").')
                return redirect('Home')
            rssdSelectedBanks = "Location: " + string.capwords(usbankswithbranchesnearLocation) + " within " + milesDistance + " Miles"
            mylist = getRequiredRSSDIDs(banks, usbankswithbranchesnearLocation, milesDistance)
            # if list is zero
            if len(mylist) == 0:
                messages.info(request,f'No banks were found for the given location ("{usbankswithbranchesnearLocation.upper()}").')
                return redirect('Home')
            rssdIDs = mylist

        elif banks == "US banks in Bank Peer Group":
            usbanksinBankPeerGroup = request.POST['usbanksinBankPeerGroup']
            rssdSelectedBanks = banks + " - " + getPeerGroup(usbanksinBankPeerGroup)
            mylist = getRequiredRSSDIDs(banks, usbanksinBankPeerGroup, "pass")
            rssdIDs = mylist

        elif banks == "Single US Bank":
            singleUSBank = request.POST['singleusbank2']
            mylist = int(singleUSBank)
            rssdSelectedBanks = getSingleBankName(mylist)
            rssdIDs = [mylist]
        elif banks == "All US banks":
            rssdSelectedBanks = "All US banks"

        # Storing values in the respective variables for periods
        if formPeriodsField == "4 consecutive quarterly reports ending":
            period = request.POST['consecutivequarterlyreportsending']
            periods = formPeriodsField
            p = DropdownMenu4Quarters.objects.get(id=period)
            periodSingleLabel = p.label
            q4 = LookupRange4Quarters.objects.filter(id=period)
            for q in q4:
                periodsList.append(q.value)
                periodsLabelsList.append(q.label)
        elif formPeriodsField == "4 consecutive year-end reports ending":
            periods = formPeriodsField
            period = request.POST['consecutiveyearendreportsending']
            p = DropdownMenu4Years.objects.get(id=period)
            periodSingleLabel = p.label
            q5 = LookupRange4Years.objects.filter(id=period)
            for q in q5:
                periodsList.append(q.value)
                periodsLabelsList.append(q.label)


        # RSSD IDs report page required dictionary
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "RID": singleUSBank,
            "DataCount": formDataItems,
            "SelectedPeriodL": periods+" "+periodSingleLabel,
            "PeriodLables": periodsLabelsList,
            "FPeriodsLables": f"{periodsLabelsList[0]},{periodsLabelsList[1]},{periodsLabelsList[2]},{periodsLabelsList[3]}",
            "Banks": banks,
            "PeriodSelection": periods,
            "SinglePeriodLabel": periodSingleLabel,
            "BranchesStateValue": usbankswithbranchesinState,
            "BLocation": usbankswithbranchesnearLocation,
            "Milesdistance": milesDistance,
            "PGroup": usbanksinBankPeerGroup,
            "RSSDIDs": rssdIDs
        }

        # Handling all the cases and sending data to the report template according to the user input
        # All US Banks
        if banks == "All US banks" and formDataItems == "1":
            # Getting data from the bank data table via smart logics
            d = getAllBanksData(request,formDataItems,periodsList,[dataField1])
            return render(request,"report.html",{"Data":d,"RequiredItems":requiredItems})

        elif banks == "All US banks" and formDataItems == "2":
            d = getAllBanksData(request,formDataItems, periodsList, [dataField1,dataField2])
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        elif banks == "All US banks" and formDataItems == "3":
            d = getAllBanksData(request, formDataItems, periodsList, [dataField1, dataField2, dataField3])
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        elif banks == "All US banks" and formDataItems == "4":
            d = getAllBanksData(request, formDataItems, periodsList, [dataField1, dataField2, dataField3,dataField4])
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        elif banks == "All US banks" and formDataItems == "5":
            d = getAllBanksData(request, formDataItems, periodsList, [dataField1, dataField2, dataField3,dataField4,dataField5])
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        elif banks == "All US banks" and formDataItems == "6":
            d = getAllBanksData(request, formDataItems, periodsList, [dataField1, dataField2, dataField3,dataField4,dataField5,dataField6])
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        # Banks with RSSDs
        elif banks != "All US banks" and formDataItems == "1":
            d = getRSSDBanksData(request,formDataItems, periodsList,[dataField1],rssdIDs)
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        elif banks != "All US banks" and formDataItems == "2":
            d = getRSSDBanksData(request,formDataItems, periodsList,[dataField1,dataField2],rssdIDs)
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        elif banks != "All US banks" and formDataItems == "3":
            d = getRSSDBanksData(request,formDataItems, periodsList,[dataField1,dataField2,dataField3],rssdIDs)
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        elif banks != "All US banks" and formDataItems == "4":
            d = getRSSDBanksData(request,formDataItems, periodsList,[dataField1,dataField2,dataField3,dataField4],rssdIDs)
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        elif banks != "All US banks" and formDataItems == "5":
            d = getRSSDBanksData(request,formDataItems, periodsList,[dataField1,dataField2,dataField3,dataField4,dataField5],rssdIDs)
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

        elif banks != "All US banks" and formDataItems == "6":
            d = getRSSDBanksData(request,formDataItems, periodsList,[dataField1,dataField2,dataField3,dataField4,dataField5,dataField6],rssdIDs)
            return render(request, "report.html", {"Data": d, "RequiredItems": requiredItems})

    else:
        return render(request,'invalid-request.html')
