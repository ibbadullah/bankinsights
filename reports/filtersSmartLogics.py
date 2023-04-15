from reports.models import *
from reports.locationGeocoding import getGeoLocation
from django.db.models import Q
import itertools
from itertools import chain

# load more range
def getFromTo(r1,r2,total,req):
    range1 = int(r1)
    range2 = int(r2)
    total = int(total)
    if req != "loadmore":
        return [0,30]
    elif range2 >= total:
        range1 = range1
        range2 = total
        return [range1, range2]
    else:
        range1 = range2
        range2 = range2 + 30
        return [range1, range2]


# view for getting required rssd_Ids from different tables
def getRequiredRSSDIDs(case,param1,param2):
    rssdIDs = []
    if case == "US banks with branches in State":
        q1 = BankBranch.objects.filter(state=param1).values_list('rssd_id_hq',flat=True)
        q2 = BankHq.objects.filter(state=param1).values_list('rssd_id',flat=True)
        rssdIDs = list(chain(q1,q2))
        return rssdIDs
    elif case == "US banks with branches near Location":
        param2 = int(param2)
        # Converting miles to meters
        distanceRange = param2 * 1609.34
        gl = getGeoLocation(param1)
        # Firing spatial query
        bankbranchq = BankBranch.objects.raw(
            "SELECT * FROM `bank_branch` WHERE ST_Distance(`Location`, ST_GeomFromText(%s,4326)) <= %s;",
            [gl, distanceRange])
        for b in bankbranchq:
            rssdIDs.append(b.rssd_id_hq)
        print(len(rssdIDs))
        bankbrancHQ = BankHq.objects.raw(
            "SELECT * FROM `bank_hq` WHERE ST_Distance(`Location`, ST_GeomFromText(%s,4326)) <= %s;",
            [gl, distanceRange])
        for b in bankbrancHQ:
            rssdIDs.append(b.rssd_id)
        print(len(rssdIDs))
        return rssdIDs
    elif case == "US banks in Bank Peer Group":
        q2 = BankHq.objects.filter(peer_group=param1)
        for q in q2:
            rssdIDs.append(q.rssd_id)
        return rssdIDs

# Method for replacing non existing rows with NR
def replaceNonExistingRows(rssd1,rssd2,data):
    listIndex = 0
    for d in rssd1:
        listIndex += 1
        if d in rssd2:
            pass
        else:
            data.insert(listIndex - 1, None)
    return data

# Getting sorted bank names
def getSortedBankNames(rssdIDs,r1,r2):
    rssdIDsList = []
    q = BankHq.objects.filter(rssd_id__in=rssdIDs).values_list('rssd_id').distinct().order_by('bank')[r1:r2]
    for myid in q:
        rssdIDsList.append(myid[0])
    return rssdIDsList

# Getting sorted bank names in descending order
def getSortedBankNamesDes(rssdIDs,r1,r2):
    rssdIDsList = []
    q = BankHq.objects.filter(rssd_id__in=rssdIDs).values_list('rssd_id').distinct().order_by('-bank')[r1:r2]
    for myid in q:
        rssdIDsList.append(myid[0])
    return rssdIDsList

# column sort dynamic
def sortColumn(request,columnName,sort):
    csessionSort = str(request.session['sort'])
    # use the list count method. Find
    sortCount = sort.count(csessionSort)
    print(sortCount)
    if csessionSort == 'clear':
        columnName = "-" + columnName
        return columnName
    elif csessionSort in sort:
        if (int(sortCount % 2)) == 0:
            print("The number is even :" + str(sortCount))
            columnName = "-" + columnName
            return columnName
        else:
            print("The number is odd :" + str(sortCount))
            return columnName
    else:
        columnName = "-" + columnName
        return columnName

# get colum values in the right order - No need anymore but just for future reference
def getColumnValues(id,period,column):
    try:
        data = BankData.objects.values_list(column).get(period=period,rssd_id=id)
        return data
    except:
        return None

# deleting sessions
def deleteSession(request):
    try:
        request.session['sort'] = 'clear'
    except:
        pass

