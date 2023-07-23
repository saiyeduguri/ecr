from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import ROC,RAC,RMC,COP,REG
from django.core.mail import send_mail
from django.conf import settings


def login(request):
    if request.method== 'POST':
        username = request.POST['name']
        password = request.POST['password']
        request.session['user'] = username
        ch=REG.objects.get(username=username)
        psd=ch.password
        

        if  psd==password:

            return render(request,'userview.html',{'name':username})
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    
def userview(request):
    name = request.session.get('user')
    return render(request,'userview.html',{'name':name})

def sign(request):

    if request.method == 'POST':
        
        username = request.POST['name']
        password1 = request.POST['pswd']
        password2 = request.POST['confpswd']
        email = request.POST['email']
        mob = request.POST['mobile']
        aadhar =request.POST['aadhar']
        add =request.POST['address']
        
        if password1==password2:
            if REG.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('sign')
            elif REG.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('sign')
            else:   
                user = REG(username=username, password=password1, email=email,mobile=mob,aadhar=aadhar,address=add)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('sign')
        return redirect('/')
        
    else:
        return render(request,'signup.html')
def roc(request):
    if request.method == 'POST':
        inc_det = request.POST['dai']
        area_det = request.POST['area']
        mobile = request.POST['phone']
        time = request.POST['time']
        psn=request.POST['psn']
        type=request.POST['type']
        vict_det = request.POST['victim']
        name = request.session.get('user')
        ro = ROC(username=name,incident_details=inc_det,area_details=area_det,mobile=mobile,time=time,type=type,PSNumber=psn,victim_details=vict_det)
        ro.save();
        return render(request,'userview.html')

    else:
        return render(request,'roc.html')

def rac(request):
    if request.method == 'POST':
        inc_det = request.POST['dai']
        area_det = request.POST['area']
        mobile = request.POST['phone']
        time = request.POST['time']
        vict_det = request.POST['victim']
        psn=request.POST['psn']
        type=request.POST['type']
        img=request.POST['img1']
        name1 = request.session.get('user')
        ra = RAC(username=name1,incident_details=inc_det,area_details=area_det,mobile=mobile,time=time,type=type,PSNumber=psn,victim_details=vict_det,image=img)
        ra.save();
        return render(request,'userview.html')

    else:
        return render(request,'rac.html')
    
def rmc(request):
    if request.method == 'POST':
        age =  request.POST['age']
        attr =  request.POST['attr']
        native =  request.POST['area']
        app_name =  request.POST['nap']
        missplace =  request.POST['place']
        mobile = request.POST['phone']
        time = request.POST['time']
        type=request.POST['type']
        psn=request.POST['psn']
        img=request.POST['img1']
        name = request.session.get('user')
        rm = RMC(name=name,age=age,attributes=attr,native_place=native,applicant_name=app_name,mobile=mobile,type=type,time=time,place_missed=missplace,PSNumber=psn,image=img)
        rm.save();
        return render(request,'userview.html')
    else:
        return render(request,'rmc.html')

def secindex(request):
        name = request.session.get('user')
        return render(request,'secindex.html',{'name':name})

def viewstatus(request):

    name = request.session.get('user')
    ch1=ROC.objects.get(username=name)
    st1=ch1.status
    ch2=RAC.objects.get(username=name)
    st2=ch2.status
    ch3=RMC.objects.get(applicant_name=name)
    st3=ch3.status

    return render(request,'viewstatus.html',{'name':name,'type1':'complaint','type2':'crime','type3':'missing','status1':st1,'status2':st2,'status3':st3})


def coplogin(request):
    if request.method== 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        request.session['copname'] = username
        ch=COP.objects.get(username=username)
        ps=ch.password
        if ps == password:
            return redirect('copview')
        else:
            messages.info(request,'invalid credentials')
            return redirect('coplogin')

    else:
        return render(request,'coplogin.html')   
     
def copview(request):
    name = request.session.get('copname')
    p=COP.objects.get(username=name)
    pin=p.PSNumber
    m=RMC.objects.filter(PSNumber=pin)
    a=RAC.objects.filter(PSNumber=pin)
    o=ROC.objects.filter(PSNumber=pin)

   
    return render(request,'copview.html',{'m':m,'a':a,'o':o})

def sendmail(request):
    sid = request.POST['sop']
    stype = request.POST['stype']
    cid = request.POST['cop']
    ctype = request.POST['ctype']
    em="saiyeduguri@gmail.com"
    subject="heii"
    message="hope you are doing well"
    if sid != "" and stype!="":
        if stype=='rac':
            ca=RAC.objects.get(id=sid)
            name=ca.username
            RAC.objects.filter(id=sid).update(status="under progress")
            subject='CRIME CASE REG'
            message='Your case has been registered and we will contact you shortly....We are with you'
            na=REG.objects.get(username=name)
            em=na.email
        elif stype=='rmc':
            cm=RMC.objects.get(id=sid)
            name=cm.applicant_name
            RMC.objects.filter(id=sid).update(status="under progress")
            nm=REG.objects.get(username=name)
            em=nm.email
            subject='MISSING CASE REG'
            message='Your case has been registered and we will contact you shortly'
        else :
            co=ROC.objects.get(id=sid)
            name=co.username
            ROC.objects.filter(id=sid).update(status="under progress")
            no=REG.objects.get(username=name)
            em=no.email
            subject='COMPLAINT REG'
            message='Your case has been registered and we will contact you shortly'
            from_email=settings.EMAIL_HOST_USER
            to_email=[em]   #must be list
            fail_silently = False
            send_mail(subject,message,from_email,to_email,fail_silently)
    if cid != "" and ctype!="":
        cid = request.POST['cop']
        ctype = request.POST['ctype']
        if ctype=='rac':
            saa=RAC.objects.get(id=cid)
            sau=saa.username
            RAC.objects.fiter(username=sau).delete()
        elif ctype=='roc':
            soa=RMC.objects.get(id=cid)
            sou=soa.username
            ROC.objects.fiter(username=sou).delete()
        else:
            sma=RMC.objects.get(id=cid)
            smu=sma.applicant_name
            delm=RMC.objects.get(applicant_name=smu)
            delm.delete()
    return render(request,'coplogin.html')

def vmp(request):
    if request.method== 'POST':
        num = request.POST['num']
        m=RMC.objects.filter(PSNumber=num)
        
        return render(request,'viewvmp.html',{'m':m})
    else:
        return render(request,'vmp.html')   

def vca(request):
    if request.method== 'POST':
        num = request.POST['num']
        o=ROC.objects.filter(PSNumber=num)
        
        
        a=RAC.objects.filter(PSNumber=num)
    
        


        return render(request,'viewvca.html',{'o':o,'a':a})
    else:
        return render(request,'vca.html')

def index(request):
    return render(request,'index.html')




