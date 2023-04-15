import googlemaps
from .models import *
from .bankdataFields import *

geolocation = googlemaps.Client(key='AIzaSyBueo3VNKIPVLJBi3iMbU1iUyQO70GGeOM')
# getting latitude and longitude
def getGeoLocation(address):
    location = geolocation.geocode(address)
    print(location)
    if location == []:
        return "Nothing found"
    else:
        lat = location[0]["geometry"]["location"]["lat"]
        lon = location[0]["geometry"]["location"]["lng"]
        location = f"POINT({str(lat)} {str(lon)})"
        return location

# getting ip address
def GetIp(request):
    x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forward:
        ip = x_forward.split(',')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

# getting db column for bank data model
def getColumnName(labelId):
    q = NavigationValuesData.objects.get(id=labelId)
    columnLabel = q.db_column
    getName = bankDataModelFields.get(columnLabel.replace('`',''))
    return getName

# getting row and column heading for table and PDF
def getRowColumnHeading(labelIdsList):
    dataList = []
    for id in labelIdsList:
        dataList.append(NavigationValuesData.objects.get(id=id))
    return dataList

# getting state for report page displaying
def getStateLabel(value):
    q = DropdownMenuState.objects.get(value=value)
    return q.label

# Getting peer group
def getPeerGroup(value):
    q = DropdownMenuPeerGroup.objects.get(value=value)
    return q.label

# Getting single bank name
def getSingleBankName(rssdId):
    try:
        query = BankHq.objects.get(rssd_id=rssdId)
        return query.bank
    except:
        m = "Not found"
        return m

# Security check for validating the traffic
def securityCheck(request):
    whiteListIPs = ['8.44.147.43','127.0.0.1']
    whiteListOrigns = ['https://bankinsights.dreamhosters.com/','https://bankinsights.io/']
    userIP = str(GetIp(request))
    userOrign = request.META.get('HTTP_REFERER')
    try:
        if userOrign in whiteListOrigns:
            request.session['allowedOrign'] = True
            return True
        elif userIP in whiteListIPs:
            return True
        elif request.session['allowedOrign'] == True:
            return True
        elif userOrign not in whiteListOrigns:
            request.session['allowedOrign'] = False
            return False
        else:
            return False
    except:
        return False
