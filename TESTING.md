<h5 id=testing></h5>  

# **Testing**  

## **Contents:**  

- [**Testing**](#testing)
  * [**Automated Testing**](#automated)
  * [**Development Testing**](#development)
  * [**Manual Testing**](#manual)
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

<h5 id=products></h5>  

**Products Page**  

<h5 id=detail></h5>  

**Product Detail Page**

<h5 id=basket></h5>  

**basket Page**

<h5 id=checkout></h5>  

**Checkout Page**

<h5 id=success></h5>  

**Checkout Success Page**

<h5 id=profile></h5>  

**Profile Page**

<h5 id=location></h5>  

**Where to find us Page**

---  

<h5 id=compatibility></h5>  

## **Compatibility** 

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