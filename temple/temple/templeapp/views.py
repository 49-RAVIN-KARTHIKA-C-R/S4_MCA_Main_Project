import re
from datetime import datetime
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from templeapp.models import *
from django.core.mail import send_mail
import random
def index(request):
    return render(request,'index.html')
def login1(request):
    return render(request,'LOGIN.html')
def logout(request):
    auth.logout(request)
    return render(request,'LOGIN.html')
@login_required(login_url='/')
def mng_committee(request):
    ob = committee.objects.all()
    return render(request, 'ADMIN-ADD & MANAGE COMMITTEE.html',{'val':ob})
@login_required(login_url='/')
def add_mng_committee(request):
    return render(request, 'ADMIN-ADD & MANAGE COMMITTEE_ADDING NEW.html')
@login_required(login_url='/')

def add_mng_auditorium(request):
    ob=auditorium.objects.all()
    return render(request, 'ADMIN-ADD -MANAGE AUDITORIUM.html',{'val':ob})
@login_required(login_url='/')

def tmp_pgm_page(request):
    ob=program.objects.all()
    return render(request, 'ADMIN-ADD PROGRAM PAGE.html',{'val':ob})
@login_required(login_url='/')

def add_video(request):
    ob=videos.objects.all()
    return render(request, 'ADMIN-ADD VIDEO.html',{'val':ob})
@login_required(login_url='/')

def aud_bill_generate(request,id):
    ob=auditorium_booking.objects.get(id=id)
    ob1=auditorium.objects.get(id=2)
    return render(request, 'ADMIN-AUDITORIUM BILL GENERATE.html',{'v':ob,'v1':ob1})
@login_required(login_url='/')

def aud_bill_generate1(request,id):
    ob=auditorium_booking.objects.get(id=id)
    ob1=auditorium.objects.get(id=2)
    return render(request, 'ADMIN-AUDITORIUM BILL GENERATE1.html',{'v':ob,'v1':ob1})
@login_required(login_url='/')

def admin_home(request):
    return render(request, 'ADMIN-HOME PAGE.html')
@login_required(login_url='/')

def manage_auditorium(request):
    ob = auditorium.objects.all()
    return render(request, 'ADMIN-MANAGE AUDITORIUM.html',{'val':ob})
@login_required(login_url='/')

def add_tmp_pgm_page(request):
    ob = program.objects.all()
    return render(request, 'ADMIN-PGM PAGE-ADDING NEW.html',{'val':ob})
@login_required(login_url='/')

def user_manage(request):
    ob=user.objects.all()
    return render(request, 'ADMIN-USER MANAGEMENT.html',{'val':ob})
@login_required(login_url='/')

def admin_view_videos(request):
    ob=videos.objects.all()
    print(ob)
    return render(request, 'ADMIN-VIDEOS.html',{'val':ob})
@login_required(login_url='/')

def mng_aud_booking(request):
    ob=auditorium_booking.objects.all()
    return render(request, 'ADMIN-VIEW & MANAGE AUDITORIUM BOOKING.html',{'val':ob})
@login_required(login_url='/')

def view_verified_booking(request):
    ob=auditorium_booking.objects.all()
    return render(request, 'ADMIN-VIEW-AUDITORIUM BOOKING.html',{'v':ob})
@login_required(login_url='/')

def view_user_manage(request):
    ob=login.objects.all()
    return render(request, 'ADMIN-VIEW _USER MANAGEMENT.html',{'val':ob})
@login_required(login_url='/')

def view_reports_auditorium(request):
    return render(request, 'ADMIN-VIEW REPORTS OF AUDITORIUM.html')
@login_required(login_url='/')

def view_reports_auditorium1(request):
    sdate=request.POST['textfield']
    edate=request.POST['textfield2']
    ob=auditorium_booking.objects.filter(Q(date__gte=sdate,date__lte=edate,status='approved')|Q(date__gte=sdate,date__lte=edate,status='paid'))
    ob1=auditorium_booking.objects.filter(Q(date__gte=sdate,date__lte=edate,status='approved')|Q(date__gte=sdate,date__lte=edate,status='paid')).aggregate(Count('id'))
    return render(request, 'ADMIN-VIEW REPORTS OF AUDITORIUM.html',{'v':ob,'v1':ob1,'total':ob1['id__count'],'sdate':sdate,'edate':edate})
@login_required(login_url='/')

def view_add_committee(request):
    return render(request, 'ADMIN-VIEW-ADD & MANAGE COMMITTEE.html')
@login_required(login_url='/')

def view_add_pgm(request):
    return render(request, 'ADMIN-VIEW-ADD PGM.html')
@login_required(login_url='/')

def view_manage_aud(request):
    return render(request, 'ADMIN-VIEW-MANAGE AUDITORIUM.html')
@login_required(login_url='/')

def edit_manage_committee(request,id):
    ob=committee.objects.get(login_id__id=id)
    request.session['cid']=id
    return render(request, 'ADMIN_EDIT_MANAGE_COMMITTEE.html',{'val':ob})
@login_required(login_url='/')

def edit_manage_auditorium(request,id):
    ob=auditorium.objects.get(id=id)
    request.session['aid']=id
    return render(request, 'ADMIN-EDIT-MANAGE-AUDITORIUM.html',{'val':ob})
@login_required(login_url='/')

def edit_temple_pgm(request,id):
    ob=program.objects.get(id=id)
    request.session['tpm']=id
    return render(request, 'ADMIN-EDIT-TEMPLE-PGM.html',{'val':ob})
@login_required(login_url='/')

def edit_videos(request,id):
    ob=program.objects.get(id=id)
    request.session['vid']=id
    return render(request, 'ADMIN-EDIT-VIDEOS.html',{'val':ob})
@login_required(login_url='/')

def about_chitti(request):
    ob=chitti.objects.filter(committee_id__login_id__id=request.session['lid'])
    return render(request, 'COMMITTEE-ABOUT CHITTI.html',{'val':ob})
@login_required(login_url='/')

def add_about_chitti(request):
    return render(request, 'COMMITTEE-ADD ABOUT CHITTI.html')
@login_required(login_url='/')

