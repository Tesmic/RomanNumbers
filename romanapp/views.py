from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    temp={}
    temp['number']=51
    
    context ={'temp':temp}
    return render(request,'index.html',context)
 #   return HttpResponse({'a':1})

def calculate(request):
    context ={'roman':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['number']=request.POST.get('number')
        
        #Datapreprocessing Convert the values to float
        if temp['number'].isnumeric() == True:
            number=int(temp['number'])
            rn = upto5000(number)       
            context ={'roman':rn,'temp':temp }
        else:
            context ={'roman':"Not a Valid number",'temp':temp }
        
    return render(request,'index.html',context)

def upto5000(n):
    roman =""
    r1=""
    r10=""
    r100=""
    r1000=""
    n1=n%10
    n10=(n%100)//10
    n100=(n%1000)//100
    n1000=n//1000
    r1=onetoten(n1,"I","V","X")
    r10=onetoten(n10,"X","L","C")
    r100=onetoten(n100,"C","D","M")
    if n1000 > 0 :
        for i in range(1,n1000+1):
            r1000 = r1000 + "M"
    roman = r1000 + r100 + r10 + r1
    return roman
def onetoten(number,start,mid,end):
    roman=""
    if number < 4 :
        for i in range(1,number+1):
            roman= roman + start
    elif number < 7 :
        if number == 4 :
            roman= start + mid
        if number == 5 :
            roman= mid
        if number == 6 :
            roman= mid + start
    elif number < 9 :
        roman =mid
        for j in range(6,number+1):
            roman= roman + start
    elif number == 9:
        roman = start + end
    else :
        roman = end
    return roman