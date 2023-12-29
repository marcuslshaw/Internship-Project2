
Feature: Test Case Verify Community

  @firefox
  Scenario: Firefox Test Scenario
    Given Open main page_v2
    Then Log into the page_v2
    And Click on settings_v2
    And Click on community_v2
    And Verify pages_v2
    Then Verify contact_v2

  @chrome
  Scenario: Chrome Test Scenario
    Given Open main page_v2
    Then Log into the page_v2
    And Click on settings_v2
    And Click on community_v2
    And Verify pages_v2
    Then Verify contact_v2

      # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/second_testcase_v2.feature
