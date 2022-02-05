document.getElementById('id_single_or_married').setAttribute('onchange','SOMFunc();');
let SOM = document.getElementById('id_single_or_married');
if (SOM.value == "متاهل") document.getElementById('spouse_info').style.display = "";
function SOMFunc() {
    var value = document.getElementById("id_single_or_married").value;
    if (value == "متاهل") {
        document.getElementById('spouse_info').style.display = "";
        document.getElementById('id_spouse_fullname').required = true;
        document.getElementById('id_spouse_phone').required = true;
        document.getElementById('id_child_num').required = true;
    }
    else {
        document.getElementById('spouse_info').style.display = "none";
        document.getElementById('id_spouse_fullname').required = false;
        document.getElementById('id_spouse_phone').required = false;
        document.getElementById('id_child_num').required = false;
    }
}