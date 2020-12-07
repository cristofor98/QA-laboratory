Feature: Validate the review functionality

  Scenario: Verify sending review form with invalid email
    Given I am on the product page
    When Click on REVIEW tab
    And Populate review form with username "cristofor" and email "cristofor" and message "asfasfasfsafa"
    And Click on SEND button
    Then A warning message "Enter an email address" appears
    
 Scenario Outline: Verify sending review form with empty fields
    Given I am on the product page
    When Click on REVIEW tab
    And Populate review form with "<username>" "<email>" "<message>"
    And Click on SEND button
    Then A warning message "Fill out this field" appears

    Examples:
      | username | email          | message |
      |          | cristofor.fistic@ati.utm.md  | aafasfasfasfa    |
      |  cristofor    |                | afasfsafasfa     |
      |  cristofor    | cristofor.fistic@ati.utm.md  |         |


  Scenario: Verify sending review form with valid email
    Given I am on the product page
    When Click on REVIEW tab
    And Populate review form with username "cristofor" and email "cristofor.fistic@atiumt.md" and message "asfasfsafsafa"
    And Click on SEND button
    Then The review is posted