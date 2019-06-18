@application
Feature: check inportia it solution application functionality
  @homepage
  Scenario: check functionality of inpoortia home page
    Then click on selenium
    Then back to home page
    Then click on react
    Then back to home page
    Then click on python
    Then back to home page
    Then click on java
    Then back to home page
    Then click on android
    Then back to hame page
  @internship
  Scenario: check functionality of internship functionality
    Given click on internship
    Then check title is matching with Industry Handshake Programme In Pune
    Then click on home
  @batch
  Scenario: check functionality of batch schedule
    Then click on batch schedule
    Then check titile is matching with Our Upcoming Batch
    Then click to home page
  @cource
  Scenario: check functionality of cources
    Then click on cources
    Then click on selenium tranning
    Then click on home
    Then click on cources
    Then click on angular js
    Then check title is matching with AngularJS Training in Ravet, Pimple Saudagar Pune
    Then click on home
    Then click on cources
    Then click on python
    Then check title is matching with Python Training Institute In Ravet Pune
    Then click on home
    Then click on cources
    Then click on java
    Then check title is matching with Java Training Institute In Ravet Pune - Call Us Today
    Then click on home
    Then click on cources
    Then click on react
    Then check title is matching with React Training In Pimple Saudagar, Ravet Pune
    Then check links are 5
  @contact
  Scenario: check functionality of contact
    Then click on contact
    Then check title is matching with Contact Inportia For Best IT Training In Pune
  @registration
  Scenario: check functionality of registration
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutfirstname
  Scenario: check functionality of registration without enter first name
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutlastname
  Scenario: check functionality of registration without enter last name
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button


  @withoutgender
  Scenario: check functionality of registration without selecting gender
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutdateofbirth
  Scenario: check functionality of registration without enter date of birth
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutemailid
  Scenario: check functionality of registration without enter email id
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutmobilenumber
  Scenario: check functionality of registration without enter mobile number
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutarea
  Scenario: check functionality of registration without enter area
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutzipcode
  Scenario: check functionality of registration without enter zip code
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button

  @withoutqualification
  Scenario: check functionality of registration without select qualification
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutstudent
  Scenario: check functionality of registration without select student
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutcollage
  Scenario: check functionality of registration without enter collage name
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutcource
  Scenario: check functionality of registration without select cource
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutknow
  Scenario: check functionality of registration without select what did you come to know
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @withoutcomment
  Scenario: check functionality of registration without enter comment
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then click on submit button
  @registration
  Scenario: check functionality of registration
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then click on submit button

  @invalidfirstname
  Scenario: check functionality of registration with entering invalid first name
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as 123456
    Then enter last name as khande
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button

  @invalidlastname
  Scenario: check functionality of registration with entering invalid last name
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as 358358
    Then select gender as Male
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button

  @genderasfemale
  Scenario: check functionality of registration with selecting gender as female
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Female
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @invaliddateofbirth
  Scenario: check functionality of registration with entering invalid date of birth
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Female
    Then enter date of birth as 1996/09/14
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @invalidemailid
  Scenario: check functionality of registration with entering invalid email id
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Female
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123rediffmail.com
    Then enter mobile number as 7387453376
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button
  @invalidmobilenumber
  Scenario: check functionality of registration with entering invalid mobile number
    Then click on register
    Then check title is matching with Registration for Programming in Python Workshop
    Then Enter first name as prashant
    Then enter last name as khande
    Then select gender as Female
    Then enter date of birth as 14/09/1996
    Then enter email id as khandeprashant123@rediffmail.com
    Then enter mobile number as 73874533
    Then enter area as ravet
    Then enter zip code as 431001
    Then select qualification as BCA
    Then select what do you do as Student
    Then enter collage name as collage of management Aurangabad
    Then select cource as Internship
    Then select what did you come to know as WhatsApp
    Then Enter comment as i would like to attend session from inportia it solutions
    Then click on submit button

