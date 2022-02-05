<p align="center">
  
  <img src="https://s20.picofile.com/file/8447413126/picoschool.png" alt="PicoSchool" width="40%">
  
  <p align="center">
    <i style="margin-top: 10px; display: block;">
    Advanced school management system written in Django :)
    </i>
  </p>
  
  <hr style="border: 1px solid #00ff00ff;">
</p>

<h3 style="margin: 30px 0 -5px 0;">
⚙️ Config the project
</h3>

<p>
First you should make venv for this project.
So in the main root of project you should type this command in your Terminal or Console: 
</p>
<pre>
python -m venv venv
</pre>
<p>
Now you should activate your venv.
So in the main root of project you should type this command in your Terminal or Console: 
</p>
<b>
In Linux/macOS:
</b>
<pre>
source venv/bin/activate
</pre>
<b>
In Windows:
</b>
<pre>
venv/Scripts/activate.ps1
</pre>

<p>
After activating venv you should install the <b>requirements.txt</b> packages. So type this command in your Terminal or Console: 
</p>
<pre>
pip install -r requirements.txt
</pre>

<hr>

<h5>
Configuration of project almost done.
</h5>
<h3 style="margin: 30px 0 -5px 0;">
🏁 Run the project
</h3>
<p>
First of all, please enter the following command in the Terminal or Console to make sure the project is configured correctly:
</p>
<pre>
python manage.py check
</pre>
<p>
You should see This message:
  <strong>
    <i>
      "System check identified no issues (0 silenced)."
    </i>
  </strong>
  <br>
  If you see this message you can run project. So type this command in Terminal or Console:
</p>
<pre>
python manage.py runserver 8002
</pre>
<h4>
Congratulations, you ran the project correctly ✅
</h4>

<p>
Now copy/paste this address in your browser URL bar:
</p>
<pre>
http://127.0.0.1:8002/
</pre>

<hr>
<h3 style="margin: 30px 0 -5px 0;">
✅ Use the project
</h3>
<h5>
Now you should Login into the PicoSchool. 
</h5>
<p>
In default Database, we have some sample user in custom Roles. <br>
You can login to PicoSchool with different roles, the usernames and passwords of these sample users in the default database are listed below:
</p>
<ul>
  <li>
    Manager role:
<pre>
username: Admin
password: Admin12345
</pre>
  </li>
  <li>
    Teacher role:
<pre>
username: 0934567899
password: Admin12345
</pre>
  </li>
  <li>
    Student role:
<pre>
username: 0923456789
password: Admin12345
</pre>
  </li>
  <li>
    Parent role:
<pre>
username: 0934567898
password: Admin12345
</pre>
  </li>
</ul>

<h4>
Main admin panel path:
</h4>
<pre>
http://127.0.0.1:8002/pico-school/
</pre>


<h6 align="center" style="font-weight: 200;">
  Licensed by <b>Coilaco</b>
</h6>
