from .models import *
from .bankdataFields import *
from .locationGeocoding import *
from .graphs import *
import itertools
from .filtersSmartLogics import replaceNonExistingRows
from django.shortcuts import render

# Getting sort rssd IDs
def getSortRSSDsBankNames(idsList,r1,r2):
    myIDs = []
    q = BankHq.objects.filter(rssd_id__in=idsList).values_list('rssd_id').distinct().order_by('bank')[r1:r2]
    for mylist in q:
        myIDs.append(mylist[0])
    return myIDs

# Getting period data for all banks with RSSD IDs
def getPeriodData(period,column,rssdIDs):
    total = len(rssdIDs)
    queryTotal = BankData.objects.filter(period=period,rssd_id__in=rssdIDs).values_list(column).count()
    if total == queryTotal:
        d = BankData.objects.filter(period=period,rssd_id__in=rssdIDs).extra(
            select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rssdIDs))},
            order_by=['manual']).values_list(column,flat=True)
        return d
    else:
        d = itertools.chain(BankData.objects.filter(period=period, rssd_id__in=rssdIDs).extra(
            select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rssdIDs))},
            order_by=['manual']).values_list(column, 'rssd_id'))
        rssd2 = []
        data = []
        for mydataList in d:
            data.append(mydataList[0])
            rssd2.append(mydataList[1])
        finalData = replaceNonExistingRows(rssdIDs, rssd2, data)
        return finalData


