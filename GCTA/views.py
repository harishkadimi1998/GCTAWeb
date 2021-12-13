from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import sys
import json
sys.path.insert(0, '/KcBalViews/')
sys.path.insert(0, '/KavinCommon/')
from .KcBalViews import ConsentView,RegisterView,Bal_PreAndPost
from .KavinCommon import kavinCommon
from datetime import datetime,timedelta
from datetime import date





# Create your views here.
def index(request):
    if request.session.has_key('username'):
        # username = request.session['username']
        return redirect('HomePage')
    else:
      return render(request,'index.html')

@csrf_exempt
def Login(request):
    if request.method == 'POST':
        UserId = request.POST['userid']
        Password = request.POST['pwd']
        
        sql=f"select * from master_tbl_user where fld_username= '{UserId}'  and fld_password='{Password}'"
     
        cursor = connection.cursor()
        connection.commit()
        cursor.execute(sql)
        result = cursor.fetchall()
        request.session['fld_rfid']=result[0][2]
        cnt=cursor.rowcount
       
        #request.session['username'] = UserId
        if cnt == 1:
            user_rfid=request.session['fld_rfid']=result[0][2]
            login_userid=1
            
            res=f"call sp_cmn_userlog('{user_rfid}','{login_userid}')"
            cursor = connection.cursor()
            connection.commit()
            result = cursor.execute(res)
            return HttpResponse("success")
        else:
            return HttpResponse("something wentwrong!!")

def HomePage(request):
        user_rfid=request.session['fld_rfid']
        # username = request.session['username']
        return render(request,'HomePage.html')

def Logout(request):
        session_id = request.session['fld_rfid']
        sql=f"select fld_user_login_datetime from cmn_userlog  WHERE fld_user_rfid ={session_id} and fld_is_active=1"
     
        cursor = connection.cursor()
        connection.commit()
        cursor.execute(sql)
        result = cursor.fetchall()
        fld_user_login_datetime=result[0][0]
        # dt = datetime.datetime
        cnt=cursor.rowcount
        curdate = datetime.now()
        diff = (curdate) - (fld_user_login_datetime)

        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        dateandtime =f'{hours}:{minutes}:{seconds}'


        sql=f"UPDATE cmn_userlog SET fld_is_active =0,fld_user_logout_time='{curdate}',fld_user_session_duration='{dateandtime}' WHERE fld_user_rfid ={session_id} and fld_is_active=1"
        cursor = connection.cursor()
        connection.commit()
        result = cursor.execute(sql)
        del request.session['fld_rfid']
        return redirect('/')

def RegisterPage(request):
    # empty list
    context = []
    Identifyas = kavinCommon.fillddl("SELECT fld_option_code,fld_option_name FROM bind_tbl_i_identify_as","")
    tuberculosis = kavinCommon.fillddl("SELECT fld_option_code,fld_option_name FROM bind_tbl_tuberculosis","")
    Person = kavinCommon.fillddl("SELECT fld_option_code,fld_option_name FROM bind_tbl_i_am_a_person","")
    context = {
    "Identifyasddl": Identifyas,
    "Personddl": Person,
    "tuberculosisddl": tuberculosis
    }
    return render(request,'RegisterPage.html',context)

@csrf_exempt
def Register(request):
    return RegisterView.RegisterView(request)

def Submission(request):
    return render(request,'Submission.html')

def Forgotpassword(request):
    return render(request,'forgotpassword.html')

def Consentpage(request):
    context = []
    YesorNoddl = kavinCommon.fillddl("SELECT fld_option_code,fld_option_name FROM bind_tbl_yesorno","")
    context = {
    "YesorNoddl": YesorNoddl
    }
    return render(request,'Consent.html',context)


@csrf_exempt
def Consent(request):
    return ConsentView.ConsentView(request)
    
def Pre_and_post(request):
    context = []
    YesorNoddl = kavinCommon.fillddl("SELECT fld_option_code,fld_option_name FROM bind_tbl_yesorno","")
    context = {
    "YesorNoddl": YesorNoddl
    }
    return render(request,'Pre_and_post.html',context)

@csrf_exempt
def Pre_and_post_insert(request): 
    return Bal_PreAndPost.Pre_and_post_insert_Bal(request)

def Register_display(request): 
    return RegisterView.Register_reg_display(request)

def reg_show(request,id):
    return RegisterView.Register_show(request,id)

#Change Password Form Display
def ChangePaswordPage(request):
    return render(request,'Change_password.html')

#Change Password
@csrf_exempt
def Changepwd(request):
    if request.method == 'POST':
        currentpwd = request.POST['txt_cntpwd']
        newpwd = request.POST['txt_new_pwd']
        session_id = request.session['fld_rfid']

        sql=f"select fld_password from master_tbl_user  WHERE fld_rf_id ={session_id} and fld_is_active=1"
        cursor = connection.cursor()
        connection.commit()
        cursor.execute(sql)
        result = cursor.fetchall()
        fld_password=result[0][0]
        
        if currentpwd==fld_password:
            sql=f"UPDATE master_tbl_user SET fld_password='{newpwd}' WHERE fld_rf_id ={session_id} and fld_is_active=1"
            cursor = connection.cursor()
            connection.commit()
            result = cursor.execute(sql)
            return HttpResponse("success")
        else:
            return render(request,'Change_password.html')
    
   



@csrf_exempt
def Sendmail(request):
    result = RegisterView.Sendmail_insert(request)
    return result

def ProfilePage(request): 
    return render(request,'ProfilePage.html')

def ChangePhoto(request): 
    return render(request,'ChangePhoto.html')
#def Register_view(request): 
    #return Register_display.Register_display()

# def FilldllData(query,slctedValue):
#      Data = kavinCommon.fillddl()
#      return HttpResponse(Data)