from django.shortcuts import render , redirect
from django.http import HttpResponse
import time
from copy import deepcopy
from .models import Billpayers , Billnonpayers

# Create your views here.

def home(request):
    return render(request , 'first.html')
def exit(request):
    global amount_decr
    global amount_debit1
    global amount_debit2
    global amount_tempdecr1
    global amount_tempdecr2
    global commpr
    global commprall
    global amount_payer 
    global name_payer 
    global name_nonpayer 

    amount_decr= []
    amount_debit1= []
    amount_debit2 = []
    amount_tempdecr1 = []
    amount_tempdecr2 = []
    name_nonpayer = []
    commpr = []
    commprall = []
    name_nonpayer = []
    name_payer = []
    return render(request , 'first.html')



def second(request):

    bill_payers = Billpayers.objects.all()
    return render(request , 'second.html' , {'checker':'False' , 'bill_payers':bill_payers})




def third(request):

    local_count = 0
    bill_payers = Billpayers.objects.all()
    for i in bill_payers:
        local_count+=1
    if local_count == 0:
        return render(request ,'second.html' ,{'errmsg' : 'Number of payers cannot be null', 'checker':'True'} )
    else:  
        bill_nonpayers = Billnonpayers.objects.all()
        return render(request ,'third.html',{'bill_nonpayers':bill_nonpayers})
def thirdback(request):
    global amount_decr
    global amount_debit1
    global amount_debit2
    global amount_tempdecr1
    global amount_tempdecr2
    global commpr
    global commprall
    global amount_payer 
    global name_payer 
    global name_nonpayer 
    bill_nonpayers = Billnonpayers.objects.all()
    return render(request,'third.html',{'bill_nonpayers':bill_nonpayers})

def backtest(request):
    return render(request ,'third.html')
u = 0
frr = []
name_payer =[]
amount_payer = []
payer = []

def forth(request):
    duplicate_local = False
    temp2 = request.POST['temp']
    temp1 = request.POST['temp1']
    if temp2.isalnum() == False or temp1.isnumeric() == False or temp1 == '0' :
        return render(request ,'modal.html' , {'checkblank' :'True' , 'blankmsg' : 'Please give proper input'})
    else:
        bill_payers = Billpayers.objects.all()
        for i in bill_payers:
            if((temp2 == i.temp2) and (temp1 == i.temp1)):
                duplicate_local = True
                bill_payers_duplicate = Billpayers.objects.all().filter(temp2 = temp2)
                return render(request,'modal.html',{'duplicate':'True', 'war_msg': 'This name and amount already exist' , 'bill_payers_duplicate':bill_payers_duplicate })       
        if duplicate_local == False:
            bill_payers = Billpayers.objects.create(temp2 = temp2 , temp1 = temp1 )
            bill_payers.save()
            bill_payers = Billpayers.objects.all()
            return render(request,'second.html',{'bill_payers': bill_payers , 'duplicate':'False' })

def sixth(request,id):
    duplicate_local = False
    bill_payers = Billpayers.objects.all().filter(id=id)
    bill_payers_edit = Billpayers.objects.get(id=id)
    temp2 = request.POST['temp']
    temp1 = request.POST['temp1']
    if temp2.isalnum() == False or temp1.isnumeric() == False or temp1 == '0' :        
        return render(request ,'editor.html' , {'checkblank' :'True' , 'blankmsg' : 'Please give proper input','bill_payers':bill_payers})
    else:
        bill_payers_editor = Billpayers.objects.all()        
        for j in bill_payers:
            for i in bill_payers_editor:
                if(i.temp2 != j.temp2 or i.temp1 != j.temp1 ):
                    if((temp2 == i.temp2) and (temp1 == i.temp1)):
                        duplicate_local = True
                        if (duplicate_local == True):                            
                            bill_payers_duplicate = Billpayers.objects.all().filter(temp2 = temp2)
                            return render(request,'editor.html',{'duplicate':'True', 'war_msg': 'This name and amount already exist' , 'bill_payers_duplicate':bill_payers_duplicate,'bill_payers':bill_payers })       
        if duplicate_local == False:
            bill_payers_edit.temp2 = request.POST['temp']
            bill_payers_edit.temp1 = request.POST['temp1']
            bill_payers_edit.save()
            bill_payers_append = Billpayers.objects.all()
            return render(request,'second.html',{'bill_payers': bill_payers_append })

