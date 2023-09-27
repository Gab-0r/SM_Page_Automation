Feature: contactUs
  As user
  I want to visit source meridian website
  In order to contact with the company

  Background: go to source meridian website
    Given the url of the website
    And the website is displayed

  Scenario: correctly form submit
    Given the user enter correct information to form
    And mark the checkbox to aceppt terms and conditions
    And click the submit button
    Then the form is submit correctly

  Scenario: wrong name
    Given the user enter correct company, email, phone, help info
    And enter a wrong name
    And mark the checkbox to accept terms and conditions
    And click the submit button
    Then an error message for name is displayed

  Scenario: wrong email
    Given the user enter correct name, company, phone, help info
    And enter a wrong email
    And mark the checkbox to accept terms and conditions
    And click the submit button
    Then an error message for email is displayed

  Scenario: wrong phone
    Given the user enter correct name, company, email, help info
    And enter a wrong phone
    And mark the checkbox to accept terms and conditions
    And click the submit button
    Then an error message for phone is displayed

  Scenario: wrong company
    Given the user enter correct name, email, phone, help info
    And enter a wrong company
    And mark the checkbox to accept terms and conditions
    And click the submit button
    Then an error message for company is displayed

  Scenario: empty fields
    Given the user enter correct information to form
    And leaves an emtpy field
    Then an error message for empty field is displayed

  Scenario: checkbox not checked
    Given the user enter correct information to form
    Then an error message for terms and conditions is displayed