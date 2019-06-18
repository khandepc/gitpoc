from selenium import webdriver
from selenium.webdriver.support import select as sel
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# for launching app
def launch_app(browser_name, url):
    global driver
    if browser_name == "chrome":
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument("start-maximized")
        chromeoptions.add_argument("disable-notifications")
        chromeoptions.add_argument("--disable-infobars")
        chromeoptions.add_argument("--ignore-certificate-errors")
        chromeoptions.add_argument("--disable-extensions")
        driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe", options=chromeoptions)
    elif browser_name == "firefox":
        # firefoxoptions=webdriver.FirefoxOptions()
        # firefoxoptions.add_argument("start-maximized")
        # firefoxoptions.add_argument("disable-notifications")
        # firefoxoptions.add_argument("--disable-infobars")
        # firefoxoptions.add_argument("--ignore-certificate-errors")
        # firefoxoptions.add_argument("--disable-extensions")
        driver=webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
    elif browser_name == "ie":
        ieoptions=webdriver.IeOptions()
        ieoptions.add_argument("start-maximized")
        ieoptions.add_argument("disable-notifications")
        ieoptions.add_argument("--disable-infobars")
        ieoptions.add_argument("--ignore-certificate-errors")
        ieoptions.add_argument("--disable-extensions")
        driver=webdriver.Ie(executable_path="./drivers/IEDriverServer.exe",options=ieoptions)
    else:
        print("invalid browser name")

    driver.get(url)


# for closing browser
def close_app():
    driver.quit()


# to find element
def get_element(locater_type, locater):
    element = None
    if locater_type == "id":
        return driver.find_element_by_id(locater)
    elif locater_type == "name":
        return driver.find_element_by_name(locater)
    elif locater_type == "classname":
        return driver.find_element_by_class_name(locater)
    elif locater_type == "linktext":
        return driver.find_element_by_link_text(locater)
    elif locater_type == "partiallinktext":
        return driver.find_element_by_partial_link_text(locater)
    elif locater_type == "tagname":
        return driver.find_element_by_tag_name(locater)
    elif locater_type == "css":
        return driver.find_element_by_css_selector(locater)
    elif locater_type == "xpath":
        return driver.find_element_by_xpath(locater)
    else:
        print("invalid locater type")


# to find element's
def get_elements(locater_type, locater):
    element = None
    if locater_type == "id":
        return driver.find_elements_by_id(locater)
    elif locater_type == "name":
        return driver.find_elements_by_name(locater)
    elif locater_type == "classname":
        return driver.find_elements_by_class_name(locater)
    elif locater_type == "linktext":
        return driver.find_elements_by_link_text(locater)
    elif locater_type == "partiallinktext":
        return driver.find_elements_by_partial_link_text(locater)
    elif locater_type == "tagname":
        return driver.find_elements_by_tag_name(locater)
    elif locater_type == "css":
        return driver.find_elements_by_css_selector(locater)
    elif locater_type == "xpath":
        return driver.find_elements_by_xpath(locater)
    else:
        print("invalid locater type")


# to get page_details
def get_page_details(detail_type):
    if detail_type == "title":
        return driver.title
    elif detail_type == "url":
        return driver.current_url
    elif detail_type == "windowcount":
        return len(driver.window_handles)
    elif detail_type == "handle":
        return driver.current_window_handle
    elif detail_type == "handles":
        return driver.window_handles
    else:
        print("incorrect detail_type")


# to perform_action
def perform_action(element, action_type, value=None, extra=None):
    return_value = None
    if action_type == "select":
        element = sel.Select(element)
        element.select_by_visible_text(value)
    elif action_type == "click":
        element.click()
    elif action_type == "settext":
        element.send_keys(value)
    elif action_type == "gettext":
        return_value = element.text
    elif action_type == "getattribute":
        return_value = element.get_attribute(value)
    return return_value


# to switch_windows
def switch_to_another_window():
    parent_handle = driver.current_window_handle
    all_handles = driver.window_handles

    for handle in all_handles:
        if parent_handle != handle:
            driver.switch_to.window(handle)
            driver.maximize_window()
            break


# to perform_mouse_keyboard_action
def perform_mouse_keyboard_action(action_type, value=None, source_element=None, dest_element=None):
    ac = ActionChains(driver)
    if action_type == "click":
        ac.click(source_element)
    elif action_type == "rightclick":
        ac.context_click(source_element)
    elif action_type == "dragdrop":
        ac.drag_and_drop(source_element, dest_element)
    elif action_type == "movetoelement":
        ac.move_to_element(source_element)
    elif action_type == "clickandhold":
        ac.click_and_hold(source_element)
    elif action_type == "keydown":
        ac.key_down(value, source_element)
    elif action_type == "keyup":
        ac.key_up(value, source_element)
    elif action_type == "doubleclick":
        ac.double_click(source_element)
    ac.perform()


# to capture_screenshots
def capture_screenshot(file_name):
    driver.save_screenshot("./reports/screenshots/" + file_name + ".png")


# to switch_frames
def switch_to_frame(element, parent=None):
    if parent:
        driver.switch_to.parent_frame()
    else:
        driver.switch_to.frame(element)


# for wait operations
def explicit_wait_empliment(element, locator, condition_type=None):
    driver_wait = wait.WebDriverWait(driver, 30)
    if condition_type == 'visibility':
        element = expected_conditions.visibility_of_element_located((By.XPATH, locator))
    driver_wait.until(element)


def switch_to_another_object(obj_type, expected_value=None):
    if obj_type == "window":
        main_handle = get_page_details("handle")
        all_handles = get_page_details("handles")
        for handle in all_handles:
            driver.switch_to.window(handle)
            actual_title = get_page_details("title")
            if actual_title == expected_value:
                break
            else:
                continue
    elif obj_type == "frame":
        driver.switch_to.frame(expected_value)
    elif obj_type == "alert":
        alert = driver.switch_to.alert
        if expected_value == "accept":
            alert.accept()
        elif expected_value == "dismiss":
            alert.dismiss()


def forword_and_back_action(obj_type):
    if obj_type == "forword":
        driver.forward()
    elif obj_type == "back":
        driver.back()

