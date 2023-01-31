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
* Email notifications
When someone books a session or leaves a comment on the blog I would like to have email notifications to all superusers so that they can follow up and action them accordingly.

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
The appropriate validators have been used with no warnings for HTML, CSS, Javascript and Python. Manual testing was used extensively with there being no dead links.
With the various forms the testing went as follows
1. Contact Form
	i. An empty form will not submit
	ii. Emails that aren't the correct format will not submit
	iii. Empty fields that are not required will not submit
	iv. When submission occurs with valid input fields, the form is sent and a success message appears.
2. Subscribe Form
	i. An empty form will not submit
	ii. Emails that aren't the correct format will not submit
	iii. When submission occurs with valid input fields, the form is sent and a success message appears.
3. Blog Comments
	i. An empty form will not submit
	ii. Emails that aren't the correct format will not submit
	iii. Empty fields that are not required will not submit
	iv. When submission occurs with valid input fields, the form is sent and a success message appears.
4. Booking Form
	i. An empty form will not submit
	ii. Emails that aren't the correct format will not submit
	iii. Empty fields that are not required will not submit
	iv. Form will submit with empty comment section (the only non required field)
	v. When details are saved from profile, they are carried through as long as the user is logged in.
	vi. When submission occurs with valid input fields, the form is sent and it carries through the information to the checkout page.
5. Checkout Form
	i. Wont submit without valid card details.
	ii. Error messages are displayed correctly below the stripe input.
	iii. Loading overlay is properly displayed whilst loading.
	iv. Confirmation message is displayed when valid card details are submitted.

Different screen sizes automatically resize the content with no problems. The only problem is with iOS safari browsers which don't display the fixed background properly. This isn't a huge problem however as it is still readable and stylistically doesn't distract from the aesthetic of the app.

In regards to the user stories
### Home Page
1. All services are displayed on the home page and on the booking page and clicking on the navbar "services" link takes you straight to correct location.
2. The contact form is on the home page and there is a functioning link in the footer to take you to that part of the site.
3. There is a section on the home page regarding this and clicking on the navbar "Meet The DM" link takes you straight to correct location.
4. The Navbar is available on all pages and takes you to every part of the site, meaning that the user should never need to use the back button.
5. The blog links work and a small preview of the blog is displayed on the main page.
6. The link to the FAQ page is visible in the navbar on all pages.
### Blog
7. There is a variety of blog posts with more on the way.
8. See above
9. The search bar is visible on all blog pages and will let users search for keywords in the titles and the content of the blog itself.
10. Each blog has a space to leave comments and superusers have control over moderating the comments before they are posted.
11. Blog posts are easily addable through the admin page and have the option of saving it as a draft without it being posted to the page.
12. Images are easily uploaded through the admin page however only one per blog.
### Booking
13. Availability is visible through the dropdown which automatically updates when one is booked or is deleted manually from the admin page by a superuser.
14. Was no longer relevant by the time the app was complete. However a summary of the booking is displayed before a customer pays through stripe.
15. Was no longer relevant by the time the app was complete. However there is a back button so customers do not have to commit to the booking before paying if they have click the wrong date or service by accident.
16. Payment is available through stripe simply and easily.
17. Emails are sent out with details when the booking is confirmed
18. I use the Stripe service which is safe and secure.
19. Basic details are save to the profile which are then automatically put into the booking form.
20. Superusers can input the dates and times they are available on the admin site easily.
21. All the bookings are stored on the admin side of things.
### Profile
22. Bookings are easily visible on the admin page with a link to the user and the comments they have left also.
23. Contact details are easily updatable on the profile page.
24. Signing up is simple with allauth and visible on all pages.
25. Login and Log Out is also simple with allauth and visible on all pages.
26. On the login page, it is simple to recover your password with allauth.
27. There is an email verification system built in to allauth and personalised by me.
28. The subscribe option is available on all pages in the footer and is very easy and quick to use.

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
* The blog post "Adventure Hooks" was inspired by a [Reddit Post](https://www.reddit.com/r/DnD/comments/9adid0/50_adventure_hooks_to_steal_for_your_game/) by /DreadTheBard.

### Media
* The photos used in this site were obtained from pixabay.



