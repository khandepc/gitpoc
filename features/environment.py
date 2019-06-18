from generic import selenuimbase_revision as sb

import time

def before_step(context, step):
    pass

def after_step(context, step):
    pass

#These run before and after every step.
def before_scenario(context, scenario):
    sb.launch_app("chrome","http://inportia.com/")
    actual_title=sb.get_page_details('title')
    expected_title='Inportia - Provides Automation And IT Professional Training'
    assert actual_title==expected_title,actual_title+'is not matching with'+expected_title

def after_scenario(context, scenario):
    sb.capture_screenshot(scenario.name)
    sb.close_app()

#These run before and after each scenario is run.
def before_feature(context, feature):
    pass

def after_feature(context, feature):
    pass
#These run before and after each feature file is exercised.
def before_tag(context, tag):
    pass

def after_tag(context, tag):
    pass

#These run before and after a section tagged with the given name.
# They are invoked for each tag encountered in the order they’re found in the feature file.
# See controlling things with tags.
def before_all(context):
    pass

def after_all(context):
    pass