<h5 id=testing></h5>  

# **Testing**  

## **Contents:**  

- [**Testing**](#testing)
  * [**Automated Testing**](#automated)
  * [**Development Testing**](#development)
  * [**Manual Testing**](#manual)
    + [**Header and Footer**](#header)
    + [**Login/Registration Page**](#login)
    + [**Products**](#products)
    + [**Product Detail**](#detail)
    + [**basket**](#basket)
    + [**Checkout**](#checkout)
    + [**Checkout Success**](#success)
    + [**Profile**](#profile)
    + [**Where to find us**](#location)
  * [**Compatibility**](#compatibility)
  * [**Validators**](#validators)
  * [**Bugs and Finds**](#bugs)

---  

<div style="float:right;">
<a href="#testing">Back to Top</a>
</div>  

<h5 id=automated></h5>  

## **Automated Testing**  
Automated test, better known as [Unit testing](https://docs.python.org/3/library/unittest.html), is a softare testing method.  
Here individial units of code are put under tests to determine the quality of your code. Here the   
code that has been written for an application has small test scripts written for the units, to check if  
the code behaves as expected. 
The aim to get atleast 70% coverage of the website tested through unit tests.  
I have created a test folder under each app with significant code. The folder/file structure is as follows:  
- tests  
    + test_forms.py
    + test_models.py
    + test_views.py  

Each file has been split to test functions of teh views, models and the form code.    
To test each app you can key in the following and change the path as required:  

> `python3 manage.py test bag.test`  

This can further be specified with an extention of the specific test you wish to test alone:  

> `python3 manage.py test bag.test.test_views.<test_name>`  

The tests should pass to show:  

- . (a dot) in the terminal for each test passed  
- E in the terminal for each test that returns an error 
- F in the terminal for each test that returns as failed 

We can use an application called [coverage.py](https://coverage.readthedocs.io/en/coverage-5.3/) to run our tests 
and to see how much of our app we have tested.  

To run coverage add the following commands in your terminal:  
> `coverage run manage.py test`  

To get a report on the application you have just ran:  
> `coverage report`  

To create this report in HTML:  
> `coverage.HTML`
 
---  

<div style="float:right;">
<a href="#testing">Back to Top</a>
</div>  

<h5 id=development></h5>  

## **Development Testing**  
Django give the user many gimmicks, one that is particulally useful in development is setting   
'Debug' in the settings.py file to 'True':  

- settings.py
    + `DEBUG=True`  

This allows the app in progress to be tested with debugger locally. Where there is an error in   
the code, or if there is code missing, the locally rendered app would crash displaying a very   
specific error message, detailing where the error can be found and possibly how to fix it,  
i.e '{% endblock %} expected'.
 
---  

<div style="float:right;">
<a href="#testing">Back to Top</a>
</div>  

<h5 id=manual></h5>  

## **Manual Testing**   
Manual testing, is where each feature is tested on various screen sizes and browsers to check  
if the app responds as it should. I will use the 'user stories' to guide the testing; however,  
otherfactors will be considered.

<h5 id=header></h5>  

### **Header, and Footer**  
**_User Stories_**  
- As a customer i would like an easy-to-follow navigation   

**_Tests_**   
- does the footer redirect onto new tabs as expected  
- does the header collapse at a smaller screen width  
- does the search bar expand on hovered
- do all links in the navigation work  
- does the promo strip collase and rotate information on smaller screens  
- does the drop down navigation collapse
- does the search bar work 

**_Results_**  
- Some test were fully functional on all devices used for testing, with various screen sizes.  
- the search bar only filters searched when teh user hits enter on a large screen, the icon   
does not submit the query.

<h5 id=login></h5>  

### **Login/Registration Page**
**_User Stories_** 
- As a user i would like to register easily  
- As a user i would like to easily login and out  
- As a user i would like to easily recover PW’s (just in case)  
- As a user i would want to receive emails in relation to my activity, such as: confirmation emails

**_Tests_**   
- easily accesible from the profile icon, and from the drop down on smaller screens  
- login and register appear in drop down when no user is logged in  
- logout and profile appear in drop down when user is logged in  
- google login works and redirects accordingly
- confirmation email sent to user upon purchase  
- cofirmation email sent to user who registers  
- fields labled correcly  
- empty fields flag up an error  
- message to confirm user activity (login, logout) 
- home and sign in buttons redirect as expected

**_Results_**  
- Some test were fully functional on all devices used for testing, with various screen sizes.  
- however, if a user who has signed in through google and purchases an item, a confirmation  
email is not sent to them
- the confirmation email that sends shows the business name as 'example' 

<h5 id=products></h5>  

### **Products Page**  
**_User Stories_**  
- As a user i would like to be able to view all products 
- As a customer i would like to be able to filter my search preference 
- As a customer i would like to have more than one way to filter my search  

**_Tests_**   
- all products visable with key info  
- numbe rof products shown ina row reduce as screen size decreases  
- promotional carousel to render for large screens only  
- promotional carousel to be hidden when category selected  
- pagination works, disabled 'next' and 'previous' buttons when no pages to follow  
- quick add button works and adds to bag  
- image and info icon works and redirects correctly  
- message to confirm teh addition to your bag (from quick adds)

**_Results_**  
- some test were fully functional on all devices used for testing, with various screen sizes. 
- however, i found that when a category was selected, although the carousel is hidden   
theres an empty space that drops the page further down. 

<h5 id=detail></h5>  

### **Product Detail Page**
**_User Stories_**  
- As a user i would like to be able to view specific product details  

**_Tests_**   
- image redirects to new tab  
- description and directions visable  
- back to shop button and add to basket buttons work  
- social media links open a new tab and redirect correctly  
- input field and add to basket work 
- reviews visable to all users  
- reviews related to that product id show on that page
- user is only able to add a review if they are logged in  

**_Results_**  
- test were fully functional on all devices used for testing, with various screen sizes.  

<h5 id=basket></h5>  

### **basket Page**
**_User Stories_**  
- As a user i would like to view the number of items in my basket and the cost  
- As a customer i would like to be able to alter my basket

**_Tests_**   
- does the basket update with the number of items added and removed from the bag
- buttons to 'continue shopping' and to 'checkout' redirect correctly
- ability to increase, decrease and delete items 
- changing teh quantity changes the product total
- delivery costs and free delivery display in accordance with the basket total

**_Results_**  
- test were fully functional on all devices used for testing, with various screen sizes.  

<h5 id=checkout></h5>  

### **Checkout Page**
**_User Stories_**  
- As a customer i would like a quick and simple checkout process  
- As a customer i would like a pre-filled details at checkout

**_Tests_**   
- address pre-filled, if user has updated this in their profile  
- if fields are left blank, user is advised by pop-up 
- toggle saves address to profile  
- errors to show 'if' and 'where' the information has been keyed in wrong  
- loader works to show user the app is doing something
- delivery cost shows seperate to the basket total and total price
- buttons to go back and adjust bag or to complete order  
- order summary is visable  

**_Results_**  
- test were fully functional on all devices used for testing, with various screen sizes.  

<h5 id=success></h5>  

### **Checkout Success Page**
**_User Stories_**  
- As a customer i would like a successful payment page with a summary of my order  

**_Tests_**   
- all information releevant to that order is visable
- a button to redirect from that page  
- on larger screens the carousel is visable  
- carousel images redirect to the product detail page for the item clicked on  
- message to confirm this is a historic order

**_Results_**  
- test were fully functional on all devices used for testing, with various screen sizes.  


<h5 id=profile></h5>  

### **Profile Page**  
**_User Stories_**  
- As a user i would like a profile page where I can manage my details and view my purchases   

**_Tests_**   
- account easily accessible from navigation system  
- profile will only show once the user is logged in  
- order history visable, and redirects correctly  
- user able to update and save address to their profile
- user able to navigate to other pages in the app

**_Results_**  
- test were fully functional on all devices used for testing, with various screen sizes.   


<h5 id=location></h5>  

### **Where to find us Page**
Although no user stories, still a nice feature to have.  

**_Tests_**   
- user is able to drag around the map 
- user is able to zoom in and out of the map  
- user is able to access street maps
- hyperlinks working and redirecting on new tabs 
- information is clear 
- navigation accessible

**_Results_**  
- test were fully functional on all devices used for testing, with various screen sizes.  

---  

<div style="float:right;">
<a href="#testing">Back to Top</a>
</div>  

<h5 id=compatibility></h5>  

## **Compatibility**  

Not all users will use the same browsers, nor will they use the same device. Therefore it is   
important to check compatibility with all brosers (or atleast the most popular ones), and to also   
test against various screen sizes. Not all people shop from a desktop, as the internet continues   
to grow, the demand to shop on the go is increasing. Therefore it is important to create a good UX  
by simplifying applications to render neatly, and clearly on mobile devices too.

The following table illustrates the compatibility on various screen sizes and browsers:  

<table>
<tbody><tr>
<th>Device</th>
<th>Images</th>
<th>Links</th>
<th>Navbar</th>
<th>Formatting Error</th>
<th>Notes</th>
</tr>
<th>Desktop W/Screen</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>No Error</td>
<td>Works ok</td>
</tr>
<tr>
<th>Desktop</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>No Error</td>
<td>Works ok</td>
</tr>
<tr>
<th>Laptop</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>No Error</td>
<td>Works ok</td>
</tr>
<tr>
<th>IPad</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>No Error</td>
<td>Works ok</td>
</tr>
<tr>
<th>IPhone X</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>No Error</td>
<td>Works ok</td>
</tr>
<tr>
<th>IPhone 5</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>Some Errors</td>
<td>Works ok</td>
</tr>
<tr>
<th>Samsung</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>No Error</td>
<td>Works ok</td>
</tr>
<tr>
<th>Explorer</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>No Error</td>
<td>Slight zoomed out appearance</td>
</tr>
<tr>
<th>Safari</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>No Error</td>
<td>Works ok</td>
</tr>
<tr>
<th>Chrome</th>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>No Error</td>
<td>Zoomed in appearance</td>
</tr>
</tbody></table>

---  

<div style="float:right;">
<a href="#testing">Back to Top</a>
</div>  

<h5 id=validators></h5>  

## **Validators**
**HTML**
All HTML files were tested through [W3C Markup Validation](https://validator.w3.org/), by direct input.  
This lists errors and warnings in relation to your HTML code specifying lines and elements/attributes effected.  
My application used Jinja templating language, that is entwind with the HTML content, whih is which is why i  
had many 'bad value' errors. There were a few minor errors such as not specifying `<!DOCTYPE html>`,  
but these errors can safely be ignored as this is included in the base.  
No other significant errors were found.

**CSS**
All the CSS files were tested through [W3C CSS Validation](https://jigsaw.w3.org/css-validator/validator), by direct input.  
This lists errors and warnings in relation to your CSS code specifying lines and the errors found. I   
recieved a few errors in relation to webkit as an unknown vendor. I also got errors notifying me that some  
of my styling choices such as the border colours and backgrounds to be of the same colours. However, these   
errors can safely be ignored as this is included in the base.  
No other errors were found.

**JavaScript**
All the JS files were tested through [Esprima](https://esprima.org/demo/validate.html) by direct input.  
If there was a syntax error, a squiggly red line would appear under the code which would reveal the errors   
once hovered over. All code was syntactically valid.

**Python**
All the Python files were tested using 'flake8' which lists all errors in relation to Python on every  
page of your application. I had a few indentation erros, and 'line too long' errors. I corrected these   
where possible. I also used [PEP8 online](http://pep8online.com/) and further changes were made to make the code  
PEP8 compliant where possible.  

---  

<div style="float:right;">
<a href="#testing">Back to Top</a>
</div>  

## **Bugs and Finds**  
When testing the application i found when clicking on teh search icon, a bloack thick out of line border would   
appear. After searching online i found the solution, the suggestions were to add `outline:0 !important;`  
to the CSS property for the icon, and it worked.


