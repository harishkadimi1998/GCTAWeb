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
        request.session['username'] = UserId
        return HttpResponse('success')

def HomePage(request):
        # username = request.session['username']
        return render(request,'HomePage.html')

def Logout(request):
    del request.session['username']
    
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


@csrf_exempt
def Sendmail(request):
    result = RegisterView.Sendmail_insert(request)
    return result

#def Register_view(request): 
    #return Register_display.Register_display()

# def FilldllData(query,slctedValue):
#      Data = kavinCommon.fillddl()
#      return HttpResponse(Data)