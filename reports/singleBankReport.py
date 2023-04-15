from .models import *
from django.shortcuts import render
from .smartLogics import getRSSDBanksData,securityCheck
from urllib.parse import unquote

# view for single bank report
def singleBankReport(request):
    if securityCheck(request) == False:
        return render(request,'invalid-request.html')
    # Getting url variable values
    id = request.GET.get('id')
    periods = request.GET.get('periods')
    columns = request.GET.get('columns')
    dataCount = request.GET.get('count')
    labels = request.GET.get('labels')
    # Unquoting.
    id = unquote(id)
    id = id.replace('"','')
    id = id.replace("'","")
    id = int(id)
    labels = labels.replace("]","")
    labels = labels.replace("[", "")
    labels = unquote(labels)
    labels = labels.replace("'", "")
    labels = labels.replace(" ","")
    print(labels)
    labels = labels.split(",")
    # Splitting by comma
    periods = periods.split(',')
    columns = columns.split(',')

    if dataCount == "1":
        # Getting data from the bank data table via smart logics
        d = getRSSDBanksData(request, dataCount, periods, [columns[0]],[id])
        requiredItems = {
            "PeriodLables": labels,
            "DataCount": dataCount,
            "PeriodSelection": periods,
            "FPeriodsLables": labels[0]+","+labels[1]+","+labels[2]+","+labels[3]
        }
        return render(request, "single-bank-report/single-report.html", {"Data": d, "RequiredItems": requiredItems})
    elif dataCount == "2":
        d = getRSSDBanksData(request, dataCount, periods, [columns[0],columns[1]], [id])
        requiredItems = {
            "PeriodLables": labels,
            "DataCount": dataCount,
            "PeriodSelection": periods,
            "FPeriodsLables": labels[0]+","+labels[1]+","+labels[2]+","+labels[3]
        }
        return render(request, "single-bank-report/single-report.html", {"Data": d, "RequiredItems": requiredItems})
    elif dataCount == "3":
        d = getRSSDBanksData(request, dataCount, periods, [columns[0],columns[1],columns[2]], [id])
        requiredItems = {
            "PeriodLables": labels,
            "DataCount": dataCount,
            "PeriodSelection": periods,
            "FPeriodsLables": labels[0] + "," + labels[1] + "," + labels[2] + "," + labels[3]
        }
        return render(request, "single-bank-report/single-report.html", {"Data": d, "RequiredItems": requiredItems})
    elif dataCount == "4":
        d = getRSSDBanksData(request, dataCount, periods, [columns[0],columns[1],columns[2],columns[3]], [id])
        requiredItems = {
            "PeriodLables": labels,
            "DataCount": dataCount,
            "PeriodSelection": periods,
            "FPeriodsLables": labels[0] + "," + labels[1] + "," + labels[2] + "," + labels[3]
        }
        return render(request, "single-bank-report/single-report.html", {"Data": d, "RequiredItems": requiredItems})
    elif dataCount == "5":
        d = getRSSDBanksData(request, dataCount, periods, [columns[0],columns[1],columns[2],columns[3],columns[4]], [id])
        requiredItems = {
            "PeriodLables": labels,
            "DataCount": dataCount,
            "PeriodSelection": periods,
            "FPeriodsLables": labels[0] + "," + labels[1] + "," + labels[2] + "," + labels[3]
        }
        return render(request, "single-bank-report/single-report.html", {"Data": d, "RequiredItems": requiredItems})
    elif dataCount == "6":
        d = getRSSDBanksData(request, dataCount, periods, [columns[0],columns[1],columns[2],columns[3],columns[4],columns[5]], [id])
        requiredItems = {
            "PeriodLables": labels,
            "DataCount": dataCount,
            "PeriodSelection": periods,
            "FPeriodsLables": labels[0] + "," + labels[1] + "," + labels[2] + "," + labels[3]
        }
        return render(request, "single-bank-report/single-report.html", {"Data": d, "RequiredItems": requiredItems})

