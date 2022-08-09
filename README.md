# Shopping Chart

Shopping Chart is a Full-Stack E-commerce Application that allows users to buy the license for trading algorithm via a full functioning Stripe paying systems and user authentication.

The deployed site can be found [HERE](https://mr-shopping-chart.herokuapp.com/)

![Title](readme/images/amiresponsive.png)

<br/>
<br/>
<br/>

# SECTION 1: UX

## 1. Strategy

### 1.1 E-Commerce Strategy & Business Model:

The E-Commerce business model offers clients the possibility to purcase a monthly subscription to use live trading algorithms.

The site offers various kind of strategies which cover different asset classes:
- Stocks
- Fixed Income (Bonds)
- Cryptocurrencies
- Fx Rates

This business idea is intrinsically adapt to an Ecommerce, since the niche of educated users interested in investing via trading algorithms have a knowledge and interest in the world of coding and web in general that is far higher than average.

Moreover, the product is much easier to promote and sell via a web platform: physical stores are not competing in this sector.

As part of the Ecommerce strategy, Users also have the ability to browse the site's blog, rate its post and comment it, as well as access the glossary of the site. All with the purpose of creating education material connected to the world of algorithm investing.


### 1.2 Marketing Strategy:

Shopping Chart marketing strategy includes Search Engine Optimisation, Content Marketing, Email Marketing, Social Media Marketing and Paid Web Marketing.

### Search Engine Optimization

The main objective of the Search Engine Optimization strategy is to have the Shopping Chart website a favorable high ranking on search engine results pages, as a part of the web marketing strategy. To achieve this objective, keyword research has been performed, an on-page optimization has been conducted, and an off-page strategy has been planned for the future.

**Keyword Research**

The Search Engine Optimization process is started by determining the keywords, both short-tail and long tail. To help determine these keywords, first the critical questions about the users were answered, which were “What do our users need?” In this case it is ready to deploy strategic trading algorithms.

Based on that answer, three general topics had been formulated: algorithmic trading, algo strategy, and trading software. Then a Google Search on these topics helped find related search inquiries to list possible keywords ideas. Was run also a keyword research on [Wordtracker](https://www.wordtracker.com/search) to find other possible keyword ideas and review those keywords’ volume and competitive difficulty.

From that research, we determined the following keywords:

Short Tail Keywords:
- Algorithmic trading strategy
- Strategic algo traders

Long Tail Keywords:
- Top algorithmic trading strategy
- Best strategies for algo traders
- Ready to deploy algo trading strategies

**SEO Implementation**

In order to build a solid SEO-smart website, pages were written systematically in order to contain the determined keywords. “Keyword stuffing” was avoided, in a way that the copywriting of the website is logical, seamlessly readable and with intentional messaging. In addition to that, the social links at the footer of the site are meant to be excluded from Search Engines for ranking purposes. For that reason, the rel="noopener” attribute has been applied to exclude social links.

Beyond the internal links, the site includes links to external sites that have good Domain Authority to support for backlinks opportunities, such as [Investopedia](https://www.investopedia.com/) and trusted brokerage or trading platforms. These external links are mainly included within the blog posts, as they are informational and educational, making them the most strategic part of the site to cite other players in the trading field

The meta data (title, description, and keywords) for all pages and products have also been added to further support the search engine optimization as seen in the following screenshot.
An useful feature regards the use of the descrption (showed also in the algorithm page) and the keywords (visible only to the admin), in the meta tags of the web pages. This allows more specific and easy to update SEO strategy.

![Title](readme/images/seo-screenshot1.png)
![Title](readme/images/seo-screenshot2.png)

Furthermore, two important files to help with the SEO strategy have been added to the site, which are the sitemap.xml and the robots.txt. The sitemap file lists the site’s important page URL's, making sure that search engines are able to crawl them and understand the website structure. On the other hand, the robots.txt is a text file that tells search engines the prohibited pages where they are not allowed to go on our website - listing any folders or files that are not supposed to be crawled or indexed by search engines. Having these files is a foundational part of the whole SEO strategy and should help improve the site’s visibility and SEO ranking.


**Further SEO Plan**
 
In the future, to help with the SEO ranking and as a part of the extensive marketing strategy, the plan is to reach out to bloggers and blog aggregators in order to obtain backlinks to our website. The more articles, or blog posts that mention and link to Shopping Chart, the better the website will rank in certain search engines and for certain keywords.


### Content Marketing

The main target of Shopping Chart are independent traders who seek ways to make profit from algorithmic trading. These users are usually not professional traders, and they lack the skill to do the algorithm coding themselves. This is where our products (ready to deploy trading algorithms) propose real value. With this nature of the users, the marketing approach is more educational to gain their trust first, before selling them the products.

For that reason, Shopping Chart puts a heavy focus on its blog as the center of the content marketing strategy. The blog is planned to be an authoritative, trustworthy, and reliable source for anything related to algorithmic trading. In this way, users who are interested in anything about algorithmic trading will come to the website looking for guides, tips, news, and updates; then possibly converted to make a purchase of the trading algorithm.

In the future, this type of educational content marketing will be expanded to be more interactive on other channels such as podcast and video (YouTube) in order to attract a larger audience and gain more presence.


### Social Media Marketing

As part of the “building trust” marketing approach, an official Facebook business page for the Shopping Chart site has been designed. The page is dedicated to announce any news and updates regarding the products, as well as interactive connection with the trading community. Facebook is currently improving their security and there have been issues in creating a real business page, especially for the ones related to trading. The screenshot below is the mockup design as a guidance for the upcoming Facebook page. 

![Title](readme/images/facebook.png)

Other than Facebook, Shopping Chart is planned to have a Twitter account. Twitter is proven to be the most favorite platform for updates among traders. Shopping Chart Twitter account will focus more on announcing interesting remarks of stocks and related news or updates. 


### Email Marketing

Email marketing is one of the must-have tools for all e-commerce businesses. This marketing channel is believed to be the most effective as all users must have an email address, and we can reach out to them easily using emails. As part of the Shopping Chart marketing strategy, we have included an email newsletter sign up form in the footer section, completed with GDPR consent, for users to opt-in in receiving news or updates from Shopping Chart.

Via collecting user emails, Shopping Chart plans to send out a weekly newsletter with market updates and special offers only for newsletter subscribers. On top of that, Shopping Chart will set up an automated email to upsell customers some time after their purchases to check out similar trading algorithms that may interest them.


### Paid Web Marketing

To boost the SEO ranking and marketing, Shopping Chart plans to also include Paid Web Marketing in the marketing strategy. The main search engine to rank and to target is Google Search, for that reason, we will focus on planning advertising campaigns on Google Search Ads. The strategy will include creating ad campaigns on the defined keywords and to target a certain demographic that fits our users and to start within a geographical area.

<br/>
<br/>
<br/>

# SECTION 2: User Stories

## Scope and AGILE method

The Scope of the site is broadly encompassed in the follwing main tasks:

1. Create an Ecommerce Website App to allow users to purchase trading algorithm
2. Create an educational platform for the community to increase education and encourage members to purchase more strategies

### **1 - Ecommerce Website App - User Story Mapping:**

### *As a site user I can:*
- View a list of algorithms so that I can sort and select the one I am interested in by rating, price, category.
- Select an algorithm category in the navbar so that I can filter them and see the ones I am interested in
- Insert a keyword in the search bar so that I can retrieve all the Algorithms that contain that word in their name or in their description
- Select an Algorithm so that I can view details in its page: price per month, return, volatility, rating and description.
- Add and delete products in the shopping bag for the chosen license period, so that I select what products I want to purchase
- Insert my address payment information, check out and proceed with the payment
- Receive an email confirmation after checking out so that I can have a record of the purchase on my e-mail and receive the link to retrieve the algorithm code
- Receive notifications for relevant actions so that I can receive feedbacks and reinforce what I am doing
- Register in the site so that I can create a personal account
- Login/Logout so that I can enter in my personal account
- Access a personal user profile so that I can view my order history and confirmations, as well as save my payment information
- Sign on a newsletter so that I can be updated about the latest products and deals

### *As a site owner I can:*
- Create, Read, Update and Delete Algorithms from the site so that I can manage the algorithm list easily, without using the Django Admin. By inserting keywords and description, I can also actively manage the SEO Strategy.


### **2 - Educational Platform - User Story Mapping:**

### *As a site user I can:*
- Read a glossary so that I can get educated regarding industry terminology
- Read the site's blog so that I can be informed regarding relevant industry themes.
- Read all user ratings and comments and Create, Read, Update or Delete my own rating and comments so that I can express my opinion and see what the community says.

### *As a site owner I can:*
- Create, Read, Update and Delete glossary terms from the site so that I can manage the terms list easily.
- Create, Read, Update and Delete blog posts via django admin so that I can keep the blog updated.



To deliver the scope of the project, an Agile approach to Software Development has been pursued for the project implementation. The tool used for this purpose is the **Github Kanban board** functionality, managing the life cycle of the issues from *To Do's* to *in progress* and eventually *Done*. 


<br/>
<br/>
<br/>

# SECTION 3: FULL STACK WEBSITE IMPLEMENTATION

The overall website is implemented via the Django Framework functionality

## Back-End: Database Structure
The site uses PostgrSQL, which is an open-source relational database system compatible with most programming languages.
The database schema below illustrates the Data Model and Fields created, with the relationship between them.

Some of the models take inspiration from the CI PP5 walkthrough project, however some of those models had been modified to better assist a product that does not have a delivery cost or size: the models has been modified including fields such has Return, Volatility, License Period and Keywords, the latter for better SEO management. 
Moreover, four additional models were created:
 - Newsletter: to manage in the database the request to be added to the mailing list from the user
 - Glossary: to manage the list of terms and description
 - Post: to store information regardin the blog posts
 - Comment: to store user comments and 1 to 5 star user ratings 

![ERD](readme/images/erd.png)

## Front-End: Site Structure
Below are presented the wireframes created during the site project planning, which consitutes a first draft on how the site should appear, taking into consideration the user stories included.

- Wireframe 1 - Homepage

![Home page](readme/images/homepage-wireframe.png)

- Wireframe 2 - Algorithm list

![Algorithm List page](readme/images/algo-list-wireframe.png)

- Wireframe 3 - Algorithm detail

![Algorithm Detail page](readme/images/algo-detail-wireframe.png)

- Wireframe 4 - Shopping Bag page

![Bag page](readme/images/bag-wireframe.png)

- Wireframe 5 - Blog

![Blog](readme/images/blog-wireframe.png)

- Wireframe 6 - Glossary

![Glossary](readme/images/glossary-wireframe.png)


## Design

The website was designed using the Bootstrap framework in order to create a fully responsive site.

### Colour palette

The color used are mainly yellow, blue and black and create a high contrast in the page: a must in the Fintech design adopted by several competitors.

![Colour-palette](readme/images/colour-palette.png)

### Images

Most of the images were modified via Adobe Photoshop to increase their quality, contrast or meaning, and are all sourced from [Pexels](http://www.pexels.com)

Several images are added in the site, increasing the tech flavour that the user experiences navigating the pages.

Moreover, how can one represent a list of algorithm via images? The choice was to create a template image that adapts to the algorithm main category, subcategory and strategy. Changing colours and wording the risk of repetitive cards is mitigated.

![Product images](readme/images/product-images.png)



### Icons

The Icons used are created with the help of the following sites:
- [fontawesome](https://fontawesome.com/start)
- [favicon](https://www.favicon.io/) 


## Features

* ### Home Page and Navigation Bar:
The navigation bar is intuitive: users can always return to the algorithm list, which shows the list of all the algorithms. Moreover, users can filter the algorithm by category, visit the blog, the glossary, log in, register or log out.
In the homepage, the user is called to action in order to explore more of the products offered.

![homepage](readme/images/homepage.png)


* ### Algorithm List:

The Algorithm List page contains a list of all of the algorithms available on the site, together with options for sorting by price, category, name and rating. The page will also display a count of the displayed products, and will have a search bar at the top of the page.

![algo-list](readme/images/algo-list.png)


* ### Algorithm Detail:

The algorithm detail page is reached by clicking on the image of any of the algorithm cards in the listr. The user will retrieve the most important information about the produtct, such as name, license price per month, rating, description, total return and volatility. With buttons the user can specify how many months of licensing he wants to purchase and add it to the shopping bag.

If the user is a superuser, from this page he can access links to update or delete the algorithm

![algo-detail](readme/images/algo-detail.png)


* ### Shopping Bag

In the shopping bag, the user can see all the purchased products and adjust the license period / remove them. 

![shopping-bag](readme/images/shopping-bag.png)


* ### Checkout page

By clicking "Secure Checkout" in the shopping bag, the user goes in the checkout page in which he can insert the delivery information and the credit card number to be debited. If registered, the user can also save his delivery information for future purchases.

![checkout](readme/images/checkout.png)


* ### Order confirmation

Once the checkout is completed and the user submits the order, he will be redirected to an order confirmation screen showing a record of his order in detail, with  order number, delivery address, the product details, the delivery address and other relevan information. A call to action button will ask them to continue shopping in the site.

![order-confirmation](readme/images/order-confirmation.png)


When the user successfully submit the order, he will also receive a confirmation email on the provided address with an order recap and the link to access the algorithm code.

![email-confirmation](readme/images/email-confirmation.png)



* ### Add/Delete a product

The site Admin can always delete or add/modify a new product via its algorithm management page, accessible under the My Account tab. This feature is essential for product inventory management and SEO optimization via description and keywords.

To delete it, it will be sufficient to press the button Delete which will appear to the Admin if he is in the algorithm list or in the algorithm details page.

![algo-admin](readme/images/algo-admin.png)


* ### User Authentication & Profile Page

As anticipated, a user can register, log-in or sign-out via proper and standard allauth forms. He can also access his profile page, in which he can update his delivery information and view his order history.

![profile-page](readme/images/user-profile.png)



* ### Glossary

A site user can access the glossary, in which a list of terms will be shown along with its description, for educational purpose.
If the site user is a superuser (shown below), he can successfully update or delete a term, in order to populate the list and keep it updated.

![glossary](readme/images/glossary.png)


* ### Blog and Blog posts

In the blog section, the user can view a list of blog posts with the title and a small description about the topic trated.

![blog](readme/images/blog.png)


The user can click on the post of interest and read the full article.

![blog-post](readme/images/post.png)


Moreover, the registered user is allowed to post comments and ratings, in order to express his opinion, give a rating and engage with the community.
The user can also edit and delete his previous comments and ratings.

![post-comments](readme/images/comment.png)


* ### Newsletter Signup

At the bottom of every page of the site, a banner asks user to submit their email in order to receive future offers and material. The user must consento to the site privacy policy, which can be read via link below.

![newsletter](readme/images/newsletter.png)


<br/>
<br/>
<br/>

# SECTION 4: Testing, Bugs and Future Features

The tests below are part of the manual testing procedures employed to verify the correct functioning of the website features

## Functionalities Testing

**Authorisation & authentication Testing:**

n | Test Case | Result | Pass/Fail 
------------- | ------------- | ------------- | ------------ 
1 | Account register | Clicking on the signup button, the user goes in the signup page, compiles the required fields and clicks on the Sign Up Button | Pass
2 | Email Verification| After submitting his data, the user is redirected to a new page and is informed about a confirmation email sent to the address provided in the signup form| pass
3 | Confirmation email | The user effectively receives the mail with the confirmation link, which leads to the confirmation page of the site. Once confirmed, the account is successfully created and the user can log in with his new profile | pass |
4 | Log Out | Clicking on My Account > Log Out, the user logs out of the site after confirmation| pass

**General site functiionality testing:**

n | Test Case | Result | Pass/Fail
------------- | ------------- | ------------- | ------------ 
1 | Algorithm List Pages | Clicking in the all algorithm button, the user effectively views the list, that can be filtered and sorted. Same applies for every macro category (stock, fixed income, Crypto&Fx) | pass
2 | Glossary Page | Clicking in the proper tab, the glossary is correctly loaded | pass
3 | Blog Page| Clicking in the proper tab, the blog is correctly loaded | pass
4 | My Account Page| Clicking on the My Account button, the user can enter is profile page | pass
5 | Shopping Bag Page | Clicking on the Shopping Bag button, the user can view his current shopping bag | pass
6 | Homepage | Clicking on the site logo, the user can view the homepage | pass


**Algorithm details testing:**

n | Test Case | Result | Pass/Fail
------------- | ------------- | ------------- | ------------ 
1 | Algorithm Detail | clicking on the algorithm card in the list, the user can enter in its details page | pass 
2 | License Period Selector | The user can select the license period via plus and minus buttons, without going below 1 | pass
3 | Keep Shopping Button | The Button effectively redirects to the algorithm list | pass
4 | Algorithm Delete | As an Admin, the user can delete the product via proper button | pass
5 | Algorithm Update | As an Admin, the user can go to the product update page via proper button | pass

**Shopping bag testing:**

n | Test Case | Result | Pass/Fail
------------- | ------------- | ------------- | ------------ 
1 | Add to Bag | clicking the add to bag button, the product is effectively added in the bag | pass
2 | License period selector | The user can update the license period previously chosen | pass
3 | Remove Button | The user can remove an algorithm in the bag via proper button | pass
4 | Secure Checkout button | By clicking the button, the user is redirected to the checkout page | pass
5 | Keep Shopping Button | By clicking the button, the user is effectively redirected to the algorithm list | pass

**Checkout testing:**
n | Test Case | Result | Pass/Fail
------------- | ------------- | ------------- | ------------ 
1 | Name and delivery details | User is presented with a form in which he can insert all the relevant data | pass
2 | Adjust bag button | Clicking it, the user can go back to the bag to adjust it | pass
3 | Product List and Subtotal | User is presented with an order summary withthe list of items chosen along with its subtotal | pass
4 | Complete Order Button | Clicking the button, the order is processed and a confirmation page loads with all the relevant order informations | pass
5 | Order Email Confirmation | The user is notified via email of the order | pass

**Glossary testing:**

n | Test Case | Result | Pass/Fail
------------- | ------------- | ------------- | ------------ 
1 | List of Terms | The user can easily see the list of terms along with their descriptions | pass
2 | Edit Terms | As an Admin, the user can click on Edit and upload a form to amend the term name or description | pass
3 | Delete Terms | As an Admin, the user can click on Delete and delete the term from the list | pass
4 | Upload new Terms | As an Admin, the user can compile the form for a new term and submit it successfully | pass


**Blog testing:**

n | Test Case | Result | Pass/Fail
------------- | ------------- | ------------- | ------------ 
1 | Blog list view | in the blog list, a user can click on the read more button and enter in the blog post specific page | pass
2 | Post Comment | The registered user writes a comment in the form, assigns a rating ad submit it successfully | pass
3 | Edit Comment | The registered user can Edit only his own comments and ratings successfully | pass
4 | Delete Comment | The registered user can Delete only his own comments and ratings | pass


## Validation Testing

Every piece of code written and used for this Full Stack Web Application has been tested via industry standard validators. 

### HTML
All the pages passed successfully the [W3C](https://validator.w3.org/) HTML validation test

Below an example:
![HTML Validator](readme/images/html-validator.png)

### CSS
All the CSS Code passed successfully the [Jigsaw-W3C](https://jigsaw.w3.org/css-validator/) HTML validation test

Below an example:
![CSS Validator](readme/images/css-validator.png)


### JavaScript
All the JavaScript Code used passed successfully the [JSHint](https://jshint.com/) validation test

Below an example:
![JS Validator](readme/images/js-validator.png)


### Python
All the Pyhton Code used passed successfully the [PEP8](http://pep8online.com/) validation test

Below an example:
![Python Validator](readme/images/py-validator.png)


### Lighthouse Audit
All the pages received scores higher than 90 in SEO, Accessibility, and Best Practices. Performance sometimes had a score of around 80 because some pictures are in high resolution. Given this, the performance of the site looks still solid and page rendering is not excessively slow. 

Below an example both for desktop and mobile views:
![lighthouse Validator Desktop](readme/images/lighthouse-validator.png)
![lighthouse Validator Mobile](readme/images/mobile-lighthouse-validator.png)


### Cross Browser and Device Testing
- The site has been tested on multiple devices screen sizes with the proper Chrome emulator. All the elements of the pages are rendered properly and are fully responsive. The Bootstrap5 Grid System has been largely used in the HTML code, greatly facilitating the development of responsive pages.
- The website has been successfully tested on Safari, Chrome and Firefox.


## Bugs

### Resolved Bugs

- Stripe Webhook not functioning properly: This problem occurred during the refactoring of the code. I accidentally cut with the "/" character a template literal longer than the allowed string length. This caused an ERROR500 during the payments.succeeded phase. After reverting to the previous day repository status, I was able to identify the typo and solve it.

- Minus button not greyed out in the license period quantity selector of the bag page. As mentioned during the course, the code refactoring employed in the lectures causes a misfunction of a JS code. The JS employed to grey out the minus button for the license period data was originally calling the element via ID. With the refactoring, a duplicate of the license period selector was created and the ID would work only on one of the two, used for the mobile view, making the feature not functioning in the desktop view. I duplicated the code with a separate ID to solve the problem.


### Unresolved Bugs
As of today, there are no unresolved bugs in the site


## Future Features

- Performance Chart in the Algorithm Details page: in this way the user will have a much better understanding of the past performance of the algorithm

- Enquiry Session: a form used by the user to ask specific or general question to the site owner

- Glossary Terms in Algorithmic Details: each Algorithm in its details will have a section with all the terms related to its strategy, so that the user can easily access them and document itself in the glossary


# Section 5: Deployment


### Project Deployment - needs adapting for AWS and Stripe

1- Heroku

To deploy the project through Heroku these steps were followed:
1. Sign up / Log in to [Heroku](https://www.heroku.com/)
2. From the main Heroku Dashboard page select 'New' and then 'Create New App'
3. Give the project a name and select a suitable region, then select create app.
4. Click on the 'Resources' tab and search for 'Heroku Postgres' as this is the add-on you will use for the deployed database.
5. In the settings tab, reveal config vars and insert the DATABASE_URL along with its SECRET_KEY, the Amazon Web Services access keys (used for data storage) and the STRIPE keys, used for the payment app:
![heroku-config-vars](readme/images/heroku-config-vars.png)
6. Once everything is set up, you are ready to deploy: there is the proper functionality in the 'deploy' tab, but this needs prior GitHub connection. Unfortunately, as of the date of this writing, the GitHub connection is not functioning.
To solve it, you can deploy via Gitpod terminal. To do so:
     - Log in your Heroku account from GitPod, entering: "heroku login -i"
     - Once authenticated, enter: "heroku git:remote -a {app_name}", where app_name is the name given on Heroku to the app just created.
     - Add and commit any changes to the code, if applicable.
     - Push both to GitHub and Heroku entering the following commands:
       - "git push origin main"
       - "git push heroku main"


2 - Amazon AWS
<br>
Shopping Chart uses Amazon AWS for data storage of static and media files.
1. Navigate in a browser to Amazon AWS, log in, or create an account and log in. 
2. Create a new S3 bucket for the site and create a static directory and media directory within the bucket.
3. From the dashboard - copy the bucket details into the settings file.
    * you will require the following:
        - Storage Bucket Name
        - Storage Bucket Region Name
        - Access Key ID
        - Secret Access Key
    * configure these settings in the settings file
* in the env.py file created earlier 
    - add os.environ["AWS_ACCESS_KEY_ID"] = "paste in your access key"
    - add os.environ["AWS_SECRET_ACCESS_KEY"] = "paste in your secret access key"


## Credits

### Media Credits
- Images for companies were found on: <a href="https://www.pexels.com/it-it"><strong>Pexels</strong></a> and adapted using Photoshop.

### Code Credits 
- The code structure is based on the material provided during the <a href="https://codeinstitute.net/global/"><strong>Code Institute</strong></a> course, especially from the Boutique Ado walkthrough project.
- Other minor code credits are displayed as comments in the website code.

 
## Acknowledgments
A special thank to:
- My mentor <a href="https://github.com/maliahavlicek"><strong>Malia</strong></a> for her help, motivation and belief in my capabilities.
- My family and my partner, for their patience and support demonstrated during the whole course.