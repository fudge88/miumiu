<h5 id=testing></h5>  

# **Testing**  

## **Contents:**  

- [**Testing**](#testing)
  * [**Automated Testing**](#automated)
  * [**Development Testing**](#development)
  * [**Manual Testing**](#manual)
    + [**Home**](#home)
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


<h5 id=developemnt></h5>  

---  

<h5 id=automated></h5>  

## **Automated Testing**  
 
---  

<h5 id=development></h5>  

## **Development Testing**  
Django give the user many gimmicks, one that is particulally useful in development is setting   
'Debug' in the settings.py file to 'True':  

> settings.py
>> `DEBUG=True`  

This allows the app in progress to be tested with debugger locally. Where there is an error in   
the code, or if there is code missing, the locally rendered app would crash displaying a very   
specific error message, detailing where the error can be found and possibly how to fix it,  
i.e '{% endblock %} expected'.
 
---  

<h5 id=manual></h5>  

## **Manual Testing**   
Manual testing, is where each feature is tested on various screen sizes and browsers to check  
if the app responds as it should. I will use the 'user stories' to guide the testing; however,  
otherfactors will be considered.

<h5 id=home></h5>  

### **Home Page**  
**_User Stories_** 
- As a user i would like to view the number of items in my basket and the cost  
- As a customer i would like to be able to filter my search preference  
- As a customer i would like an easy-to-follow navigation   

<h5 id=login></h5>  

### **Login/Registration Page**
**_User Stories_** 
- As a user i would like to register easily  
- As a user i would like to easily login and out  
- As a user i would like to easily recover PW’s (just in case)  
- As a user i would want to receive emails in relation to my activity, such as: confirmation emails

<h5 id=products></h5>  

### **Products Page**  
**_User Stories_**  
- As a user i would like to be able to view all products 
- As a customer i would like to have more than one way to filter my search  

<h5 id=detail></h5>  

### **Product Detail Page**
**_User Stories_**  
- As a user i would like to be able to view specific product details  

<h5 id=basket></h5>  

### **basket Page**
**_User Stories_**  
- As a customer i would like to be able to alter my basket

<h5 id=checkout></h5>  

### **Checkout Page**
**_User Stories_**  
- As a customer i would like a quick and simple checkout process  
- As a customer i would like a pre-filled details at checkout

<h5 id=success></h5>  

### **Checkout Success Page**
**_User Stories_**  
- As a customer i would like a successful payment page with a summary of my order

<h5 id=profile></h5>  

### **Profile Page**  
**_User Stories_**  
- As a user i would like a profile page where I can manage my details and view my purchases    

<h5 id=location></h5>  

### **Where to find us Page**
**_User Stories_** 

---  

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

<h5 id=validators></h5>  

## **Validators**
HTML
All HTML files were tested through [W3C Markup Validation](https://validator.w3.org/), by direct input.  
This lists errors and warnings in relation to your HTML code specifying lines and elements/attributes effected.  
My application used Jinja templating language, that is entwind with the HTML content, whih is which is why i  
had many 'bad value' errors. There were a few minor errors such as not specifying `<!DOCTYPE html>`,  
but these errors can safely be ignored as this is included in the base.  
No other significant errors were found.

CSS
All the CSS files were tested through [W3C CSS Validation](https://jigsaw.w3.org/css-validator/validator), by direct input.  
This lists errors and warnings in relation to your CSS code specifying lines and the errors found. I   
recieved a few errors in relation to webkit as an unknown vendor. I also got errors notifying me that some  
of my styling choices such as the border colours and backgrounds to be of the same colours. However, these   
errors can safely be ignored as this is included in the base.  
No other errors were found.

JavaScript
All the JS files were tested through [Esprima](https://esprima.org/demo/validate.html) by direct input.  
If there was a syntax error, a squiggly red line would appear under the code which would reveal the errors   
once hovered over. All code was syntactically valid.

Python
All the Python files were tested using 'flake8' which lists all errors in relation to Python on every  
page of your application. I had a few indentation erros, and 'line too long' errors. I corrected these   
where possible. I also used [PEP8 online](http://pep8online.com/) and further changes were made to make the code  
PEP8 compliant where possible.
