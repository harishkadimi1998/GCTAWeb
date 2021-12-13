from django.db import models

# Create your models here.

class Trn_tbl_registration(models.Model):
    fld_slno =models.AutoField(primary_key=True)
    fld_rn =models.IntegerField ()
    fld_rf_id =models.IntegerField()
    fld_full_name =models.CharField(max_length=100)
    fld_i_identify_as_id =models.IntegerField()
    fld_i_identify_as_name =models.CharField(max_length=100)
    fld_age =models.CharField(max_length=100)
    fld_country_of_residence =models.CharField(max_length=100)
    fld_email =models.CharField(max_length=100)
    fld_telephone_number =models.CharField(max_length=100)
    fld_tuberculosis_id =models.IntegerField()
    fld_tuberculosis_name =models.CharField(max_length=100)
    fld_am_person_id =models.IntegerField()
    fld_am_person_name =models.CharField(max_length=100)
    fld_organizational_affiliations =models.CharField(max_length=100)
    fld_working_with_TB_HIV =models.CharField(max_length=100)
    fld_part_of_this_training =models.CharField(max_length=100)
    fld_is_active =models.IntegerField (default=1)
    fld_sys_inserted_datetime =models.DateTimeField(auto_now_add=True)
    fld_modified_no =models.CharField(max_length=100)
    fld_modified_datetime =models.CharField(max_length=100)
    fld_is_deleted =models.CharField(max_length=100,default='')
    fld_reason_for_delete =models.CharField(max_length=100)
    fld_deleted_datetime =models.CharField(max_length=100,default='')
    fld_logged_in_user_id =models.CharField(max_length=100)
    fld_data_source =models.CharField(max_length=100)
    fld_form_start_time =models.CharField(max_length=100)
    fld_form_end_time =models.CharField(max_length=100)
    fld_is_eligeble_to_login =models.CharField(max_length=100,default='')


class Trn_tbl_consent_form(models.Model):
    fld_slno =models.AutoField(primary_key=True)
    fld_rn = models.IntegerField()
    fld_rf_id =models.IntegerField()
    fld_name = models.CharField(max_length=150, null= True)
    fld_my_name_id = models.CharField(max_length=150, null= True)
    fld_my_name_name = models.CharField(max_length=150, null= True)
    fld_views_experiences_id =models.IntegerField()
    fld_views_experiences_name = models.CharField(max_length=150, null= True)
    fld_visual_materials_featuring_me_posters_id =models.IntegerField()
    fld_visual_materials_featuring_me_posters_name = models.CharField(max_length=150, null= True)
    fld_Videos_featuring_me_id =models.IntegerField()
    fld_Videos_featuring_name = models.CharField(max_length=150, null= True)
    fld_date  =models.DateField()
    fld_address =  models.CharField(max_length=150, null= True)
    fld_Telephone = models.IntegerField()
    fld_email = models.CharField(max_length=150, null= True)
    fld_is_active = models.IntegerField()
    fld_sys_inserted_datetime = models.DateTimeField(auto_now_add=True)
    fld_modified_no =models.CharField(max_length=150, null= True)
    fld_modified_datetime =models.CharField(max_length=150, null= True)
    fld_is_deleted =models.CharField(max_length=150, null= True,default='')
    fld_reason_for_delete =models.CharField(max_length=150, null= True)
    fld_deleted_datetime =models.CharField(max_length=150, null= True,default='')
    fld_logged_in_user_id =models.CharField(max_length=150, null= True)
    fld_data_source =models.CharField(max_length=150, null= True)
    fld_form_start_time =models.CharField(max_length=150, null= True)
    fld_form_end_time =models.CharField(max_length=150, null= True)



class Trn_tbl_pre_and_post_questionnaire(models.Model):
    fld_slno =models.AutoField(primary_key=True)
    fld_rn = models.IntegerField()
    fld_rf_id =models.IntegerField()
    fld_issues_of_people_living_with_tb_id=models.IntegerField()
    fld_issues_of_people_living_with_tb_name=models.CharField(max_length=150, null= True)
    fld_tb_affects_only_the_lungs_id=models.IntegerField()
    fld_tb_affects_only_the_lungs_name=models.CharField(max_length=150, null= True)
    fld_opportunistic_infection_for_people_living_with_hiv_id=models.IntegerField()
    fld_opportunistic_infection_for_people_living_with_hiv_name=models.CharField(max_length=150, null= True)
    fld_tb_is_a_poor_mans_disease_id=models.IntegerField()
    fld_tb_is_a_poor_mans_disease_name=models.CharField(max_length=150, null= True)
    fld_education_on_tb_and_its_modes_of_transmission_id=models.IntegerField()
    fld_education_on_tb_and_its_modes_of_transmission_name=models.CharField(max_length=150, null= True)
    fld_reactive_advocacy_that_works_id=models.IntegerField()
    fld_reactive_advocacy_that_works_name=models.CharField(max_length=150, null= True)
    fld_advocacy_is_note_off_event_id=models.IntegerField()
    fld_advocacy_is_note_off_event_name=models.CharField(max_length=150, null= True)
    fld_stakeholders_refer_individuals_and_institutions_id=models.IntegerField()
    fld_stakeholders_refer_individuals_and_institutions_name=models.CharField(max_length=150, null= True)
    fld_Social_media_role_in_the_tb_response_id=models.IntegerField()
    fld_Social_media_role_in_the_tb_response_name=models.CharField(max_length=150, null= True)
    fld_ltbt_has_all_the_symptoms_of_tb_id=models.IntegerField()
    fld_ltbt_has_all_the_symptoms_of_tb_name=models.CharField(max_length=150, null= True)
    fld_email=models.CharField(max_length=150, null= True)
    fld_is_active = models.IntegerField()
    fld_sys_inserted_datetime = models.DateTimeField(auto_now_add=True)
    fld_modified_no =models.CharField(max_length=150, null= True)
    fld_modified_datetime =models.CharField(max_length=150, null= True)
    fld_is_deleted =models.CharField(max_length=150, null= True,default='')
    fld_reason_for_delete =models.CharField(max_length=150, null= True)
    fld_deleted_datetime =models.CharField(max_length=150, null= True,default='')
    fld_logged_in_user_id =models.CharField(max_length=150, null= True)
    fld_data_source =models.CharField(max_length=150, null= True)
    fld_form_start_time =models.CharField(max_length=150, null= True)
    fld_form_end_time =models.CharField(max_length=150, null= True)