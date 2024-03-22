Feature: Saucedemo Logo
    Scenario: Logo presence on Saucedemo home page
        Given launch chrome browser
        When open sauce demo homepage
        Then verify that the logo present on page
        And close browser