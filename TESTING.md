Debug=True
The app was constantly testing with debugger locally: debug=True throughout all the development process.  
Every time when there was an error (when app crashed), the debugger displayed an error message to the view,  
that allowed me to find the location of the error and fix it.


Validators
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