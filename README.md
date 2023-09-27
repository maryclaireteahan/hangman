# HANGMAN
- [INTRODUCTION](#introduction)
- [USER EXPERIENCE UX](#user-experience-ux)
  * [USER STORIES](#user-stories)
- [SCOPE](#scope)
- [STRUCTURE](#structure)
- [FLOWCHART](#flowchart)
- [FEATURES](#features)
  + [EXISTING FEATURES](#existing-features)
  + [FUTURE FEATURES](#future-features)
- [LANGUAGES USED](#languages-used)
- [TECHNOLOGIES USED](#technologies-used)
- [DATA STORAGE](#data-sorage)
- [BUGS OR ERRORS](#bugs-or-errors)
- [UNFIXED BUGS](#unfixed-bugs)
- [TESTING](#testing)
- [MANUAL TESTING](#manual-testing)
- [DEPLOYMENT](#deployment)
- [CREDITS](#credits)
- [ACKNOWLEDGEMENTS](#acknowledgements)


## INTRODUCTION

In HANGMAN the player's objective is to guess the hidden word. The player has 10 lives to guess the word. If the player guesses a letter present in the word the letter will appear in the word section and they will move on to their next guess. If the player guesses a letter that is not present in the word they will lose one life and the Hangman starts to be built. Each incorrect letter brings the hangman closer to being built. If all the lives are spent before the word is guessed, the hangman is fully built and the player loses the game. If the player guesses the word before the lives are spent they win the game.

![alt-text](assets/images/readme/start.png)

[The live project can be viewed here](https://maryclaireteahan-hangman-1cf25dd2c58c.herokuapp.com/)




## USER EXPERIENCE UX
### USER STORIES

As a general user, I want to:
1. Easily navigate through the game
2. Be able to understand the rules of the game.
3. See the correctness of the validation of my input values.
4. Be able to see what letters I have already selected.
5. Be able to see how many lives I have left


During the design, tests were carried out to try out visuals and initial features before establishing the final project repository.
## SCOPE
The project scope follows the minimal viable features approach for the initial project. However the scope is such that interactive features to enhance the user experience will be added in the future.
For the implementation of the ATM banking system I have planned the following features:
- Data from spreadsheet that contains the user's account and transactions to be displayed to the user in tables.
- Account creation starts from the beginning of the program if the user has no account.
- User account will be validated, if correct an option screen will be displayed to the user otherwise user will be referred back to create an account.
- The deposit option enables the user to add money to his/her account on passing the validation of the input data. The value of the amount, status, and date time is inserted into the transaction spreadsheet table.
- The withdraw option like the deposit option enables the user to remove money from his/her account if the amount input is valid. The amount requested by the user, status, and date time are inserted into the transactions spreadsheet table.
- The program displays warnings in all stages if input values are not given in the correct format.
- On-demand, a transaction table is displayed to the account holder if any, showing all his/her transactions with date time, amount, and status with reasons if the status is a failure.

## STRUCTURE
The user experience design is explicit, with features positioned conventionally. Navigation starts from the welcome message and intuitively exits the user if he wishes to.


### FLOWCHART
The Flowchart for my program was created using [LucidChart](https://lucid.app/lucidchart/0ea6b3ea-15d2-4224-8d87-f4cb79c1e504/edit?view_items=~A_qna7e~gO6%2CiA_qin-594Lj%2C-GCynUns-Lhk%2CWBCyDKANY6n8%2CtC_q.ugc0ykY%2C_GCyBuRiyuT8%2CUGaBpbitNrDr%2CNB_qjtwegra6%2CyN_qZtRYAS.k%2CQN_qc7A-Pjza%2C6ACyekr7hI1x%2CBO_qRQaICLUb%2CzO_qtwRH1phF%2CKO_q84z1~jpx%2CuxCyBT4_5jLN%2CRFCyzRnMuJP-%2CUO_q5KIubTSn%2CMO_qeyLKl4_R%2C2S_qwij~7oDz%2CFR_qFxsGLjv_%2C5R_q6sAcUmY5%2CMS_q.m.BR.cC%2C~S_qmapQ8_ev%2CrQ_qbucEDzrK%2CJECy.U-fqIgL%2CWACyobxv.xXf%2CVR_qYUxERad.&invitationId=inv_7aa4366a-6d4a-4551-b117-b9f5e4cd5eb2) and it visually represents how the system works.

![alt-text](assets/readme/images/flowchart.png)

## FEATURES
### EXISTING FEATURES
The program has a feature that will ease the work of bank workers by not taking the pains of registering every customer. Also, remove the hassle of customers creating accounts in banks.
For simulating a real-life experience, the system is linked to a <b>Google Spreedsheet</b> that can be accessed [here](https://docs.google.com/spreadsheets/d/19-2VbDweehojeCg4YcLQOBKUNskHD-2ef7-phK18IgQ/edit?usp=sharing).

- When the user launches the programm a welcome image is displayed with a question, if the user has an account or not.

![alt-text](assets/images/readme/start.png)
- Any input error by the user is caught and the corresponding message is displayed.

![alt-text](assets/images/readme/start_err.png)

- A no answer from the user will prompt the user to create an account.

![alt-text](assets/images/readme/account.png)

![alt-text](assets/images/readme/create_err1.png)
- A yes answer implies the user has an account and the programm will prompt the user for validation of his/credentials thrice.
If the user is unable to give correct credentials the programm returns back to start welcome question state.

![alt-text](assets/images/readme/acc_valid_err.png)

- If a user successfully logs in to the system, the option menu is displayed to the user.

![alt-text](assets/images/readme/options.png)

- If the user chooses option 3, his/her account details are displayed in a table for the user.

![alt-text](assets/images/readme/account_details.png)

- If the user chooses option 4, his/her transactions are shown on a table with the date time the transactions where made and there status.

![alt-text](assets/images/readme/transaction.png)

- If the user chooses option 1, he/she will be promted to enter the amount in figures to deposit. The transaction will be inserted to the transaction table.

![alt-text](assets/images/readme/depo_er.png)

- If the user chooses option 2, he/she will be prompted to enter the amount in figures, all errors are caught by the programm and the transaction is inserted into the transaction table.

![alt-text](assets/images/readme/withd_er.png)

- If there is an input error from the user, the programm also checks the balance of the user if there are sufficient funds and if everything is ok the user is then allowed to withdraw funds consequently with a success message.

![alt-text](assets/images/readme/withd_suc.png)


## DATA STORAGE

The data used in this project is stored in google sheet through the google api cloud platform

![alt-text](assets/images/readme/accsheet.png)

![alt-text](assets/images/readme/transheet.png)


### FUTURE FEATURES
- Implement a more modern and secure way to save user's credentials
- Enable user's to do payment of utilities(water,gas, internet, telephone, etc)
- Implement an email message sent to customers about their current account weekly.

### LANGUAGES USED
- [Python](https://www.python.org/)

### TECHNOLOGIES USED
Git was used for version control.

[Gitpod](https://github.com/Code-Institute-Org/python-essentials-template) was used as the IDE

[Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-809923745462:kwd-33511936169&km_CPC_Country=20483&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=CjwKCAiA2rOeBhAsEiwA2Pl7Q5KsmhzrrvhWJy2CYebbpJzHxt99Tj-XuCHr2wL0hH5yf4c1nGYkMhoCLYgQAvD_BwE) was used for the flowchart.

[pep8](https://pep8ci.herokuapp.com/) was used to validate the python code.

[Heroku](https://id.heroku.com/) was used to deploy the project.

### BUGS OR ERRORS
The following bug was found and squashed:

During the development process, the desire to give a good user experience was placed as the priority as a result, the code to achieve that aim was refactored several times. Finally, this was achieved, by introducing the function (do_options) and validating each user input in the (create_user) function.


### UNFIXED BUGS
There are no known outstanding bugs.


### TESTING

All the python files where tested in  [pep8](https://pep8ci.herokuapp.com/)


### MANUAL TESTING
Various users tested the atm application. Feedback was overall positive from all users.

The following functioned as intended:

- Account creation of user works correctly and inserts user credentials to google spreadsheet.
- Validation of user if prompted for credentials
- Shows a menu of options to a logged-in user
- The deposit function gives corresponding feedback depending on the user's input.
- Like the deposit function, the withdraw function also gives the corresponding feedback to the user depending on the input.
- On-demand users logged in can get details of their account or their transaction in a table.


The following were also tested and function correctly:
- Every input of users is validated, and the corresponding error/success message is displayed.
- The google spreadsheet is updated on every successful creation of an account.
- On every deposit or withdraw function call, the google spreadsheet is updated.
- The purpose of the application can be seen as the ease to create a user account.


## DEPLOYMENT
- This site was deployed by completing the following steps:
1. Log in to [Heroku](https://id.heroku.com/) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu   select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
8. Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
9. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
10. Repeat step 9 to add node.js. o, Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to GitHUB

### FORKING 
Fork this project by following the steps:
1. Open [GitHub](https://github.com/)
2. Click on the project to be forked
3. Find the Fork button at the top right of the page
4. Once you click the button the fork will be in your repository

### CLONING
Clone this project by following the steps:
1. Open [GitHub](https://github.com/)
2. On the [repository](https://github.com/Dee68/milestone_project3) click the Code green button, right above the code window
3. You will be provided with three options to choose from, HTTPS, SSH, or GitHub CLI, click the clipboard icon in order to copy the URL
4. In your IDE open Git Bash
5. Enter the command git clone followed by the copied URL
6. The project is cloned.

## CREDITS
- The code for linking to the Google Spreadsheet and manipulating it was taken and adapted from the Code Institute Love Sandwiches tutorial
- The welcome message on the start of the programm was adapted from [ASCII Art generator](https://fsymbols.com/generators/carty/)
- The word_wrap function for animating the text was adapted from [Animated text tutorial](https://www.youtube.com/watch?v=2h8e0tXHfk0)
- The bank card and bank note images from [emoji](https://getemoji.com/)


## ACKNOWLEDGEMENTS
- My mentor Jack Wachira for his extraordinary insight, constructive criticism, encouragement, and continuous vital feedback.
- My code institute facilitator Irene Neveile for keeping up with my schedules.
- Friends and colleagues that helped in testing the application.






# **Hangman**

In HANGMAN the player's objective is to guess the hidden word. The player has 10 lives to guess the word. If the player guesses a letter present in the word the letter will appear in the word section and they will move on to their next guess. If the player guesses a letter that is not present in the word they will lose one life and the Hangman starts to be built. Each incorrect letter brings the hangman closer to being built. If all the lives are spent before the word is guessed, the hangman is fully built and the player loses the game. If the player guesses the word before the lives are spent they win the game.


  - [View the Live Website Here](https://hangers.herokuapp.com/)
## Table of contents 
* [Hangman](#hangman)
    * [User Experience](#user-experience)
        * [Project Goals](#project-goals)
        * [User Stories](#user-stories)
        * [Colors](#colors)
        * [Technology Used](#technology-used)
          * [Languages](#languages)
		  * [Libraries](#libraries)
    * [Flow Chart](#flow-chart)
    * [Features](#features)
    * [Testing](#testing)
        * [Testing User Stories](#testing-user-stories)
        * [Validation Testing](#validation-testing)
        * [Bugs](#bugs)
        * [Manual Testing](#manual-testing)
    * [Future Features](#future-features)
    * [Deployment](#deployment)
    * [Credits](#credits)


## User experience

### Project Goals

- The goal is to provide the user with a game that is fun as well as challenging. The user has to have a realistic opportunity to guess the word while also being reminded of the fact they have limited lives.

### User Stories

As a user, I want to:
- Be able to easily navigate through the game
- Be able to understand the rules of the game.
- Be able to see what letters I have already selected.
- Be told when I have input the same letter a second time.
- Be told when I have input an invalid character.
- Be able to see how many lives I have left
- Be told what the word is if I can't guess it.


### Colors

- The game features a colored header in the introduction as well as colored dividers after each input.When a Y/N input is required, Y/N is in green so the user will be more likely to realise those are their optiohns. When an invalid input has been entered the error handling is returned in red to draw the user's attention to the fact they have made an error.The countdown of the lives is colored differently. Lives 10-8 are green to show the user has plenty of lives left. Lives 7-4 is yellow to show the user is starting to run low. Lives 3-0 is red to imply urgency and that the user has to be careful how they choose their letters as they are about to die.

### Technology Used

- #### Languages:

   - Python

- #### Libraries
  * [Git](https://git-scm.com/)
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
  * [GitHub](https://github.com/)
    * GitHub is used to store the project's code after being pushed from Git
  * [Heroku](https://id.heroku.com)
    * Heroku was used to deploy the live project
  * [Lucidchart](https://lucid.app/)
    * Lucidchart was used to creating the flowchart
  * [CI Python Linter](https://pep8ci.herokuapp.com/)
    * The PEP8 was used to validate all the Python code
  * [Patorjk](https://patorjk.com)
    * Patorjk (ASCII Art Generator) was used to create a banner across the game


## Flow Chart

<details><summary>Screenshots</summary>
<img src="assets/readme/images/flowchart.png">
</details>

The Flowchart for my program was created using [LucidChart](https://lucid.app/lucidchart/0ea6b3ea-15d2-4224-8d87-f4cb79c1e504/edit?view_items=~A_qna7e~gO6%2CiA_qin-594Lj%2C-GCynUns-Lhk%2CWBCyDKANY6n8%2CtC_q.ugc0ykY%2C_GCyBuRiyuT8%2CUGaBpbitNrDr%2CNB_qjtwegra6%2CyN_qZtRYAS.k%2CQN_qc7A-Pjza%2C6ACyekr7hI1x%2CBO_qRQaICLUb%2CzO_qtwRH1phF%2CKO_q84z1~jpx%2CuxCyBT4_5jLN%2CRFCyzRnMuJP-%2CUO_q5KIubTSn%2CMO_qeyLKl4_R%2C2S_qwij~7oDz%2CFR_qFxsGLjv_%2C5R_q6sAcUmY5%2CMS_q.m.BR.cC%2C~S_qmapQ8_ev%2CrQ_qbucEDzrK%2CJECy.U-fqIgL%2CWACyobxv.xXf%2CVR_qYUxERad.&invitationId=inv_7aa4366a-6d4a-4551-b117-b9f5e4cd5eb2). It is a visual representation of how the game works.


## Features
### Welcome screen

<details><summary>Screenshots</summary>
<img src="assets/readme/images/screen/intro.png">
</details>

- Welcomes user to the game. Asks user whether or not they would like to play

### Second screen

<details><summary>Screenshots</summary>
<img src="assets/readme/images/screen/rules1.png">

</details>

- If user answered Y to the first screen they will be brought to the second screen. Here they are asked if they would like to see the rules.

### Rules screen

<details><summary>Screenshots</summary>
<img src="assets/readme/images/screen/rules2.png">
</details>

- If the user selected Y to the previous question they will be shown a list of rules for the game.

### Game screen

<details><summary>Screenshots</summary>
<img src="assets/readme/images/game_play/game_play.png">
<img src="assets/readme/images/game_play/game_play1.png">
<img src="assets/readme/images/game_play/game_play2.png">
<img src="assets/readme/images/game_play/game_play3.png">
<img src="assets/readme/images/game_play/game_play4.png">
<img src="assets/readme/images/game_play/game_play5.png">
<img src="assets/readme/images/game_play/game_play6.png">
<img src="assets/readme/images/game_play/game_play7.png">
<img src="assets/readme/images/game_play/game_play8.png">
<img src="assets/readme/images/game_play/game_play9.png">
<img src="assets/readme/images/game_play/game_play10.png">
<img src="assets/readme/images/game_play/game_play11.png">
<img src="assets/readme/images/game_play/game_play12.png">
</details>

- 

### End game screen

<details><summary>Screenshots</summary>
<img src="assets/readme/images/screen/game_win.png">
</details>
<details><summary>Screenshots</summary>
<img src="assets/readme/images/screen/game_loss1.png">
<img src="assets/readme/images/screen/game_loss2.png">

</details>

- If the user managed to guess all the letters in the word before their lives ran out they are presented with a message of congratulations and are also let know how many lives they had left. If the user doesn't guess the word before their lives run out they will be presented with a message comiserating with them while also noting the full word. The hangman will also be fully completed.

## Testing

### Testing User Stories

 - Be able to asily navigate through the game

| **Feature**  | **Action**                  | **Expected Result**                                          | **Actual Result** |
| ------------ | --------------------------- | ------------------------------------------------------------ | ----------------- |
| Welcome screen | There is a input field inquiring if the user would like to play. | Type "Y" and move closer to the game play. | It works as expected |

<details><summary>Screenshots</summary>
<img src="assets/readme/images/screen/intro.png">
</details>

- Be able to understand the rules of the game.

| **Feature** | **Action**                           | **Expected Result**                                           | **Actual Result** |
| ----------- | ------------------------------------ | ------------------------------------------------------------- | ----------------- |
| Rules screen | After the first "Y" the user is asked if they want to read the rules. The input requires either "Y" for yes or "N" for no | Type "Y" and the rules for the game are displayed. | It works as expected |

<details><summary>Screenshots</summary>
<img src="assets/readme/images/screen/rules1.png">
<img src="assets/readme/images/screen/rules2.png">
</details>

- Be able to see what letters I have already selected.

| **Feature** | **Action**                                         | **Expected Result**                            | **Actual Result** |
| ----------- | -------------------------------------------------- | ---------------------------------------------- | ----------------- |
| Game Play Screen | After each letter selection the letter is added to a list of guessed letters which is printed each round. | Each guessed letter is clearly visible after each round.| It works as expected |

<details><summary>Screenshots</summary>
<img src="assets/readme/images/game_play/game_play5.png">
</details>

- Be told when I have input the same letter a second time.

| **Feature** | **Action**                                 | **Expected Result**                                                                     | **Actual Result** |
| ----------- | ------------------------------------------ | --------------------------------------------------------------------------------------- | ----------------- |
| Game Play screen  | Input a letter that has already been guessed and is listed in the guessed letters section. | An error is printed stating that the letter has already been input. The user's lives are not effected. | It works as expected |

<details><summary>Screenshots</summary>
<img src="assets/readme/images/errors/error8_game.png">
</details>

- Be told when I have input an invalid character.

| **Feature** | **Action**                                     | **Expected Result**                                                                | **Actual Result** |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| Game Play screen | Input a character that is not a valid option i.e. anythine other than a letter from the alphabet. | A message appears telling the user that it was an invalid input. | It works as expected |

<details><summary>Screenshots</summary>
<img src="assets/readme/images/errors/error6_game.png">
</details>

- Be able to see how many lives I have left.

| **Feature** | **Action**                                     | **Expected Result**                                                                | **Actual Result** |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| Game Play screen  | Lives will decrease with each incorrect letter chosen. | The number decreases by one with each incorrect guess and the color will also change from green to yellow to read as the number decreases.| It works as expected |

<details><summary>Screenshots</summary>
<img src="assets/readme/images/game_play/game_play2.png">
<img src="assets/readme/images/game_play/game_play6.png">
<img src="assets/readme/images/game_play/game_play11.png">
</details>

- Be told what the word is if I can't guess it.

| **Feature** | **Action**                                     | **Expected Result**                                                                | **Actual Result** |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| End game screen  | Lose the game. | When the user loses the game by running out of lives before they were able to guess the word, a message will appear telling them the word.| It works as expected |


<details><summary>Screenshots</summary>
<img src="assets/readme/images/screen/game_loss1.png">
</details>


 ### Validation Testing
- Used CI Python Linter to validate my code

<details><summary>Validated code</summary>
<img src="assets/readme/images/validation.png">
</details>

 ### Bugs
| **Bug**                                                                                                         | **Fix**                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Couldn't connect function levels() to the game() function to upload difficulty level across game| Redo whole function levels() with changed while loop|
| The user name wasn't appearing across the game     | Created a global variable called name                                                                                             |
| After reading the rules for the game and playing the game user was only able to play the game twice before the error message appeared, basically, the user was stuck in  levels() function                                                  | Created a new function to ask the user if he wishes to read the rules or not, and separated rules() function from levels() function          |
| Poor visual presentation of the game   | Introduced colorama and add spacing to the print statements across the game       |
| In the levels() function user had to confirm his choice twice before he was able to continue with the game                  | Created global variable 'lives', which were later on called for the user tries instead levels() function                                                                                                   |
| After finishing thegame once user was only able to choose a difficulty level before the terminal was cut out                            | called game() function bellow levels() function in end_game() function                                                                                                    |
| Print statements from different screens were pilling up on top of each other, with user inputs and progress of the game                          | Imported os and created function which was used across the game to clear the terminal screen                                 |
| Too long lines during code                   | Run and formatted code through black.vercel.app                              |
| Game worked locally but not on Heroku app                   |  Created new excell sheet with new credentials and repeated process of connecting APIs, googleshet, heroku                           |
                                                                                                         
 ### Manual Testing
  #### Welcome screen

<details><summary>Screenshots</summary>
<img src="assets/readme_img/input_name_invalid.png">
</details>

  - I've tested that the input field for name takes only alphabet letters and nothing else and that error message is displayed to the user that warns the user of his input

 #### Decide to check the rules screen 

<details><summary>Screenshots</summary>
<img src="assets/readme_img/2nd_ivalid.png">
</details>

   - I've tested that the user is allowed to enter only letters that are displayed on the screen and that the error message is shown to the user and that those options lead the user to the screen that he chose to go to

 #### Rules screen

<details><summary>Screenshots</summary>
<img src="assets/readme_img/rules_invalid.png">
</details>

  - I've tested that user can only input the letter "P" which will take a user to the next screen, the wrong input is displayed to the user

 #### Game screen

<details><summary>Screenshots</summary>
<img src="assets/readme_img/game_invalid_character.png">
</details>
<details><summary>Screenshots</summary>
<img src="assets/readme_img/game_same_let.png">
</details>
<details><summary>Screenshots</summary>
<img src="assets/readme_img/wrondg_guess.png">
</details>

  - I've tested multiple inputs on this screen
  - If a user repeats the letter that he already guessed error message will be displayed to the user
  - If a user inputs the number or any other special character error message will be displayed to the user
  - If a user inputs is wrong error message will notify the user 

#### End game screen

<details><summary>Screenshots</summary>
<img src="assets/readme_img/end_invalid.png">
</details>

  - I've tested that the user is only allowed to input letters that are instructed on the screen and that with wrong input error message displays to user 

 #### Score screen

<details><summary>Screenshots</summary>
<img src="assets/readme_img/leader_invalid.png">
</details>

   - I've tested that user is only allowed to press letter "B" to go back to previous screen and that error message is displayed to the user if he puts wrong input

 #### Hangman game

  - I've tested that all instructions are displayed to the user and that all inputs that the user has to type will bring user to desired and expected outcome like it's displayed on the screens across the game
   - I've tested that score on the game page is with the rules of the game and that the overall score is uploaded to the google sheet and that data is printed out on the final screen if a user wishes to check the leaderboard
  - Also tested that data is presented to the user from top (best score) to the bottom

## Future Features
   - Features that I would like to add to the game would be, different categories that users can pick to guess the secret word
   - Use API services to randomly get words rather than storing them in folders
   - The user to be able to use a hint if he gets stuck
  
## Deployment
### Gitpod and git
 -  I created a repository in Github, named it Portafolio-3, and used the template Code-Institute-org/python-essentials-template
 -  Once the repository is created, click the green button to the right (Gitpod) to open Gitpod
 -  In the terminal, I've used the python3 run.py file provided by the template
 - At regular appropriate intervals the latest version of the code was saved via the git add and git commit commands. Appropriate commit messages were added to control the revisions.
- The git push command was used to push all committed code and documentation to the repository for secure storage.
 

### Heroku
This project was deployed using Code Institutes mock terminal for Heroku.

-  Log in to Heroku and click "New" and "Create new app"
-  Name the new app and click "Create new app".
-  In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list).
-  While still in "Settings", click "Reveal Config Vars" and add the following; KEY: PORT, VALUE: 8000. and
content from creds.json file
-  Click on "Deploy" and select your deploy method and search for the repository name.
-  Click "Connect" on a selected repository.
-  Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
-  Heroku will now deploy the app.

## Credits
- Code & Content
  - I give credit to [Stack overflow](https://www.stackoverflow.com/), [MDN Web Docs](https://developer.mozilla.org/en-US/) & [W3 Schools](https://www.w3schools.com/) for helping me resolve issues with Python while coding through
  - Inspiration and guidance/problem solving through project came from [kite](https://www.youtube.com/@KiteHQ), [Sanjin Dedic](https://www.youtube.com/@SanjinDedic), [Tech with Tim](https://www.youtube.com/@TechWithTim) 
   youtube channels, and [Geeksforgeeks](https://www.geeksforgeeks.org/), [Codefather](https://codefather.tech/) websites
  - Credits for code os.system('cls' if os.name == 'nt' else 'clear') that clear screen was found on [stackoverflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
  - Credits for my hangman art go to  [Ascii](https://ascii.co.uk/art/hangman)
  - To create banner for my page with title name I used [Patorjk](https://patorjk.com/)
  - Giving credit to [Lucid chart](ttps://www.lucidchart.com/) for providing tools to easily create my flow chart
  - Credits for centering my content in the terminal with the code  os.get_terminal_size().columns goes to [Geeksforgeeks](https://www.geeksforgeeks.org/)

  - The code for linking to the Google Spreadsheet and manipulating it was taken and adapted from the Code Institute Love Sandwiches tutorial
  - The welcome message on the start of the programm was adapted from [ASCII Art generator](https://fsymbols.com/generators/carty/)
  - The word_wrap function for animating the text was adapted from [Animated text tutorial](https://www.youtube.com/watch?v=2h8e0tXHfk0)
  - The bank card and bank note images from [emoji](https://getemoji.com/)


- Acknowledgment
  - Special thank you goes to mentors Narander and Jubril who helped me to finish my project
  - I would like to thank tutor support from Code Institue for their help, as well as the whole  Code Institue for giving me the opportunity to attend this course and to work on this project
  - I would also like to thank my colleagues for their support
  - Last but not least I would like to thank our coordinator Irene from Code Institute for giving guidance and schedules on daily basis in the classroom
















  