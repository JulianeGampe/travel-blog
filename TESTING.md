## Testing 

## Manual Testing

### Testing User Stories

The website functionality with all user stories has been tested manually while logged in as testusers, site owner/admin and while not logged in. Additional tests from the user perspective have been made by a friend who created a user account for themselves. 

1. As a user I can see the homepage so that I know at first glance what the website is about.
    ![Instructions](documentation/screenshots/homepage.png)
2. As a user I can find out more about the site owner so that I will gain some background information.
    ![Instructions](documentation/screenshots/aboutme.png)
3. As a user I can see contact information so that I can get in touch with the site owner.
    ![Instructions](documentation/screenshots/contact.png)
4. As a user I can see the blog posts so that I can read about the travel journey.
    ![Instructions](documentation/screenshots/blog.png)
5. As a user I can register for an account so that I can comment and like posts.
    ![Instructions](documentation/screenshots/signup.png)
    - The signup was tested with testaccounts.
    - It is not possible to sign up with missing or incorrect fields.
      ![Instructions](documentation/screenshots/signuptest.png)
    - After sign up the user can login. All necessary fields have to be filled correctly.
      ![Instructions](documentation/screenshots/signintest.png)  
    - When signed in the logout option appears and logout is possible.
      ![Instructions](documentation/screenshots/logouttest.png)
6. As a user I can leave a comment to a post so that I can share my opinion and make travel suggestions.
    ![Instructions](documentation/screenshots/commentslogin.png)
    - Leaving comments was tested with testaccounts.
    - It is not possible to submit an empty comment.
    - The comment is not published immediately, but has to be approved by the admin first.
      ![Instructions](documentation/screenshots/commentstest.png)      
      ![Instructions](documentation/screenshots/messagestwo.png)
7. As a user I can edit my comment so that I have the possibility to update my comment.
    - Editing comments was tested with testaccounts.
    - It is not possible to edit comments of other users.
    - After editing the comment has to be approved by the admin before beeing published.
      ![Instructions](documentation/screenshots/commentsedittest.png)
      ![Instructions](documentation/screenshots/commentsedittesttwo.png)
8. As a user I can delete my comment so that I am able to remove a comment I don´t want to be visible any longer.
    - Deleting comments was tested with testaccounts.
    - It is not possible to delete comments of other users.
      ![Instructions](documentation/screenshots/commentsedittest.png)
      ![Instructions](documentation/screenshots/commentsdeletetest.png) 
9. As a user I can like a post so that I can show if I liked the content of the post.
    - Liking posts was tested with testaccounts.
    - Liking a post is only possible when logged in.
      - Post Detail not logged in:
      ![Instructions](documentation/screenshots/likesnotlogin.png)
      - Post Detail logged in:     
      ![Instructions](documentation/screenshots/likestest.png)   
10. As a user/site owner I can see the comments so that I can read the conversation.
    - All approved comments can be seen, even when not logged in.
    - Comments can not be edited or deleted when not logged in.
      ![Instructions](documentation/screenshots/commentsnotlogin.png)    
11. As a user/site owner I can see the likes for each post so that I know which post is very popular.
    - Likes can be seen when not logged in: On the blog page and on the blog details page.
    - Liking a post is only possible when logged in.
      - Main blog page:
      ![Instructions](documentation/screenshots/postoverview.png) 
      - Post Detail not logged in:
      ![Instructions](documentation/screenshots/likesnotlogin.png)
      - Post Detail logged in:     
      ![Instructions](documentation/screenshots/likestest.png)  
12. As a user/site owner I can see a message after I have left a comment/created a post on the frontend so that I know that the comment/post was successfully generated.
      ![Instructions](documentation/screenshots/messagestwo.png)
      ![Instructions](documentation/screenshots/messagesthree.png)
