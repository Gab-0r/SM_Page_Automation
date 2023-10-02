Feature: contactUs
  As user
  I want to visit source meridian website
  In order to contact with the company

  Background: go to source meridian website
    Given the user has accessed to sm website
    And the index page is displayed
    And click menu button
    And click contact us

  Scenario: correctly form submit
    Given the user has accessed to contact us page
    And the user enter correct information to form
    And mark the checkbox to aceppt terms and conditions
    And click submit button
    Then the form is submit correctly

  Scenario Outline: wrong value in <field> field
    Given the user enter correct information to form
    And enter string <value> in <field> field
    And mark the checkbox to aceppt terms and conditions
    And click submit button
    Then an error <msg_expected> is displayed

  Examples:
    | field | value | msg_expected |
    | name  |  None | empty name |
    | name  | juan??  | invalid name  |
    | email | juan.orozco | invalid email |
    | email | None        | empty email   |
    | email | juan.orozco@sourcemeridian  | invalid email |
    | phone | 301757a93 | invalid phone |
    | phone | 301757_3 | invalid phone |
    | phone | None      | empty phone   |
    | company  | None | empty company  |

#  Scenario: checkbox not clicked
#    Given the user has accessed to contact us page
#    And the user enter correct information to form
#    And click submit button
#    Then an error empty checkbox is displayed