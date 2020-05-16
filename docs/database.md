# Database Structure

* Two tables
  * survey_responses
  * demographics
* Each table will have an id column, which serves as primary key.
* The demographics table will have a foreign key, which will be used to join with survey_responses table.
* If survey question is not answered or if some years have additional survey questions that other years don't have, then the value will be saved as null in the database.
* Each row will have a year column to distinguish between survey results of different years.

## Table - survey_responses

* 72 columns

| Field Name      | Type | Question | Years Applicable To
| :------------- | :----------: | :----------: | :----------: |
|  `id` | String PK |
|  `year` | Integer |
|  `number_employees` | Integer | How many employees does your company or organization have? | 2014, 2016, 2017, 2018, 2019
| `is_tech_company` | Boolean | Is your employer primarily a tech company/organization? | 2014, 2016, 2017, 2018, 2019
| `employer_provides_mental_health_benefits` | String | Does your employer provide mental health benefits as part of healthcare coverage? | 2014, 2016, 2017, 2018, 2019
| `knows_options_available` | String | Do you know the options for mental health care available under your employer-provided health coverage? | 2014, 2016, 2017, 2018, 2019
| `employer_formally_discussed_mental_health` | String | Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)? | 2014, 2016, 2017, 2018, 2019
| `employer_offers_resources` | String | Does your employer offer resources to learn more about mental health disorders and options for seeking help? | 2014, 2016, 2017, 2018, 2019
| `is_anonymity_protected_by_employer` | String | Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer? | 2014, 2016, 2017, 2018, 2019
| `level_difficulty_asking_for_leave` | String | If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it be to ask for that leave? | 2014, 2016, 2017, 2018, 2019
| `comfortable_talking_physical_mental_coworkers` | String | Would you feel more comfortable talking to your coworkers about your physical health or your mental health? | 2017, 2018, 2019
| `comfortable_discussing_with_supervisor` | String | Would you feel comfortable discussing a mental health issue with your direct supervisor(s)? | 2014, 2016, 2017, 2018, 2019
| `has_discussed_with_employer` | Boolean | Have you ever discussed your mental health with your employer? | 2017, 2018, 2019
| `conversation_with_employer` | Boolean | Describe the conversation you had with your employer about your mental health, including their reactions and what actions were taken to address your mental | 2017, 2018, 2019
| `comfortable_discussing_with_coworkers` | String | Would you feel comfortable discussing a mental health issue with your coworkers? | 2014, 2016, 2017, 2018, 2019
| `has_discussed_with_coworkers` | Boolean | Have you ever discussed your mental health with coworkers?| 2017, 2018, 2019
| `conversation_with_coworkers` | String | Describe the conversation with coworkers you had about your mental health including their reactions. | 2017, 2018, 2019
| `had_coworker_discuss_mental_health` | Boolean | Have you ever had a coworker discuss their or another coworker's mental health with you? | 2017, 2018, 2019
| `conversation_coworker_had` | String | Describe the conversation your coworker had with you about their mental health (please do not use names). | 2017, 2018, 2019
| `employer_physical_health_importance` | Integer | Overall, how much importance does your employer place on physical health?| 2017, 2018, 2019
| `employer_mental_health_importance` | Integer | Overall, how much importance does your employer place on mental health? | 2017, 2018, 2019
| `has_previous_employers`| Boolean | Do you have previous employers? | 2016, 2017, 2018, 2019
| `is_previous_employer_tech_company` | Boolean | Was your employer primarily a tech company/organization? | 2017, 2018, 2019
| `previous_employer_provided_mental_health_benefits` | String | Have your previous employers provided mental health benefits? | 2016, 2017, 2018, 2019
| `aware_options_from_previous_employer` | String | Were you aware of the options for mental health care provided by your previous employers? | 2016, 2017, 2018, 2019
| `previous_employer_formally_discussed_mental_health` | String | Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)? | 2016, 2017, 2018, 2019
| `previous_employer_offered_resources` | String | Did your previous employers provide resources to learn more about mental health disorders and how to seek help? | 2016, 2017, 2018, 2019
| `is_anonymity_protected_by_previous_employer` | String | Was your anonymity protected if you chose to take advantage of mental health or substance abuse treatment resources with previous employers? | 2016, 2017, 2018, 2019
| `comfortable_talking_physical_mental_previous_employer` | String | Would you have felt more comfortable talking to your previous employer about your physical health or your mental health? | 2017, 2018, 2019
| `comfortable_discussing_with_previous_supervisor` | String | Would you have been willing to discuss your mental health with your direct supervisor(s)? | 2016, 2017, 2018, 2019
| `has_discussed_with_previous_employer` | Boolean | Did you ever discuss your mental health with your previous employer? | 2017, 2018, 2019
| `conversation_with_previous_employer` | String | Describe the conversation you had with your previous employer about your mental health, including their reactions and actions taken to address your mental | 2017, 2018, 2019
| `willing_discuss_with_previous_coworkers` | String | Would you have been willing to discuss your mental health with your coworkers at previous employers? | 2016, 2017, 2018, 2019
| `has_discussed_with_previous_coworkers` | Boolean | Did you ever discuss your mental health with a previous coworker(s)? | 2017, 2018, 2019
| `conversation_with_previous_coworkers` | String | Describe the conversation you had with your previous coworkers about your mental health including their reactions. | 2017, 2018, 2019
| `had_previous_coworker_discuss_mental_health` | Boolean | Did you ever have a previous coworker discuss their or another coworker's mental health with you? | 2017, 2018, 2019
| `conversation_previous_coworker_had` | String | Describe the conversation your coworker had with you about their mental health (please do not use names). | 2017, 2018, 2019
| `previous_employer_physical_health_importance` | Integer | Overall, how much importance did your previous employer place on physical health? | 2017, 2018, 2019
| `previous_employer_mental_health_importance` | Integer | Overall, how much importance did your previous employer place on mental health? | 2017, 2018, 2019
| `currently_has_mental_health_disorder` | String | Do you currently have a mental health disorder? | 2016, 2017, 2018, 2019
| `has_been_diagnosed` | String | Have you ever been diagnosed with a mental health disorder? | 2016, 2017, 2018, 2019
| `had_disorder_in_past` | String | Have you had a mental health disorder in the past? | 2016, 2017, 2018,2019
| `sought_treatment_for_mental_health` | Boolean | Have you ever sought treatment for a mental health disorder from a mental health professional? | 2014, 2016, 2017, 2018, 2019
| `has_family_history` | String | Do you have a family history of mental illness? | 2014, 2016, 2017, 2018, 2019
| `interferes_with_work` | String | If you have a mental health condition, do you feel that it interferes with your work? | 2014
| `interferes_with_work_treated` | String | If you have a mental health disorder, how often do you feel that it interferes with your work when being treated effectively? | 2016, 2017, 2018, 2019
| `interferes_with_work_not_treated` | String | If you have a mental health disorder, how often do you feel that it interferes with your work when NOT being treated effectively (i.e., when you are experiencing symptoms)? | 2016, 2017, 2018, 2019
| `observations_of_others` | String | Have your observations of how another individual who discussed a mental health issue made you less likely to reveal a mental health issue yourself in your current workplace? | 2016, 2017, 2018, 2019
| `willingness_to_share` | Integer | How willing would you be to share with friends and family that you have a mental illness? | 2016, 2017, 2018, 2019
| `physical_health_in_interview` | String | Would you be willing to bring up a physical health issue with a potential employer in an interview? | 2014, 2016, 2017, 2018, 2019
| `comments_physical_health_in_interview` | String | Why or why not? | 2014, 2016, 2017, 2018, 2019
| `mental_health_in_interview` | String | Would you bring up your mental health with a potential employer in an interview? | 2014, 2016, 2017, 2018, 2019
| `comments_mental_health_in_interview` | String | Why or why not? | 2014, 2016, 2017, 2018, 2019
| `is_openly_identified` | Integer | Are you openly identified at work as a person with a mental health issue? | 2018, 2019
| `how_think_coworkers_would_react` | Integer | If they knew you suffered from a mental health disorder, how do you think that your team members/co-workers would react? | 2017, 2018, 2019
| `experienced_unsupportive_response` | String | Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace? | 2016, 2017, 2018, 2019
| `comments_unsupportive_response` | String | Describe the circumstances of the badly handled or unsupportive response. | 2017, 2018, 2019
| `experienced_supportive_response` | String | Have you observed or experienced a supportive or well handled response to a mental health issue in your current or previous workplace? | 2017, 2018, 2019
| `comments_supportive_response` | String | Describe the circumstances of the supportive or well handled response. | 2017, 2018, 2019
| `tech_industry_level_support` | Integer | Overall, how well do you think the tech industry supports employees with mental health issues? | 2017, 2018, 2019
| `comments_improve_mental_health_support` | String | Briefly describe what you think the industry as a whole and/or employers could do to improve mental health support for employees. | 2017, 2018, 2019
| `additional_comments` | String | If there is anything else you would like to tell us that has not been covered by the survey questions, please use this space to do so. | 2014, 2017, 2018, 2019
| `discussing_mental_health_has_consequences` | String | Do you think that discussing a mental health issue with your employer would have negative consequences? | 2014, 2016
| `discussing_physical_health_has_consequences` | String | Do you think that discussing a physical health issue with your employer would have negative consequences? | 2014, 2016
| `employer_takes_mental_seriously_as_physical` | String | Do you feel that your employer takes mental health as seriously as physical health? | 2014, 2016
| `observed_consequences_for_coworkers`| String| Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace? | 2014, 2016
| `discussing_mental_has_consequences_previous_employer` | String | Do you think that discussing a mental health disorder with previous employers would have negative consequences? | 2016
| `discussing_physical_has_consequences_previous_employer` | String | Do you think that discussing a physical health issue with previous employers would have negative consequences? | 2016
| `previous_employer_took_mental_seriously_as_physical` | String | Did you feel that your previous employers took mental health as seriously as physical health? | 2016
| `observed_consequences_for_previous_coworkers` | String | Did you hear of or observe negative consequences for co-workers with mental health issues in your previous workplaces? | 2016
| `feels_mental_health_hurts_career` | String | Do you feel that being identified as a person with a mental health issue would hurt your career? | 2016
| `thinks_coworkers_view_negatively` | String | Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue? | 2016

## Table - demographics

* 9 columns.

| Field       | Type | Question | Years Applicable To
| :------------- | :----------: | :----------: | :----------: |
|  `id` | String PK |
| `age` | Integer | What is your age? | 2014, 2016, 2017, 2018, 2019
| `gender` | String | What is your gender? | 2014, 2016, 2017, 2018, 2019
| `country_living_in` | String | What country do you live in? | 2014, 2016, 2017, 2018, 2019
| `race` | String |  What is your race? | 2017, 2018, 2019
| `country_working_in` | String | What country do you work in? | 2016, 2017, 2018, 2019
| `works_remotely` | String | Do you work remotely (outside of an office) at least 50% of the time? | 2014, 2016