def cm_add_pgms(request):
    ob=committe_program.objects.all()
    return render(request, 'COMMITTEE-ADD PGMS.html',{'val':ob})
@login_required(login_url='/')

def chitti_details_mbr(request):
    ob=chitti_details.objects.filter(chitti_id__committee_id__login_id__id=request.session['lid'])
    return render(request, 'COMMITTEE-CHITTI DETAILS OF MEMBER.html',{'val':ob})
@login_required(login_url='/')

def committee_home(request):
    ob=committee.objects.all()
    obb = committee.objects.get(login_id__id=request.session['lid'])
    print(obb, "***********************************************")
    return render(request, 'COMMITTEE-HOME PAGE.html',{'val':ob,'val1': obb})
@login_required(login_url='/')

def committee_pgms(request):
    ob=committe_program.objects.filter(committee_id__login_id__id=request.session['lid'])
    return render(request, 'COMMITTEE-PGMS.html',{'val':ob})
@login_required(login_url='/')

def cm_select_winners(request):
    ob=chitti.objects.filter(committee_id__login_id__id=request.session['lid'])
    return render(request, 'COMMITTEE-SELECT WINNERS.html',{'val':ob})
@login_required(login_url='/')

def verified_members(request):
    ob=members.objects.all()
    return render(request, 'COMMITTEE-VERIFIED MEMBER.html',{'val':ob})
@login_required(login_url='/')

def verify_members(request):
    ob=members.objects.filter(committee_id__login_id__id=request.session['lid'])
    return render(request, 'COMMITTEE-VERIFY MEMBER.html',{'val':ob})
@login_required(login_url='/')

def cm_view_about_chitti(request):
    return render(request, 'COMMITTEE-VIEW ABOUT CHITTI.html')
@login_required(login_url='/')

def cm_view_add_pgms(request):
    return render(request, 'COMMITTEE-VIEW ADD PGMS.html')
@login_required(login_url='/')

def cm_view_payed_chitti(request):
    ob1 = chitti.objects.filter(committee_id__login_id__id=request.session['lid'])
    return render(request, 'COMMITTEE-VIEW PAYED CHITTI  MEMBERS.html',{'v':ob1})
@login_required(login_url='/')

def cm_view_payed_chitti1(request):
    ob1 = chitti.objects.all()
    chiti=request.POST['chittitype']
    request.session['cid']=chiti
    mnth=request.POST['month']
    request.session['month']=mnth
    oob=chitti_details.objects.filter(chitti_id__id=chiti)
    ob = chitti_payment.objects.filter(details_id__chitti_id__id=chiti, date__month=mnth,
                                       date__year=datetime.today().year)

    return render(request, 'COMMITTEE-VIEW PAYED CHITTI  MEMBERS.html',
                      {'res':oob,'val': ob, 'v': ob1, 'mnth': int(mnth), 'c': int(chiti)})
@login_required(login_url='/')

def cm_view_payed_chitti2(request,id):
    ob1 = chitti.objects.all()
    chiti=request.session['cid']
    mnth=request.session['month']
    oob=chitti_details.objects.filter(chitti_id__id=chiti)
    try:
        ob = chitti_payment.objects.get(details_id__chitti_id__id=chiti, date__month=mnth,
                                           date__year=datetime.today().year,details_id=id)
        return render(request, 'COMMITTEE-VIEW PAYED CHITTI  MEMBERS.html',
                          {'res':oob,'value': ob, 'v': ob1, 'mnth': int(mnth), 'c': int(chiti)})
    except:
        return render(request, 'COMMITTEE-VIEW PAYED CHITTI  MEMBERS.html',
                      {'res': oob, 'value': '0', 'v': ob1, 'mnth': int(mnth), 'c': int(chiti)})

@login_required(login_url='/')


def cm_view_selected_winners(request):
    ob=chitti_details.objects.filter(status='allotted',chitti_id__committee_id__login_id__id=request.session['lid'])
    obb=winner.objects.values('date').distinct()
    ob1 = chitti.objects.filter(committee_id__login_id__id=request.session['lid'])
    print(obb,"===============================================")
    ob2=chitti.objects.filter(committee_id__login_id__id=request.session['lid'])
    return render(request, 'COMMITTEE-VIEW SELECTED WINNERS.html',{'val':ob,'val1':obb,'v1':ob1,'v2':ob2})
@login_required(login_url='/')

def cm_view_temple_pgm(request):
    ob=program.objects.all()
    return render(request, 'COMMITTEE-VIEW TEMPLE PGMS.html',{'val':ob})
@login_required(login_url='/')

def cm_view_winners(request):
    ob=chitti.objects.filter(committee_id__login_id__id=request.session['lid'])
    return render(request, 'COMMITTEE-VIEW WINNERS.html',{'v':ob})
@login_required(login_url='/')

def cm_view_winners1(request):
    chiti=request.POST['chittitype']
    mnth=request.POST['month']
    ob=chitti.objects.all()
    obb=winner.objects.filter(date__month=mnth,date__year=datetime.today().year,chitti_id__id=chiti)
    print(obb,"=========================")
    ob1=chitti.objects.get(id=chiti)
    return render(request, 'COMMITTEE-VIEW WINNERS.html',{'v':ob,'c':int(chiti),'mnth':int(mnth),'res':obb,'amt':ob1})
@login_required(login_url='/')

def cm_view_video(request):
    ob=videos.objects.all()
    return  render(request,'COMMITTEE-VIEW-VIDEO.html',{'val':ob})
@login_required(login_url='/')

def cm_edit_add_chitti(request,id):
    ob = chitti.objects.get(id=id)
    request.session['eac'] = id
    return render(request,'COMMITTIEE- EDIT ADD CHITTI.html',{'val':ob})
@login_required(login_url='/')

def cm_edit_cm_pgm(request,id):
    ob=committe_program.objects.get(id=id)
    request.session['ecp']=id
    return render(request,'COMMITTEE-EDIT-CM-PGM.html',{'val':ob})
@login_required(login_url='/')

