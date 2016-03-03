Feature: Test CW Task
  Implement a tool for converting markdown to HTML
  Scenario: A given input
    Given I opened the app
    When I load the file from URL: https://gist.githubusercontent.com/minivan/f29e2759c44d13e39b5b/raw/7bc948fc89d467db05d879e61ac09a7f70f75362/input.md
    And I convert to HTML
    Then I see a result like the one at the URL: https://gist.githubusercontent.com/minivan/a2de5b21a649d7ad0f7f/raw/1398320f80223fe7e666cddd0774b5f71a7cf53e/output.html

#  Scenario: A wrong input
#    Given I opened the app
#    When I load the file from URL: ImNotAnURL
#    And I convert to HTML
#    Then I see an InvalidInput error