$('#id_parent option').addClass("ParentDP");
let ParentDropdown = document.getElementById("ParentDropdown");
let id_parent = document.getElementById("id_parent");
id_parent.size = "10";
let parent_options = id_parent.getElementsByTagName("OPTION");
for (let i = 0; i < parent_options.length; i++){
    if (parent_options[i].selected)
        ParentDropdown.innerText = parent_options[i].innerText;
}

$(".ParentDP").click(function(){
    ParentDropdown.innerText = this.innerText;
});
// =================================
$('#id_student_class option').addClass("ClassDP");
let ClassDropdown = document.getElementById("ClassDropdown");
let id_class = document.getElementById("id_student_class");
id_class.size = "10";
let class_options = id_class.getElementsByTagName("OPTION");
for (let i = 0; i < class_options.length; i++){
    if (class_options[i].selected)
        ClassDropdown.innerText = class_options[i].innerText;
}

$(".ClassDP").click(function(){
    ClassDropdown.innerText = this.innerText;
});