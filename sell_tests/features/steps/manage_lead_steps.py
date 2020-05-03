from behave import when, then
from behave.runner import Context

from sell_tests.page_objects.add_lead_form_page import AddLeadFormPage
from sell_tests.page_objects.lead_datails_page import LeadDetailsPage
from sell_tests.page_objects.leads_page import LeadsPage
from sell_tests.page_objects.navigation_bar_page import NavigationBarPage


@when("user adds new Lead")
def add_new_lead(context: Context):
    navigation_bar_page = NavigationBarPage()
    add_lead_form_page = AddLeadFormPage()
    for row in context.table:
        navigation_bar_page.click_lead_in_add_menu()
        add_lead_form_page.set_first_name(row["first_name"])
        add_lead_form_page.set_last_name(row["last_name"])
        add_lead_form_page.set_company_name(row["company_name"])
        add_lead_form_page.click_save_and_visit_button()


@then("lead status is '{expected_status}'")
def verify_lead_status(context: Context, expected_status: str):
    current_status = LeadDetailsPage().get_current_status()
    assert current_status == expected_status, f"Lead should have '{expected_status}' status, " \
                                              f"but has '{current_status}' status."


@when("user goes to Lead details for '{lead_name}'")
def go_to_lead_details(context: Context, lead_name: str):
    NavigationBarPage().click_leads_button()
    leads_page = LeadsPage()
    if not leads_page.is_lead_on_list(lead_name):
        __remove_all_fillers()
    leads_page.select_lead_by_name(lead_name)


def __remove_all_fillers():
    leads_page = LeadsPage()
    if not leads_page.is_clear_all_filters_button_displayed():
        leads_page.click_filters_button()
    leads_page.click_clear_all_filters_button()
