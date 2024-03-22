Feature: Saucedemo Login
    Background : common steps
        Given I launch  browser
        When  I open application
        And   Enter valid username and password
        And   Click on login 

    Scenario: Logo to Saucedemo 
        Then User must login to the product page

    Scenario: Product Selection  
        When  I click on product name
        Then  Product description should be displayed