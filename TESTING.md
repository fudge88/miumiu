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
Debug=True
The app was constantly testing with debugger locally: debug=True throughout all the development process.  
Every time when there was an error (when app crashed), the debugger displayed an error message to the view,  
that allowed me to find the location of the error and fix it.  

 
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
All the HTML files were tested through W3C Markup Validation Service. Since it does not recognize Jinja2  
templating language, it showed a number of errors. There were also few minor errors and warning that can be  
safely ignored. Apart from that, no other errors were found across the html pages.  

CSS
All the CSS files were tested through W3C CSS Validation Service. Since it does not recognize CSS variables  
(colours and fonts variables were used), there were several Parse Errors found. These errors can be safely  
ignored as they are not errors in fact. The rest of the CSS files was completely valid.  

JavaScript
All the JS files were tested through Esprima and JSHint validators, code was syntactically valid. "$" was not  
defined by JSHint.  

Python
All the Python files were tested through PEP8 Online validator and further changes were made to make the code  
PEP8 compliant where possible.  