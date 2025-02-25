# Feature Description
Feature: Testing Feature which to test the HKO 9 days forecast page
  # Tag annotation on pytest
  # Scenario Title

@Q2
  Scenario: Open the HKO app and verify the first date on 9-day forecast page

    Given user go to the homepage
    When user click menu and select forecast submenu to choose nine day forecast
    Then verify the first date is correct in nine day forecast page
