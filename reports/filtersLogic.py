from .models import *
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from urllib.parse import unquote
from reports.filtersSmartLogics import getRSSDLoadMSortBNClearFl,dynamicRangePeriods, getFromTo, getRequiredRSSDIDs, dynamicRange, sortColumn, dynamicSortRSSDIDs, getFirstColumn, getPeriodIndex, dynamicRangeRSSDIds,getLoadMSortBNClearFl
from .bankdataFields import *
from .locationGeocoding import *
from .graphs import getAverageGraphData, getAverageGraphDataRSSD
from django.db.models import Q
import string
from reports.smartLogics import securityCheck

# filters main view
def filterReportView(request):
    if securityCheck(request) == False:
        return render(request,'invalid-request.html')
    # Getting all url variables values
    requestType = request.GET.get('req')
    dataCount = request.GET.get('count')
    periods = request.GET.get('periods')
    pLables = request.GET.get('lableslist')
    columns = request.GET.get('columns')
    banks = request.GET.get('bank')
    range1 = request.GET.get('f1')
    range2 = request.GET.get('f2')
    sort = request.GET.get('sort')
    bnsort = request.GET.get('bnsort')
    rangeFilter = request.GET.get('range')
    selectedPeriodLabel = request.GET.get('speriod')
    selectedQuarterLabel = request.GET.get('slabel')
    branchState = request.GET.get('bstates')
    branchesLocation = request.GET.get('blocation')
    milesDistance = request.GET.get('m')
    peerGroup = request.GET.get('pgroup')
    rssdID = request.GET.get('rid')
    rangesList = request.GET.get('rangeslist')
    sortsList = request.GET.get('sortslist')
    # getting range values from url parameters
    fromRange = request.GET.get('r1')
    toRange = request.GET.get('r2')
    # unquoting some variables
    banks = unquote(banks)
    selectedPeriodLabel = unquote(selectedPeriodLabel)
    selectedQuarterLabel = unquote(selectedQuarterLabel)
    # converting important variables into list
    periods = periods.split(",")
    columns = columns.split(",")
    # splitting period lables
    pLables = pLables.split(",")

    # storing sort in the session
    mySortList = sortsList.split(',')
    request.session['sort'] = sort
    print(mySortList)
    # rssd ids report page dictionary variables
    rssdSelectedBanks = None
    rssdSelectedPeriod = selectedPeriodLabel+" "+selectedQuarterLabel

    # Getting RSSD IDs
    rssdIDs = None
    if banks == "US banks with branches in State":
        rssdSelectedBanks = banks+" - "+getStateLabel(branchState)
        mylist = getRequiredRSSDIDs(banks, branchState, "pass")
        rssdIDs = mylist

    elif banks == "US banks with branches near Location":
        rssdSelectedBanks = "Location: "+string.capwords(branchesLocation)+" within "+ milesDistance+" Miles"
        print(rssdSelectedBanks)
        mylist = getRequiredRSSDIDs(banks, branchesLocation, milesDistance)
        rssdIDs = mylist

    elif banks == "US banks in Bank Peer Group":
        rssdSelectedBanks = banks+" - "+getPeerGroup(peerGroup)
        mylist = getRequiredRSSDIDs(banks, peerGroup, "pass")
        rssdIDs = mylist

    elif banks == "Single US Bank":
        mylist = int(rssdID)
        rssdSelectedBanks = getSingleBankName(mylist)
        rssdIDs = [mylist]
    # RSSD IDs report page required dictionary
    rssdRequiredData = {
        "SelectedBanksL": rssdSelectedBanks,
        "SelectedPeriodL": rssdSelectedPeriod,
        "PeriodLables": pLables,
        "RangesList": rangesList.split(","),
        "SortsList": sortsList.split(","),
        "RSSDIDs": rssdIDs
    }


    # ========== Filter checks for loadmore reports with All US banks option ================================= #
    # Filter checks for load more reports for all us banks
    if requestType == requestType and dataCount == "1" and banks == "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0]).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total,requestType)
        Column1 = getColumnName(columns[0])
        b_rssdID = BankData.objects.filter(period=periods[0]).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType,periods[0],Column1,myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType,periods[1],Column1,myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType,periods[2],Column1,myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType,periods[3],Column1,myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "2" and banks == "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0]).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        b_rssdID = BankData.objects.filter(period=periods[0]).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "3" and banks == "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0]).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        b_rssdID = BankData.objects.filter(period=periods[0]).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        p9 = getLoadMSortBNClearFl(request,requestType, periods[0], Column3, myIds,bnsort,rn[0],rn[1])
        p10 = getLoadMSortBNClearFl(request,requestType, periods[1], Column3, myIds,bnsort,rn[0],rn[1])
        p11 = getLoadMSortBNClearFl(request,requestType, periods[2], Column3, myIds,bnsort,rn[0],rn[1])
        p12 = getLoadMSortBNClearFl(request,requestType, periods[3], Column3, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "4" and banks == "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0]).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        b_rssdID = BankData.objects.filter(period=periods[0]).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        p9 = getLoadMSortBNClearFl(request,requestType, periods[0], Column3, myIds,bnsort,rn[0],rn[1])
        p10 = getLoadMSortBNClearFl(request,requestType, periods[1], Column3, myIds,bnsort,rn[0],rn[1])
        p11 = getLoadMSortBNClearFl(request,requestType, periods[2], Column3, myIds,bnsort,rn[0],rn[1])
        p12 = getLoadMSortBNClearFl(request,requestType, periods[3], Column3, myIds,bnsort,rn[0],rn[1])
        p13 = getLoadMSortBNClearFl(request,requestType, periods[0], Column4, myIds,bnsort,rn[0],rn[1])
        p14 = getLoadMSortBNClearFl(request,requestType, periods[1], Column4, myIds,bnsort,rn[0],rn[1])
        p15 = getLoadMSortBNClearFl(request,requestType, periods[2], Column4, myIds,bnsort,rn[0],rn[1])
        p16 = getLoadMSortBNClearFl(request,requestType, periods[3], Column4, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3,Column4]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "5" and banks == "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0]).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        b_rssdID = BankData.objects.filter(period=periods[0]).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        p9 = getLoadMSortBNClearFl(request,requestType, periods[0], Column3, myIds,bnsort,rn[0],rn[1])
        p10 = getLoadMSortBNClearFl(request,requestType, periods[1], Column3, myIds,bnsort,rn[0],rn[1])
        p11 = getLoadMSortBNClearFl(request,requestType, periods[2], Column3, myIds,bnsort,rn[0],rn[1])
        p12 = getLoadMSortBNClearFl(request,requestType, periods[3], Column3, myIds,bnsort,rn[0],rn[1])
        p13 = getLoadMSortBNClearFl(request,requestType, periods[0], Column4, myIds,bnsort,rn[0],rn[1])
        p14 = getLoadMSortBNClearFl(request,requestType, periods[1], Column4, myIds,bnsort,rn[0],rn[1])
        p15 = getLoadMSortBNClearFl(request,requestType, periods[2], Column4, myIds,bnsort,rn[0],rn[1])
        p16 = getLoadMSortBNClearFl(request,requestType, periods[3], Column4, myIds,bnsort,rn[0],rn[1])
        p17 = getLoadMSortBNClearFl(request,requestType, periods[0], Column5, myIds,bnsort,rn[0],rn[1])
        p18 = getLoadMSortBNClearFl(request,requestType, periods[1], Column5, myIds,bnsort,rn[0],rn[1])
        p19 = getLoadMSortBNClearFl(request,requestType, periods[2], Column5, myIds,bnsort,rn[0],rn[1])
        p20 = getLoadMSortBNClearFl(request,requestType, periods[3], Column5, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "6" and banks == "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0]).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        Column6 = getColumnName(columns[5])
        b_rssdID = BankData.objects.filter(period=periods[0]).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        p9 = getLoadMSortBNClearFl(request,requestType, periods[0], Column3, myIds,bnsort,rn[0],rn[1])
        p10 = getLoadMSortBNClearFl(request,requestType, periods[1], Column3, myIds,bnsort,rn[0],rn[1])
        p11 = getLoadMSortBNClearFl(request,requestType, periods[2], Column3, myIds,bnsort,rn[0],rn[1])
        p12 = getLoadMSortBNClearFl(request,requestType, periods[3], Column3, myIds,bnsort,rn[0],rn[1])
        p13 = getLoadMSortBNClearFl(request,requestType, periods[0], Column4, myIds,bnsort,rn[0],rn[1])
        p14 = getLoadMSortBNClearFl(request,requestType, periods[1], Column4, myIds,bnsort,rn[0],rn[1])
        p15 = getLoadMSortBNClearFl(request,requestType, periods[2], Column4, myIds,bnsort,rn[0],rn[1])
        p16 = getLoadMSortBNClearFl(request,requestType, periods[3], Column4, myIds,bnsort,rn[0],rn[1])
        p17 = getLoadMSortBNClearFl(request,requestType, periods[0], Column5, myIds,bnsort,rn[0],rn[1])
        p18 = getLoadMSortBNClearFl(request,requestType, periods[1], Column5, myIds,bnsort,rn[0],rn[1])
        p19 = getLoadMSortBNClearFl(request,requestType, periods[2], Column5, myIds,bnsort,rn[0],rn[1])
        p20 = getLoadMSortBNClearFl(request,requestType, periods[3], Column5, myIds,bnsort,rn[0],rn[1])
        p21 = getLoadMSortBNClearFl(request,requestType, periods[0], Column6, myIds,bnsort,rn[0],rn[1])
        p22 = getLoadMSortBNClearFl(request,requestType, periods[1], Column6, myIds,bnsort,rn[0],rn[1])
        p23 = getLoadMSortBNClearFl(request,requestType, periods[2], Column6, myIds,bnsort,rn[0],rn[1])
        p24 = getLoadMSortBNClearFl(request,requestType, periods[3], Column6, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "Period21": p21,
            "Period22": p22,
            "Period23": p23,
            "Period24": p24,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5,Column6]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    # Filter checks for load more, sort and clear filters reports for rssd Ids
    elif requestType == requestType and dataCount == "1" and banks != "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total,requestType)
        Column1 = getColumnName(columns[0])
        b_rssdID = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType,periods[0],Column1,myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType,periods[1],Column1,myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType,periods[2],Column1,myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType,periods[3],Column1,myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs,
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "2" and banks != "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        b_rssdID = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "3" and banks != "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        b_rssdID = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        p9 = getLoadMSortBNClearFl(request,requestType, periods[0], Column3, myIds,bnsort,rn[0],rn[1])
        p10 = getLoadMSortBNClearFl(request,requestType, periods[1], Column3, myIds,bnsort,rn[0],rn[1])
        p11 = getLoadMSortBNClearFl(request,requestType, periods[2], Column3, myIds,bnsort,rn[0],rn[1])
        p12 = getLoadMSortBNClearFl(request,requestType, periods[3], Column3, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "4" and banks != "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        b_rssdID = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        p9 = getLoadMSortBNClearFl(request,requestType, periods[0], Column3, myIds,bnsort,rn[0],rn[1])
        p10 = getLoadMSortBNClearFl(request,requestType, periods[1], Column3, myIds,bnsort,rn[0],rn[1])
        p11 = getLoadMSortBNClearFl(request,requestType, periods[2], Column3, myIds,bnsort,rn[0],rn[1])
        p12 = getLoadMSortBNClearFl(request,requestType, periods[3], Column3, myIds,bnsort,rn[0],rn[1])
        p13 = getLoadMSortBNClearFl(request,requestType, periods[0], Column4, myIds,bnsort,rn[0],rn[1])
        p14 = getLoadMSortBNClearFl(request,requestType, periods[1], Column4, myIds,bnsort,rn[0],rn[1])
        p15 = getLoadMSortBNClearFl(request,requestType, periods[2], Column4, myIds,bnsort,rn[0],rn[1])
        p16 = getLoadMSortBNClearFl(request,requestType, periods[3], Column4, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3,Column4],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "5" and banks != "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        b_rssdID = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        p9 = getLoadMSortBNClearFl(request,requestType, periods[0], Column3, myIds,bnsort,rn[0],rn[1])
        p10 = getLoadMSortBNClearFl(request,requestType, periods[1], Column3, myIds,bnsort,rn[0],rn[1])
        p11 = getLoadMSortBNClearFl(request,requestType, periods[2], Column3, myIds,bnsort,rn[0],rn[1])
        p12 = getLoadMSortBNClearFl(request,requestType, periods[3], Column3, myIds,bnsort,rn[0],rn[1])
        p13 = getLoadMSortBNClearFl(request,requestType, periods[0], Column4, myIds,bnsort,rn[0],rn[1])
        p14 = getLoadMSortBNClearFl(request,requestType, periods[1], Column4, myIds,bnsort,rn[0],rn[1])
        p15 = getLoadMSortBNClearFl(request,requestType, periods[2], Column4, myIds,bnsort,rn[0],rn[1])
        p16 = getLoadMSortBNClearFl(request,requestType, periods[3], Column4, myIds,bnsort,rn[0],rn[1])
        p17 = getLoadMSortBNClearFl(request,requestType, periods[0], Column5, myIds,bnsort,rn[0],rn[1])
        p18 = getLoadMSortBNClearFl(request,requestType, periods[1], Column5, myIds,bnsort,rn[0],rn[1])
        p19 = getLoadMSortBNClearFl(request,requestType, periods[2], Column5, myIds,bnsort,rn[0],rn[1])
        p20 = getLoadMSortBNClearFl(request,requestType, periods[3], Column5, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "6" and banks != "All US banks" and sort == '' and rangeFilter == '':
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list(getColumnName(columns[0])).count()
        rn = getFromTo(range1, range2, total, requestType)
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        Column6 = getColumnName(columns[5])
        b_rssdID = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list('rssd_id',flat=True)
        myIds = b_rssdID
        p1 = getLoadMSortBNClearFl(request,requestType, periods[0], Column1, myIds,bnsort,rn[0],rn[1])
        p2 = getLoadMSortBNClearFl(request,requestType, periods[1], Column1, myIds,bnsort,rn[0],rn[1])
        p3 = getLoadMSortBNClearFl(request,requestType, periods[2], Column1, myIds,bnsort,rn[0],rn[1])
        p4 = getLoadMSortBNClearFl(request,requestType, periods[3], Column1, myIds,bnsort,rn[0],rn[1])
        p5 = getLoadMSortBNClearFl(request,requestType, periods[0], Column2, myIds,bnsort,rn[0],rn[1])
        p6 = getLoadMSortBNClearFl(request,requestType, periods[1], Column2, myIds,bnsort,rn[0],rn[1])
        p7 = getLoadMSortBNClearFl(request,requestType, periods[2], Column2, myIds,bnsort,rn[0],rn[1])
        p8 = getLoadMSortBNClearFl(request,requestType, periods[3], Column2, myIds,bnsort,rn[0],rn[1])
        p9 = getLoadMSortBNClearFl(request,requestType, periods[0], Column3, myIds,bnsort,rn[0],rn[1])
        p10 = getLoadMSortBNClearFl(request,requestType, periods[1], Column3, myIds,bnsort,rn[0],rn[1])
        p11 = getLoadMSortBNClearFl(request,requestType, periods[2], Column3, myIds,bnsort,rn[0],rn[1])
        p12 = getLoadMSortBNClearFl(request,requestType, periods[3], Column3, myIds,bnsort,rn[0],rn[1])
        p13 = getLoadMSortBNClearFl(request,requestType, periods[0], Column4, myIds,bnsort,rn[0],rn[1])
        p14 = getLoadMSortBNClearFl(request,requestType, periods[1], Column4, myIds,bnsort,rn[0],rn[1])
        p15 = getLoadMSortBNClearFl(request,requestType, periods[2], Column4, myIds,bnsort,rn[0],rn[1])
        p16 = getLoadMSortBNClearFl(request,requestType, periods[3], Column4, myIds,bnsort,rn[0],rn[1])
        p17 = getLoadMSortBNClearFl(request,requestType, periods[0], Column5, myIds,bnsort,rn[0],rn[1])
        p18 = getLoadMSortBNClearFl(request,requestType, periods[1], Column5, myIds,bnsort,rn[0],rn[1])
        p19 = getLoadMSortBNClearFl(request,requestType, periods[2], Column5, myIds,bnsort,rn[0],rn[1])
        p20 = getLoadMSortBNClearFl(request,requestType, periods[3], Column5, myIds,bnsort,rn[0],rn[1])
        p21 = getLoadMSortBNClearFl(request,requestType, periods[0], Column6, myIds,bnsort,rn[0],rn[1])
        p22 = getLoadMSortBNClearFl(request,requestType, periods[1], Column6, myIds,bnsort,rn[0],rn[1])
        p23 = getLoadMSortBNClearFl(request,requestType, periods[2], Column6, myIds,bnsort,rn[0],rn[1])
        p24 = getLoadMSortBNClearFl(request,requestType, periods[3], Column6, myIds,bnsort,rn[0],rn[1])
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": getRSSDLoadMSortBNClearFl(requestType,periods[0],myIds,bnsort,rn[0],rn[1]),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "Period21": p21,
            "Period22": p22,
            "Period23": p23,
            "Period24": p24,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5,Column6],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": total
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})


    # getting reports in sort with load more function
    elif dataCount == "1" and banks == "All US banks" and sort != '' and rangeFilter == '' and requestType == requestType:
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        firstColumn = getFirstColumn(sort, [Column1])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]

        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0], total, targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1], total, targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2], total, targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3], total, targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "2" and banks == "All US banks" and sort != '' and rangeFilter == '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        firstColumn = getFirstColumn(sort, [Column1, Column2])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0],total,targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1],total,targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2],total,targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3],total,targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0],total,targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1],total,targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2],total,targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3],total,targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    # Progress 3
    elif requestType == requestType and dataCount == "3" and banks == "All US banks" and sort != '' and rangeFilter == '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        firstColumn = getFirstColumn(sort, [Column1, Column2, Column3])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0],total,targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1],total,targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2],total,targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3],total,targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0],total,targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1],total,targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2],total,targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3],total,targetRIDs)
        p9 = dynamicSortRSSDIDs(request,sort, 31, Column3, periods[0],total,targetRIDs)
        p10 = dynamicSortRSSDIDs(request,sort, 32, Column3, periods[1],total,targetRIDs)
        p11 = dynamicSortRSSDIDs(request,sort, 33, Column3, periods[2],total,targetRIDs)
        p12 = dynamicSortRSSDIDs(request,sort, 34, Column3, periods[3],total,targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "4" and banks == "All US banks" and sort != '' and rangeFilter == '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        firstColumn = getFirstColumn(sort, [Column1, Column2, Column3, Column4])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0], total, targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1], total, targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2], total, targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3], total, targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0], total, targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1], total, targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2], total, targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3], total, targetRIDs)
        p9 = dynamicSortRSSDIDs(request,sort, 31, Column3, periods[0], total, targetRIDs)
        p10 = dynamicSortRSSDIDs(request,sort, 32, Column3, periods[1], total, targetRIDs)
        p11 = dynamicSortRSSDIDs(request,sort, 33, Column3, periods[2], total, targetRIDs)
        p12 = dynamicSortRSSDIDs(request,sort, 34, Column3, periods[3], total, targetRIDs)
        p13 = dynamicSortRSSDIDs(request,sort, 41, Column4, periods[0], total, targetRIDs)
        p14 = dynamicSortRSSDIDs(request,sort, 42, Column4, periods[1], total, targetRIDs)
        p15 = dynamicSortRSSDIDs(request,sort, 43, Column4, periods[2], total, targetRIDs)
        p16 = dynamicSortRSSDIDs(request,sort, 44, Column4, periods[3], total, targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3,Column4]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "5" and banks == "All US banks" and sort != '' and rangeFilter == '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        firstColumn = getFirstColumn(sort, [Column1, Column2, Column3, Column4, Column5])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0], total, targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1], total, targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2], total, targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3], total, targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0], total, targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1], total, targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2], total, targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3], total, targetRIDs)
        p9 = dynamicSortRSSDIDs(request,sort, 31, Column3, periods[0], total, targetRIDs)
        p10 = dynamicSortRSSDIDs(request,sort, 32, Column3, periods[1], total, targetRIDs)
        p11 = dynamicSortRSSDIDs(request,sort, 33, Column3, periods[2], total, targetRIDs)
        p12 = dynamicSortRSSDIDs(request,sort, 34, Column3, periods[3], total, targetRIDs)
        p13 = dynamicSortRSSDIDs(request,sort, 41, Column4, periods[0], total, targetRIDs)
        p14 = dynamicSortRSSDIDs(request,sort, 42, Column4, periods[1], total, targetRIDs)
        p15 = dynamicSortRSSDIDs(request,sort, 43, Column4, periods[2], total, targetRIDs)
        p16 = dynamicSortRSSDIDs(request,sort, 44, Column4, periods[3], total, targetRIDs)
        p17 = dynamicSortRSSDIDs(request,sort, 51, Column5, periods[0], total, targetRIDs)
        p18 = dynamicSortRSSDIDs(request,sort, 52, Column5, periods[1], total, targetRIDs)
        p19 = dynamicSortRSSDIDs(request,sort, 53, Column5, periods[2], total, targetRIDs)
        p20 = dynamicSortRSSDIDs(request,sort, 54, Column5, periods[3], total, targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "6" and banks == "All US banks" and sort != '' and rangeFilter == '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        Column6 = getColumnName(columns[5])
        firstColumn = getFirstColumn(sort, [Column1, Column2, Column3, Column4, Column5, Column6])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex]).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0], total, targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1], total, targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2], total, targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3], total, targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0], total, targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1], total, targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2], total, targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3], total, targetRIDs)
        p9 = dynamicSortRSSDIDs(request,sort, 31, Column3, periods[0], total, targetRIDs)
        p10 = dynamicSortRSSDIDs(request,sort, 32, Column3, periods[1], total, targetRIDs)
        p11 = dynamicSortRSSDIDs(request,sort, 33, Column3, periods[2], total, targetRIDs)
        p12 = dynamicSortRSSDIDs(request,sort, 34, Column3, periods[3], total, targetRIDs)
        p13 = dynamicSortRSSDIDs(request,sort, 41, Column4, periods[0], total, targetRIDs)
        p14 = dynamicSortRSSDIDs(request,sort, 42, Column4, periods[1], total, targetRIDs)
        p15 = dynamicSortRSSDIDs(request,sort, 43, Column4, periods[2], total, targetRIDs)
        p16 = dynamicSortRSSDIDs(request,sort, 44, Column4, periods[3], total, targetRIDs)
        p17 = dynamicSortRSSDIDs(request,sort, 51, Column5, periods[0], total, targetRIDs)
        p18 = dynamicSortRSSDIDs(request,sort, 52, Column5, periods[1], total, targetRIDs)
        p19 = dynamicSortRSSDIDs(request,sort, 53, Column5, periods[2], total, targetRIDs)
        p20 = dynamicSortRSSDIDs(request,sort, 54, Column5, periods[3], total, targetRIDs)
        p21 = dynamicSortRSSDIDs(request,sort, 61, Column6, periods[0], total, targetRIDs)
        p22 = dynamicSortRSSDIDs(request,sort, 62, Column6, periods[1], total, targetRIDs)
        p23 = dynamicSortRSSDIDs(request,sort, 63, Column6, periods[2], total, targetRIDs)
        p24 = dynamicSortRSSDIDs(request,sort, 64, Column6, periods[3], total, targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "Period21": p21,
            "Period22": p22,
            "Period23": p23,
            "Period24": p24,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5,Column6]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})



    # getting reports in range with load more function
    elif dataCount == "1" and banks == "All US banks" and sort == '' and rangeFilter != '' and requestType == requestType:
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        firstColumn = getFirstColumn(rangeFilter, [Column1])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex]).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRange(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "2" and banks == "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex]).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRange(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter, myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter, myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter, myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "3" and banks == "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2, Column3])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex]).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRange(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter,myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter,myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter,myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter,myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter,myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter,myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter,myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter,myRangeList)
        p9 = dynamicRangePeriods(fromRange, toRange, periods[0], Column3, 31, rangeFilter,myRangeList)
        p10 = dynamicRangePeriods(fromRange, toRange, periods[1], Column3, 32, rangeFilter,myRangeList)
        p11 = dynamicRangePeriods(fromRange, toRange, periods[2], Column3, 33, rangeFilter,myRangeList)
        p12 = dynamicRangePeriods(fromRange, toRange, periods[3], Column3, 34, rangeFilter,myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "4" and banks == "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2, Column3,Column4])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex]).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRange(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter, myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter, myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter, myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter, myRangeList)
        p9 = dynamicRangePeriods(fromRange, toRange, periods[0], Column3, 31, rangeFilter, myRangeList)
        p10 = dynamicRangePeriods(fromRange, toRange, periods[1], Column3, 32, rangeFilter, myRangeList)
        p11 = dynamicRangePeriods(fromRange, toRange, periods[2], Column3, 33, rangeFilter, myRangeList)
        p12 = dynamicRangePeriods(fromRange, toRange, periods[3], Column3, 34, rangeFilter, myRangeList)
        p13 = dynamicRangePeriods(fromRange, toRange, periods[0], Column4, 41, rangeFilter, myRangeList)
        p14 = dynamicRangePeriods(fromRange, toRange, periods[1], Column4, 42, rangeFilter, myRangeList)
        p15 = dynamicRangePeriods(fromRange, toRange, periods[2], Column4, 43, rangeFilter, myRangeList)
        p16 = dynamicRangePeriods(fromRange, toRange, periods[3], Column4, 44, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3,Column4]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "5" and banks == "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2, Column3, Column4, Column5])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex]).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRange(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter, myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter, myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter, myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter, myRangeList)
        p9 = dynamicRangePeriods(fromRange, toRange, periods[0], Column3, 31, rangeFilter, myRangeList)
        p10 = dynamicRangePeriods(fromRange, toRange, periods[1], Column3, 32, rangeFilter, myRangeList)
        p11 = dynamicRangePeriods(fromRange, toRange, periods[2], Column3, 33, rangeFilter, myRangeList)
        p12 = dynamicRangePeriods(fromRange, toRange, periods[3], Column3, 34, rangeFilter, myRangeList)
        p13 = dynamicRangePeriods(fromRange, toRange, periods[0], Column4, 41, rangeFilter, myRangeList)
        p14 = dynamicRangePeriods(fromRange, toRange, periods[1], Column4, 42, rangeFilter, myRangeList)
        p15 = dynamicRangePeriods(fromRange, toRange, periods[2], Column4, 43, rangeFilter, myRangeList)
        p16 = dynamicRangePeriods(fromRange, toRange, periods[3], Column4, 44, rangeFilter, myRangeList)
        p17 = dynamicRangePeriods(fromRange, toRange, periods[0], Column5, 51, rangeFilter, myRangeList)
        p18 = dynamicRangePeriods(fromRange, toRange, periods[1], Column5, 52, rangeFilter, myRangeList)
        p19 = dynamicRangePeriods(fromRange, toRange, periods[2], Column5, 53, rangeFilter, myRangeList)
        p20 = dynamicRangePeriods(fromRange, toRange, periods[3], Column5, 54, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "6" and banks == "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0]).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        Column6 = getColumnName(columns[5])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2, Column3, Column4, Column5, Column6])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex]).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRange(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter, myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter, myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter, myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter, myRangeList)
        p9 = dynamicRangePeriods(fromRange, toRange, periods[0], Column3, 31, rangeFilter, myRangeList)
        p10 = dynamicRangePeriods(fromRange, toRange, periods[1], Column3, 32, rangeFilter, myRangeList)
        p11 = dynamicRangePeriods(fromRange, toRange, periods[2], Column3, 33, rangeFilter, myRangeList)
        p12 = dynamicRangePeriods(fromRange, toRange, periods[3], Column3, 34, rangeFilter, myRangeList)
        p13 = dynamicRangePeriods(fromRange, toRange, periods[0], Column4, 41, rangeFilter, myRangeList)
        p14 = dynamicRangePeriods(fromRange, toRange, periods[1], Column4, 42, rangeFilter, myRangeList)
        p15 = dynamicRangePeriods(fromRange, toRange, periods[2], Column4, 43, rangeFilter, myRangeList)
        p16 = dynamicRangePeriods(fromRange, toRange, periods[3], Column4, 44, rangeFilter, myRangeList)
        p17 = dynamicRangePeriods(fromRange, toRange, periods[0], Column5, 51, rangeFilter, myRangeList)
        p18 = dynamicRangePeriods(fromRange, toRange, periods[1], Column5, 52, rangeFilter, myRangeList)
        p19 = dynamicRangePeriods(fromRange, toRange, periods[2], Column5, 53, rangeFilter, myRangeList)
        p20 = dynamicRangePeriods(fromRange, toRange, periods[3], Column5, 54, rangeFilter, myRangeList)
        p21 = dynamicRangePeriods(fromRange, toRange, periods[0], Column6, 61, rangeFilter, myRangeList)
        p22 = dynamicRangePeriods(fromRange, toRange, periods[1], Column6, 62, rangeFilter, myRangeList)
        p23 = dynamicRangePeriods(fromRange, toRange, periods[2], Column6, 63, rangeFilter, myRangeList)
        p24 = dynamicRangePeriods(fromRange, toRange, periods[3], Column6, 64, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "Period21": p21,
            "Period22": p22,
            "Period23": p23,
            "Period24": p24,
            "AverageGraphsData": getAverageGraphData(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5,Column6]),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": banks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})



    # ========= RSSD IDs section - Getting filter records with RSSD IDs =========== #
        # getting reports in sort with load more function
    elif dataCount == "1" and banks != "All US banks" and sort != '' and rangeFilter == '' and requestType == requestType:
        # storing sort in session
        totalUnique = BankData.objects.filter(period=periods[0],rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        firstColumn = getFirstColumn(sort, [Column1])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0], total, targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1], total, targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2], total, targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3], total, targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "2" and banks != "All US banks" and sort != '' and rangeFilter == '':
        # storing sort in session
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        firstColumn = getFirstColumn(sort, [Column1, Column2])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0],total,targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1],total,targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2],total,targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3],total,targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0],total,targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1],total,targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2],total,targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3],total,targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    # Progress 3
    elif requestType == requestType and dataCount == "3" and banks != "All US banks" and sort != '' and rangeFilter == '':
        # storing sort in session
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        firstColumn = getFirstColumn(sort, [Column1, Column2, Column3])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0],total,targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1],total,targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2],total,targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3],total,targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0],total,targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1],total,targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2],total,targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3],total,targetRIDs)
        p9 = dynamicSortRSSDIDs(request,sort, 31, Column3, periods[0],total,targetRIDs)
        p10 = dynamicSortRSSDIDs(request,sort, 32, Column3, periods[1],total,targetRIDs)
        p11 = dynamicSortRSSDIDs(request,sort, 33, Column3, periods[2],total,targetRIDs)
        p12 = dynamicSortRSSDIDs(request,sort, 34, Column3, periods[3],total,targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "4" and banks != "All US banks" and sort != '' and rangeFilter == '':
        # storing sort in session
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        firstColumn = getFirstColumn(sort, [Column1, Column2, Column3, Column4])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0], total, targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1], total, targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2], total, targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3], total, targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0], total, targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1], total, targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2], total, targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3], total, targetRIDs)
        p9 = dynamicSortRSSDIDs(request,sort, 31, Column3, periods[0], total, targetRIDs)
        p10 = dynamicSortRSSDIDs(request,sort, 32, Column3, periods[1], total, targetRIDs)
        p11 = dynamicSortRSSDIDs(request,sort, 33, Column3, periods[2], total, targetRIDs)
        p12 = dynamicSortRSSDIDs(request,sort, 34, Column3, periods[3], total, targetRIDs)
        p13 = dynamicSortRSSDIDs(request,sort, 41, Column4, periods[0], total, targetRIDs)
        p14 = dynamicSortRSSDIDs(request,sort, 42, Column4, periods[1], total, targetRIDs)
        p15 = dynamicSortRSSDIDs(request,sort, 43, Column4, periods[2], total, targetRIDs)
        p16 = dynamicSortRSSDIDs(request,sort, 44, Column4, periods[3], total, targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3,Column4],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "5" and banks != "All US banks" and sort != '' and rangeFilter == '':
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        firstColumn = getFirstColumn(sort, [Column1, Column2, Column3, Column4, Column5])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0], total, targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1], total, targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2], total, targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3], total, targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0], total, targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1], total, targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2], total, targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3], total, targetRIDs)
        p9 = dynamicSortRSSDIDs(request,sort, 31, Column3, periods[0], total, targetRIDs)
        p10 = dynamicSortRSSDIDs(request,sort, 32, Column3, periods[1], total, targetRIDs)
        p11 = dynamicSortRSSDIDs(request,sort, 33, Column3, periods[2], total, targetRIDs)
        p12 = dynamicSortRSSDIDs(request,sort, 34, Column3, periods[3], total, targetRIDs)
        p13 = dynamicSortRSSDIDs(request,sort, 41, Column4, periods[0], total, targetRIDs)
        p14 = dynamicSortRSSDIDs(request,sort, 42, Column4, periods[1], total, targetRIDs)
        p15 = dynamicSortRSSDIDs(request,sort, 43, Column4, periods[2], total, targetRIDs)
        p16 = dynamicSortRSSDIDs(request,sort, 44, Column4, periods[3], total, targetRIDs)
        p17 = dynamicSortRSSDIDs(request,sort, 51, Column5, periods[0], total, targetRIDs)
        p18 = dynamicSortRSSDIDs(request,sort, 52, Column5, periods[1], total, targetRIDs)
        p19 = dynamicSortRSSDIDs(request,sort, 53, Column5, periods[2], total, targetRIDs)
        p20 = dynamicSortRSSDIDs(request,sort, 54, Column5, periods[3], total, targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "6" and banks != "All US banks" and sort != '' and rangeFilter == '':
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        Column6 = getColumnName(columns[5])
        firstColumn = getFirstColumn(sort, [Column1, Column2, Column3, Column4, Column5, Column6])
        periodIndex = getPeriodIndex(sort)
        rangeTotal = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').count()
        # Getting total & range numbers
        rn = getFromTo(range1, range2, rangeTotal, requestType)
        b_rssdID = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list('rssd_id').order_by(
            sortColumn(request,firstColumn,mySortList))[rn[0]:rn[1]]
        targetRIDs = []
        for d in b_rssdID:
            targetRIDs.append(d[0])
        total = len(targetRIDs)
        p1 = dynamicSortRSSDIDs(request,sort, 11, Column1, periods[0], total, targetRIDs)
        p2 = dynamicSortRSSDIDs(request,sort, 12, Column1, periods[1], total, targetRIDs)
        p3 = dynamicSortRSSDIDs(request,sort, 13, Column1, periods[2], total, targetRIDs)
        p4 = dynamicSortRSSDIDs(request,sort, 14, Column1, periods[3], total, targetRIDs)
        p5 = dynamicSortRSSDIDs(request,sort, 21, Column2, periods[0], total, targetRIDs)
        p6 = dynamicSortRSSDIDs(request,sort, 22, Column2, periods[1], total, targetRIDs)
        p7 = dynamicSortRSSDIDs(request,sort, 23, Column2, periods[2], total, targetRIDs)
        p8 = dynamicSortRSSDIDs(request,sort, 24, Column2, periods[3], total, targetRIDs)
        p9 = dynamicSortRSSDIDs(request,sort, 31, Column3, periods[0], total, targetRIDs)
        p10 = dynamicSortRSSDIDs(request,sort, 32, Column3, periods[1], total, targetRIDs)
        p11 = dynamicSortRSSDIDs(request,sort, 33, Column3, periods[2], total, targetRIDs)
        p12 = dynamicSortRSSDIDs(request,sort, 34, Column3, periods[3], total, targetRIDs)
        p13 = dynamicSortRSSDIDs(request,sort, 41, Column4, periods[0], total, targetRIDs)
        p14 = dynamicSortRSSDIDs(request,sort, 42, Column4, periods[1], total, targetRIDs)
        p15 = dynamicSortRSSDIDs(request,sort, 43, Column4, periods[2], total, targetRIDs)
        p16 = dynamicSortRSSDIDs(request,sort, 44, Column4, periods[3], total, targetRIDs)
        p17 = dynamicSortRSSDIDs(request,sort, 51, Column5, periods[0], total, targetRIDs)
        p18 = dynamicSortRSSDIDs(request,sort, 52, Column5, periods[1], total, targetRIDs)
        p19 = dynamicSortRSSDIDs(request,sort, 53, Column5, periods[2], total, targetRIDs)
        p20 = dynamicSortRSSDIDs(request,sort, 54, Column5, periods[3], total, targetRIDs)
        p21 = dynamicSortRSSDIDs(request,sort, 61, Column6, periods[0], total, targetRIDs)
        p22 = dynamicSortRSSDIDs(request,sort, 62, Column6, periods[1], total, targetRIDs)
        p23 = dynamicSortRSSDIDs(request,sort, 63, Column6, periods[2], total, targetRIDs)
        p24 = dynamicSortRSSDIDs(request,sort, 64, Column6, periods[3], total, targetRIDs)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "Period21": p21,
            "Period22": p22,
            "Period23": p23,
            "Period24": p24,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5,Column6],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})


    # Range with RSSD IDs and load more functionality
    elif dataCount == "1" and banks != "All US banks" and sort == '' and rangeFilter != '' and requestType == requestType:
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        firstColumn = getFirstColumn(rangeFilter, [Column1])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRangeRSSDIds(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter,rssdIDs)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "2" and banks != "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRangeRSSDIds(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter,rssdIDs)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter, myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter, myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter, myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "3" and banks != "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2, Column3])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRangeRSSDIds(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter,rssdIDs)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter,myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter,myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter,myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter,myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter,myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter,myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter,myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter,myRangeList)
        p9 = dynamicRangePeriods(fromRange, toRange, periods[0], Column3, 31, rangeFilter,myRangeList)
        p10 = dynamicRangePeriods(fromRange, toRange, periods[1], Column3, 32, rangeFilter,myRangeList)
        p11 = dynamicRangePeriods(fromRange, toRange, periods[2], Column3, 33, rangeFilter,myRangeList)
        p12 = dynamicRangePeriods(fromRange, toRange, periods[3], Column3, 34, rangeFilter,myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "4" and banks != "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2, Column3,Column4])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRangeRSSDIds(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter,rssdIDs)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter, myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter, myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter, myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter, myRangeList)
        p9 = dynamicRangePeriods(fromRange, toRange, periods[0], Column3, 31, rangeFilter, myRangeList)
        p10 = dynamicRangePeriods(fromRange, toRange, periods[1], Column3, 32, rangeFilter, myRangeList)
        p11 = dynamicRangePeriods(fromRange, toRange, periods[2], Column3, 33, rangeFilter, myRangeList)
        p12 = dynamicRangePeriods(fromRange, toRange, periods[3], Column3, 34, rangeFilter, myRangeList)
        p13 = dynamicRangePeriods(fromRange, toRange, periods[0], Column4, 41, rangeFilter, myRangeList)
        p14 = dynamicRangePeriods(fromRange, toRange, periods[1], Column4, 42, rangeFilter, myRangeList)
        p15 = dynamicRangePeriods(fromRange, toRange, periods[2], Column4, 43, rangeFilter, myRangeList)
        p16 = dynamicRangePeriods(fromRange, toRange, periods[3], Column4, 44, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3,Column4],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "5" and banks != "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2, Column3, Column4, Column5])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRangeRSSDIds(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter,rssdIDs)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter, myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter, myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter, myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter, myRangeList)
        p9 = dynamicRangePeriods(fromRange, toRange, periods[0], Column3, 31, rangeFilter, myRangeList)
        p10 = dynamicRangePeriods(fromRange, toRange, periods[1], Column3, 32, rangeFilter, myRangeList)
        p11 = dynamicRangePeriods(fromRange, toRange, periods[2], Column3, 33, rangeFilter, myRangeList)
        p12 = dynamicRangePeriods(fromRange, toRange, periods[3], Column3, 34, rangeFilter, myRangeList)
        p13 = dynamicRangePeriods(fromRange, toRange, periods[0], Column4, 41, rangeFilter, myRangeList)
        p14 = dynamicRangePeriods(fromRange, toRange, periods[1], Column4, 42, rangeFilter, myRangeList)
        p15 = dynamicRangePeriods(fromRange, toRange, periods[2], Column4, 43, rangeFilter, myRangeList)
        p16 = dynamicRangePeriods(fromRange, toRange, periods[3], Column4, 44, rangeFilter, myRangeList)
        p17 = dynamicRangePeriods(fromRange, toRange, periods[0], Column5, 51, rangeFilter, myRangeList)
        p18 = dynamicRangePeriods(fromRange, toRange, periods[1], Column5, 52, rangeFilter, myRangeList)
        p19 = dynamicRangePeriods(fromRange, toRange, periods[2], Column5, 53, rangeFilter, myRangeList)
        p20 = dynamicRangePeriods(fromRange, toRange, periods[3], Column5, 54, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(","),
            "RSSDIDs": rssdIDs
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})

    elif requestType == requestType and dataCount == "6" and banks != "All US banks" and sort == '' and rangeFilter != '':
        totalUnique = BankData.objects.filter(period=periods[0], rssd_id__in=rssdIDs).values_list(
            getColumnName(columns[0])).count()
        Column1 = getColumnName(columns[0])
        Column2 = getColumnName(columns[1])
        Column3 = getColumnName(columns[2])
        Column4 = getColumnName(columns[3])
        Column5 = getColumnName(columns[4])
        Column6 = getColumnName(columns[5])
        firstColumn = getFirstColumn(rangeFilter, [Column1, Column2, Column3, Column4, Column5, Column6])
        periodIndex = getPeriodIndex(rangeFilter)
        # Getting total & range numbers
        total = BankData.objects.filter(period=periods[periodIndex],rssd_id__in=rssdIDs).values_list(firstColumn).count()
        rn = getFromTo(range1, range2, total, requestType)
        b_rssdID = BankData.objects.filter(
            **dynamicRangeRSSDIds(fromRange, toRange, periods[periodIndex], firstColumn, rangeFilter,
                           rangeFilter,rssdIDs)).values_list('rssd_id')[rn[0]:rn[1]]
        myRangeList = []
        for d in b_rssdID:
            myRangeList.append(d[0])
        p1 = dynamicRangePeriods(fromRange, toRange, periods[0], Column1, 11, rangeFilter, myRangeList)
        p2 = dynamicRangePeriods(fromRange, toRange, periods[1], Column1, 12, rangeFilter, myRangeList)
        p3 = dynamicRangePeriods(fromRange, toRange, periods[2], Column1, 13, rangeFilter, myRangeList)
        p4 = dynamicRangePeriods(fromRange, toRange, periods[3], Column1, 14, rangeFilter, myRangeList)
        p5 = dynamicRangePeriods(fromRange, toRange, periods[0], Column2, 21, rangeFilter, myRangeList)
        p6 = dynamicRangePeriods(fromRange, toRange, periods[1], Column2, 22, rangeFilter, myRangeList)
        p7 = dynamicRangePeriods(fromRange, toRange, periods[2], Column2, 23, rangeFilter, myRangeList)
        p8 = dynamicRangePeriods(fromRange, toRange, periods[3], Column2, 24, rangeFilter, myRangeList)
        p9 = dynamicRangePeriods(fromRange, toRange, periods[0], Column3, 31, rangeFilter, myRangeList)
        p10 = dynamicRangePeriods(fromRange, toRange, periods[1], Column3, 32, rangeFilter, myRangeList)
        p11 = dynamicRangePeriods(fromRange, toRange, periods[2], Column3, 33, rangeFilter, myRangeList)
        p12 = dynamicRangePeriods(fromRange, toRange, periods[3], Column3, 34, rangeFilter, myRangeList)
        p13 = dynamicRangePeriods(fromRange, toRange, periods[0], Column4, 41, rangeFilter, myRangeList)
        p14 = dynamicRangePeriods(fromRange, toRange, periods[1], Column4, 42, rangeFilter, myRangeList)
        p15 = dynamicRangePeriods(fromRange, toRange, periods[2], Column4, 43, rangeFilter, myRangeList)
        p16 = dynamicRangePeriods(fromRange, toRange, periods[3], Column4, 44, rangeFilter, myRangeList)
        p17 = dynamicRangePeriods(fromRange, toRange, periods[0], Column5, 51, rangeFilter, myRangeList)
        p18 = dynamicRangePeriods(fromRange, toRange, periods[1], Column5, 52, rangeFilter, myRangeList)
        p19 = dynamicRangePeriods(fromRange, toRange, periods[2], Column5, 53, rangeFilter, myRangeList)
        p20 = dynamicRangePeriods(fromRange, toRange, periods[3], Column5, 54, rangeFilter, myRangeList)
        p21 = dynamicRangePeriods(fromRange, toRange, periods[0], Column6, 61, rangeFilter, myRangeList)
        p22 = dynamicRangePeriods(fromRange, toRange, periods[1], Column6, 62, rangeFilter, myRangeList)
        p23 = dynamicRangePeriods(fromRange, toRange, periods[2], Column6, 63, rangeFilter, myRangeList)
        p24 = dynamicRangePeriods(fromRange, toRange, periods[3], Column6, 64, rangeFilter, myRangeList)
        data = {
            "ColumnHeadings": getRowColumnHeading(columns),
            "BankNamesColumn": b_rssdID,
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "Period9": p9,
            "Period10": p10,
            "Period11": p11,
            "Period12": p12,
            "Period13": p13,
            "Period14": p14,
            "Period15": p15,
            "Period16": p16,
            "Period17": p17,
            "Period18": p18,
            "Period19": p19,
            "Period20": p20,
            "Period21": p21,
            "Period22": p22,
            "Period23": p23,
            "Period24": p24,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periods, dataCount, [Column1,Column2,Column3,Column4,Column5,Column6],rssdIDs),
            "F1": rn[0],
            "F2": rn[1],
            "TotalUniqueBanks": totalUnique
        }
        requiredItems = {
            "SelectedBanksL": rssdSelectedBanks,
            "SelectedPeriodL": selectedPeriodLabel+" "+selectedQuarterLabel,
            "PeriodLables": pLables,
            "RangesList": rangesList.split(","),
            "SortsList": sortsList.split(",")
        }
        return render(request,'filtered-report.html',{"Data":data,"RequiredItems":requiredItems})
