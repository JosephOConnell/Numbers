# NUMBERS

![Numbers](https://github.com/JosephOConnell/Numbers/blob/main/images/numbers.png)

## About Numbers
Numbers is a great way to help get kids into maths and using some basic logic.
This game is built for children who are at the age of learning basic math.
It has a maths game that gives 5 questions with random numbers that focuses on basic math questions in four topics "Addition, Subtraction, Multiplicat and Division". 
It also has a higher or lower game that helps users use logic to guess the correct number but also brings a bit of fun when comparing scores with parents.
Then to finish it off I have some fun 17 facts about numbers just for a bit of ectra knowledge.

![Thanks You](https://github.com/JosephOConnell/Numbers/blob/main/images/thanks.png)

- **random_maths_quiz**
  - The random math quiz consists of four topics:
   - Addition: This operation is used when you want to find the total, or sum, of two or more amounts.
   - Subtraction: This operation is used when you want to find the difference between two amounts or how much of something you have left after a quantity is used. For example, if you want to find the change owed after spending an amount of money.
   - Division: Division is used when sharing or grouping items. For example, if you want to know how many doughnuts you can buy with €6 if one doughnut costs €1.50, you would do €6 ÷ €1.50.
   - Multiplication : This operation is also used for totals and sums but when there is more than one of the same number. For example if you are buying five packs of apples that cost £1.20 each, you would do 5 * €1.20.
  
  ![Random Math Quiz](https://github.com/JosephOConnell/Numbers/blob/main/images/maths.png)
  ![Addition](https://github.com/JosephOConnell/Numbers/blob/main/images/addition.png)
  ![Subtraction](https://github.com/JosephOConnell/Numbers/blob/main/images/subtraction.png)
  ![Multiplication](https://github.com/JosephOConnell/Numbers/blob/main/images/multiply.png)
  ![Division](https://github.com/JosephOConnell/Numbers/blob/main/images/division.png)

- **higher_lower** 
  - The Higher-Lower game is a simple guessing game where the player tries to guess a randomly chosen number within a specified range.
  - The range in this game is between 1 and 50.
  - The object of the game is to guess the correct number in the lowest amount of tries.

  ![Higher Lower](https://github.com/JosephOConnell/Numbers/blob/main/images/higher-lower.png)

- **number_facts**
  - Number facts is a collect of 17 Facts about Numbers.
  - We have spreadsheet set up on Google Sheets API that is used for the backend.
  - The Google Sheets API allows us to pull the values from the sheet and post it to the terminal.

  ![Number Facts](https://github.com/JosephOConnell/Numbers/blob/main/images/facts.png)

- **Flowcharts**
    - Simple Maths Flowchart
    ![Simple Maths Flowchart](https://github.com/JosephOConnell/Numbers/blob/main/images/simplemaths_flowchart.png)
    - Higher or Lower Flowchart
    ![Higher / Lower Flowchart](https://github.com/JosephOConnell/Numbers/blob/main/images/higherlower_flowchart.png)
    - Number Facts Flowchart
    ![Number Facts Flowchart](https://github.com/JosephOConnell/Numbers/blob/main/images/numberfacts_flowchart.png)

### Testing

| **TEST**                            | **ACTION**                                       | **EXPECTATION**                                              | **RESULT**        |
| ----------------------------------- | ------------------------------------------------ | ------------------------------------------------------------ | ----------------- |
| main() | Choose each of the 4 options | Brings me to the selected function | Pass |
| exit_terminal() | When pickedn | Should call the thank you message and exit out of the terminal | Pass |
| play_again() | When picked | Brings you back to the main menu | Pass |
| number_facts() | When picked | Will bring up number facts and ask do you want another | Pass |
| Google Sheets | Call the info of google sheet | Number facts show on the terminal | Pass |
| higher_lower() | When picked | Brings you to the higher lower game | Pass |
| random_maths_quiz() | Choose each of the 4 options | Brings me to the selected function | Pass |
| addition() | When picked | 5 Addition maths questions | Pass |
| subtraction() | When picked | 5 Subtraction maths questions | Pass |
| multiplication() | When picked | 5 multiplication maths questions | Pass |
| division() | When picked | 5 division maths questions | Pass |
| try/except | Press wrong number, symbol or letter | Brings user back to the choices | Pass |


**CI Python Linter**
- I checked my code on the Code Institiute Python Linter and had no errors returned.
- [CI Python Linter](https://pep8ci.herokuapp.com/)
![Linter](https://github.com/JosephOConnell/Numbers/blob/main/images/linter.png)

### Unfixed Bugs
- As of now I have one bug.
 - Not all the text is cleared from the terminal.

### Deployment
- **Deploying on Heroku**
    - Visit the Heroku site and create an account
    - Click the "New" Button
    - Provide a name for the app in the App name input field
    - Select your region from the choose region dropdown menu
    ![New Account](https://github.com/JosephOConnell/Numbers/blob/main/images/create-new.png)
    - Click the "Create App" button
    ![App Name](https://github.com/JosephOConnell/Numbers/blob/main/images/app-name.png)
    - Once redirected, proceed to the settings tab
    - Click on the "config vars" button
    ![Settings](https://github.com/JosephOConnell/Numbers/blob/main/images/settings.png)
    - Supply a KEY of PORT and it's value of 8000. The click the "add" button
    ![Buildpacks](https://github.com/JosephOConnell/Numbers/blob/main/images/buildpacks.png)
    - Next step is to add Buildpacks, click the "Add Buildpack" button
    - The python buildpack needs to be added first then the nodejs buildpack
    ![GitHub Deploy](https://github.com/JosephOConnell/Numbers/blob/main/images/github-deploy.png)
    - Once the buildpacks have completed, go to the deploy screen, once in the deploy screen, select GitHub as the deployment method and connect your GitHub profile
    ![Deploy](https://github.com/JosephOConnell/Numbers/blob/main/images/deploys.png)
    - Search for the repository that you wish to deploy to Heroku and click "connect"
    - Once your repository is connected to Heroku you can choose to either manually or automatically deploy your app.
    - By selecting automatic deploys, Heroku will build a new version of the app each time a change has been pushed to the repository
    - If your build is successful you will then be able to visit the live site by clicking the link that is provided to you by Heroku
    - Command to add packages to requirements.txt, pip3 freeze --local > requirements.txt

- **Google Sheets API**
    - Create or log in to your Google account.
    - Open [Google Sheets](https://docs.google.com/spreadsheets/d/1__ltkTdQJLYQHurtllcTy11LKDLcOEcVVGFX2uUldPQ/edit#gid=0).
    - Name your doc as per your requirement.
    - Open [Google Cloud](https://console.cloud.google.com/welcome?project=numbers-400819).
    - Now you need to create a New Project.
    - When the project is set up go to API's and Services
    - We need to go to API Library. Find google drive and enable it.
    - Next find click on the Create Credentials.
    ![Credentials](https://github.com/JosephOConnell/Numbers/blob/main/images/creds.png)
    ![cred type](https://github.com/JosephOConnell/Numbers/blob/main/images/creds-type.png)
    ![Service Account](https://github.com/JosephOConnell/Numbers/blob/main/images/service_name.png)
    ![Account Details](https://github.com/JosephOConnell/Numbers/blob/main/images/access.png)
    ![Manage](https://github.com/JosephOConnell/Numbers/blob/main/images/manage.png)
    ![Keys](https://github.com/JosephOConnell/Numbers/blob/main/images/keys.png)
    ![JSON File](https://github.com/JosephOConnell/Numbers/blob/main/images/json.png)
    - Next we have to go back to API Library, find Google Sheets and enable it.

The live link can be found here - [Numbers](https://numbers-game-8b4eba16a846.herokuapp.com/)


### Content and Media Credits

- **CREDITS**
  - [Code Institute](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master)
  - [Stack Overflow](https://stackoverflow.co/)
  - [Bro-Code](https://www.youtube.com/watch?v=XKHEtdqhLK8)
  - [pypi](https://pypi.org/project/pyfiglet/)
  - [PYnative](https://pynative.com/python-random-choice/)
  - [geeksforgeeks](https://www.geeksforgeeks.org/python-remove-square-brackets-from-list/)
  - [OpenLearn](https://www.open.edu/openlearn/mod/oucontent/view.php?id=87283&section=_unit2.1#:~:text=The%20four%20operations%20are%20addition%2C%20subtraction%2C%20multiplication%20and%20division.)