13. As a site owner I can create, read and update my posts so that I can manage my travel blog appropriately.
    - Admin backend panel:
      ![Instructions](documentation/screenshots/adminbackend.png)
    - Creating, updating and deleting posts is also possible from the frontend, when logged in as admin.
    - The admin backend panel should therefore only be used for maintainance. 
14. As a site owner I can create, update and delete my posts from the frontend so that I do not need use the admin tool.
    - When logged in as admin the "admin" page is accessible.
      ![Instructions](documentation/screenshots/navigationbar.png)
    - Creating and updating posts has been tested with the admin account.
    - Posts can only be created with all necessary fields filled in and only with valid data.
      ![Instructions](documentation/screenshots/adminpostcreatetest.png)
      ![Instructions](documentation/screenshots/adminpostcreatetesttwo.png)
    - When logged in as admin the edit and delete buttons are available for the posts and posts can be edited and deleted.
      ![Instructions](documentation/screenshots/adminpostedit.png)
      ![Instructions](documentation/screenshots/adminposteditdetail.png)
      ![Instructions](documentation/screenshots/adminpostdelete.png)
15. As a site owner I can create drafts so that I don't have to publish the post immediately and can finish it later.
    - When creating a post the status "draft" can be selected.
    - Drafts are appearing on the blog page, when the admin is logged in.
      ![Instructions](documentation/screenshots/adminpostcreatetest.png)
      ![Instructions](documentation/screenshots/blogadmin.png)
16. As a site owner I can approve or disapprove comments so that I can filter out questionable comments.
      ![Instructions](documentation/screenshots/adminbackendcomments.png)
      - Approving and deleting comments is possible from the frontend admin page as well.
      - The admin backend panel should therefore only be used for maintainance.
17. As a site owner I can approve comments from the frontend so that I don't have to use the admin tool.
    - When logged in as admin the "admin" page is accessible.
      ![Instructions](documentation/screenshots/navigationbar.png)
    - User comments appear here. New comments can be approved or deleted.
    - Already approved comments can be seen as well, with the option to delete.
      ![Instructions](documentation/screenshots/admintwo.png)

