Feature: joinUs
  As user
  I want to visit source meridian website
  In order to apply to apply for an open position

  Background: go to source meridian website
    Given the user has accessed to sm website
    And the index page is displayed
    And click menu button
    And click join us

  Scenario: apply for an open position correctly
    Given the user has accessed to join us page
    Given the user search the QA Automation open position
    And the user has accessed to QA Automation position page
    When the user enter correct information to form
    And the user attach the cv
    Then the CV was charged succesfully