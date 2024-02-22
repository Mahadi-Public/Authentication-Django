<h1>Django Authentication & CRUD Operations</h1> <br/>

<h4> Follow these commands to run this project: </h4>
<ul>
  <li>git clone https://github.com/Mahadi-Public/Authentication-Django.git  <br/>  or  <br/> git clone git@github.com:Mahadi-Public/Authentication-Django.git </li>
  <li>create a virtual environment using these commands: <br/> <b> python -m venv env  or  python3 -m venv env </b> <br/> to activate the environment, use these commands: <br/> on Ubuntu: <b> source  env/bin/activate </b> or <br/>   on Windows:  <b> env\Scripts\activate </b>  <br/> To deactivate, use this command: <b> deactivate </b> </li>
  <li>use this command to install dependencies: <b> pip install -r requirements.txt </b> </li>
  <li>create <b> .env </b> file in the root of the project. <br/> add the contents of using <b>env.example</b> to the <b>.env</b> file. <br/> <br/> to Add user host and passwords <br/> <br/>  Go to  <b> Google Accounts => Security => 2-Step-Verification = > enter your gmail passwords => App passwords => Enter app name => create   </b> </li>
  <li> Use these commands to <b>  python manage.py migrate </b>  <br/> and create a superuser using this command: <b> python manage.py createsuperuser </b> <br/> now run the server using this command: <b> python manage.py runserver </b> </li>
</ul>

<h4> Run this Docker using these commands: </h4>
<ul>
  <li> Run and Build using this command:  <b> docker-compose up --build </b> </li>
  <li> Stop containers using this command: <b> docker-compose down </b> </li>
  <li> Check containers using this command: <b> docker-compose ps </b></li>
</ul>