# Get load or sort bank names
def getLoadMSortBNClearFl(request,reqType,period,column,rssdIDs,bnsort,r1,r2):
    total = len(rssdIDs)
    queryTotal = BankData.objects.filter(period=period, rssd_id__in=rssdIDs).values_list(column).count()
    if reqType == "loadmore" and bnsort == '':
        rIds = getSortedBankNames(rssdIDs,r1,r2)
        if total == queryTotal:
            q = itertools.chain(BankData.objects.filter(period=period,rssd_id__in=rIds).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rIds))},
                order_by=['manual']).values_list(column,flat=True))
            return q
        else:
            d = itertools.chain(BankData.objects.filter(period=period, rssd_id__in=rIds).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rIds))},
                order_by=['manual']).values_list(column,'rssd_id'))
            rssd2 = []
            data = []
            for mydataList in d:
                data.append(mydataList[0])
                rssd2.append(mydataList[1])
            finalData = replaceNonExistingRows(rIds, rssd2, data)
            return finalData
    elif reqType == "clearfilters" and bnsort == '':
        deleteSession(request)
        rIds = getSortedBankNames(rssdIDs,r1,r2)
        if total == queryTotal:
            q = itertools.chain(BankData.objects.filter(period=period,rssd_id__in=rIds).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rIds))},
                order_by=['manual']).values_list(column,flat=True))
            return q
        else:
            d = itertools.chain(BankData.objects.filter(period=period, rssd_id__in=rIds).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rIds))},
                order_by=['manual']).values_list(column,'rssd_id'))
            rssd2 = []
            data = []
            for mydataList in d:
                data.append(mydataList[0])
                rssd2.append(mydataList[1])
            finalData = replaceNonExistingRows(rIds,rssd2, data)
            return finalData
    else:
        rIds = getSortedBankNamesDes(rssdIDs,r1,r2)
        if total == queryTotal:
            q = itertools.chain(BankData.objects.filter(period=period, rssd_id__in=rIds).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rIds))},
                order_by=['manual']).values_list(column,flat=True))
            return q
        else:
            d = itertools.chain(BankData.objects.filter(period=period, rssd_id__in=rIds).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rIds))},
                order_by=['manual']).values_list(column,'rssd_id'))
            rssd2 = []
            data = []
            for mydataList in d:
                data.append(mydataList[0])
                rssd2.append(mydataList[1])
            finalData = replaceNonExistingRows(rIds, rssd2, data)
            return finalData

# Get RSSD_ID load or sort bank names
def getRSSDLoadMSortBNClearFl(reqType,period,rssdIDs,bnsort,r1,r2):
    if reqType == "loadmore" and bnsort == "":
        rIds = getSortedBankNames(rssdIDs,r1,r2)
        q = BankData.objects.filter(period=period, rssd_id__in=rIds).extra(
            select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rIds))},
            order_by=['manual']).values_list('rssd_id')
        return q
    elif reqType == "clearfilters" and bnsort == "":
        rIds = getSortedBankNames(rssdIDs,r1,r2)
        q = BankData.objects.filter(period=period, rssd_id__in=rIds).extra(
            select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rIds))},
            order_by=['manual']).values_list('rssd_id')
        return q
    else:
        rIds = getSortedBankNamesDes(rssdIDs,r1,r2)
        q = BankData.objects.filter(period=period, rssd_id__in=rIds).extra(
            select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rIds))},
            order_by=['manual']).values_list('rssd_id')
        return q


# dynamic filters range from queryset
def dynamicRange(fromValue,toValue,period,column,cellNo,rangeNo):
    r1 = int(fromValue)
    r2 = int(toValue)
    cellNo = int(cellNo)
    rangeNo = int(rangeNo)
    column = column+"__range"
    if cellNo == rangeNo:
        mydict = {
            "period": period,
            column: [r1,r2]
        }
        return mydict
    else:
        mydict = {
            "period": period
        }
        return mydict

# dynamic filters passing for range from queryset
def dynamicRangeRSSDIds(fromValue,toValue,period,column,cellNo,rangeNo,rssdIds):
    r1 = int(fromValue)
    r2 = int(toValue)
    cellNo = int(cellNo)
    rangeNo = int(rangeNo)
    column = column+"__range"
    if cellNo == rangeNo:
        mydict = {
            "rssd_id__in": rssdIds,
            "period": period,
            column: [r1,r2]
        }
        return mydict
    else:
        mydict = {
            "rssd_id__in": rssdIds,
            "period": period
        }
        return mydict

