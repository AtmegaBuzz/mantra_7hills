from django.shortcuts import redirect, render
from .models import *
# Create your views here.

#  redirect to managing committee 
def redirect_managing_committee(request):

    return redirect("managing-committee/")



def managing_committee(request):

    committee = Committee.objects.all()

    context = {
        'committee':committee,
    }

    return render(request,"managingCommittee.html",context)

def dosAndDonts_view(request):

    return render(request,"dosanddonts.html")

def rar_view(request):

    return render(request,"rar.html")

def expenses_view(request):

    labels = []
    data = []
    bgcolor = ["#673ab7","#303f9f","#2196f3",
        "#00897b","#40c4ff","#1b5e20",
        "#00b8d4","#d32f2f","#4fc3f7","#0091ea"
        ]

    queryset = Expense.objects.all()
    for item in queryset:
        labels.append(item.type)
        data.append(item.expense)
       

    context = {
        'labels':labels,
        'data':data,
        'bgcolor':bgcolor
    }

    return render(request,"expenses.html",context)