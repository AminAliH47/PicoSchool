function filterStudents() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("studentsDP");
  a = div.getElementsByTagName("BUTTON");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function filterBooks() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("filterInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("booksDP");
  a = div.getElementsByTagName("BUTTON");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

$('.student').click(function(){
    const student_dp = document.getElementById('studentRPDropdown');
    student_dp.innerText = this.innerText;
})