# Dynamic range function for periods
def dynamicRangePeriods(fromRange, toRange, period, column, cellNo, rangeNo,rssdIDs):
    total = len(rssdIDs)
    queryTotal = BankData.objects.filter(
        **dynamicRangeRSSDIds(fromRange, toRange, period, column, cellNo, rangeNo, rssdIDs)).values_list(column).count()
    if total == queryTotal:
        d = BankData.objects.filter(
                **dynamicRangeRSSDIds(fromRange, toRange, period, column, cellNo, rangeNo,rssdIDs)).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rssdIDs))},
                order_by=['manual']).values_list(column,flat=True)
        return d
    else:
        d = BankData.objects.filter(period=period,rssd_id__in=rssdIDs).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rssdIDs))},
                order_by=['manual']).values_list(column,'rssd_id')
        rssd2 = []
        data = []
        for mydataList in d:
            data.append(mydataList[0])
            rssd2.append(mydataList[1])
        finalData = replaceNonExistingRows(rssdIDs, rssd2, data)
        return finalData


# sort function for dynamic sorting with RSSD IDs
def dynamicSortRSSDIDs(request,sort,cellNo,column,period,total,rssdIDs):
    print(request.GET.get('sortslist'))
    sort = int(sort)
    sortList = request.GET.get('sortslist').split(',')
    sortCount = sortList.count(str(sort))
    cellNo = int(cellNo)
    if sort == cellNo:
        if str(sort) in sortList:
            if (int(sortCount % 2)) == 0:
                print("The number is even :" + str(sortCount))
                d = itertools.chain(
                    BankData.objects.filter(period=period, rssd_id__in=rssdIDs).values_list(column, flat=True).order_by(
                        "-"+column))
                return d
            else:
                print("The number is odd :" + str(sortCount))
                d = itertools.chain(
                    BankData.objects.filter(period=period, rssd_id__in=rssdIDs).values_list(column, flat=True).order_by(
                        column))
                return d
        elif request.session['sort'] == 'clear':
            d = itertools.chain(
                BankData.objects.filter(period=period, rssd_id__in=rssdIDs).values_list(column, flat=True).order_by(
                    "-" + column))
            return d
        else:
            d = itertools.chain(
                BankData.objects.filter(period=period, rssd_id__in=rssdIDs).values_list(column, flat=True).order_by(
                    "-" + column))
            return d
    else:
        # Checking selected total and query total
        queryTotal = BankData.objects.filter(rssd_id__in=rssdIDs,period=period).values_list(column).count()
        if total == queryTotal:
            d = itertools.chain(BankData.objects.filter(rssd_id__in=rssdIDs, period=period).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rssdIDs))},
                order_by=['manual']).values_list(column,flat=True))
            return d
        else:
            # Call the get method and check every value
            d = BankData.objects.filter(rssd_id__in=rssdIDs, period=period).extra(
                select={'manual': 'FIELD(`RSSD ID`,%s)' % ','.join(map(str, rssdIDs))},
                order_by=['manual']).values_list(column,'rssd_id')
            rssd2 = []
            data = []
            for mydataList in d:
                data.append(mydataList[0])
                rssd2.append(mydataList[1])
            finalData = replaceNonExistingRows(rssdIDs,rssd2,data)
            return finalData



# get first column for sorting & filtering
def getFirstColumn(param,columnsList):
    param = int(param)
    if param == 11 or param == 12 or param == 13 or param == 14:
        return columnsList[0]
    elif param == 21 or param == 22 or param == 23 or param == 24:
        return columnsList[1]
    elif param == 31 or param == 32 or param == 33 or param == 34:
        return columnsList[2]
    elif param == 41 or param == 42 or param == 43 or param == 44:
        return columnsList[3]
    elif param == 51 or param == 52 or param == 53 or param == 54:
        return columnsList[4]
    else:
        return columnsList[5]

# get period index from for first column
def getPeriodIndex(param):
    param = int(param[1])
    if param == 1:
        return 0
    elif param == 2:
        return 1
    elif param == 3:
        return 2
    else:
        return 3