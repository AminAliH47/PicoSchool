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

<div dir="ltr">
<pre>
python -m venv venv
</pre>
</div>

<p>
حالا باید venv خودتون رو فعال کنید. <br>
  در روت (root) اصلی پروژه باید این دستور را در ترمینال یا کنسول خود تایپ کنید: 
</p>
<b>
در Linux/macOS:
</b>
<div dir="ltr">
<pre>
source venv/bin/activate
</pre>
</div>
<b>
در Windows:
</b>

<div dir="ltr">
<pre>
venv/Scripts/activate.ps1
</pre>
</div>

<p>
  بعد از فعالسازی venv شما باید پکیج های <b> requirements.txt </b> را نصب کنید. <br> 
پس در روت (root) اصلی پروژه باید این دستور را در ترمینال یا کنسول خود تایپ کنید: 
</p>

<div dir="ltr">
<pre>
pip install -r requirements.txt
</pre>
</div>

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

<div dir="ltr">
<pre>
python manage.py check
</pre>
</div>

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

<div dir="ltr">
<pre>
python manage.py runserver 8002
</pre>
</div>

<h4>
  تبریک، شما پروژه رو به درستی اجرا کردید ✅ 
</h4>

<p>
  حالا این آدرس رو در نوار URL مرورگر خود وارد کنید:
</p>

<div dir="ltr">
<pre>
http://127.0.0.1:8002/
</pre>
</div>

<hr>
<h3>
✅ استفاده از پروژه
</h3>
<h5>
  حالا شما باید در PicoSchool لاگین کنید.
</h5>
<p>
  در پایگاه داده (Database) پیشفرض، ما چند کاربر نمونه در نقش های مختلف داریم. <br>
  شما می‌تونید با نقش های مختلف در PicoSchool لاگین کنید، نام کاربری و گذرواژه این کاربران نمونه در پایگاه داده پیشفرض در زیر فهرست شدند:  
</p>
<ul>
  <li>
    نقش Manager (مدیر):
    
<pre>
username: Admin
password: Admin12345
</pre>

  </li>
  <li>
   نقش Teacher (دبیر):
   
<pre>
username: 0934567899
password: Admin12345
</pre>

  </li>
  <li>
    نقش Student (دانش آموز):
    
<pre>
username: 0923456789
password: Admin12345
</pre>

  </li>
  <li>
   نقش Parent (والدین):
   
<pre>
username: 0934567898
password: Admin12345
</pre>

  </li>
</ul>

<h4>
🔒 مسیر ادمین پنل اصلی:
</h4>

<div dir="ltr">
<pre>
http://127.0.0.1:8002/pico-school/
</pre>
</div>

<hr>
<h4>
  ⭐️ حالا شما می‌تونید از تمام قابلیت های PicoSchool استفاده کنید.
</h4>

<p>
برای استفاده کامل و کاربردی از PicoSchool، در حال آماده سازی یک آموزش ساده هستیم که می توانید در ویکی (wiki) همین ریپازیتوری (repository) مشاهده کنید.
<b>
  <a href="https://github.com/AminAliH47/PicoSchool/wiki">ویکی PicoSchool</a>  
</b>
</p>

<br>
<h6 align="center">
  Licensed by <b>Coilaco</b>
</h6>

  
</div>
