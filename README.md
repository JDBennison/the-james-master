# The James Master
Dungeons and Dragons has been a passion of mine for over twenty years and one of the things I love most is introducing new people to the hobby. Speaking to many friends, acquaintances and strangers, I have found that a lot of people want to play but find the prospect of running a game quite daunting and that’s where The James Master came from. I wanted to offer my services as a professional Dungeon Master to groups looking to learn to play, looking to play a one off adventure or for people who want to hire someone to run a campaign over a number of weeks. I think this will appeal to teenagers who have never played before, right up to corporate clients who want to run games as a team building event for their staff.
## UX
### User Stories
[Here is a link to the user stories put together](https://github.com/JDBennison/the-james-master/tree/master/media/userstories.xlsx)

### Links To Wireframes
[Here is a link to all of the wireframes for The James Master](https://github.com/JDBennison/the-james-master/tree/master/media/wireframes)

## Features
Here are a list of the features that I have included in this project and features that are yet to be implemented
### Existing Features
* Log In/Register
Using allauth templates the users are able to log in and register securely with email authorisation.
* Profile View
A user can view all of their previous and upcoming bookings as well as updating their name and phone number which are saved and added to new booking forms automatically.
* FAQ
Commonly asked questions are displayed for customers to view and hopefully answer any lingering doubts or misconceptions they have.
* Booking System
The booking system is slimline and simple for users to select available dates and pay for them. There is also a personalised summary for each customer with details of their order and things they might need to know before making the final payment
* Blog View
Users are able to look through the blog and see recent blogs on every page so that they can deep dive into any subject about roleplaying. As time goes on, more content will be added regarding specific topics for new players, as well as different systems that they can play that aren’t just Dungeons and Dragons.
* Blog Update
Through the admin page, superusers can write their own blogs, save them as drafts and add pictures before they are published to the website with ease.
* Blog Search
On all the blog pages, customers can search for keywords within blog posts so they can read post on the things they are interested in
* Contact Form
Customers are able to send initial enquiries and questions on the home page with a simple form.
* Newsletter signup
On every page in the footer, a customer can sign up for a newsletter subscription with ease.


### Features Left to Implement
* Log In With Social Media Accounts
In future updates I would like to further research how to let users sign in with Facebook and Google.
* Automated date adding
Currently, available dates are added manually by a superuser. I would like to be able to add an automated system to create regular weekly available dates which can be manually closed off. Also I would like to be able to automatically close down dates that are in the past.
* Calendar View
When customers come to book, rather than a drop down list, I would like to get a calendar view so that they can easily and visually see when the dates are.
* Multiple Dungeon Masters
If the company were to expand I would hire other dungeon masters and would like for the users to be able to see individual people’s calendars and book them specifically.
* Multiple bookings
For customers booking the Ongoing Campaign, they need to book a minimum of six sessions and currently have to do each one individually. I would like to create a more complex system for customers to book multiple sessions at once. I believe this would help me not lose customers who might book one session and then never get back to me again.
* Local Time Zones
For customers who might want to book online sessions from other countries it would be great to get a system which localises the times of the game based on where they are based.
* Blog archive
Once more blogs are written it would be good to have an archive facility so that users can go through month by month and look into past  blog posts
* In site blog writing
As opposed to going into the admin site, I would like to build a page for superusers to write blogs within the site itself and manage existing blogs.
* Blog pictures
In future blogs it may be prudent to be able to add pictures throughout the blog to make it more eye catching for the user.
* User notes
As a backend function I would like to be able to put notes on each users profile regarding characters and games they have played so that if other dungeon masters are going to run for them, they can read up on what they have experienced so far. Also a facility to be able to upload files, such as character sheets, so that they are easily accessible for all super users.

## Technologies Used
For the basics of front end I mostly used HTML5, CSS3 and Javascript and back end I used Python and Django along with the following libraries and frameworks
* [Bootstrap](https://getbootstrap.com/)
	* For formatting and structure
* [JQuery](https://jquery.com/)
	* To initialise materialize components. 
* [Font Awesome](https://fontawesome.com/)
	* For icons throughout the website.
* [Favicon Generator](https://realfavicongenerator.net/)
	* To create the favicon.
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
	* For the login and registering process
* [Heroku](https://www.heroku.com/)
	* For deployment
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/)
	* For easy rendering of forms
* [Stripe](https://stripe.com/gb)
	* For card payments
* [AWS](https://aws.amazon.com/)
	* For storage of static and media files
* [Tiny MCE](https://www.tiny.cloud/)
	* For the blog input, it stores the text as html to allow easy formatting.

## Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.
Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.
For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:
	1.	Contact form:
	i.	Go to the "Contact Us" page
	ii.	Try to submit the empty form and verify that an error message about the required fields appears
	iii.	Try to submit the form with an invalid email address and verify that a relevant error message appears
	iv.	Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment
### Heroku
To deploy my application I used Heroku and there were a number of steps to follow before I could do this.
1. To protect all of my environment content variables, I put these in an env.py file and added this to a .gitignore file so they weren't saved on Github for everyone to see. I also added them into Herokus Config Vars for production.
2. I needed to make sure that I had a requirements.txt file with a list of all the packages I had installed to make my application run. In the console I simply typed in pip3 freeze > requirements.txt.
3. Creating a Procfile which is tells Heroku what command to run to make my app work. Mine simply says web: web: gunicorn the_james_master.wsgi:application
4. Connect GitHub to Heroku. I found it much easier to go to the deploy menu on Heroku and connect it directly to my GitHub account so that when I pushed my code, it automatically deployed to Heroku.
*NOTE: I must also make sure DEBUG = False in settings.py*
If there are any problems with deployment there will be a log of the error created which you can view on the Heroku dashboard.

### AWS
I also used AWS to store static and media files. To do this I followed the following steps.
1. After creating an account, I opened up S3 and created a new bucket, choosing the region closest to me, making sure to uncheck the box that blocks all public access
2. On the properties tab I turned on static website hosting with generic index and error document values.
3. On the permissions tab I pasted in this CORS configuration
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
4. I then generated a security policy for this bucked which is the s3 bucket policy, allowing all principles. Before copying it over I added /* to the end of the Resource section to allow access to all resources.
5. On the Access Control List I made sure to give list ibexes access to everyone.
6. Searching for IAM I created a group called manage-the-james-master
7. I then created a policy by importing an S3 full access policy but pasting in the bucket ARN into the resource section, adding in a second line with the same ARN but with a /* afterwards.
8. On the groups tab I then attached the policy to the group I had created in step 6.
9. On the users page I clicked Add User, gave them programmatic access and then put the user into the group created. I then downloaded the CSV and added those credentials into the Heroku app Config Variables.
10. To connect AWS to django I installed django-storages and boto3. In settings I added AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY with a link to the config variables. Also I needed to add a custom domain AWS_S3_CUSTOM_DOMAIN, so that django knows to look at S3 for media and static files.


### Cloning the project
If you wish to clone the project to expand the ideas created there are a number of different ways to do this

#### GitHub
* To manually download it you can go to my GitHub repo and upload it to your IED of choice.
* Install the requirements.txt by typing in pip3 install -r requirements.txt.
* You will also need to update the environment variables before you run the app with your own, especially for STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET and your own SECRET_KEY.
Once done you can run Play Park Pubs by typing python3 manage.py runserver

#### CLI
* Type the following into the CLI gh repo clone JDBennison/the-james-master
* Install the requirements.txt by typing in pip3 install -r requirements.txt.
* You will also need to update the environment variables before you run the app with your own, especially for STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET and your own SECRET_KEY.
Once done you can run Play Park Pubs by typing python3 manage.py runserver


## Credits

### Content
* The text was written by James Bennison unless stated otherwise.
* The blog post "Adventure Hooks" was inspired by a [Reddit Post](https://www.reddit.com/r/DnD/comments/9adid0/50_adventure_hooks_to_steal_for_your_game/) by /DreadTheBard

### Media
* The photos used in this site were obtained from pixabay.