def seventh(request,id):
    duplicate_local = False
    bill_nonpayers = Billnonpayers.objects.all().filter(id=id)
    bill_nonpayers_edit = Billnonpayers.objects.get(id=id)
    temp5 = request.POST['temp5']
    if temp5.isalnum() == False :
        return render(request ,'edit.html' , {'checkblanksec' :'True' , 'blankmsgsec' : 'Please give proper input','bill_nonpayers' : bill_nonpayers})
    else:
        bill_nonpayers_editor = Billnonpayers.objects.all()        
        for j in bill_nonpayers:
            for i in bill_nonpayers_editor:
                if(i.temp5 != j.temp5):
                    if(temp5 == i.temp5):
                        duplicate_local = True
                        if (duplicate_local == True):                            
                            bill_nonpayers_duplicate = Billnonpayers.objects.all().filter(temp5 = temp5)
                            return render(request,'edit.html',{'duplicate':'True', 'war_msg': 'This name already exists' , 'bill_nonpayers_duplicate':bill_nonpayers_duplicate,'bill_nonpayers':bill_nonpayers })       
        if duplicate_local == False:
            bill_nonpayers_edit.temp5 = request.POST['temp5']
            bill_nonpayers_edit.save()
            bill_nonpayers_edit = Billnonpayers.objects.all()
            return render(request,'third.html',{'bill_nonpayers': bill_nonpayers_edit })


def modal(request):
    return render(request,'modal.html', { 'checkblank' :'False' })
def modalsec(request):
    return render(request,'modalsec.html',{ 'checkblanksec' :'False'})


def fifth(request):
    duplicate_local = False
    temp5 = request.POST['temp5']
    if temp5.isalnum() == False :
        return render(request ,'modalsec.html' , {'checkblanksec' :'True' , 'blankmsgsec' : 'Please give proper input'})
    else:
        bill_nonpayers = Billnonpayers.objects.all()
        for i in bill_nonpayers:
            if(temp5 == i.temp5):
                duplicate_local = True
                bill_nonpayers_duplicate = Billnonpayers.objects.all().filter(temp5 = temp5)
                return render(request,'modalsec.html',{'duplicate':'True', 'war_msg': 'This name already exists' , 'bill_nonpayers_duplicate':bill_nonpayers_duplicate })       

        if duplicate_local == False :
            bill_nonpayers = Billnonpayers.objects.create(temp5 = temp5)
            bill_nonpayers.save()
            bill_nonpayers = Billnonpayers.objects.all()
            return render(request,'third.html',{'bill_nonpayers':bill_nonpayers,'duplicate':'False'})


def delete(request,id):
    global name_nonpayer
    global namer
    global count_nonpayer
    bill_nonpayers_delete = Billnonpayers.objects.filter(id=id).delete()
    bill_nonpayers_append = Billnonpayers.objects.all()
    return render(request,'third.html',{'bill_nonpayers':bill_nonpayers_append})


def deleter(request,id):
    global name_payer
    global temper
    global amount_payer
    global payer
    global u        
    bill_payers_delete = Billpayers.objects.filter(id=id).delete()
    bill_payers_append = Billpayers.objects.all()
    return render(request,'second.html',{'bill_payers':bill_payers_append} )


def editor(request,id,temp2,temp1):
    
    bill_payers_editor = Billpayers.objects.get(id=id)
    name_payer = bill_payers_editor.temp2
    price_payer = bill_payers_editor.temp1
    bill_payers_editor = Billpayers.objects.all().filter(id=id)
    return render(request,'editor.html',{'bill_payers':bill_payers_editor ,'name_payer':name_payer ,'price_payer':price_payer } )

def edit(request,id,temp5):
    bill_nonpayers_edit = Billnonpayers.objects.get(id=id)
    name_nonpayer = bill_nonpayers_edit.temp5
    bill_nonpayers_edit = Billnonpayers.objects.all().filter(id=id)
    return render(request,'edit.html',{'bill_nonpayers': bill_nonpayers_edit,'name_nonpayer':name_nonpayer})

