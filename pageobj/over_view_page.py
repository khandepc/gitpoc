from generic import selenuimbase_revision as sb
xpath_all_links_over="//a[@class='nav-link color-wh']"

def get_over_view_links_element():
    return sb.get_elements("xpath",xpath_all_links_over)