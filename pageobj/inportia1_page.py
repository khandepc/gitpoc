from generic import selenuimbase_revision as sb

#home page elements
xpath_selenium="//div/a[contains(text(),'SELENIUM')]"
xpath_angular="//div/a[contains(text(),'ANGULAR JS')]"
xpath_react="//div/a[contains(text(),'REACT')]"
xpath_python="//div/a[contains(text(),'PYTHON')]"
xpath_java="//div/a[contains(text(),'JAVA')]"
xpath_android="//div/a[contains(text(),'ANDROID')]"
xpath_internship="//li/a[@class='nav-link color-wh'][contains(text(),'Internship')]"
xpath_home="//li[@class='breadcrumb-item']/a[contains(text(),'Home')]"
xpath_angular_error="//body/h1[contains(text(),'Not Found')]"
xpath_batch_schedule="//li/a[@class='nav-link color-wh'][contains(text(),'Batch Schedule')]"

#cource dropdown elements
xpath_cources="//a[@id='navbarDropdownPortfolio']"
xpath_selenium_traning="//a[@class='dropdown-item color-wh'][contains(text(),'Selenium Training')]"
xpath_cource_angular="//a[@class='dropdown-item color-wh'][contains(text(),'AngularJS')]"
xpath_cource_python="//a[@class='dropdown-item color-wh'][contains(text(),'Python')]"
xpath_cource_java="//a[@class='dropdown-item color-wh'][contains(text(),'Java')]"
xpath_cource_react="//a[@class='dropdown-item color-wh'][contains(text(),'React')]"
xpath_home_cource="//ol/li/a[contains(text(),'Home')]"

#sylabus elements
xpath_sylabus="//*[@id='pills-profile-tab']"
xpath_cource_links="//div/a[@class='dropdown-item color-wh']"

#contact elements
xpath_contact="//li[@class='nav-item']/a[contains(text(),'Contact')]"


#registration form elements
xpath_register="//li/a[contains(text(),'Register')]"
xpath_first_name="//div/input[@name='fname']"
name_last_name="lname"
name_gender="gender"
name_date_of_birth="dob"
name_email_id="email"
name_mobile_number="phone"
name_area="area"
name_city="city"
name_zip_code="zipcode"
name_qualification="qualification"
xpath_what_do_you_do="//select[@name='profession']"
name_collage_name="organisation"
name_cource="course"
name_what_did_you_come_to_know="know"
name_comment="comment"
xpath_submit_button="//div/button[@type='submit']"

#home page methods(functions)
def get_selenium_element():
    return sb.get_element("xpath",xpath_selenium)

def get_angular_element():
    return sb.get_element("xpath",xpath_angular)

def get_react_element():
    return sb.get_element("xpath",xpath_react)

def get_python_element():
    return sb.get_element("xpath",xpath_python)

def get_java_element():
    return sb.get_element("xpath",xpath_java)

def get_android_element():
    return sb.get_element("xpath",xpath_android)

def get_internship_element():
    return sb.get_element("xpath",xpath_internship)

def get_home_element():
    return sb.get_element("xpath",xpath_home)

def get_angular_error_element():
    return sb.get_element("xpath",xpath_angular_error)

def get_batch_schedule_element():
    return sb.get_element("xpath",xpath_batch_schedule)


def get_sylabus_element():
    return sb.get_element("xpath",xpath_sylabus)

def get_link_cource_element():
    return sb.get_elements("xpath",xpath_cource_links)


#cource dropdown methods(functions)
def get_cources_element():
    return sb.get_element("xpath",xpath_cources)

def get_selenium_tranning_element():
    return sb.get_element("xpath",xpath_selenium_traning)

def get_angular_cource_element():
    return sb.get_element("xpath",xpath_cource_angular)

def get_python_cource_element():
    return sb.get_element("xpath",xpath_cource_python)

def get_java_cource_element():
    return sb.get_element("xpath",xpath_cource_java)

def get_react_cource_element():
    return sb.get_element("xpath",xpath_cource_react)

def get_home_cource_element():
    return sb.get_element("xpath",xpath_home_cource)

#contact methods(functions)
def get_contact_element():
    return sb.get_element("xpath",xpath_contact)

#register form methods(functions)
def get_register_element():
    return sb.get_element("xpath",xpath_register)

def get_first_name_element():
    return sb.get_element("xpath",xpath_first_name)

def get_last_name_element():
    return sb.get_element("name",name_last_name)

def get_gender_element():
    return sb.get_element("name",name_gender)

def get_date_of_birth_element():
    return sb.get_element("name",name_date_of_birth)

def get_email_id_element():
    return sb.get_element("name",name_email_id)

def get_mobile_number_element():
    return sb.get_element("name",name_mobile_number)

def get_area_element():
    return sb.get_element("name",name_area)

def get_city_element():
    return sb.get_element("name",name_city)

def get_zip_code_element():
    return sb.get_element("name",name_zip_code)

def get_qualification_element():
    return sb.get_element("name",name_qualification)

def get_what_do_you_do_element():
    return sb.get_element("xpath",xpath_what_do_you_do)

def get_collage_name_element():
    return sb.get_element("name",name_collage_name)

def get_registration_cource_element():
    return sb.get_element("name",name_cource)

def get_what_did_you_come_to_know_element():
    return sb.get_element("name",name_what_did_you_come_to_know)

def get_comment_element():
    return sb.get_element("name",name_comment)

def get_submit_button_element():
    return sb.get_element("xpath",xpath_submit_button)