def mbr_chitti_details1(request):
    oo = members.objects.get(login_id__id=request.session['lid'])
    ob1 = chitti.objects.filter(committee_id=oo.committee_id)
    # ob1=chitti.objects.all()
    print(ob1,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return render(request,'MEMBER-CHITTI DETAILS1.html',{'v':ob1})
@login_required(login_url='/')

def mbr_chitti_details(request):
    try:
        chiti=request.POST['chittitype']
        ob=chitti_details.objects.filter(member_id__login_id__id=request.session['lid'],chitti_id__id=chiti)
        ob1=chitti_payment.objects.get(details_id__member_id__login_id__id=request.session['lid'],date__month=datetime.today().month,date__year=datetime.today().year,details_id__chitti_id__id=chiti)
        print(ob1,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        oo = members.objects.get(login_id__id=request.session['lid'])
        ob2 = chitti.objects.filter(committee_id=oo.committee_id)
        return render(request,'MEMBER-CHITTI DETAILS1.html',{'val':ob,'v':ob2,'count':int(chiti),'p':int(1)})
    except:
        chiti = request.POST['chittitype']
        ob = chitti_details.objects.filter(member_id__login_id__id=request.session['lid'], chitti_id__id=chiti)
        oo = members.objects.get(login_id__id=request.session['lid'])
        ob2 = chitti.objects.filter(committee_id=oo.committee_id)
        return render(request, 'MEMBER-CHITTI DETAILS1.html', {'val': ob, 'v': ob2, 'count': int(chiti), 'p': int(0)})
@login_required(login_url='/')

def mbr_edit_profile(request):
    ob=members.objects.get(login_id__id=request.session['lid'])
    return render(request, 'MEMBER-EDIT PROFILE.html',{'val':ob})
@login_required(login_url='/')

def member_home(request):
    return render(request, 'MEMBER-HOME PAGE.html')
@login_required(login_url='/')

def mbr_payment(request,id):
    request.session['cdid']=id
    ob = members.objects.get(login_id__id=request.session['lid'])
    obb = chitti_details.objects.get(member_id__login_id__id=request.session['lid'],id=id)
    request.session['amt']=obb.chitti_id.chitti_amount
    return render(request, 'MEMBER-PAYMENT.html',{'v':obb,'v2':ob})
@login_required(login_url='/')

def mbr_profile(request):
    ob=members.objects.get(login_id__id=request.session['lid'])
    return render(request, 'MEMBER-PROFILE.html',{'val':ob})
def mbr_registration(request):
    ob=committee.objects.all()
    return render(request, 'MEMBER-REGISTRATION.html',{'val':ob})
@login_required(login_url='/')

def mbr_view_cm_pgm(request):
    oo = members.objects.get(login_id__id=request.session['lid'])
    ob = committe_program.objects.filter(committee_id=oo.committee_id)
    # ob=committe_program.objects.all()
    return render(request, 'MEMBER-VIEW COMMITTEE PGM.html',{'val':ob})
@login_required(login_url='/')

def mbr_view_payment(request):
    return render(request, 'MEMBER-VIEW PAYMENT.html')
@login_required(login_url='/')

def mbr_view_tmp_pgm(request):
    ob = program.objects.all()
    return render(request, 'MEMBER-VIEW TEMPLE PGMS.html', {'val': ob})
@login_required(login_url='/')

def mbr_view_video(request):
    ob = videos.objects.all()
    return render(request, 'MEMBER-VIEW VIDEO.html',{'val':ob})
@login_required(login_url='/')

def mbr_view_winner(request):
    oo=members.objects.get(login_id__id=request.session['lid'])
    ob1 = chitti.objects.filter(committee_id=oo.committee_id)
    ob = chitti_details.objects.filter(status='allotted')
    obb = winner.objects.values('date').distinct()
    print(obb, "===============================================")
    ob2 =chitti.objects.filter(committee_id=oo.committee_id)
    return render(request, 'MEMBER-VIEW WINNER.html', {'val': ob, 'val1': obb, 'v1': ob1, 'v2': ob2})
    # return render(request, 'MEMBER-VIEW WINNER.html')
@login_required(login_url='/')

def mbr_view_paid_chitti_status(request,id):
    ob=chitti_payment.objects.filter(details_id__id=id).values('date')
    print(ob,"========================")
    return render(request, 'MEMBER -VIEW PAYMENT HISTORY.html',{'v':ob})
@login_required(login_url='/')


def mbr_pay_month(requset):
    return  render(requset,'MEMBER-PAY-MONTH.html')


@login_required(login_url='/')

def usr_adv_payment(request):
    return render(request, 'USER-ADVANCE PAYMENT.html')
@login_required(login_url='/')

def usr_aud_booking(request):
    ob=user.objects.get(login_id__id=request.session['lid'])
    current=str(datetime.today().date())
    print(current)
    return render(request, 'USER-AUDITORIUM BOOKING.html',{'val':ob,'cdt':current})
@login_required(login_url='/')

def usr_edit_profile(request):
    ob=user.objects.get(login_id__id=request.session['lid'])
    return render(request, 'USER-EDIT PROFILE.html',{'val':ob})
@login_required(login_url='/')

def user_home(request):
    return render(request, 'USER-HOME PAGE.html')
@login_required(login_url='/')

def user_terms_and_conditions(request):
    return render(request,'USER-TERMS AND CONDITIONS ON PAYMENT.html')
# def usr_home(request):
#     return render(request, 'USER-PROFILE.html')
def usr_registration(request):
    return render(request, 'USER-REGISTRATION FORM OF USER.html')
@login_required(login_url='/')

def usr_view_adv_payment(request):
    ob=user.objects.get(login_id__id=request.session['lid'])
    obb=auditorium.objects.get(id=2)
    request.session['amt']=obb.advance_charge
    # request.session['bid']=id
    return render(request, 'USER-ADVANCE PAYMENT.html',{'val':ob,'v1':obb})
@login_required(login_url='/')

def make_payy(request):
    bank1=request.POST['bank']
    ifc=request.POST['textfield22']
    pin=request.POST['textfield23']
    accno=request.POST['textfield24']
    amt=request.session['amt']
    cid=request.session['cdid']
    ob=bank.objects.get(bank_name=bank1,ifsc=ifc,pin=pin,acc_no=accno)
    print(ob,"===========================")
    if ob is None:
        return HttpResponse('''<script>alert("Invalid User"),window.location="/member_home"</script>''')
    else:
        ob.amount=ob.amount-amt
        ob.save()
        aob=chitti_payment()
        aob.date=datetime.today()
        ob1=chitti_details.objects.get(id=cid)
        aob.details_id=ob1
        aob.status='paid'
        aob.save()
        return HttpResponse('''<script>alert("Payment Done!!!"),window.location="/member_home"</script>''')
@login_required(login_url='/')

def make_pay(request):
    bank1=request.POST['bank']
    ifc=request.POST['textfield2']
    pin=request.POST['textfield3']
    accno=request.POST['textfield4']
    amt=request.session['amt']
    bid=request.session['bid']
    ob=bank.objects.get(bank_name=bank1,ifsc=ifc,pin=pin,acc_no=accno)
    print(ob,"===========================")
    if ob is None:
        return HttpResponse('''<script>alert("Invalid User"),window.location="/user_home"</script>''')
    else:
        ob.amount=ob.amount-amt
        ob.save()
        aob=auditorium_booking.objects.get(id=bid)
        aob.status='paid'
        aob.save()
        return HttpResponse('''<script>alert("Payment Done!!!"),window.location="/user_home"</script>''')

@login_required(login_url='/')


def usr_declaration(request,id):
    request.session['bid']=id
    return render(request, 'USER-DECLARATION.html')
@login_required(login_url='/')

def usr_view_aud(request):
    ob=auditorium.objects.get(id=2)
    return render(request, 'USER-VIEW AUDITORIUM.html',{'val':ob})
@login_required(login_url='/')

def usr_view_aud_bill(request):
    return render(request, 'USER-VIEW AUDITORIUM BILL.html')
@login_required(login_url='/')
def usr_view_booking_sts(request):
    ob=auditorium_booking.objects.filter(user_id__login_id__id=request.session['lid'])
    return render(request, 'USER-VIEW BOOKING STATUS.html',{'val':ob})
@login_required(login_url='/')
def usr_view_tmp_pgm(request):
    ob=program.objects.all()
    return render(request, 'USER-VIEW TEMPLE PGM.html',{'val':ob})
@login_required(login_url='/')

def usr_view_video(request):
    ob=videos.objects.all()
    return render(request, 'USER-VIEW VIDEO.html',{'val':ob})
@login_required(login_url='/')

def usr_profile(request):
    ob=user.objects.get(login_id__id=request.session['lid'])
    return render(request,'USER-PROFILE.html',{'val':ob})
def usr_view_history(request):
    return render(request, 'USER-HISTORY.html')


#create add part

def login2(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    try:
        ob=login.objects.get(user_name=uname,password=pswd)
        print(ob,"=======")
        if ob is None:
            return HttpResponse('''<script>alert("Invalid"),window.location="/"</script>''')
        elif ob.type=="admin":
            request.session['lid']=ob.id
            obb=auth.authenticate(username='admin',password='admin')
            if obb is not None:
                auth.login(request,obb)
            return redirect("/admin_home")
        elif ob.type=="committee":
            request.session['lid']=ob.id
            obb = auth.authenticate(username='admin', password='admin')
            if obb is not None:
                auth.login(request, obb)
            return redirect("/committee_home")
        elif ob.type=="member":
            request.session['lid']=ob.id
            obb = auth.authenticate(username='admin', password='admin')
            if obb is not None:
                auth.login(request, obb)
            return redirect("/member_home")
        elif ob.type == "user":
            request.session['lid']=ob.id
            obb = auth.authenticate(username='admin', password='admin')
            if obb is not None:
                auth.login(request, obb)
            return redirect("/user_home")
        else:
            return HttpResponse('''<script>alert("Invalid"),window.location="/"</script>''')
    except:
        return HttpResponse('''<script>alert("Invalid"),window.location="/"</script>''')

def member_login(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    hname=request.POST['textfield3']
    street=request.POST['textfield4']
    city=request.POST['textfield5']
    pin=request.POST['textfield6']
    phonenumber=request.POST['textfield7']
    email=request.POST['textfield8']
    aadhar=request.POST['textfield9']
    cm_name=request.POST['committieename']
    uname = request.POST['textfield10']
    pswd = request.POST['textfield11']
    photo = request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(photo.name,photo)
    lob=login()
    lob.user_name=uname
    lob.password=pswd
    lob.type='pending'
    lob.save()
    mob=members()
    mob.first_name=fname
    mob.last_name=lname
    mob.house_name=hname
    mob.street=street
    mob.city=city
    mob.pin=pin
    mob.phone=phonenumber
    mob.email=email
    mob.aadhar_number=aadhar
    mob.photo=fn
    mob.login_id=lob
    cid=committee.objects.get(login_id__id=cm_name)
    mob.committee_id=cid
    mob.save()
    return HttpResponse('''<script> alert("Successfully registered");window.location="/"</script>''')


def user_login(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    fathersname=request.POST['textfield22']
    hname=request.POST['textfield3']
    street=request.POST['textfield4']
    city=request.POST['textfield5']
    pin=request.POST['textfield6']
    phone_number=request.POST['textfield7']
    email=request.POST['textfield8']
    aadhar_number=request.POST['textfield9']
    uname=request.POST['textfield10']
    pwd=request.POST['textfield11']
    photo=request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(photo.name, photo)
    lob=login()
    lob.user_name=uname
    lob.password=pwd
    lob.type = 'pending'
    lob.save()
    uob=user()
    uob.first_name=fname
    uob.last_name=lname
    uob.fathers_name=fathersname
    uob.house_name=hname
    uob.street=street
    uob.city=city
    uob.pin=pin
    uob.phone=phone_number
    uob.email=email
    uob.aadhar_number=aadhar_number
    uob.photo=fn
    uob.login_id=lob
    uob.save()
    return HttpResponse('''<script> alert("Successfully registered");window.location="/"</script>''')
#add (admin)
@login_required(login_url='/')

def add_committee(request):
    try:
        cm_name=request.POST['textfield']
        president=request.POST['textfield2']
        secretary=request.POST['textfield6']
        no_members=request.POST['textfield3']
        phn=request.POST['textfield4']
        email1=request.POST['textfield9']
        uname=request.POST['textfield7']
        pwd=request.POST['textfield8']
        lob = login()
        lob.user_name = uname
        lob.password = pwd
        lob.type = 'committee'
        lob.save()
        ac=committee()
        ac.committee_name = cm_name
        ac.president=president
        ac.secretary=secretary
        ac.no_members=no_members
        ac.phone=phn
        ac.email=email1
        ac.login_id = lob
        ac.save()
        send_mail('TEMPLE', "YOUR LOGIN USERNAME & PASSWORD IS  -" + uname+","+pwd, 'ravinkarthikacr1998@gmail.com', [email1],
                  fail_silently=False)
        return HttpResponse('''<script> alert("Successfully added");window.location="/mng_committee"</script>''')
    except:
        return HttpResponse('''<script> alert("failed");window.location="/mng_committee"</script>''')


@login_required(login_url='/')

def add_auditorium(request):
    aud_name=request.POST['textfield']
    place=request.POST['textfield2']
    phone=request.POST['textfield3']
    seats=request.POST['textfield4']
    charge=request.POST['textfield5']
    details = request.POST['textfield7']
    ad_pay = request.POST['textfield6']
    photo=request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(photo.name, photo)
    ad=auditorium()
    ad.auditorium_name=aud_name
    ad.place=place
    ad.phone=phone
    ad.seats=seats
    ad.charge=charge
    ad.details=details
    ad.advance_charge=ad_pay
    ad.photo=fn
    ad.save()
    return HttpResponse('''<script> alert("Successfully added");window.location="/manage_auditorium"</script>''')


@login_required(login_url='/')

def add_temple_pgm(request):
    pgm=request.POST['textfield']
    guest=request.POST['textfield2']
    date=request.POST['textfield3']
    time=request.POST['textfield4']
    photo=request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(photo.name,photo)
    at=program()
    at.program=pgm
    at.guest=guest
    at.date=date
    at.time=time
    at.photo=fn
    at.save()
    return HttpResponse('''<script> alert("Successfully added");window.location="/tmp_pgm_page"</script>''')





@login_required(login_url='/')

def add_video2(request):
    ename = request.POST['textfield']
    video = request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(video.name, video)
    av = videos()
    av.subject = ename
    av.video = fn
    av.date_time = datetime.now()
    av.save()
    return HttpResponse('''<script> alert("Successfully added");window.location="/admin_view_videos"</script>''')

#member
@login_required(login_url='/')

def join_chitti_mbr(request):
    return HttpResponse('''<script> alert("Successfully added");window.location="/admin_view_videos"</script>''')


#add committee
@login_required(login_url='/')

def add_about_chitti1(request):
    chname = request.POST['textfield']
    no_mem = request.POST['textfield2']
    detail = request.POST['textfield3']
    amount = request.POST['textfield4']
    duration=request.POST['textfield5']
    total_amt = request.POST['textfield6']
    aac = chitti()
    aac.type = chname
    aac.no_members=no_mem
    aac.details = detail
    aac.committee=committee.objects.get(login_id__id=request.session['lid'])
    aac.winning_amounts = amount
    aac.duration=duration
    aac.chitti_amount=total_amt
    aac.date=datetime.today()
    aac.status='pending'
    aac.save()
    return HttpResponse('''<script> alert("Successfully added");window.location="/about_chitti"</script>''')
@login_required(login_url='/')

def add_committee_pgm(request):
    pgm=request.POST['textfield']
    venue=request.POST['textfield2']
    date=request.POST['textfield3']
    time=request.POST['textfield4']
    acp=committe_program()
    acp.program=pgm
    acp.venue=venue
    acp.date=date
    acp.time=time
    acp.committee_id=committee.objects.get(login_id__id=request.session['lid'])
    acp.save()
    return HttpResponse('''<script> alert("Successfully added");window.location="/committee_pgms"</script>''')


#edit button user
@login_required(login_url='/')

def edit_button_usr_profile(request):
    fname = request.POST['textfield']
    lname = request.POST['textfield2']
    ftname = request.POST['textfield10']
    hname=request.POST['textfield3']
    street=request.POST['textfield4']
    city=request.POST['textfield5']
    pin= request.POST['textfield6']
    ph=request.POST['textfield7']
    email=request.POST['textfield8']
    aadno=request.POST['textfield9']
    photo=request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(photo.name, photo)
    ebp=user()
    ebp.first_name = fname
    ebp.last_name=lname
    ebp.fathers_name=ftname
    ebp.house_name=hname
    ebp.street=street
    ebp.city=city
    ebp.pin=pin
    ebp.phone=ph
    ebp.email=email
    ebp.aadhar_number=aadno
    ebp.photo=fn
    ebp.save()
    return HttpResponse('''<script> alert("Successfully edited");window.location="/usr_profile"</script>''')



#edit admin
@login_required(login_url='/')

def editmngaud(request,id):
    request.session['aid']=id
    ob=auditorium.objects.get(id=id)
    return render(request, 'ADMIN-EDIT-MANAGE-AUDITORIUM.html',{'val':ob})
@login_required(login_url='/')

def editmngcm(request,id):
    request.session['cid'] = id
    ob = committee.objects.get(login_id__id=id)
    return render(request,'ADMIN_EDIT_MANAGE_COMMITTEE.html',{'val':ob})
@login_required(login_url='/')

def edittemplepgm(request,id):
    request.session['tpm']=id
    ob=program.objects.get(id=id)
    return render(request,'ADMIN-EDIT-TEMPLE-PGM.html',{'val':ob})
@login_required(login_url='/')

def editvideos(request,id):
    request.session['vid']=id
    ob=videos.objects.get(id=id)
    return render(request,'ADMIN-EDIT-VIDEOS.html',{'val':ob})
@login_required(login_url='/')

def editcommitteepgm(request,id):
    request.session['ecp']=id
    ob=committe_program.objects.get(id=id)
    return render(request,'COMMITTEE-EDIT-CM-PGM.html',{'val':ob})

#edit(committee)
@login_required(login_url='/')

def editaboutchitti(request,id):
    request.session['eac']=id
    ob=chitti.objects.get(id=id)
    return render(request,'COMMITTIEE- EDIT ADD CHITTI.html',{'val':ob})
@login_required(login_url='/')

def editcmpgm(request,id):
    request.session['ecp']=id
    ob=committe_program.get(id=id)
    return render(request, 'COMMITTEE-EDIT-CM-PGM.html', {'val': ob})


#update button admin
@login_required(login_url='/')

def update_committee_mng(request):
    cm_name=request.POST['textfield']
    president=request.POST['textfield22']
    secretary=request.POST['textfield2']
    no_of_members=request.POST['textfield3']
    phone=request.POST['textfield4']
    email1=request.POST['textfield5']
    mcb=committee.objects.get(login_id__id=request.session['cid'])
    mcb.committee_name=cm_name
    mcb.president=president
    mcb.secretary=secretary
    mcb.no_members=no_of_members
    mcb.phone=phone
    mcb.email=email1
    mcb.save()
    return HttpResponse('''<script> alert("Successfully updated");window.location="/mng_committee"</script>''')
@login_required(login_url='/')

def update_manage_auditorium(request):
    try:
        name=request.POST['textfield']
        place=request.POST['textfield2']
        phone=request.POST['textfield3']
        seats=request.POST['textfield4']
        charge=request.POST['textfield7']
        details=request.POST['textfield5']
        adv_payment=request.POST['textfield6']
        photo=request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name, photo)
        uma=auditorium.objects.get(id=request.session['aid'])

        uma.auditorium_name=name
        uma.place=place
        uma.phone=phone
        uma.seats=seats
        uma.charge=charge
        uma.details=details
        uma.advance_charge=adv_payment
        uma.photo=fn
        uma.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/manage_auditorium"</script>''')
    except:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        phone = request.POST['textfield3']
        seats = request.POST['textfield4']
        charge = request.POST['textfield7']
        details = request.POST['textfield5']
        adv_payment = request.POST['textfield6']
        uma = auditorium.objects.get(id=request.session['aid'])

        uma.auditorium_name = name
        uma.place = place
        uma.phone = phone
        uma.seats = seats
        uma.charge = charge
        uma.details = details
        uma.advance_charge = adv_payment
        uma.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/manage_auditorium"</script>''')

@login_required(login_url='/')

def update_temple_pgm(request):
    try:
        pgm=request.POST['textfield']
        guest=request.POST['textfield2']
        date=request.POST['textfield3']
        time=request.POST['textfield4']
        photo=request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name, photo)

        utp=program.objects.get(id=request.session['tpm'])
        utp.program=pgm
        utp.guest=guest
        utp.date=date
        utp.time=time
        utp.photo=fn
        utp.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/tmp_pgm_page"</script>''')
    except:
        pgm = request.POST['textfield']
        guest = request.POST['textfield2']
        date = request.POST['textfield3']
        time = request.POST['textfield4']

        utp = program.objects.get(id=request.session['tpm'])
        utp.program = pgm
        utp.guest = guest
        utp.date = date
        utp.time = time
        utp.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/tmp_pgm_page"</script>''')
@login_required(login_url='/')

def update_committee_pgm(request):
    try:
        pgm = request.POST['textfield']
        venue = request.POST['textfield2']
        date = request.POST['textfield3']
        time = request.POST['textfield4']
        ucp=committe_program.objects.get(id=request.session['ecp'])
        ucp.program=pgm
        ucp.venue=venue
        ucp.date=date
        ucp.time=time
        ucp.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/committee_pgms"</script>''')
    except:
        pgm = request.POST['textfield']
        venue = request.POST['textfield2']
        date = request.POST['textfield3']
        time = request.POST['textfield4']
        ucp=committe_program.objects.get(id=request.session['ecp'])
        ucp.program = pgm
        ucp.venue = venue
        ucp.date = date
        ucp.time = time
        ucp.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/committee_pgms"</script>''')

@login_required(login_url='/')

def update_videos(request):
    try:
        ename=request.POST['textfield']
        video=request.POST['file']
        fs = FileSystemStorage()
        fn = fs.save(video.name, video)
        uv=videos.objects.get(id=request.session['vid'])
        uv.subject=ename
        uv.date_time = datetime.now()
        uv.video=fn
        uv.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/admin_view_videos"</script>''')
    except:
        ename = request.POST['textfield']

        uv = videos.objects.get(id=request.session['vid'])
        uv.subject = ename
        uv.date_time = datetime.now()

        uv.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/admin_view_videos"</script>''')

#update committee
@login_required(login_url='/')

def update_about_chitti(request):
    chtype=request.POST['textfield']
    no_mem=request.POST['textfield2']
    detail=request.POST['textfield3']
    amount=request.POST['textfield4']
    duration=request.POST['textfield5']
    ttl_amt=request.POST['textfield6']
    uac=chitti.objects.get(id=request.session['eac'])
    uac.type=chtype
    uac.no_members=no_mem
    uac.details=detail
    uac.amounts=amount
    uac.duration=duration
    uac.total_amounts=ttl_amt
    uac.save()
    return HttpResponse('''<script> alert("Successfully updated");window.location="/about_chitti"</script>''')
@login_required(login_url='/')

def update_user_profile(request):
    try:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        ftname = request.POST['textfield10']
        hname = request.POST['textfield3']
        street = request.POST['textfield4']
        city = request.POST['textfield5']
        pin = request.POST['textfield6']
        ph = request.POST['textfield7']
        email = request.POST['textfield8']
        aadno = request.POST['textfield9']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name,photo)
        uup = user.objects.get(login_id__id=request.session['lid'])
        uup.first_name = fname
        uup.last_name = lname
        uup.fathers_name = ftname
        uup.house_name = hname
        uup.street = street
        uup.city = city
        uup.pin = pin
        uup.phone = ph
        uup.email = email
        uup.aadhar_number = aadno
        uup.photo = fn
        uup.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/usr_profile"</script>''')
    except:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        ftname = request.POST['textfield10']
        hname = request.POST['textfield3']
        street = request.POST['textfield4']
        city = request.POST['textfield5']
        pin = request.POST['textfield6']
        ph = request.POST['textfield7']
        email = request.POST['textfield8']
        aadno = request.POST['textfield9']
        uup = user.objects.get(login_id__id=request.session['lid'])
        uup.first_name = fname
        uup.last_name = lname
        uup.fathers_name = ftname
        uup.house_name = hname
        uup.street = street
        uup.city = city
        uup.pin = pin
        uup.phone = ph
        uup.email = email
        uup.aadhar_number = aadno

        uup.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/usr_profile"</script>''')


#member update profile
@login_required(login_url='/')

def update_member_profile(request):
    try:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        hname = request.POST['textfield3']
        street = request.POST['textfield4']
        city = request.POST['textfield5']
        pin = request.POST['textfield6']
        ph = request.POST['textfield7']
        email = request.POST['textfield8']
        aadno = request.POST['textfield9']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name,photo)
        uup = members.objects.get(login_id__id=request.session['lid'])
        uup.first_name = fname
        uup.last_name = lname
        uup.house_name = hname
        uup.street = street
        uup.city = city
        uup.pin = pin
        uup.phone = ph
        uup.email = email
        uup.aadhar_number = aadno
        uup.photo = fn
        uup.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/mbr_profile"</script>''')
    except:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        hname = request.POST['textfield3']
        street = request.POST['textfield4']
        city = request.POST['textfield5']
        pin = request.POST['textfield6']
        ph = request.POST['textfield7']
        email = request.POST['textfield8']
        aadno = request.POST['textfield9']


        uup = members.objects.get(login_id__id=request.session['lid'])
        uup.first_name = fname
        uup.last_name = lname
        uup.house_name = hname
        uup.street = street
        uup.city = city
        uup.pin = pin
        uup.phone = ph
        uup.email = email
        uup.aadhar_number = aadno

        uup.save()
        return HttpResponse('''<script> alert("Successfully updated");window.location="/mbr_profile"</script>''')



#delete (admin)
@login_required(login_url='/')

def delete_videos(request,id):
    ob=videos.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Successfully deleted");window.location="/admin_view_videos"</script>''')

@login_required(login_url='/')

def delete_temple_pgm(request,id):
    ob=program.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Successfully deleted");window.location="/tmp_pgm_page"</script>''')

@login_required(login_url='/')

def delete_manage_auditorium(request,id):
    ob=auditorium.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Successfully deleted");window.location="/manage_auditorium"</script>''')
@login_required(login_url='/')

def delete_manage_committee(request,id):
    ob=committee.objects.get(login_id__id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Successfully deleted");window.location="/mng_committee"</script>''')

#delete committee
@login_required(login_url='/')

def delete_about_chitti(request,id):
    ob=chitti.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Successfully deleted");window.location="/about_chitti"</script>''')
@login_required(login_url='/')

def delete_cm_pgm(request,id):
    ob=committe_program.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Successfully deleted");window.location="/committee_pgms"</script>''')

#approve or reject (admin)
@login_required(login_url='/')

def approve_user(request,id):
    ob = login.objects.get(id=id)
    ob.type = 'user'
    ob.save()
    return HttpResponse('''<script> alert("Successfully approved");window.location="/user_manage"</script>''')
@login_required(login_url='/')

def approve_user_booking(request,id):
    ob=auditorium_booking.objects.get(id=id)
    ob.status = 'approved'
    ob.save()
    return HttpResponse('''<script> alert("Successfully approved");window.location="/mng_aud_booking"</script>''')
@login_required(login_url='/')

def reject_user_booking(request,id):
    ob=auditorium_booking.objects.get(id=id)
    ob.status = 'rejected'
    ob.save()
    return HttpResponse('''<script> alert("Successfully rejected");window.location="/admin_home"</script>''')

@login_required(login_url='/')

def reject_user(request,id):
    ob = login.objects.get(id=id)
    ob.type = 'REJECTED'
    ob.save()
    return HttpResponse('''<script> alert("Successfully Rejected");window.location="/user_manage"</script>''')

#approve or reject (committee)
@login_required(login_url='/')

def approve_member(request,id):
    ob =login.objects.get(id=id)
    ob.type='member'
    ob.save()
    return HttpResponse('''<script> alert("Successfully approved");window.location="/verify_members"</script>''')
@login_required(login_url='/')

def reject_member(request,id):
    ob=login.objects.get(id=id)
    ob.type='Rejected'
    ob.save()
    return HttpResponse('''<script> alert("Successfully Rejected");window.location="/verify_members"</script>''')


#user button
@login_required(login_url='/')

def user_book_button(request):
    rp=request.POST.getlist('checks')
    date=request.POST['textfield6']
    # time=request.POST['textfield7']
    fn_type=request.POST['type']
    details=request.POST['textfield4']
    generators=request.POST['generator']
    ubb=auditorium_booking()
    ubb.details=rp
    ubb.date=date
    # ubb.time=time
    ubb.type=fn_type
    ubb.details=details
    ubb.status='pending'
    ubb.generator=generators
    ob=user.objects.get(login_id__id=request.session['lid'])
    ubb.user_id=ob
    ubb.save()
    return HttpResponse('''<script> alert("Auditorium booking is done");window.location="/user_home"</script>''')
@login_required(login_url='/')

def user_adv_pay(request):
    try:
        bank_name=request.POST['textfield2']
        ifsc_code=request.POST['textfield22']
        pin=request.POST['textfield23']
        acc_no=request.POST['textfield24']
        bd=request.POST['textfield25']
        ob=bank.objects.get(bank_name=bank_name,ifsc=ifsc_code,pin=pin,acc_no=acc_no)
        if ob is not None:
            ubb=auditorium_payment()
            ubb.current_date=datetime.today()
            ubb.status='advance-paid'
            uob=user.objects.get(login_id__id=request.session['lid'])
            ubb.user_id=uob
            ubb.booking_date=bd
            ubb.save()
            return HttpResponse('''<script> alert("Payement successfully");window.location="/user_home"</script>''')
        else:
            return HttpResponse('''<script> alert("Invalid user");window.location="/user_home"</script>''')
    except:
        return HttpResponse('''<script> alert("Invalid user");window.location="/user_home"</script>''')
#committee
@login_required(login_url='/')

def winners_slt_chitti_search(request):
    chitti_name= request.POST['chittitype']
    # month=request.POST['month']
    # print(month,"====================")
    btn=request.POST['Submit']
    if btn == 'SEARCH':
        # request.session['month'] = month
        # print(request.session['month'],"month================")
        request.session['cid'] = chitti_name
        print(request.session['cid'],"cc================")
        wt=chitti_details.objects.filter(chitti_id__id=chitti_name,status='pending')
        ob=chitti.objects.all()
        return render(request, 'COMMITTEE-SELECT WINNERS.html',{'val1':wt,'val':ob,'c':int(request.session['cid'])})
    else:
        current_year = datetime.today().year
        print(current_year)
        current_month=datetime.today().month
        print(current_month)
        obs=winner.objects.filter(chitti_id__id=request.session['cid'],date__month=current_month,date__year=current_year)
        print(obs,"**************")
        if len(obs)!=0:
            return HttpResponse(
                '''<script> alert("This month winner is already alotted!!!");window.location="/committee_home"</script>''')
        else:
            print("##################################################################")
            rp = request.POST.getlist('checks[]')
            for i in rp:
                ob = members.objects.get(login_id__id=i)
                obb = winner()
                obb.member_id = ob
                cob=chitti.objects.get(id=request.session['cid'])
                obb.chitti_id=cob
                obb.date = datetime.today()
                obb.save()
                rob=chitti_details.objects.get(member_id__login_id__id=ob.login_id.id,chitti_id__id=request.session['cid'])
                rob.status='allotted'
                rob.date=datetime.today()
                rob.save()
        return HttpResponse('''<script> alert("Submitted successfully");window.location="/committee_home"</script>''')
@login_required(login_url='/')

def view_winners_slt_chitti_search(request):
    chitti_name= request.POST['chittitype']
    print(chitti_name)
    wt=chitti_details.objects.filter(chitti_id=chitti_name,status='pending')
    # obb=chitti_details.objects.get(chitti_id__id=chitti_name)
    # ob1=winner.objects.values('date').distinct()
    ob1=winner.objects.filter(chitti_id__id=chitti_name,date__month=datetime.today().month).values('date').distinct()
    print(ob1)
    ob=chitti.objects.get(id=chitti_name)
    print(ob,"888888888888888888888888888888")
    obb=winner.objects.filter(chitti_id__id=chitti_name,date__month=datetime.today().month)
    ob2 = chitti.objects.all()
    return render(request, 'COMMITTEE-VIEW SELECTED WINNERS.html',{'val':ob,'v':ob1,'v1':obb,'v2':ob2,'count':int(chitti_name)})
#member
@login_required(login_url='/')

def mbr_view_winners_slt_chitti_search(request):
    chitti_name= request.POST['chittitype']
    print(chitti_name)
    wt=chitti_details.objects.filter(chitti_id=chitti_name,status='pending')
    # obb=chitti_details.objects.get(chitti_id__id=chitti_name)
    ob1=winner.objects.filter(chitti_id__id=chitti_name,date__month=datetime.today().month,date__year=datetime.today().year).values('date').distinct()
    ob=chitti.objects.get(id=chitti_name)
    obb=winner.objects.filter(chitti_id__id=chitti_name,date__month=datetime.today().month,date__year=datetime.today().year)
    # ob2 = chitti.objects.all()
    oo=members.objects.get(login_id__id=request.session['lid'])
    ob2 = chitti.objects.filter(committee_id=oo.committee_id)
    return render(request, 'MEMBER-VIEW WINNER.html',{'val':ob,'v':ob1,'v1':obb,'v2':ob2,'count':int(chitti_name)})
@login_required(login_url='/')

def mbr_join_chitti(request):
    oo=members.objects.get(login_id__id=request.session['lid'])
    ob=chitti.objects.filter(status='pending',committee_id=oo.committee_id)
    obb=chitti_details.objects.filter(member_id__login_id__id=request.session['lid']).values('chitti_id').distinct()
    print(obb,"======")
    ob1=chitti_details.objects.exclude(chitti_id__id__in=ob)
    print(ob1,"=====")
    return render(request, 'MEMBER-JOIN CHITTI.html',{'val': ob,'v':obb})
@login_required(login_url='/')

def join_chitti_mbr(request,id):
    # cid=request.GET['id']
    # request.session['cid'] = id
    # obb=chitti_details.objects.get(member_id__login_id__id=request.session['lid'],chitti_id=id)
    # if len(obb) == 0:
    ob=chitti_details()
    ob1=chitti.objects.get(id=id)
    ob.chitti_id=ob1
    ob.status='pending'
    ob.date=datetime.today()
    ob2=members.objects.get(login_id__id=request.session['lid'])
    ob.member_id=ob2
    ob.save()
    return HttpResponse('''<script> alert("Successfully joined");window.location="/mbr_join_chitti"</script>''')
@login_required(login_url='/')

def mbr_join_chitti_search(request):
    chitti_name= request.POST['chittitype']
    print(chitti_name)
    oo = members.objects.get(login_id__id=request.session['lid'])
    ob = chitti.objects.filter(committee_id=oo.committee_id)
    obb=chitti.objects.filter(id=chitti_name,status='pending')
    print(obb)
    try:
        ob1 = chitti_details.objects.get(chitti_id__id=chitti_name,member_id__login_id__id=request.session['lid'])
        print(ob1,"=================")
        if ob1 is None:
            return render(request, 'MEMBER-JOIN CHITTI.html', {'val': ob, 'v1': obb, 'count': int(chitti_name), 'c': int(0)})
        else:
            return render(request, 'MEMBER-JOIN CHITTI.html',{'val':ob,'v1':obb,'count':int(chitti_name),'c':int(1)})
    except:
        return render(request, 'MEMBER-JOIN CHITTI.html',
                      {'val': ob, 'v1': obb, 'count': int(chitti_name), 'c': int(0)})
@login_required(login_url='/')

def close_chitti(request,id):
    ob=chitti.objects.get(id=id)
    ob.status='closed'
    ob.save()
    return HttpResponse('''<script> alert("Closed");window.location="/about_chitti"</script>''')

# Create your views here.
