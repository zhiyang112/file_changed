CREATE OR REPLACE TABLE `data-{ENVIRONMENT}-warehouse.talent_acquisition.ct_job_app` CLUSTER BY company_id, job_id AS (
SELECT  ja.company_id 
        ,ja.job_id 
        ,j.title                                      AS job_title 
        ,j.role                                       AS job_role 
        ,j.status                                     AS job_status 
        ,ja.id                                        AS job_application_id 
        ,ja.first_name 
        ,ja.last_name 
        ,ja.place_formatted_address 
        ,ja.nationality 
        ,ja.source 
        ,ja.status 
        ,ja.last_status_changed_at 
        ,ja.is_questionnaires_required 
        ,ja.is_video_required 
        ,ja.total_questionnaires_completed 
        ,ja.total_questionnaires 
        ,ROUND(ja.assessment_completion_percentage,2) AS assessment_completion_percentage 
        ,ja.assessment_completed_at 
        ,ja.total_screenings_completed 
        ,ja.total_screenings 
        ,ROUND(ja.criteria_met_percentage,2)          AS criteria_met_percentage 
        ,ja.has_passed_screening 
        ,ja.role_fit_score                            AS role_fit_score 
        ,ja.culture_fit_score                         AS culture_fit_score 
        ,ja.submitted_at 
        ,ja.completed_at 
        ,ja.created_at 
        ,ja.updated_at
FROM `data-{ENVIRONMENT}-warehouse.talent_acquisition.job_application` ja
LEFT JOIN `data-{ENVIRONMENT}-warehouse.talent_acquisition.job` j
ON ja.job_id = j.id ) jaa