from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@csrf_exempt
def ConsentView(request):
    if request.method == 'POST':
        name = request.POST['name']
        mynameid=request.POST['myname']
        myname=request.POST['mynameName']
        experienceid=request.POST['experience']
        experience=request.POST['experienceName']
        photographsid=request.POST['photographs']
        photographs=request.POST['photographsName']
        videosid=request.POST['videos']
        videos= request.POST['videosName']
        date=request.POST['date']
        address=request.POST['address']
        cnt_num=request.POST['cnt_num']
        email=request.POST['email']
        fld_logged_in_user_id = request.session['username']
        fld_data_source ='W'
        fld_form_start_time =''
        fld_form_end_time =''
        sql = "call sp_consent_form("+"'"+name+"'"+","+"'"+mynameid+"'"+","+"'"+myname+"'"+","+"'"+experienceid+"'"+","+"'"+experience+"'"+","+"'"+photographsid+"'"+","+"'"+photographs+"'"+","+"'"+videosid+"'"+","+"'"+videos+"'"+","+"'"+date+"'"+","+"'"+address+"'"+","+"'"+cnt_num+"'"+","+"'"+email+"'"+","+"'"+fld_logged_in_user_id+"'"+","+"'"+fld_data_source+"'"+","+"'"+fld_form_start_time+"'"+","+"'"+fld_form_end_time+"'"+")"
        cursor = connection.cursor()
        connection.commit()
        result = cursor.execute(sql)
        if result == 1:
            return HttpResponse("success")
        else:
            return HttpResponse("something wentwrong!!")