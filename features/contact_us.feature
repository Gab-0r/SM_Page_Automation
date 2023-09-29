Feature: contactUs
  As user
  I want to visit source meridian website
  In order to contact with the company

  Background: go to source meridian website
    Given the user has accessed to sm website
    And the index page is displayed
    And click menu button
    And click contact us

#  Scenario: correctly form submit
#    Given the user has accessed to contact us page
#    And the user enter correct information to form
#    And mark the checkbox to aceppt terms and conditions
#    And click submit button
#    Then the form is submit correctly

  Scenario Outline: wrong value in <field> field
    Given the user enter correct information to form
    And enter string <value> in <field> field
    And mark the checkbox to accept terms and conditions
    And click the submit button
    Then an error message for <field> is displayed

  Examples:
    | field | value |
    | name  | juan_ |


#  Scenario: wrong email
#    Given the user enter correct name, company, phone, help info
#    And enter a wrong email
#    And mark the checkbox to accept terms and conditions
#    And click the submit button
#    Then an error message for email is displayed
#
#  Scenario: wrong phone
#    Given the user enter correct name, company, email, help info
#    And enter a wrong phone
#    And mark the checkbox to accept terms and conditions
#    And click the submit button
#    Then an error message for phone is displayed
#
#  Scenario: wrong company
#    Given the user enter correct name, email, phone, help info
#    And enter a wrong company
#    And mark the checkbox to accept terms and conditions
#    And click the submit button
#    Then an error message for company is displayed
#
#  Scenario: empty fields
#    Given the user enter correct information to form
#    And leaves an emtpy field
#    Then an error message for empty field is displayed
#
#  Scenario: checkbox not checked
#    Given the user enter correct information to form
#    Then an error message for terms and conditions is displayed