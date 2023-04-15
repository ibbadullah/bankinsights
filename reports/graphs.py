from .models import *
from django.db.models import Avg
from django.shortcuts import render, HttpResponse
from django.views import View
from urllib.parse import unquote
from .locationGeocoding import *


# Graphs average data for the report page for all US Banks
def getAverageGraphData(request,periodsList,dataCount,columnNamesList):
    totalBanks = BankHq.objects.values('bank').distinct()
    totalBanks = totalBanks.count()
    if dataCount == "1":
        av1 = BankData.objects.filter(period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]))
        av2 = BankData.objects.filter(period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]))
        av3 = BankData.objects.filter(period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]))
        av4 = BankData.objects.filter(period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks" : totalBanks
        }
        return data
    elif dataCount == "2":
        av1 = BankData.objects.filter(period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]))
        av2 = BankData.objects.filter(period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]))
        av3 = BankData.objects.filter(period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]))
        av4 = BankData.objects.filter(period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        return data
    elif dataCount == "3":
        av1 = BankData.objects.filter(period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]),avg1_3=Avg(columnNamesList[2]))
        av2 = BankData.objects.filter(period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]),avg2_3=Avg(columnNamesList[2]))
        av3 = BankData.objects.filter(period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]),avg3_3=Avg(columnNamesList[2]))
        av4 = BankData.objects.filter(period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]),avg4_3=Avg(columnNamesList[2]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        return data
    elif dataCount == "4":
        av1 = BankData.objects.filter(period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]),avg1_3=Avg(columnNamesList[2]),avg1_4=Avg(columnNamesList[3]))
        av2 = BankData.objects.filter(period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]),avg2_3=Avg(columnNamesList[2]),avg2_4=Avg(columnNamesList[3]))
        av3 = BankData.objects.filter(period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]),avg3_3=Avg(columnNamesList[2]),avg3_4=Avg(columnNamesList[3]))
        av4 = BankData.objects.filter(period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]),avg4_3=Avg(columnNamesList[2]),avg4_4=Avg(columnNamesList[3]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        return data
    elif dataCount == "5":
        av1 = BankData.objects.filter(period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]),avg1_3=Avg(columnNamesList[2]),avg1_4=Avg(columnNamesList[3]),avg1_5=Avg(columnNamesList[4]))
        av2 = BankData.objects.filter(period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]),avg2_3=Avg(columnNamesList[2]),avg2_4=Avg(columnNamesList[3]),avg2_5=Avg(columnNamesList[4]))
        av3 = BankData.objects.filter(period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]),avg3_3=Avg(columnNamesList[2]),avg3_4=Avg(columnNamesList[3]),avg3_5=Avg(columnNamesList[4]))
        av4 = BankData.objects.filter(period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]),avg4_3=Avg(columnNamesList[2]),avg4_4=Avg(columnNamesList[3]),avg4_5=Avg(columnNamesList[4]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        return data
    elif dataCount == "6":
        av1 = BankData.objects.filter(period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]),avg1_3=Avg(columnNamesList[2]),avg1_4=Avg(columnNamesList[3]),avg1_5=Avg(columnNamesList[4]),avg1_6=Avg(columnNamesList[5]))
        av2 = BankData.objects.filter(period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]),avg2_3=Avg(columnNamesList[2]),avg2_4=Avg(columnNamesList[3]),avg2_5=Avg(columnNamesList[4]),avg2_6=Avg(columnNamesList[5]))
        av3 = BankData.objects.filter(period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]),avg3_3=Avg(columnNamesList[2]),avg3_4=Avg(columnNamesList[3]),avg3_5=Avg(columnNamesList[4]),avg3_6=Avg(columnNamesList[5]))
        av4 = BankData.objects.filter(period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]),avg4_3=Avg(columnNamesList[2]),avg4_4=Avg(columnNamesList[3]),avg4_5=Avg(columnNamesList[4]),avg4_6=Avg(columnNamesList[5]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        return data



# Graphs average data for the report page for specific Banks
def getAverageGraphDataRSSD(request,periodsList,dataCount,columnNamesList,rssdIDs):
    totalBanks = BankHq.objects.values('bank').distinct()
    totalBanks = totalBanks.count()
    if dataCount == "1":
        av1 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]))
        av2 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]))
        av3 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]))
        av4 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks" : totalBanks
        }
        return data
    elif dataCount == "2":
        av1 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]))
        av2 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]))
        av3 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]))
        av4 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        return data
    elif dataCount == "3":
        av1 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]),avg1_3=Avg(columnNamesList[2]))
        av2 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]),avg2_3=Avg(columnNamesList[2]))
        av3 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]),avg3_3=Avg(columnNamesList[2]))
        av4 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]),avg4_3=Avg(columnNamesList[2]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        print("New graphs...")
        return data
    elif dataCount == "4":
        av1 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]),avg1_3=Avg(columnNamesList[2]),avg1_4=Avg(columnNamesList[3]))
        av2 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]),avg2_3=Avg(columnNamesList[2]),avg2_4=Avg(columnNamesList[3]))
        av3 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]),avg3_3=Avg(columnNamesList[2]),avg3_4=Avg(columnNamesList[3]))
        av4 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]),avg4_3=Avg(columnNamesList[2]),avg4_4=Avg(columnNamesList[3]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        return data
    elif dataCount == "5":
        av1 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]),avg1_3=Avg(columnNamesList[2]),avg1_4=Avg(columnNamesList[3]),avg1_5=Avg(columnNamesList[4]))
        av2 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]),avg2_3=Avg(columnNamesList[2]),avg2_4=Avg(columnNamesList[3]),avg2_5=Avg(columnNamesList[4]))
        av3 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]),avg3_3=Avg(columnNamesList[2]),avg3_4=Avg(columnNamesList[3]),avg3_5=Avg(columnNamesList[4]))
        av4 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]),avg4_3=Avg(columnNamesList[2]),avg4_4=Avg(columnNamesList[3]),avg4_5=Avg(columnNamesList[4]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        return data
    elif dataCount == "6":
        av1 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[0]).aggregate(avg1=Avg(columnNamesList[0]),avg1_2=Avg(columnNamesList[1]),avg1_3=Avg(columnNamesList[2]),avg1_4=Avg(columnNamesList[3]),avg1_5=Avg(columnNamesList[4]),avg1_6=Avg(columnNamesList[5]))
        av2 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[1]).aggregate(avg2=Avg(columnNamesList[0]),avg2_2=Avg(columnNamesList[1]),avg2_3=Avg(columnNamesList[2]),avg2_4=Avg(columnNamesList[3]),avg2_5=Avg(columnNamesList[4]),avg2_6=Avg(columnNamesList[5]))
        av3 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[2]).aggregate(avg3=Avg(columnNamesList[0]),avg3_2=Avg(columnNamesList[1]),avg3_3=Avg(columnNamesList[2]),avg3_4=Avg(columnNamesList[3]),avg3_5=Avg(columnNamesList[4]),avg3_6=Avg(columnNamesList[5]))
        av4 = BankData.objects.filter(rssd_id__in=rssdIDs,period=periodsList[3]).aggregate(avg4=Avg(columnNamesList[0]),avg4_2=Avg(columnNamesList[1]),avg4_3=Avg(columnNamesList[2]),avg4_4=Avg(columnNamesList[3]),avg4_5=Avg(columnNamesList[4]),avg4_6=Avg(columnNamesList[5]))
        data = {
            "AV1": av1,
            "AV2": av2,
            "AV3": av3,
            "AV4": av4,
            "TotalBanks": totalBanks
        }
        return data




