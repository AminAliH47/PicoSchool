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
اول از همه نیاز هست که شما یک venv برای پروژه درست کنید. <br>
پس در روت (root) اصلی پروژه باید این دستور را در ترمینال یا کنسول خود تایپ کنید: 
</p>
<pre>
python -m venv venv
</pre>
<p>
حالا باید venv خودتون رو فعال کنید. <br>
پس در روت (root) اصلی پروژه باید این دستور را در ترمینال یا کنسول خود تایپ کنید: 
</p>
<b>
در Linux/macOS:
</b>
<pre>
source venv/bin/activate
</pre>
<b>
در Windows:
</b>
<pre>
venv/Scripts/activate.ps1
</pre>

<p>
  بعد از فعالسازی venv شما باید پکیج های <b> requirements.txt </b> را نصب کنید. <br> 
پس در روت (root) اصلی پروژه باید این دستور را در ترمینال یا کنسول خود تایپ کنید: 
</p>
<pre>
pip install -r requirements.txt
</pre>
<h5>
پیکربندی پروژه تقریبا تمام است.
</h5>

<hr>

<h3>
🏁 اجرای پروژه
</h3>
<p>
  اول از همه، لطفا دستور زیر را در ترمینال یا کنسول خود وارد کنید تا مطمئن بشید پروژه به درستی پیکربندی شده است:
</p>
<pre>
python manage.py check
</pre>
<p>
  باید با چنین پیغامی مواجه بشید:
  <strong>
    <i>
      "System check identified no issues (0 silenced)."
    </i>
  </strong>
  <br>
  اگر این پیغام را مشاهده می‌کنید، می‌توانید پروژه را اجرا کنید. برای اجرای پروژه این دستور را در ترمینال یا کنسول وارد کنید:
</p>
<pre>
python manage.py runserver 8002
</pre>
<h4>
  تبریک، شما پروژه رو به درستی اجرا کردید ✅ 
</h4>

<p>
  حالا این آدرس رو در نوار URL مرورگر خود وارد کنید:
</p>
<pre>
http://127.0.0.1:8002/
</pre>

<hr>
<h3>
✅ استفاده از پروژه
</h3>
<h5>
  حالا شما باید در PicoSchool لاگین کنید.
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
