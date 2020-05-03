@fixture.login
Feature: Manage Lead
  Creating new leads and configuring lead statuses.

  Scenario: Creating new lead and checking his status
    When user adds new Lead
    | first_name  | last_name | company_name  |
    | John        | Smith     | Zendesk       |
    Then lead status is 'New'

   Scenario: Configuring global lead status
     Given user is in Lead statuses settings
     When user changes 'New' status to 'Test'
     And user goes to Lead details for 'John Smith'
     Then lead status is 'Test'
