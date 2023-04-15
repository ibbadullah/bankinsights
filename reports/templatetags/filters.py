from django import template
from reports.models import *
from reports.locationGeocoding import *
from django.db import connection
cursor = connection.cursor()

register = template.Library()

# getting bank name
@register.filter(name="getBankName")
def getBankName(request,rssid):
    q = BankHq.objects.get(rssd_id=rssid)
    return q.bank

# getting specific value for the
@register.filter(name="getPeriodValue")
def getPeriodValue(id,period,dataColumn):
    request = ""
    value = ""
    q = BankData.objects.filter(id=id, period=period).values_list(dataColumn)
    for d in q:
        value = q[0]
    convertStr = str(value)
    removeBrace1 = convertStr.replace('(', '')
    removeBrace2 = removeBrace1.replace(')', '')
    numberString = removeBrace2.replace(',', '')
    if numberString == "0":
        numberString = "000,000,000"
        return numberString
    else:
        return numberString


@register.simple_tag(name="testingTag")
def testingTag(column,period,id):
    # Data retrieval operation - no commit required
    cursor.execute("SELECT `Residential First 30Day` FROM bank_data where id = %s AND Period= %s",[id,period])
    row = cursor.fetchone()
    return row

# getting record for single item
@register.filter(name="getSingleValue")
def getSingleValue(id,columnPeriod):
    data = columnPeriod.split(",")
    try:
        q = BankData.objects.values_list(data[0],flat=True).get(period=data[1],rssd_id=id)
        print(q)
        if q == None:
            return "NR"
        else:
            return q

    except:
        return "-"