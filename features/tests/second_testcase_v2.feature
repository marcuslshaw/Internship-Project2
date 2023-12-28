
Feature: Test Case in Firefox

  @firefox
  Scenario: Firefox Test Scenario
    Given Open main page_v2
    Then Log into the page_v2
    And Click on settings_v2
    And Click on community_v2
    And Verify pages_v2
    Then Verify contact_v2

  Scenario: Chrome Test Scenario
    Given Open main page_v2
    Then Log into the page_v2
    And Click on settings_v2
    And Click on community_v2
    And Verify pages_v2
    Then Verify contact_v2

    @browserstack
    Scenario: browserstack Test Scenario
    Given Open main page_v2
    Then Log into the page_v2
    And Click on settings_v2
    And Click on community_v2
    And Verify pages_v2
    Then Verify contact_v2