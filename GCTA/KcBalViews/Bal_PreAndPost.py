from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@csrf_exempt
def Pre_and_post_insert_Bal(request):
    if request.method == 'POST':
        Tbissue = request.POST['txtTbissue']
        TbissueName = request.POST['txtTbissueName']
        TBeffectOnlylungs = request.POST['txtTBeffectOnlylungs']
        TBeffectOnlylungsName = request.POST['txtTBeffectOnlylungsName']
        TBopportunisticInfection= request.POST['txtTBopportunisticInfection']
        TBopportunisticInfectionName= request.POST['txtTBopportunisticInfectionName']
        TBisPoormansissue = request.POST['txtTBisPoormansissue']
        TBisPoormansissueName = request.POST['txtTBisPoormansissueName']
        modesofTransmission = request.POST['txtmodesofTransmission']
        modesofTransmissionName = request.POST['txtmodesofTransmissionName']
        ReactiveAdvocacy = request.POST['txtReactiveAdvocacy']
        ReactiveAdvocacyName = request.POST['txtReactiveAdvocacyName']
        OneoffEvent = request.POST['txtOneoffEvent']
        OneoffEventName = request.POST['txtOneoffEventName']
        Institutions = request.POST['txtInstitutions']
        InstitutionsName = request.POST['txtInstitutionsName']
        Tbresponse= request.POST['txtTbresponse']
        TbresponseName = request.POST['txtTbresponseName']
        Tbsymptoms = request.POST['txtTbsymptoms']
        TbsymptomsName = request.POST['txtTbsymptomsName']
        email=''
        fld_logged_in_user_id = request.session['username']
        fld_data_source ='W'
        fld_form_start_time =''
        fld_form_end_time =''
        sql = "call sp_pre_and_post_questionnaire("+"'"+Tbissue+"'"+","+"'"+TbissueName+"'"+","+"'"+TBeffectOnlylungs+"'"+","+"'"+TBeffectOnlylungsName+"'"+","+"'"+TBopportunisticInfection+"'"+","+"'"+TBopportunisticInfectionName+"'"+","+"'"+TBisPoormansissue+"'"+","+"'"+TBisPoormansissueName+"'"+","+"'"+modesofTransmission+"'"+","+"'"+modesofTransmissionName+"'"+","+"'"+ReactiveAdvocacy+"'"+","+"'"+ReactiveAdvocacyName+"'"+","+"'"+OneoffEvent+"'"+","+"'"+OneoffEventName+"'"+","+"'"+Institutions+"'"+","+"'"+InstitutionsName+"'"+","+"'"+Tbresponse+"'"+","+"'"+TbresponseName+"'"+","+"'"+Tbsymptoms+"'"+","+"'"+TbsymptomsName+"'"+","+"'"+email+"'"+","+"'"+fld_logged_in_user_id+"'"+","+"'"+fld_data_source+"'"+","+"'"+fld_form_start_time+"'"+","+"'"+fld_form_end_time+"'"+")"
        cursor = connection.cursor()
        connection.commit()
        result = cursor.execute(sql)
        if result == 1:
            return HttpResponse("success")
        else:
            return HttpResponse("something wentwrong!!")