def test(request):
    amount_decr = []
    amount_debit1 = []
    amount_debit2 = []
    amount_tempdecr1 = []
    amount_tempdecr2 = []
    commpr =[]
    commprall =[]
    pers_get_count = 0 
    amount_payer = []
    name_payer = []
    name_nonpayer = []
    bill_payers = Billpayers.objects.all()
    
    for i in bill_payers:
        amount_payer.append(int(i.temp1))
        name_payer.append(i.temp2)
    bill_nonpayers = Billnonpayers.objects.all()
    for j in bill_nonpayers:
        name_nonpayer.append(j.temp5)

    
    for pp in range(0,len(amount_payer)-1):
        for qq in range(0,len(amount_payer)-1):
            if(amount_payer[qq]-amount_payer[qq+1]<0):
                temp_swap = amount_payer[qq+1]
                amount_payer[qq+1] = amount_payer[qq]
                amount_payer[qq] = temp_swap
                temp_swap_name = name_payer[qq+1]
                name_payer[qq+1] = name_payer[qq]
                name_payer[qq] = temp_swap_name
    amount_total = 0
    num = len(name_payer) + len(name_nonpayer)
    payer_count = len(name_payer)
    diff = num - payer_count

    for ff in range(0,diff):
        amount_payer.append(0)
    for i in range(0,payer_count):
        amount_total = amount_total + amount_payer[i]

    amount_each = amount_total//num

    for i in range(0,num):
        temp2 = amount_payer[i] - amount_each
        amount_decr.append(temp2)
    for p in range(0,payer_count):
        if(amount_decr[p] >= 0):
            pers_get_count+=1
            first_pr = "\n"+ ' ' + name_payer[p]+' ' + "will get a total amount of Rs." + ' ' + str(abs(amount_decr[p])) + '\n'
            commprall.append(first_pr)
 

    for i in range(0,pers_get_count):
        temp10 = amount_decr[i]
        amount_tempdecr1.append(temp10)
        for j in range(pers_get_count,num):
            temp11 = amount_decr[j]
            amount_tempdecr2.append(temp11)
            if(amount_decr[j]!=0):
                if((amount_tempdecr1[i]-(0-amount_decr[j]))==0):
                    if(payer_count >= j+1):
                        second_pr = "\n" + ' ' + name_payer[i]+ ' ' + "will get Rs." + ' ' + str(abs(0-amount_decr[j])) + ' ' + "from" + ' ' + name_payer[j] + ' '
                    else:
                        k = j- payer_count
                        second_pr = "\n" + ' ' + name_payer[i]+ ' ' + "will get Rs." + ' ' + str(abs(0-amount_decr[j])) + ' ' + "from" + ' ' + name_nonpayer[k] + ' '                   
                    commpr.append(second_pr)
                    amount_tempdecr1[i] = 0
                    amount_decr[j] = 0
                    break
                
                if((amount_tempdecr1[i]-(0-amount_decr[j]))>0):
                                
                    temp4 = 0-amount_decr[j]
                    amount_debit1.append(temp4)
                    if(payer_count >= j+1):
                        third_pr = "\n" + ' ' + name_payer[i] + ' ' + "will get Rs." + ' ' + str(abs(temp4)) + ' ' + "from" + ' ' + name_payer[j]
                    else:
                        k= j- payer_count
                        third_pr = "\n" + ' ' + name_payer[i] + ' ' + "will get Rs." + ' ' + str(abs(temp4)) + ' ' + "from" + ' ' + name_nonpayer[k]
                    commpr.append(third_pr)
                    amount_tempdecr1[i] = amount_tempdecr1[i] + amount_decr[j]
                    amount_decr[j]=0
                    
                
                if((amount_tempdecr1[i]-(0-amount_decr[j]))<0):
                
                    temp5 = (amount_tempdecr1[i]+amount_decr[j])
                    if(payer_count >= j+1):
                        fourth_pr = "\n" + ' ' + name_payer[i] + ' ' + "will get Rs." + ' ' + str(abs(amount_tempdecr1[i])) + ' ' + "from"+ ' ' + name_payer[j]
                    else:
                        k= j- payer_count
                        fourth_pr = "\n" + ' ' + name_payer[i] + ' ' + "will get Rs." + ' ' + str(abs(amount_tempdecr1[i])) + ' ' + "from"+ ' ' + name_nonpayer[k]
                        
                    commpr.append(fourth_pr)
                    amount_debit2.append(amount_tempdecr1[i])
                    amount_decr.pop(j)
                    amount_decr.insert(j,temp5)
                    amount_tempdecr1[i] = 0
                    break

    return render(request ,'test.html' , {'commpr' : commpr , 'commprall': commprall } )