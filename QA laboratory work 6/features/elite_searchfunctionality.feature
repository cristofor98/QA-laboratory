Feature: Validate search functionality 
Scenario: Search for a product on website
    Given I am on the website homepage
    When I enter search term as "jacket"
    Then Search results should appear