### Javascript
- JavaScript
  - JavaScript was used for the time out function of django contrib messages.
    - This was tested manually. The messages displayed dissappear automatically.
    - The code for the message timeout function and template display has been taken from [Code Institute Django3blog](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/12_final_deployment/templates/base.html)

    ![Timeout](documentation/testing/js/jstimeoutfunction.png)

  - JavaScript was used to initiate the TinyMCE editor. 
    - This was tested manually as well. The editor works on the local and deployed site.
    - The code template was found in the [Tiny Docs Quick Start](https://www.tiny.cloud/docs/quick-start/) 

    ![TinyMCE](documentation/testing/js/jstinymceinit.png)

  - JavaScript was used to convert the post title into the slug format when creating posts on the frontend.
    - This was tested manually. The slug field is automatically populated with the post title.
    - This article from [Stackoverflow](https://stackoverflow.com/questions/1053902/how-to-convert-a-title-to-a-url-slug-in-jquery/1054862#1054862) was used to create the code.

    ![Slug](documentation/testing/js/jsslug.png)

### Browser Compatibility

- The page has been tested and works in different browsers.
  - Google Chrome
    ![Google Chrome](documentation/screenshots/googlechrome.png)
    ![Google Chrome Mobile](documentation/screenshots/googlechromemobile.png)

  - Firefox
    ![Firefox](documentation/screenshots/firefox.png)
    ![Firefox Tablet](documentation/screenshots/firefoxtablet.png)
  
  - Microsoft Edge
    ![Microsoft Edge](documentation/screenshots/microsoftedge.png)
    ![Microsoft Edge Mobile](documentation/screenshots/microsoftedgemobile.png)

### Responsiveness

- The project is responsive and functions on all standard screen sizes using the devtools device toolbar.

- The navigation, home page, blog page, about me page, contact page, sign up page, login page, logout page, admin page and the footer are readable and easy to understand.

  -  Google Chrome Desktop

    ![Google Chrome](documentation/screenshots/googlechrome.png)

  - Google Chrome Mobile

    ![Google Chrome Mobile](documentation/screenshots/googlechromemobile.png)

  - Firefox Desktop

    ![Firefox](documentation/screenshots/firefox.png)

  - Firefox Tablet

    ![Firefox Tablet](documentation/screenshots/firefoxtablet.png)
  
  - Microsoft Edge Desktop

    ![Microsoft Edge](documentation/screenshots/microsoftedge.png)
  
  - Microsoft Edge Mobile

    ![Microsoft Edge Mobile](documentation/screenshots/microsoftedgemobile.png)

## Color Testing

- All colors have been tested with a contrast checker. 
  - Contrast test #7EB6D9 against #000000. (main background color against font color)
  ![Adobe Color Test Light Blue](documentation/screenshots/contrastcheck.png)
  - Contrast test #D9C6B0 against #000000. (header and footer background color against font color)
  ![Adobe Color Test Light Brown](documentation/screenshots/contrastchecksecondcolor.png)
  - Contrast test #446EA6 against #FFFFFF. (button background color against font color)
  ![Adobe Color Test Dark Blue](documentation/screenshots/contrastcheckthirdcolor.png)

## Validator Testing 

- PEP8

  - No errors were returned from [PEP8online.com](http://pep8online.com/).

    <details>
    <summary>Click to expand to view the PEP8 testing</summary>
 
      - aboutme app

        urls.py
        
        ![urls.py](documentation/testing/pep8/aboutme/pep8aboutmeurls.png)

        views.py

        ![views.py](documentation/testing/pep8/aboutme/pep8aboutmeviews.png)

      - comments app

        admin.py

        ![admin.py](documentation/testing/pep8/comments/pep8commentsadmin.png)

        forms.py

        ![forms.py](documentation/testing/pep8/comments/pep8commentsforms.png)

        models.py

        ![models.py](documentation/testing/pep8/comments/pep8commentsmodels.png)

        urls.py

        ![urls.py](documentation/testing/pep8/comments/pep8commentsurls.png)

        views.py

        ![views.py](documentation/testing/pep8/comments/pep8commentsviews.png)

      - contact app

        urls.py

        ![urls.py](documentation/testing/pep8/contact/pep8contacturls.png)

        views.py

        ![views.py](documentation/testing/pep8/contact/pep8contactviews.png)

      - home app

        urls.py

        ![urls.py](documentation/testing/pep8/home/pep8homeurls.png)

        views.py

        ![views.py](documentation/testing/pep8/home/pep8homeviews.png)

      - posts app

        admin.py

        ![admin.py](documentation/testing/pep8/posts/pep8postsadmin.png)

        forms.py

        ![forms.py](documentation/testing/pep8/posts/pep8postsforms.png)

        models.py

        ![models.py](documentation/testing/pep8/posts/pep8postsmodels.png)

        urls.py

        ![urls.py](documentation/testing/pep8/posts/pep8postsurls.png)

        views.py

        ![views.py](documentation/testing/pep8/posts/pep8postsviews.png)

      - profile app

        forms.py

        ![forms.py](documentation/testing/pep8/profile/pep8profileforms.png)

        urls.py

        ![urls.py](documentation/testing/pep8/profile/pep8profileurls.png)

        views.py

        ![views.py](documentation/testing/pep8/profile/pep8profileviews.png)

      - main app travelblog

        urls.py

        ![urls.py](documentation/testing/pep8/travelblog/pep8travelblogurls.png)

    </details>

- HTML

  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)

    <details>
    <summary>Click to expand to view the HTML testing</summary>

      - About Me 

        [aboutme W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Faboutme%2F)

        ![aboutme](documentation/testing/html/aboutme/htmlaboutme.png)
      

      - Comments 
        
        comments.html

        [comments W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Fcomments%2Farena-di-verona%2F)

        ![comments](documentation/testing/html/comments/htmlcomments.png)
        

        comments_delete.html

        Propper authentication needed to access this page.

        ![comments_delete](documentation/testing/html/comments/htmlcommentsdelete.png)
        

        comments_edit.html

        Propper authentication needed to access this page.

        ![comments edit](documentation/testing/html/comments/htmlcommentsedit.png)
        
      
      - Home

        [home W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2F)

        ![homepage](documentation/testing/html/home/htmlhome.png)
        

      - Contact

        [contact W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Fcontact%2F)

        ![contact](documentation/testing/html/contact/htmlcontact.png)
      

      - Posts

        posts_delete.html
        
        Propper authentication needed to access this page.

        ![posts_delete](documentation/testing/html/posts/htmlpostsdelete.png)


        posts_edit.html

        Propper authentication needed to access this page.

        ![posts_edit.html](documentation/testing/html/posts/htmlpostsedit.png)

        
        posts.html

        [posts W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Fposts%2F)

        ![posts](documentation/testing/html/posts/htmlposts.png)
        

      - Profile

        approve.html

        Propper authentication needed to access this page.

        ![approve](documentation/testing/html/profile/htmlapprove.png)


        profile.html

        Propper authentication needed to access this page.

        ![profile](documentation/testing/html/profile/htmlprofile.png)


      - Account

        login.html

        [login W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Faccounts%2Flogin%2F)

        ![login](documentation/testing/html/account/htmllogin.png)


        signup.html

        [signup W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Faccounts%2Fsignup%2F)

        ![signup](documentation/testing/html/account/htmlsignup.png)


        logout.html

        [logout W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Faccounts%2Flogout%2F)  

        ![logout](documentation/testing/html/account/htmllogout.png)


    </details>

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ftravelblogproject.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

      ![CSS validation](documentation/testing/css/cssvalidation.png)

- JavaScript
  - No errors were found when passing through [JSHint](https://jshint.com/)
  ![Timeout](documentation/testing/js/jstimeoutfunction.png)
  ![TinyMCE](documentation/testing/js/jstinymceinit.png)
  ![TinyMCE](documentation/testing/js/jsslug.png)

- Accessibility
  - The page passes the accessibility test using lighthouse in devtools

    ![Lighthouse](documentation/screenshots/lighthouse.png)

## Bugs
### Fixed Bugs

The following bugs were tracked and fixed using the GitHub Issues tracker with the label of "bug".

[GitHub Issues Tracker Closed Issues](https://github.com/JulianeGampe/travel-blog/issues?q=is%3Aissue+is%3Aclosed)

- **ValueError at /second-test-post/** - [#1](https://github.com/JulianeGampe/travel-blog/issues/14)
- **Paragraph tags visible in posts** - [#2](https://github.com/JulianeGampe/travel-blog/issues/17)
- **No approval needed for comments** - [#3](https://github.com/JulianeGampe/travel-blog/issues/18)
- **Delete comment not possible when "name" spelled incorrectly** - [#4](https://github.com/JulianeGampe/travel-blog/issues/20)
- **Cancel Deletion of Comment: DoesNotExist at /delete/ --- Post matching query does not exist.** - [#5](https://github.com/JulianeGampe/travel-blog/issues/21)
- **Approval button for comments on frontend does not work** - [#6](https://github.com/JulianeGampe/travel-blog/issues/25)
- **ConnectionRefusedError at /accounts/signup/** - [#7](https://github.com/JulianeGampe/travel-blog/issues/26)
- **Image upload not working from Frontend** - [#8](https://github.com/JulianeGampe/travel-blog/issues/27)
- **Uncaught TypeError: Cannot read properties of null** [#9](https://github.com/JulianeGampe/travel-blog/issues/29)

### Remaining Bugs

- No remaining bugs that I am aware of.

---

Return to the [README](README.md) file