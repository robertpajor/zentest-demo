from behave import given, when
from behave.runner import Context

from sell_tests.page_objects.leads_settings_page import LeadsSettingsPage
from sell_tests.page_objects.navigation_bar_page import NavigationBarPage
from sell_tests.page_objects.settings_page import SettingsPage


@given("user is in Lead statuses settings")
def go_to_lead_statuses(context: Context):
    NavigationBarPage().click_settings_button()
    SettingsPage().click_leads()

    leads_settings_page = LeadsSettingsPage()
    leads_settings_page.click_lead_statuses()


@when("user changes '{old_status}' status to '{new_status}'")
def change_lead_status(context: Context, old_status: str, new_status: str):
    leads_settings_page = LeadsSettingsPage()
    leads_settings_page.click_edit_lead_status(old_status)
    leads_settings_page.change_status_name(old_status, new_status)
    leads_settings_page.click_save_status_button()
