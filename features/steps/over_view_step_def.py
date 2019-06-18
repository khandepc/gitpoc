from generic import selenuimbase_revision as sb
from pageobj import over_view_page
from behave import given,when,then


@given(u'check how many count of home page all links is {expected_links}')
def step_impl(context,expected_links):
    element=over_view_page.get_over_view_links_element()
    actual=len(element)
    assert actual==int(expected_links),actual+"is not matching with"+expected_links
    for i in element:
        res=sb.perform_action(i,"gettext")
        print(res)



