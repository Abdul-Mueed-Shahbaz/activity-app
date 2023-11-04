# Activity-App

## Backend: activity_api
### Make sure to have Python installed

### *Creating and Activating a Python Virtual Environment

1. **Open a Terminal:**
   - Open your terminal or command prompt.

2. **Navigate to Your activity_api:**
   - Use the `cd` command to navigate to the directory where you want to create the virtual environment.
   ```bash
   cd /path/to/your/project/activity_api
   
3. **Create a Python Virtual Environment:**
    ```
    python -m venv <env-name>
    ```

4. **Activate the Virtual Environment:**
    ```
    <env-name>\Scripts\activate
    ```

### *Installing required packages
```
pip install -r requirements/bast.txt
```
### *Running Migrations
```
python manage.py migrate
```
### *Staring Server
```
python manage.py runserver
```

## Frontend: activity_gui
### Make sure to have the node installed
### *Installing Packages
```
npm i
```
### *Starting App Locally
```
npm run serve
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
