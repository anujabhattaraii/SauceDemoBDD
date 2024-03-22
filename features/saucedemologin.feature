Feature: Saucedemo Login
    Scenario: Logo to Saucedemo with valid parameters
        Given I launch chrome browser
        When  I open sauce demo homepage
        And   Enter username "standard_user" and password "secret_sauce"
        And   Click on login button
        Then User must successfully login to the product page

        Scenario Outline: Login to Saucedemo with Multiple parameters
            Given I launch chrome browser
            When  I open sauce demo homepage
            And   Enter username "<username>" and password "<password>"
            And   Click on login button
            Then User must successfully login to the product page

            Examples:
             | username      | password     |
             | standard_user | secret_sauce |
             | admin         | admin123     |
             | adminxyz      | admin989     |
             | adminadmin    | zdsaassa     | 
        