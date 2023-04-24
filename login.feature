Feature: Login Functionality
    As a customer, I want to Successfully login into my account

    Scenario: Successful login with valid credentials and logout
        Given I navigate to the login page
        When I submit valid credentials
        Then I should be logged in successfully
        And I should be able to logout

        When I click "Log Out"
        Then I should be redirected to the Home page
        And I should not be logged in
        Then I should close the session

    Scenario: Unsuccessful login with invalid credentials
        Given I navigate to the login page
        When I submit invalid credentials
        Then I should see the error message
        And I should not be logged in
        And I should stay on the login page
        Then I should close the session

    Scenario: Unsuccessful login with empty/missing credentials
        Given I navigate to the login page
        When I submit empty/missing credentials
        Then I should see the error message
        And I should not be logged in
        And I should stay on the login page
        Then I should close the session




