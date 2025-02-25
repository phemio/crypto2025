# Feature Description
Feature: Testing Feature which to test the SZSE feature
  # Tag annotation on pytest
  # Scenario Title

@Q3
  Scenario Outline: Validate szse page
    Given user go to szse page
    When send the API request endpoint with pref <lang> language
    Then verify high bigger than low

    Examples:
     | lang |
     | EN   |