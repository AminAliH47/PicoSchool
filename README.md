<div dir="rtl">

  <p align="center">
  
  <img src="https://drive.google.com/uc?id=1Lp6hXe_C-_f0uCYBmsPQ2T1y4BY0n32L&export=download" alt="PicoSchool" width="40%">
  
  <p align="center">
    <i>
    سیستم پیشرفته مدیریت مدارس نوشته شده با جنگو :)
    </i>
  </p>
  
  <hr>
</p>

<h3>
⚙️ پیکربندی پروژه
</h3>

<p>
اول از همه نیاز هست که شما یک venv برای پروژه درست کنید.
پس در روت (root) اصلی پروژه باید این دستور را در ترمینال یا کنسول خود تایپ کنید: 
</p>
<pre>
python -m venv venv
</pre>
<p>
حالا باید venv خودتون رو فعال کنید.
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
<h5>
Configuration of project almost done.
</h5>

<hr>

<h3>
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
<h3>
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
🔒 Main admin panel path:
</h4>
<pre>
http://127.0.0.1:8002/pico-school/
</pre>

<hr>
<h4>
⭐️ Now you can use all the features of PicoSchool.
</h4>

<p>
To make full and practical use of PicoSchool, we are preparing a simple tutorial that you can see in the same repository wiki.
<b>
  <a href="https://github.com/AminAliH47/PicoSchool/wiki">PicoSchool Wiki</a>  
</b>
</p>

<br>
<h6 align="center">
  Licensed by <b>Coilaco</b>
</h6>

  
</div>
