from behave import given,when,then
from generic import selenuimbase_revision as sb
from pageobj import inportia1_page

@then(u'click on selenium')
def step_impl(context):
    element=inportia1_page.get_selenium_element()
    sb.perform_action(element,"click")

@then(u'back to home page')
def step_impl(context):
    sb.forword_and_back_action("back")

@then(u'click on react')
def step_impl(context):
    element=inportia1_page.get_react_element()
    sb.perform_action(element,"click")

@then(u'click on python')
def step_impl(context):
    element=inportia1_page.get_python_element()
    sb.perform_action(element,"click")

@then(u'click on java')
def step_impl(context):
    element=inportia1_page.get_java_element()
    sb.perform_action(element,"click")

@then(u'click on android')
def step_impl(context):
    element=inportia1_page.get_android_element()
    sb.perform_action(element,"click")

@then(u'back to hame page')
def step_impl(context):
    sb.forword_and_back_action("back")

@given(u'click on internship')
def step_impl(context):
    element=inportia1_page.get_internship_element()
    sb.perform_action(element,"click")

@then(u'check title is matching with {expected_title}')
def step_impl(context,expected_title):
    actual=sb.get_page_details("title")
    assert actual==expected_title,"is not matching"

@then(u'click on home')
def step_impl(context):
    element=inportia1_page.get_home_element()
    sb.perform_action(element,"click")

@then(u'click on batch schedule')
def step_impl(context):
    element=inportia1_page.get_batch_schedule_element()
    sb.perform_action(element,"click")

@then(u'check titile is matching with {expected_title}')
def step_impl(context,expected_title):
    actual=sb.get_page_details("title")
    assert actual==expected_title,"is not matching"

@then(u'click to home page')
def step_impl(context):
    element=inportia1_page.get_home_element()
    sb.perform_action(element,"click")

@then(u'click on cources')
def step_impl(context):
    element=inportia1_page.get_cources_element()
    sb.perform_action(element,"click")

@then(u'click on selenium tranning')
def step_impl(context):
    element=inportia1_page.get_selenium_tranning_element()
    sb.perform_action(element,"click")


@then(u'click on angular js')
def step_impl(context):
    element=inportia1_page.get_angular_cource_element()
    sb.perform_action(element,"click")


@then(u'check links are {expected_links}')
def step_impl(context,expected_links):
    element=inportia1_page.get_cources_element()
    sb.perform_action(element,"click")
    element=inportia1_page.get_link_cource_element()
    actual=len(element)
    assert int(actual)==int(expected_links)

@then(u'click on contact')
def step_impl(context):
    element=inportia1_page.get_contact_element()
    sb.perform_action(element,"click")




#steps of registration form
@then(u'click on register')
def step_impl(context):
    element=inportia1_page.get_register_element()
    sb.perform_action(element,"click")


@then(u'Enter first name as {value}')
def step_impl(context,value):
    element=inportia1_page.get_first_name_element()
    sb.perform_action(element,"settext",value)


@then(u'enter last name as {value}')
def step_impl(context,value):
    element=inportia1_page.get_last_name_element()
    sb.perform_action(element,"settext",value)


@then(u'select gender as {value}')
def step_impl(context,value):
    element=inportia1_page.get_gender_element()
    sb.perform_action(element,"select",value)


@then(u'enter date of birth as {value}')
def step_impl(context,value):
    element=inportia1_page.get_date_of_birth_element()
    sb.perform_action(element,"settext",value)


@then(u'enter email id as {value}')
def step_impl(context,value):
    element=inportia1_page.get_email_id_element()
    sb.perform_action(element,"settext",value)


@then(u'enter mobile number as {value}')
def step_impl(context,value):
    element=inportia1_page.get_mobile_number_element()
    sb.perform_action(element,"settext",value)


@then(u'enter area as {value}')
def step_impl(context,value):
    element=inportia1_page.get_area_element()
    sb.perform_action(element,"settext",value)


@then(u'enter zip code as {value}')
def step_impl(context,value):
    element=inportia1_page.get_zip_code_element()
    sb.perform_action(element,"settext",value)


@then(u'select qualification as {value}')
def step_impl(context,value):
    element=inportia1_page.get_qualification_element()
    sb.perform_action(element,"select",value)


@then(u'select what do you do as {value}')
def step_impl(context,value):
    element=inportia1_page.get_what_do_you_do_element()
    sb.perform_action(element,"select",value)


@then(u'enter collage name as {value}')
def step_impl(context,value):
    element=inportia1_page.get_collage_name_element()
    sb.perform_action(element,"settext",value)


@then(u'select cource as {value}')
def step_impl(context,value):
    element=inportia1_page.get_registration_cource_element()
    sb.perform_action(element,"select",value)


@then(u'select what did you come to know as {value}')
def step_impl(context,value):
    element=inportia1_page.get_what_did_you_come_to_know_element()
    sb.perform_action(element,"select",value)


@then(u'Enter comment as {value}')
def step_impl(context,value):
    element=inportia1_page.get_comment_element()
    sb.perform_action(element,"settext",value)


@then(u'click on submit button')
def step_impl(context):
    element=inportia1_page.get_submit_button_element()
    sb.perform_action(element,"click")