# getting data for all US banks data according to the data items
def getAllBanksData(request,dataCount,periodsList,labelColumnIds):
    totalReports = BankData.objects.filter(period=periodsList[0]).values_list(getColumnName(labelColumnIds[0])).count()
    requiredRSSIDs = BankData.objects.filter(period=periodsList[0]).values_list('rssd_id',flat=True)
    sortList = requiredRSSIDs
    sortedList = getSortRSSDsBankNames(sortList,0,30)
    bnames = BankData.objects.filter(period=periodsList[0],rssd_id__in=sortedList).extra(
            select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, sortedList))},
            order_by=['manual']).values_list('rssd_id')

    if dataCount == "1":
        Column1 = getColumnName(labelColumnIds[0])
        p1 = getPeriodData(periodsList[0],Column1,sortedList)
        p2 = getPeriodData(periodsList[1],Column1,sortedList)
        p3 = getPeriodData(periodsList[2],Column1,sortedList)
        p4 = getPeriodData(periodsList[3],Column1,sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "AverageGraphsData": getAverageGraphData(request,periodsList,dataCount,[Column1]),
            "ColumnNames": f"{labelColumnIds[0]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "2":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        print(totalReports)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "AverageGraphsData": getAverageGraphData(request, periodsList, dataCount, [Column1,Column2]),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "3":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        Column3 = getColumnName(labelColumnIds[2])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        p9 = getPeriodData(periodsList[0], Column3, sortedList)
        p10 = getPeriodData(periodsList[1], Column3, sortedList)
        p11 = getPeriodData(periodsList[2], Column3, sortedList)
        p12 = getPeriodData(periodsList[3], Column3, sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
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
            "AverageGraphsData": getAverageGraphData(request, periodsList, dataCount, [Column1, Column2, Column3]),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]},{labelColumnIds[2]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "4":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        Column3 = getColumnName(labelColumnIds[2])
        Column4 = getColumnName(labelColumnIds[3])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        p9 = getPeriodData(periodsList[0], Column3, sortedList)
        p10 = getPeriodData(periodsList[1], Column3, sortedList)
        p11 = getPeriodData(periodsList[2], Column3, sortedList)
        p12 = getPeriodData(periodsList[3], Column3, sortedList)
        p13 = getPeriodData(periodsList[0], Column4, sortedList)
        p14 = getPeriodData(periodsList[1], Column4, sortedList)
        p15 = getPeriodData(periodsList[2], Column4, sortedList)
        p16 = getPeriodData(periodsList[3], Column4, sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
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
            "AverageGraphsData": getAverageGraphData(request, periodsList, dataCount, [Column1, Column2, Column3, Column4]),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]},{labelColumnIds[2]},{labelColumnIds[3]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "5":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        Column3 = getColumnName(labelColumnIds[2])
        Column4 = getColumnName(labelColumnIds[3])
        Column5 = getColumnName(labelColumnIds[4])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        p9 = getPeriodData(periodsList[0], Column3, sortedList)
        p10 = getPeriodData(periodsList[1], Column3, sortedList)
        p11 = getPeriodData(periodsList[2], Column3, sortedList)
        p12 = getPeriodData(periodsList[3], Column3, sortedList)
        p13 = getPeriodData(periodsList[0], Column4, sortedList)
        p14 = getPeriodData(periodsList[1], Column4, sortedList)
        p15 = getPeriodData(periodsList[2], Column4, sortedList)
        p16 = getPeriodData(periodsList[3], Column4, sortedList)
        p17 = getPeriodData(periodsList[0], Column5, sortedList)
        p18 = getPeriodData(periodsList[1], Column5, sortedList)
        p19 = getPeriodData(periodsList[2], Column5, sortedList)
        p20 = getPeriodData(periodsList[3], Column5, sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
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
            "AverageGraphsData": getAverageGraphData(request, periodsList, dataCount,
                                                     [Column1, Column2, Column3, Column4, Column5]),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]},{labelColumnIds[2]},{labelColumnIds[3]},{labelColumnIds[4]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "6":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        Column3 = getColumnName(labelColumnIds[2])
        Column4 = getColumnName(labelColumnIds[3])
        Column5 = getColumnName(labelColumnIds[4])
        Column6 = getColumnName(labelColumnIds[5])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        p9 = getPeriodData(periodsList[0], Column3, sortedList)
        p10 = getPeriodData(periodsList[1], Column3, sortedList)
        p11 = getPeriodData(periodsList[2], Column3, sortedList)
        p12 = getPeriodData(periodsList[3], Column3, sortedList)
        p13 = getPeriodData(periodsList[0], Column4, sortedList)
        p14 = getPeriodData(periodsList[1], Column4, sortedList)
        p15 = getPeriodData(periodsList[2], Column4, sortedList)
        p16 = getPeriodData(periodsList[3], Column4, sortedList)
        p17 = getPeriodData(periodsList[0], Column5, sortedList)
        p18 = getPeriodData(periodsList[1], Column5, sortedList)
        p19 = getPeriodData(periodsList[2], Column5, sortedList)
        p20 = getPeriodData(periodsList[3], Column5, sortedList)
        p21 = getPeriodData(periodsList[0], Column6, sortedList)
        p22 = getPeriodData(periodsList[1], Column6, sortedList)
        p23 = getPeriodData(periodsList[2], Column6, sortedList)
        p24 = getPeriodData(periodsList[3], Column6, sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
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
            "AverageGraphsData": getAverageGraphData(request, periodsList, dataCount,
                                                     [Column1, Column2, Column3, Column4,Column5,Column6]),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]},{labelColumnIds[2]},{labelColumnIds[3]},{labelColumnIds[4]},{labelColumnIds[5]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data



# getting data for all US banks data according to the data items
def getRSSDBanksData(request,dataCount,periodsList,labelColumnIds,rssdIDs):
    totalReports = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[0]).values_list(getColumnName(labelColumnIds[0])).count()
    requiredRIds = BankData.objects.filter(period=periodsList[0], rssd_id__in=rssdIDs).values_list('rssd_id',flat=True)
    sortedList = getSortRSSDsBankNames(requiredRIds, 0, 30)
    bnames = BankData.objects.filter(period=periodsList[0], rssd_id__in=sortedList).extra(
        select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, sortedList))},
        order_by=['manual']).values_list('rssd_id')

    if dataCount == "1":
        Column1 = getColumnName(labelColumnIds[0])
        p1 = getPeriodData(periodsList[0],Column1,sortedList)
        p2 = getPeriodData(periodsList[1],Column1,sortedList)
        p3 = getPeriodData(periodsList[2],Column1,sortedList)
        p4 = getPeriodData(periodsList[3],Column1,sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "AverageGraphsData": getAverageGraphDataRSSD(request,periodsList,dataCount,[Column1],rssdIDs),
            "ColumnNames": f"{labelColumnIds[0]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "2":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
            "Period1": p1,
            "Period2": p2,
            "Period3": p3,
            "Period4": p4,
            "Period5": p5,
            "Period6": p6,
            "Period7": p7,
            "Period8": p8,
            "AverageGraphsData": getAverageGraphDataRSSD(request, periodsList, dataCount, [Column1,Column2],rssdIDs),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "3":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        Column3 = getColumnName(labelColumnIds[2])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        p9 = getPeriodData(periodsList[0], Column3, sortedList)
        p10 = getPeriodData(periodsList[1], Column3, sortedList)
        p11 = getPeriodData(periodsList[2], Column3, sortedList)
        p12 = getPeriodData(periodsList[3], Column3, sortedList)
        print(totalReports)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
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
            "AverageGraphsData": getAverageGraphDataRSSD(request, periodsList, dataCount, [Column1, Column2, Column3],rssdIDs),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]},{labelColumnIds[2]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "4":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        Column3 = getColumnName(labelColumnIds[2])
        Column4 = getColumnName(labelColumnIds[3])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        p9 = getPeriodData(periodsList[0], Column3, sortedList)
        p10 = getPeriodData(periodsList[1], Column3, sortedList)
        p11 = getPeriodData(periodsList[2], Column3, sortedList)
        p12 = getPeriodData(periodsList[3], Column3, sortedList)
        p13 = getPeriodData(periodsList[0], Column4, sortedList)
        p14 = getPeriodData(periodsList[1], Column4, sortedList)
        p15 = getPeriodData(periodsList[2], Column4, sortedList)
        p16 = getPeriodData(periodsList[3], Column4, sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
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
            "AverageGraphsData": getAverageGraphDataRSSD(request, periodsList, dataCount, [Column1, Column2, Column3, Column4],rssdIDs),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]},{labelColumnIds[2]},{labelColumnIds[3]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "5":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        Column3 = getColumnName(labelColumnIds[2])
        Column4 = getColumnName(labelColumnIds[3])
        Column5 = getColumnName(labelColumnIds[4])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        p9 = getPeriodData(periodsList[0], Column3, sortedList)
        p10 = getPeriodData(periodsList[1], Column3, sortedList)
        p11 = getPeriodData(periodsList[2], Column3, sortedList)
        p12 = getPeriodData(periodsList[3], Column3, sortedList)
        p13 = getPeriodData(periodsList[0], Column4, sortedList)
        p14 = getPeriodData(periodsList[1], Column4, sortedList)
        p15 = getPeriodData(periodsList[2], Column4, sortedList)
        p16 = getPeriodData(periodsList[3], Column4, sortedList)
        p17 = getPeriodData(periodsList[0], Column5, sortedList)
        p18 = getPeriodData(periodsList[1], Column5, sortedList)
        p19 = getPeriodData(periodsList[2], Column5, sortedList)
        p20 = getPeriodData(periodsList[3], Column5, sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
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
            "AverageGraphsData": getAverageGraphDataRSSD(request, periodsList, dataCount,
                                                     [Column1, Column2, Column3, Column4, Column5],rssdIDs),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]},{labelColumnIds[2]},{labelColumnIds[3]},{labelColumnIds[4]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data
    elif dataCount == "6":
        Column1 = getColumnName(labelColumnIds[0])
        Column2 = getColumnName(labelColumnIds[1])
        Column3 = getColumnName(labelColumnIds[2])
        Column4 = getColumnName(labelColumnIds[3])
        Column5 = getColumnName(labelColumnIds[4])
        Column6 = getColumnName(labelColumnIds[5])
        p1 = getPeriodData(periodsList[0], Column1, sortedList)
        p2 = getPeriodData(periodsList[1], Column1, sortedList)
        p3 = getPeriodData(periodsList[2], Column1, sortedList)
        p4 = getPeriodData(periodsList[3], Column1, sortedList)
        p5 = getPeriodData(periodsList[0], Column2, sortedList)
        p6 = getPeriodData(periodsList[1], Column2, sortedList)
        p7 = getPeriodData(periodsList[2], Column2, sortedList)
        p8 = getPeriodData(periodsList[3], Column2, sortedList)
        p9 = getPeriodData(periodsList[0], Column3, sortedList)
        p10 = getPeriodData(periodsList[1], Column3, sortedList)
        p11 = getPeriodData(periodsList[2], Column3, sortedList)
        p12 = getPeriodData(periodsList[3], Column3, sortedList)
        p13 = getPeriodData(periodsList[0], Column4, sortedList)
        p14 = getPeriodData(periodsList[1], Column4, sortedList)
        p15 = getPeriodData(periodsList[2], Column4, sortedList)
        p16 = getPeriodData(periodsList[3], Column4, sortedList)
        p17 = getPeriodData(periodsList[0], Column5, sortedList)
        p18 = getPeriodData(periodsList[1], Column5, sortedList)
        p19 = getPeriodData(periodsList[2], Column5, sortedList)
        p20 = getPeriodData(periodsList[3], Column5, sortedList)
        p21 = getPeriodData(periodsList[0], Column6, sortedList)
        p22 = getPeriodData(periodsList[1], Column6, sortedList)
        p23 = getPeriodData(periodsList[2], Column6, sortedList)
        p24 = getPeriodData(periodsList[3], Column6, sortedList)
        data = {
            "BankNamesColumn": bnames,
            "ColumnHeadings": getRowColumnHeading(labelColumnIds),
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
            "AverageGraphsData": getAverageGraphDataRSSD(request, periodsList, dataCount,
                                                     [Column1, Column2, Column3, Column4,Column5,Column6],rssdIDs),
            "ColumnNames": f"{labelColumnIds[0]},{labelColumnIds[1]},{labelColumnIds[2]},{labelColumnIds[3]},{labelColumnIds[4]},{labelColumnIds[5]}",
            "PeriodsList": f"{periodsList[0]},{periodsList[1]},{periodsList[2]},{periodsList[3]}",
            "TotalItems": totalReports,
        }
        return data


