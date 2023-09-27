# Instructions to run api-restaurants on local environment

- Clone the repository and enter in the folder of the project.
- Install python if not it's installed.
- Install virtualenv if not it's installed, to create virtual environments and install the correspondind dependencies.
- Create and activate the virtual environment using these commands: **virtualenv venv** to create the virtual environment (for convention use **venv** to name it) and this command **source /venv/bin/activate** on Linux or Mac, for Windows the command is **source /venv/Scripts/activate** to activate the virtual environment.
- Once the virtual environment is activated, run this command: **pip install -r requirements.txt** to install the corresponding dependencies.
- Once the dependencies are installed, one of them is the Flask microframework, you can use the command: **flask run** to run the application.
- You can test the API in Postman by copying the URL shown when running the command from the previous step and adding it to the end:
    -- **/restaurants/** to get all restaurants [GET]. 
    -- **/restaurants/851f799f-0852-439e-b9b2-df92c43e7672** to get information of a restaurant by id [GET].
    -- **/restaurants/** to create a restaurant [POST].
    -- **/restaurants/851f799f-0852-439e-b9b2-df92c43e7672** to update information of a restaurant [PUT].
    -- **/restaurants/851f799f-0852-439e-b9b2-df92c43e7672** to delete a restaurant [DELETE].
    -- **/restaurants/state/Sinaloa** to get information of the restaurants by state [GET].
    -- **/restaurants/state/Sinaloa/rating/4** to get information of the restaurants by state and rating [GET].
    -- **/restaurants/rating/4** to get information of the restaurants by rating [GET].
    -- **/restaurants/statistics?latitude=19.4373070507688&longitude=-99.1321159016228&radius=10** to get information about a specific zone (latitude, longitude and radius are passing as parameters).
    -- The id, state, rating, latitude and longitude are in the CSV file.
