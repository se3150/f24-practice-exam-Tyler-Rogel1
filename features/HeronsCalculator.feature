Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

Scenario: I can calculate the area of a triangle
    Given I open the url "https://byjus.com/herons-calculator/"
    # write your steps here

    When I set "3" to the inputfield "#a"
    When I set "4" to the inputfield "#b"
    When I set "5" to the inputfield "#c"
    When I click on the element ".clcbtn"

    Then I expect that element "#_d" matches the text "6"

Scenario: I can calculate the semi-perimeter of a triangle
    Then I expect that element "#_e" matches the text "6"

Scenario: I get prompted to fill all inputs if I didn't already
    When I set " " to the inputfield "#a"
    When I click on the element ".clcbtn"

    Then I expect that a alertbox contains the text "Please Enter all the Values, a, b, c"
    When I accept the alertbox

Scenario: I get prompted "square root of a negative number" if I enter 0 for a value
    When I set "0" to the inputfield "#a"
    When I click on the element ".clcbtn"

    Then I expect that a alertbox contains the text "Square root of a negative number"
