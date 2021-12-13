from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from GCTA.models import Trn_tbl_registration
from django.core.mail import send_mail
import json


@csrf_exempt
def RegisterView(request):
    
    if request.method == 'POST':
            
        fld_full_name = request.POST['txtfull_name']
        fld_i_identify_as_id = request.POST['txtidentyfy']
        fld_i_identify_as_name =request.POST['txtidentyfyName']
        fld_age = request.POST['txtage']
        fld_country_of_residence = request.POST['txtcountry']
        fld_email = request.POST['txtemail']
        fld_telephone_number = request.POST['txtcnt_num']
        fld_tuberculosis_id = request.POST['txttuberculosi']
        fld_tuberculosis_name = request.POST['txttuberculosiName']
        fld_am_person_id= request.POST['txtperson']
        fld_am_person_name = request.POST['txtpersonName']
        fld_organizational_affiliations = request.POST['txtOrganisational']
        fld_working_with_TB_HIV = request.POST['txtnarrative']
        fld_part_of_this_training = request.POST['txttraining']
        fld_logged_in_user_id =''
        fld_data_source ='W'
        fld_form_start_time =''
        fld_form_end_time =''
        sql = "call sp_registration("+"'"+fld_full_name+"'"+","+"'"+fld_i_identify_as_id+"'"+","+"'"+fld_i_identify_as_name+"'"+","+"'"+fld_age+"'"+","+"'"+fld_country_of_residence+"'"+","+"'"+fld_email+"'"+","+"'"+fld_telephone_number+"'"+","+"'"+fld_tuberculosis_id+"'"+","+"'"+fld_tuberculosis_name+"'"+","+"'"+fld_am_person_id+"'"+","+"'"+fld_am_person_name+"'"+","+"'"+fld_organizational_affiliations+"'"+","+"'"+fld_working_with_TB_HIV+"'"+","+"'"+fld_part_of_this_training+"'"+","+"'"+fld_logged_in_user_id+"'"+","+"'"+fld_data_source+"'"+","+"'"+fld_form_start_time+"'"+","+"'"+fld_form_end_time+"'"+")"
        cursor = connection.cursor()
        connection.commit()
        result = cursor.execute(sql)
        if result == 1:
            return HttpResponse("success")
        else:
            return HttpResponse("something wentwrong!!")

def Register_reg_display(request):
    data = Trn_tbl_registration.objects.all().filter(fld_is_eligeble_to_login=0)
    rec = {
    "reg_users": data
            }
        # username = request.session['username']
    return render(request,'Register_view.html',rec)  

def Sendmail_insert(request):
    if request.method == 'POST':
        TotalData = json.loads(request.body.decode('utf-8'))
        Rfid = TotalData.get('txtRfid')
        txtAction = TotalData.get('txtAction')
        if txtAction =='Accept':
            Trn_tbl_registration.objects.filter(fld_rf_id=Rfid).update(fld_is_eligeble_to_login=1)
            send_mail(
                        'congratulations',
                        'hello everyone this is me nandish reddy.',
                        'vinayaka@kavinsoft.com',
                        ['vinayakdhundashi@gmail.com'],
                        fail_silently=False,
                    )
            return HttpResponse('success')
        else:
            Trn_tbl_registration.objects.filter(fld_rf_id=Rfid).update(fld_is_eligeble_to_login=2)
            return HttpResponse('failed')

def Register_show(request,id):
    id= int(id)
    sql=f"select * from gcta_trn_tbl_registration  WHERE fld_rf_id ={id}"
    cursor = connection.cursor()
    connection.commit()
    cursor.execute(sql)
    result= cursor.fetchall()
    rec = {
    "result": result
            }
    return render(request,'Regsiter_users_edit.html',rec)  