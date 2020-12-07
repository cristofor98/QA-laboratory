Feature: Validate google search functionality

  Scenario: Verify opening google page
    When Populate URL box with "https://www.google.co.in"
    Then Redirects to google main page

  Scenario: Verify number of search results on a single page
    Given The google page is loaded
    When Populate search box with "universitate"
    And search item
    Then Present list of 11 search result

  Scenario: Verify empty search
    Given The google page is loaded
    When search item
    Then Nothing happens

  Scenario: Verify irrelevant search
    Given The google page is loaded
    When Populate search box with "universitate.com"
    And search item
    Then The link "Ați dorit să scrieți:" appears
