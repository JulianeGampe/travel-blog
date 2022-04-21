# Mia's Travel Adventures

Mia's travel adventures is a travel blog website of a fictitious blogger named Mia. It is targeted towards users who are interested in traveling and who would like to interact with the blogger and other users by leaving comments and liking posts. The user can find the blogposts of Mia as well as more information about the blogger and contact information. There is an option to create an account to be able to leave comments and like the posts.

For the blogger themselves an admin page is accessible after login, where the blogger can write posts and approve or delete comments.

![Responsive Mockup](documentation/screenshots/amiresponsive.png)

## User Stories



## UX
### Colour Scheme

[Color Tool](https://material.io/resources/color/#!/?view.left=1&view.right=1&primary.color=201773) and [Adobe Color](https://color.adobe.com/create/color-contrast-analyzer) have been used to find and test the colors. 

![Color Tool](documentation/screenshots/colortestone.png)

### Typography 

Google Fonts has been used to find the font, that is displayed on the website. [Cabin](https://fonts.google.com/specimen/Cabin?category=Sans+Serif&preview.text=Vocabulary%20Quiz&preview.text_type=custom#standard-styles) ....

To provide visual cues icons from [Font Awesome](https://fontawesome.com/) have been used in ....

### Wireframes

Wireframes created with Balsamiq were used to plan the layout of the website.

![Wireframe](documentation/wireframes/vocabularyquiz.png)



## Features 

### Existing Features

- __Header__

  - The main heading in the header will allow the user to see the purpose of the website.

![Header](documentation/screenshots/header.png)





- __Footer__

  - The footer will display a link to social media.
  - The user can click the icon to visit the social media website in a separate tab.

![Footer](documentation/screenshots/footer.png)

### Features Left to Implement

- __Feature 1__

  - A feature that allows....



## Technologies Used

- HTML was used to structure the website semantically and display it in the browser.
- CSS was used for the presentation and style of the website.
- CSS grid was used for the layout of the website.
- JavaScript was used to make the website interactive.
- [Balsamiq](https://balsamiq.com/wireframes/) was used to create the wireframes.
- [Gitpod](https://www.gitpod.io/) was used for the development of the website.
- [Github](https://github.com/) was used to store the code online.
- Git was used for version control.
- [hatchful](https://hatchful.shopify.com/) was used for the favicon.
- [Font Awesome](https://fontawesome.com/) was used for the icons.

## Testing

Due to the length of testing, you can see all tests in the [TESTING.md](TESTING.md) file.

## Deployment

- The site was deployed....

The live link can be found here - 

### Local Deployment

If you would like to make a local copy of this repository, you can clone it by typing the following command in your IDE terminal:
- `git clone https://github.com/JulianeGampe/vocabulary-quiz.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JulianeGampe/vocabulary-quiz)

## Credits 

### Content

- Code for .... has been taken from [w3schools](https://...)

### Media 

- The following websites were used to find the colors and do the contrast tests:
  - [Color Tool](https://material.io/resources/color/#!/?view.left=1&view.right=1&primary.color=201773)
  - [Adobe Color](https://color.adobe.com/create/color-contrast-analyzer)
- The font was found on [Google Fonts](https://fonts.google.com/)
  - [Cabin](https://fonts.google.com/specimen/Cabin?category=Sans+Serif&preview.text=Vocabulary%20Quiz&preview.text_type=custom#standard-styles)
- The icons in the quiz type buttons and footer were taken from [Font Awesome](https://fontawesome.com/)
  - [Animals Icon](https://fontawesome.com/v5.15/icons/paw?style=solid)
  - [Travel Icon](https://fontawesome.com/v5.15/icons/bus-alt?style=solid)
  - [Food Icon](https://fontawesome.com/v5.15/icons/utensils?style=solid)
  - [Instagram Icon](https://fontawesome.com/v5.15/icons/instagram?style=brands)
- [Balsamiq](https://balsamiq.com/wireframes/) was used to create the wireframes.
- [hatchful](https://hatchful.shopify.com/) was used for the favicon. 
- [Am I responsive](http://ami.responsivedesign.is/) has been used to create the responsive mockup of the project

### Acknowledgements

- I would like to thank...


Sources:

Help with Django blog/ function based view for comments

https://www.youtube.com/watch?v=m3hhLE1KR5Q
https://github.com/SteinOveHelset/codewithstein

Help with approval of comments
https://djangocentral.com/creating-comments-system-with-django/


Solution to make the name of the comments model the username:
https://stackoverflow.com/questions/65733442/in-django-how-to-add-username-to-a-model-automatically-when-the-form-is-submit

Help with confirmation of comment delete:
https://www.youtube.com/watch?v=3VBHWLFza4s

Help with {{ post.image.url }} cloudinary:
https://www.youtube.com/watch?v=1T6G7Znrbfg

Aboutme image
https://www.pexels.com/photo/a-woman-leaning-out-of-a-window-train-6761976/


Image as card background
https://www.tutorialspoint.com/Turn-an-image-into-a-Bootstrap-4-card-background


Text Center
https://mdbootstrap.com/docs/b4/jquery/utilities/horizontal-align/

Google Fonts
https://fonts.google.com/specimen/Kalam?category=Handwriting#glyphs

Upload cloudinary pictures from frontend:
https://jszczerbinski.medium.com/django-web-app-and-images-cloudinary-straightforward-study-ae8b5bb03e37

Using the tinymce widget in forms.py
https://django-tinymce.readthedocs.io/en/latest/usage.html#using-the-widget

Tinymce video
https://www.youtube.com/watch?v=l9VZlqCbiLk


messages video
https://www.youtube.com/watch?v=VIx3HD2gRWQ

messages timeout function and display



Welcome JulianeGampe,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
