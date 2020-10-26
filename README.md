<h5 id=miumiu-aesthetics></h5>   

# **MuiMui Aesthetics**  

People want to look and feel better longer; we have lots of literature, and many studies to  
support that ‘if you look good, you feel good’. As social media has boomed, the ‘influencer’  
markets have increased in followers, and the demand of people wanting to treat themselves with  
a bit more love and care has increased.  

MuiMui Aesthetics is simple one stop shop, for all the beauty products one can need or desire  
for their skin goals. The business breaks down the 3 elements to achieve the ultimate youthful  
glowing skin: exfoliate, mask, and moisturise. MuiMui does sell additional products, such as wax,  
for all your hair removal needs, but retains the focus on your face, body, and soul!

---  
<h5 id=contents></h5>  

## **Contents:**  

- [**MiuMiu Aesthetics**](#miumiu-aesthetics)
  * [**Contents**](#contents)
  * [**UX**](#ux)
  * [**User stories**](#user-stories)
  * [**Strategy & Scope**](#strategy)
  * [**Design**](#design)
    + [**Colors**](#colors)
    + [**Fonts**](#fonts)
  * [**Mock-ups**](#mock-ups)
  * [**Features**](#features)
    + [**NavBar**](#navbar)
    + [**Toast**](#toast)
    + [**Product Page**](#product-page)
    + [**Product Detail**](#product-detail)
    + [**Shopping basket**](#shopping-basket)
    + [**Checkout page**](#checkout-page)
    + [**Checkout Success**](#checkout-success)
  * [**Features left to implement**](#features-left-to-implement)
  * [**Technologies used**](#technologies-used)
  * [**Testing**](#testing)
  * [**Deployment**](#deployment)
    + [**Local Deployment**](#local-deployment)
    + [**Deploy to Heroku**](#deploy-to-heroku)
  * [**Credits**](#credits)


---
## **_NOTE: When testing this app, at checkout please use the following credentials:_**
> **Card Number:** 4242 4242 4242 4242  
> **Expiry Date:** Any future date  
> **Security Pin:** Any 3 numbers  
> **Zip:** Any 5 numbers

---

<h5 id=ux></h5>   

## **UX:**
A light and fruitful design, with a simple, sleek look; and an easy-to-navigate tools including  
various ways to search. The use of icons throughout the website reduces the amount of content  
needed to be displayed, thus creating a ‘east-to-navigate’, cleaner and a less cluttered feel to  
the site. The user has full control of the site, with the ability to add, delete items to their  
shopping basket. Once the user is authenticated, they are able to make payment and, add reviews  
to products; these reviews are available in the product details for all users to see. The user has  
a profile that displays their order history, and update their details, should they wish to re-order  
their previous purchases.  

On the other hand, the website also allows a ‘superuser’, who in effect is the business admin,  
to add, edit and delete products for future updates. Thus, allowing the business owner to manage  
their online presence and product line, independently.  

<h5 id=user-stories></h5>   

## **User stories:**  

#### Navigation
> **All Users:**  
>> - As a user i would like to be able to view all products 
>> - As a user i would liek to be able to view specified product details  
>> - As a user i would like to view the number of items in my basket and the incurred cost  

#### Registration and Accounts
> **User:**  
>> - As a user i would like to register easily  
>> - As a user i would like to easily login and out  
>> - As a user i would like to easily recover PW’s (just in case)  
>> - As a user i would want to receive emails in relation to my activity, such as: confirmation emails
>> - As a user i would like a profile page where I can manage my details and view my purchases    

#### Sorting and Searching
> **Customer:**  
>> - As a customer i would like to be able to filter my search preference  
>> - As a customer i would like to have more than one way to specify my search  
>> - As a customer i would like an easy-to-follow navigation   

#### Purchasing and Checkout
> **Customer:**  
>> - As a customer i would like to be able to alter my basket
>> - As a customer i would like a quick and simple to follow checkout
>> - As a customer i would like a successful payment page with a summary of my order
>> - As a customer i would like a pre-filled form for my details at checkout

---  

<h5 id=strategy></h5>   

## **Strategy/Scope:**  

**MuiMui Aesthetics** provides its users with a catalogue of products to choose from. With the  
transformation of the way business is conducted, there is now a huge focus on social media  
and its followers. As more and more influencers share their skin and beauty routines the public  
have a better and a more personal insight on how to care for themselves.  

**Users** generally like being offered categories, and multiple search options, as thisgives users more  
control and make the site more search specific to them. The more efficient a website is, the more  
likely customers will complete the cycle of purchase.  

**Admin** would be able to control the content on the websites, from users, products, and reviews.  
There is a facility to edit and delete existing products. Orders are available for the admin to  
see along with all the additional details the user would have provided, ready for shipment. The admin  
is also able to add and remove from orders.

---  

<h5 id=design></h5>   

## **Design**
The design of MuiMui is simple and allows focus on the products. The design gives the user  
the right amount of information with the emphasis on the key areas.  

<h5 id=colors></h5>   

### **Colors:**   
   
The colour scheme has been kept consistent throughout the website, where all significant buttons  
are yellow, and others are outlined in black.  

![colour scheme](/wireframes/colors.png)
  
The colours in the business logo are used in the promotion strip to inject some colour and keep  
consistency. These colours were used to accent the website, opposed to over-using colour blocks.  

Transparent gradients of the block shades were used as a background to highlight key areas or  
key information. 

I have used the [mycolor](https://mycolor.space/gradient) to create the gradient colours.     

<h5 id=fonts></h5>   

### **Fonts:**  
  
[Google Fonts- Kristi](https://fonts.google.com/specimen/Kristi?query=krist&preview.text=MuiMui%20Aesthetics&preview.text_type=custom) was used for significant headings.  
![Kristi](/wireframes/kristi.png)   

[Google Fonts- Playfair Display](https://fonts.google.com/specimen/Playfair+Display?query=play&preview.text=MuiMui%20Aesthetics&preview.text_type=custom&preview.size=34) was used for general headings.   
![Playfair Display](/wireframes/playfair.png)  

[Google Fonts- Raleway](https://fonts.google.com/specimen/Raleway?query=raleway&preview.text=MuiMui%20Aesthetics&preview.text_type=custom&preview.size=34) was used for the body of the website.   
![Raleway](/wireframes/raleway.png)   

<h5 id=icons></h5>   

**Icons:**
I have used [fontawesome](https://fontawesome.com/) as an icon library, I used their documentation to layer the basket  
total over the circle icon, I have also used font awesome’s inline icon sizing.  

<h5 id=logo></h5>   

**Logo:**
I used [canva](https://www.canva.com/design/DAEI-qYTGTI/2wbWJ9r5C8LP8SRndrMFSg/edit?category=tACZCvjI6mE) to create my 
business logo, sticking to the color theme.  
![logo](/media/logo.PNG)  

<h5 id=favicon></h5>   

**Favicon:**
I used [favicon](https://www.favicon.cc/?) to create a favicon.  

---  

<h5 id=mock-ups></h5>   

## **Mock-ups:**

The use of wireframes helps to create a visual format of the end product, this is a rough guide of  
how the finished site should aim to look.  

You can find my wireframes [here](https://github.com/fudge88/miumiu/tree/master/wireframes/wireframes).

These wireframes were created using [moqups.com](https://www.moqups.com) this allowed me to create a computer 
and a mobile  
mock-up of what MuiMui Aesthetics would look like. The main difference between the different screen sizes  
is the number of columns used to display the products.   

Structurally the major difference between the small and large screen is the navigation system. A more  
compact navbar is introduced on screen sizes 991px and below.  

In-house promotions are displayed on the larger screen, and hidden on the mobile view, to give a more neat  
and compact version of the site.  

---

<h5 id=features></h5>   

## **Features:**  
![home page](/wireframes/screenshots/home.PNG)   

<h5 id=navbar></h5>   

### **NavBar**  
**Navigation Large Screen:**  
The navigation bar on the large screen consists of a header and a menu bar.  
The header consists of interactive icons and the business logo that sits in the centre.  
- The search icon expands on hover, and the location icon redirects the user to a google map,  
and an address and opening details for MuiMui.  
- The circle icon has a count set in the centre which counts the number of items in the user’s  
basket; this defaults to 0 when empty.  
- The user icon drops down into menu options for the logged-on user or for an unauthenticated  
user to register/login.  

**Navigation Small Screen:**  
The header is hidden and a single navbar occupies the header, this contains a burger icon,  
search bar and the basket count icon.  
- The burger icon drops down to reveal the menu options, which further drop down into their subsections  
- The search icon opens an input field under the navbar  
- The basket count icon appears and functions in the same way is does in the large screen  

**Home:**   
Simple, relevant hero image of a female pampering herself. Simple message in the heading font speaking  
to the user directly, with a shop now button that redirects to all products.  

**Promotion Bar:**  
All information appears on the same strip on large screen, the smaller screen breaks down the information  
and uses a carousal to rotate the information.  

<h5 id=toast></h5>   

### **Toast:**
This displays a little pop up message that appears on the top-right of the screen confirming actions  
made by the user, i.e. added item to bag, deleted item from bag, etc.  

<h5 id=product-page></h5>   

### **Product Page:**  
![home page](/wireframes/screenshots/products.PNG)   
**Product promotion:**  
On a large screen this carousel displays 4 random products at a time from the database as a form  
of in-house advertising to the user; on a smaller screen this carousel is hidden.  

**Sorting options:**
- There is a drop-down filter on the right of page, which re-aligns to the centre for smaller screens,  
this offers the user various ways of filtering their search (in addition to the search bar).  
- There’s a product count on the left of the larger screen displaying the number of products displayed,  
this then centralises and sits under the sorting option on smaller screens  

**Product display:**  
- Products are listed in rows and columns, the columns reduce from 4 to 1 depending on the screen width,  
key information is given on each product for all screen sizes.  
- Quick add button is available under each product, which adds the product to the user’s basket in the  
quantity of 1, without redirecting the user to another page.  
- The product images are clickable and direct you to the product detail page.  

**Pagination:**  
Pagination, has been used to restrict the display of items to no more than 10 per page, this gives  
the user an indication of how many pages to view all products opposed to endlessly scrolling.  

<h5 id=product-detail></h5>   

### **Product Detail:**  
![home page](/wireframes/screenshots/product-detail.PNG)   
- This page shows individual product detail, and shows all the details associated to that product.  
- when the user clicks on the image, the image opens up on a new tab.  
- There’s a light blue block which nests a quantity input field that allows the user to type the  
quantity they would like to purchase, which is then executed by clicking the add to basket button.  
There are also social media icons in this block, that open the links on a new tab.  
- There’s a button to go back and continue shopping.  
- At the bottom of this page there are reviews for that product, all users can read this, and only  
authenticated users are able to add a review, which are time stamped should they wish to.  

<h5 id=shopping-basket></h5>   

### **Shopping basket:**  
- This page displays a summary of your order, each product is displayed on a separate row  
- This page shows the product quantity total, basket total, delivery charge (if any) and the total  
of all costs combined  
- The user is able to change the quantity of each item, and also remove the item from their basket   
altogether.

<h5 id=checkout-page></h5>   

### **Checkout page:**
- This page displays the items in your basket on the right of the page for large screens, and on top  
of the screen for mobile users.  
- The delivery and payment fields display on the left leaving the user to key in their personal  
information. If the user updates their details in their profile, the input fields on the checkout  
page would be prefilled, saving them the hassle of entering information every time they choose to  
purchase products.  
- Only displays checkout button to users who are logged-in, otherwise the user is redirected to login.  

<h5 id=checkout-success></h5>   

### **Checkout Success:**  
- Once the payments complete, the order summary is presented to the user; and email will also be sent  
confirming their order summary  
- This page also uses in-house product promotion, by displaying 2 random products in a carousel, to  
entice the customer to purchase more products, this is only available on larger screens, again to keep  
the mobile app minimal for ease of use and understanding.  
- There are 2 buttons, that could be presented depending on the route the user takes to this page. If  
the user views this page from their profile, the back to profile button with show, else it will offer  
to go back to all products.  

### **Profile:**
- The user has a profile, where they can update their delivery information.  
- The user can also view their order history, by clicking on hyperlinked order numbers which would redirect  
the user to the checkout success page for full details of that order.  

### **Login:**  
- Field for the user to login using their own username or password  
- User has an option to login using their social network login details, this enhances the users  
experience, i.e. not having to have to remember another password; a one-click login using the likes  
of google.

### **Admin:** 
- The admin is able to add products by selecting ‘project management’ from their profile drop down.  
There are also options to edit and delete from the product page and the product detail page. The delete  
function triggers a modal response to confirm if the admin wished to delete a product.
- There’s also an upload widget installed for the admin to search their own documents and add an image to  
their new or edited product accordingly.  

---

<h5 id=features-left-to-implement></h5>   

## **Features left to implement:**  
Due to time contains I was unable to factor in the following features; however, I do intend to give some  
more time to this project in the near future.  

**Membership:**  
I would like to add an option for a membership, which would coincide with the ‘30% off for members  
only', promotion. And add redirects to the promotional strip to member registration.  

**Allauth redirect:**  
Due to the ridged nature of the allauth templates, I was unable to add redirects from the checkout  
page, to the login page, and back to checkout. Due to time constraints I am unable to look into  
this at current, and will look into this in the near future to improve the UX.  

**Calculated Star Review System:**  
I would like to add a functioning ‘star’ review system to replace the static one I currently have;  
this would use the average ratings for each product to display a true reading.  

---

<h5 id=technologies-used></h5>   

## **Technologies used:**  
**Languages, Libraries and Frameworks:**  
- [HTML](https://en.wikipedia.org/wiki/HTML) - Markup language designed to be displayed in a web browser
- [CSS](https://en.wikipedia.org/wiki/CSS) - Style sheet language used for describing the presentation of a document in HTML.
- [JavaScript](https://en.wikipedia.org/wiki/JS) - a high-level, just-in-time compiled, object-oriented programming language
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - High-level, general-purpose programming language
- [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) - templating language for Python, to display back-end data in HTML
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) - Python framework for building large projects
- [Bootstrap](https://getbootstrap.com/) -  front-end framework for layout and design
- [JQuery](https://jquery.com/) - to simplify DOM manipulation and to initialize Bootstrap functions
- [Gunicorn](https://gunicorn.org/) - a Python WSGI HTTP Server to enable deployment to Heroku
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - styles Django forms  

**Databases:**  
- [SQlite3](https://www.sqlite.org/index.html) - a development database.
- [PostgreSQL](https://www.postgresql.org/) - a production database.  

**Tools, Editors:**  
- [FontAwesome](https://fontawesome.com/start) - to provide icons used across the project.
- [Google Maps](https://developers.google.com/maps/documentation/javascript/get-api-key) - to render the map in Contact page.
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [Stripe](https://stripe.com/gb) - to handle financial transactions.
- [AWS S3 Bucket](https://aws.amazon.com/) - to store static and media files in production.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for compatibility with AWS.
- [moqups](https://moqups.com/) - to create wireframes.
- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [Git](https://en.wikipedia.org/wiki/Git) - for version control.
- [GitHub](https://github.com/) - for remotely storing project's code.
- [Heroku](https://dashboard.heroku.com/apps) - to host the project.

---

<h5 id=testing></h5>   

## **Testing:**

Testing information can be found [here](https://github.com/fudge88/miumiu/tree/master/TESTING.md).  

---
<h5 id=deployment></h5>  

## **Deployment:**

<h5 id=local-deployment></h5>   

### **Local Deployment:**  
This repository can be cloned directly, by pasting the following command into the terminal:  
> `Git clone https://github.com/fudge88/miumiu`

This repository can also be cloned via the green **_‘download code’_** link above,  
selecting **_‘download zip’_**, and then extracting the file to your chosen folder.  

1. In your terminal use the **_‘cd’_** command to change into the directory you want the  
cloned directory. 
> `cd <filename>`
2.	Type:  
> `git clone https://github.com/fudge88/miumiu`  

You would need to set up your environment variables (this process can differ depending on the  
IDE you are using).

3.	We create a **_.env_** file in the root directory:
4.	Then we add this file to **_.gitignore_** file  

5. In the .env file you will be required to set the environment variables:  
>`import os`  
>>`os.environ["DEVELOPMENT"] = "True"`    
>>`os.environ["SECRET_KEY"] = "<Your Secret key>"`    
>>`os.environ["EMAIL_HOST_PASS "] = "<Your google key>"`    
>>`os.environ["EMAIL_HOST_USER "] = "<Your google email>"`    
>>`os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"`    
>>`os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"`   
>>`os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"`   
>>`os.environ['AWS_ACCESS_KEY_ID'] = 'your value'`
>>`os.environ['AWS_SECRET_ACCESS_KEY'] = 'your value'`
>>`os.environ['DEVELOPMENT'] = '1'`
6.	into your terminal key in and install all the requirements:  
> `pip3 install -r requirements.txt`  

7.	run migrations to create a database by typing:  
> `python3 manage.py make migrations`  
and then:   
> `python3 manage.py migrate`  
8.	load the data fixtures in the following order by keying in:  
> `python3 manage.py loaddata categories`  
> `python3 manage.py loaddata products`
9.	create a superuser/admin for your website, you will be prompted to key in some  
credentials follwo indtructions:  
> `python3 manage.py createsuperuser`  
10.	You can run the application using: 
> `python3 manage.py runserver`
11.	To access the admin interface, key in **_‘/admin’_** at the end of your locally deployed url.

<h5 id=deploy-to-heroku></h5>   

### **Deploy to Heroku**
**Note: the above process must be completed before deploying to Heroku.**
1.	your requirement.txt file will need to contain all your project dependencies, key in the  
following to load this folder with additional dependencies you may have added.  
> `pip3 freeze > requirements.txt`  
your requirements.txt folder should include **_gunicorn, dj-database-url, and psycopg_** for  
successful deployment to Heroku.  
2.	Create a **_Procfile_**, this tells Heroku how you would like to run the project, using the  
following command in the terminal:  
> `web: gunicorn miumiu.wsgi:application`
3.	*_git add, git commit and git push_** these files to GitHub repository.  
4.	create a new app on heroku  
5.	select the **_Resources_** tab in Heroku, then search for **_Heorku Postgresin_** the add-ons  
searchbar, select **_Hobby Dev — Free_** and click Provision button to add it to your project.  
6.	In Heroku Settings click on **_Reveal Config Vars_**. Set the following config variables there:

> AWS_ACCESS_KEY_ID	`<your aws access key>`  
> AWS_SECRET_ACCESS_KEY	`<your aws secret access key>`  
> DATABASE_URL `<your postgres database url>`  
> EMAIL_HOST_PASS `<your email password(generated by Gmail)>`  
> EMAIL_HOST_USER `<your email address>`  
> SECRET_KEY `<your secret key>`  
> STRIPE_PUBLIC_KEY	`<your stripe public key>`  
> STRIPE_SECRET_KEY	`<your stripe secret key>`  
> STRIPE_WH_SECRET `<your stripe wh key>`  
> USE_AWS `True`  
**_(aws details you will get when you set up your aws bucket)_**  

7. Back on your current workspace, **_comment out the default database configuration_** and add the following:  
> `DATABASES = {`  
>    `'default': dj_database_url.parse(os.environ.get('< Put your DATABASE_URL here >'))`  
> `}`  
8. Migrate the database models to the Postgres database by following **_steps 7-9 in the local deployment_**  
9. After migrations are complete, change database configurations to:  
> `if 'DATABASE_URL' in os.environ:`  
> `    DATABASES = {`  
> `        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))`  
> `    }`  
> `else:`  
> `     DATABASES = {`  
> `        'default': {`  
> `            'ENGINE': 'django.db.backends.sqlite3',`  
> `            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),`  
> `        }`  
> `    }`  

This allows sqlite 3 to be used in development, and postgress to be used in deployment.  
10. Add Heroku app url to the **_‘allowed_hosts’_** in your **_settings.py_** file.  
11. In Heroku select the **_deploy tab, select github_** 
12. Link Heroku to your github repository by inputting your git repository,   
and select **_enable automatic deploys_**.
13. In your gitpod terminal login to Heroku, key in:  
> `Heroku login`  

14. To build your app and deploy your project in in Heroku, key in the following:  
> `Git add .`  
> `git commit -m “<your message”`  
> `git push` to push to your GitHub repository  
> `git push Heroku master` to push to heroku  

from this point any `push` you make in the terminal will update your app in heroku,  
as the two are now linked.

---

<h5 id=credits></h5>   

## **Credits:**  

**Code**  
Alot of the content was used  from the [code institude](https://courses.codeinstitute.net/program/FullstackWebDeveloper) lessons, especially  from the mini project 'Boutique Ado';   
however, this code was customised and enhanced to fit the purpose of teh project.  
I found [codeloop](https://codeloop.org/django-pagination-complete-example/) to support me with implementing pagination   into the Django app. 
[Stackoverflow](https://stackoverflow.com/questions/21938028/how-can-i-get-a-favicon-to-show-up-in-my-django-app) was 
extreamly   
helpful with applying the logic for a favicon. [Django project components (Yuksel CELIK, PhD):](https://www.youtube.com/channel/UCtdM2qlDnpNr9bTKjVGEWkg) 
supported the  
implementation of reviews for the products. [Platform-kooperativa](http://platforma-kooperativa.org/media/uploads/article-documents/beginning_django_e-commerce.pdf) helped me further with the views and   
models of of my project. [Stackoverflow](https://stackoverflow.com/questions/48079216/add-limit-for-list-in-for-loop-django-template) proved 
extreamly useful on numerous occassions, again, helping me to   
understand how to slice through data using jinja templating. the [Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/templates.html) was very easy to   
follow when implementing social network login (google). I also used [youtube](https://www.youtube.com/watch?v=56w8p0goIfs), to help me navigate through the   
implementation of this.

**Content and Media:**  
I used [canva](https://www.canva.com/) to create a logo for my site, and used the design to to create a [Favicon](https://www.favicon.cc/).
[Stackoverflow](https://stackoverflow.com/questions/35351353/missing-visible-and-hidden-in-bootstrap-v4) helped in alot   
of the styling issues i had for example the inline display classes.
[Bootstrap](https://getbootstrap.com/docs/4.4/layout/grid/) was used for the grid system, and also   
its styling properties. 
[mdbootstrap](https://mdbootstrap.com/docs/jquery/javascript/google-maps/), helped style the map found on the locations page.
The images for the products   
were taken from [lush](https://uk.lush.com/), which was also a design inspiration.  

**Acknowledgements:**  
I would like to thank everyone who have helped me throughout this project.  
The slack community, the tutors on tutor support, my mentor. You have all been there for me to ask for help,  
no matter how big or small my query has been. You have all played a big part in encouraging me, supporting me,  
and ofcourse having alot of patience with me. Thank you.


