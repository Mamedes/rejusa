<h1>Get the code </h1>
<h3> cd flaskProject-rejusa</h3>

Virtualenv modules installation (Windows based systems)
virtualenv env
.\env\Scripts\activate

Install modules - SQLite Database
pip3 install -r requirements.txt

Set the FLASK_APP environment variable

(Windows) set FLASK_APP=run.py


Set up the DEBUG environment

(Windows) set FLASK_ENV=development

Start the application (development mode)
 --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
--port=5000    - specify the app port (default 5000)  
flask run --host=0.0.0.0 --port=5000