# single bank report
class SingleBankGraph(View):
    def get(self,request):
        if securityCheck(request) == False:
            # return render(request,'invalid-request.html')
            return HttpResponse(f"<script>location.replace('https://bankinsights.io/');</script>")
        # Getting url variables values
        dataCount = request.GET.get('count')
        rssdID = int(request.GET.get('id'))
        periods = str(request.GET.get('periods'))
        columns = str(request.GET.get('columns'))
        columnIDs = columns.split(',')
        periodsList = periods.split(',')
        # Getting labels and formatting them
        labels = request.GET.get('labels')
        labels1 = labels.replace("[","")
        labels2 = labels1.replace("]","")
        labelsFormat = unquote(labels2)
        labelsReady = labelsFormat.replace("'","")
        labelsReady = labelsReady.replace(" ","")
        outputLabels = labelsReady
        labelsList = labelsReady.split(",")

        # Getting bank detail
        bankQuery = BankHq.objects.get(rssd_id=rssdID)
        branchQuery = BankBranch.objects.filter(rssd_id_hq=rssdID).distinct()
        peerGroupLabel = DropdownMenuPeerGroup.objects.get(value=bankQuery.peer_group)
        # Required states of branches
        bankState = DropdownMenuState.objects.get(value=bankQuery.state)
        branchStatesList = []
        for s in branchQuery:
            branchStatesList.append(s.state)
        branchStatesList.append(bankState.value)
        branchStatesQuery = DropdownMenuState.objects.filter(value__in=branchStatesList).distinct().order_by('label')

        if dataCount == "1":
            columnNamesList = [getColumnName(columnIDs[0])]
            p1 = BankData.objects.filter(period=periodsList[0],rssd_id=rssdID).aggregate(avg1=Avg(columnNamesList[0]))
            p2 = BankData.objects.filter(period=periodsList[1],rssd_id=rssdID).aggregate(avg2=Avg(columnNamesList[0]))
            p3 = BankData.objects.filter(period=periodsList[2],rssd_id=rssdID).aggregate(avg3=Avg(columnNamesList[0]))
            p4 = BankData.objects.filter(period=periodsList[3],rssd_id=rssdID).aggregate(avg4=Avg(columnNamesList[0]))
            data = {
                "AV1": p1,
                "AV2": p2,
                "AV3": p3,
                "AV4": p4,
                "LabelsList": labelsList,
                "ColumnHeadings": getRowColumnHeading(columnIDs),
                "ReportLabels" : outputLabels,
                "PeerGroupLabel": peerGroupLabel.label,
                "BranchState": bankState
            }
            return render(request,'graphs/single-bank-graph.html',{"Data":data,"BankDetails":bankQuery,"BranchQuery":branchStatesQuery})
        elif dataCount == "2":
            columnNamesList = [getColumnName(columnIDs[0]),getColumnName(columnIDs[1])]
            av1 = BankData.objects.filter(period=periodsList[0],rssd_id=rssdID).aggregate(avg1=Avg(columnNamesList[0]),
                                                                           avg1_2=Avg(columnNamesList[1]))
            av2 = BankData.objects.filter(period=periodsList[1],rssd_id=rssdID).aggregate(avg2=Avg(columnNamesList[0]),
                                                                           avg2_2=Avg(columnNamesList[1]))
            av3 = BankData.objects.filter(period=periodsList[2],rssd_id=rssdID).aggregate(avg3=Avg(columnNamesList[0]),
                                                                           avg3_2=Avg(columnNamesList[1]))
            av4 = BankData.objects.filter(period=periodsList[3],rssd_id=rssdID).aggregate(avg4=Avg(columnNamesList[0]),
                                                                           avg4_2=Avg(columnNamesList[1]))

            data = {
                "AV1": av1,
                "AV2": av2,
                "AV3": av3,
                "AV4": av4,
                "LabelsList": labelsList,
                "ColumnHeadings": getRowColumnHeading(columnIDs),
                "ReportLabels": outputLabels,
                "PeerGroupLabel": peerGroupLabel.label,
                "BranchState": bankState
            }
            return render(request, 'graphs/single-bank-graph.html',
                          {"Data": data, "BankDetails": bankQuery, "BranchQuery": branchStatesQuery})
        elif dataCount == "3":
            columnNamesList = [getColumnName(columnIDs[0]),getColumnName(columnIDs[1]),getColumnName(columnIDs[2])]
            av1 = BankData.objects.filter(period=periodsList[0],rssd_id=rssdID).aggregate(avg1=Avg(columnNamesList[0]),
                                                                           avg1_2=Avg(columnNamesList[1]),
                                                                           avg1_3=Avg(columnNamesList[2]))
            av2 = BankData.objects.filter(period=periodsList[1],rssd_id=rssdID).aggregate(avg2=Avg(columnNamesList[0]),
                                                                           avg2_2=Avg(columnNamesList[1]),
                                                                           avg2_3=Avg(columnNamesList[2]))
            av3 = BankData.objects.filter(period=periodsList[2],rssd_id=rssdID).aggregate(avg3=Avg(columnNamesList[0]),
                                                                           avg3_2=Avg(columnNamesList[1]),
                                                                           avg3_3=Avg(columnNamesList[2]))
            av4 = BankData.objects.filter(period=periodsList[3],rssd_id=rssdID).aggregate(avg4=Avg(columnNamesList[0]),
                                                                           avg4_2=Avg(columnNamesList[1]),
                                                                           avg4_3=Avg(columnNamesList[2]))
            data = {
                "AV1": av1,
                "AV2": av2,
                "AV3": av3,
                "AV4": av4,
                "LabelsList": labelsList,
                "ColumnHeadings": getRowColumnHeading(columnIDs),
                "ReportLabels": outputLabels,
                "PeerGroupLabel": peerGroupLabel.label,
                "BranchState": bankState
            }
            return render(request,'graphs/single-bank-graph.html',{"Data":data,"BankDetails":bankQuery,"BranchQuery":branchStatesQuery})
        elif dataCount == "4":
            columnNamesList = [getColumnName(columnIDs[0]),getColumnName(columnIDs[1]),getColumnName(columnIDs[2]),getColumnName(columnIDs[3])]
            av1 = BankData.objects.filter(period=periodsList[0],rssd_id=rssdID).aggregate(avg1=Avg(columnNamesList[0]),
                                                                           avg1_2=Avg(columnNamesList[1]),
                                                                           avg1_3=Avg(columnNamesList[2]),
                                                                           avg1_4=Avg(columnNamesList[3]))
            av2 = BankData.objects.filter(period=periodsList[1],rssd_id=rssdID).aggregate(avg2=Avg(columnNamesList[0]),
                                                                           avg2_2=Avg(columnNamesList[1]),
                                                                           avg2_3=Avg(columnNamesList[2]),
                                                                           avg2_4=Avg(columnNamesList[3]))
            av3 = BankData.objects.filter(period=periodsList[2],rssd_id=rssdID).aggregate(avg3=Avg(columnNamesList[0]),
                                                                           avg3_2=Avg(columnNamesList[1]),
                                                                           avg3_3=Avg(columnNamesList[2]),
                                                                           avg3_4=Avg(columnNamesList[3]))
            av4 = BankData.objects.filter(period=periodsList[3],rssd_id=rssdID).aggregate(avg4=Avg(columnNamesList[0]),
                                                                           avg4_2=Avg(columnNamesList[1]),
                                                                           avg4_3=Avg(columnNamesList[2]),
                                                                           avg4_4=Avg(columnNamesList[3]))
            data = {
                "AV1": av1,
                "AV2": av2,
                "AV3": av3,
                "AV4": av4,
                "LabelsList": labelsList,
                "ColumnHeadings": getRowColumnHeading(columnIDs),
                "ReportLabels": outputLabels,
                "PeerGroupLabel": peerGroupLabel.label,
                "BranchState": bankState
            }
            return render(request, 'graphs/single-bank-graph.html',
                          {"Data": data, "BankDetails": bankQuery, "BranchQuery": branchStatesQuery})
        elif dataCount == "5":
            columnNamesList = [getColumnName(columnIDs[0]),getColumnName(columnIDs[1]),getColumnName(columnIDs[2]),getColumnName(columnIDs[3]),getColumnName(columnIDs[4])]
            av1 = BankData.objects.filter(period=periodsList[0],rssd_id=rssdID).aggregate(avg1=Avg(columnNamesList[0]),
                                                                           avg1_2=Avg(columnNamesList[1]),
                                                                           avg1_3=Avg(columnNamesList[2]),
                                                                           avg1_4=Avg(columnNamesList[3]),
                                                                           avg1_5=Avg(columnNamesList[4]))
            av2 = BankData.objects.filter(period=periodsList[1],rssd_id=rssdID).aggregate(avg2=Avg(columnNamesList[0]),
                                                                           avg2_2=Avg(columnNamesList[1]),
                                                                           avg2_3=Avg(columnNamesList[2]),
                                                                           avg2_4=Avg(columnNamesList[3]),
                                                                           avg2_5=Avg(columnNamesList[4]))
            av3 = BankData.objects.filter(period=periodsList[2],rssd_id=rssdID).aggregate(avg3=Avg(columnNamesList[0]),
                                                                           avg3_2=Avg(columnNamesList[1]),
                                                                           avg3_3=Avg(columnNamesList[2]),
                                                                           avg3_4=Avg(columnNamesList[3]),
                                                                           avg3_5=Avg(columnNamesList[4]))
            av4 = BankData.objects.filter(period=periodsList[3],rssd_id=rssdID).aggregate(avg4=Avg(columnNamesList[0]),
                                                                           avg4_2=Avg(columnNamesList[1]),
                                                                           avg4_3=Avg(columnNamesList[2]),
                                                                           avg4_4=Avg(columnNamesList[3]),
                                                                           avg4_5=Avg(columnNamesList[4]))
            data = {
                "AV1": av1,
                "AV2": av2,
                "AV3": av3,
                "AV4": av4,
                "LabelsList": labelsList,
                "ColumnHeadings": getRowColumnHeading(columnIDs),
                "ReportLabels": outputLabels,
                "PeerGroupLabel": peerGroupLabel.label,
                "BranchState": bankState
            }
            return render(request, 'graphs/single-bank-graph.html',
                          {"Data": data, "BankDetails": bankQuery, "BranchQuery": branchStatesQuery})
        elif dataCount == "6":
            columnNamesList = [getColumnName(columnIDs[0]),getColumnName(columnIDs[1]),getColumnName(columnIDs[2]),getColumnName(columnIDs[3]),getColumnName(columnIDs[4]),getColumnName(columnIDs[5])]
            av1 = BankData.objects.filter(period=periodsList[0],rssd_id=rssdID).aggregate(avg1=Avg(columnNamesList[0]),
                                                                           avg1_2=Avg(columnNamesList[1]),
                                                                           avg1_3=Avg(columnNamesList[2]),
                                                                           avg1_4=Avg(columnNamesList[3]),
                                                                           avg1_5=Avg(columnNamesList[4]),
                                                                           avg1_6=Avg(columnNamesList[5]))
            av2 = BankData.objects.filter(period=periodsList[1],rssd_id=rssdID).aggregate(avg2=Avg(columnNamesList[0]),
                                                                           avg2_2=Avg(columnNamesList[1]),
                                                                           avg2_3=Avg(columnNamesList[2]),
                                                                           avg2_4=Avg(columnNamesList[3]),
                                                                           avg2_5=Avg(columnNamesList[4]),
                                                                           avg2_6=Avg(columnNamesList[5]))
            av3 = BankData.objects.filter(period=periodsList[2],rssd_id=rssdID).aggregate(avg3=Avg(columnNamesList[0]),
                                                                           avg3_2=Avg(columnNamesList[1]),
                                                                           avg3_3=Avg(columnNamesList[2]),
                                                                           avg3_4=Avg(columnNamesList[3]),
                                                                           avg3_5=Avg(columnNamesList[4]),
                                                                           avg3_6=Avg(columnNamesList[5]))
            av4 = BankData.objects.filter(period=periodsList[3],rssd_id=rssdID).aggregate(avg4=Avg(columnNamesList[0]),
                                                                           avg4_2=Avg(columnNamesList[1]),
                                                                           avg4_3=Avg(columnNamesList[2]),
                                                                           avg4_4=Avg(columnNamesList[3]),
                                                                           avg4_5=Avg(columnNamesList[4]),
                                                                           avg4_6=Avg(columnNamesList[5]))
            data = {
                "AV1": av1,
                "AV2": av2,
                "AV3": av3,
                "AV4": av4,
                "LabelsList": labelsList,
                "ColumnHeadings": getRowColumnHeading(columnIDs),
                "ReportLabels": outputLabels,
                "PeerGroupLabel": peerGroupLabel.label,
                "BranchState": bankState
            }
            return render(request, 'graphs/single-bank-graph.html',
                          {"Data": data, "BankDetails": bankQuery, "BranchQuery": branchStatesQuery})