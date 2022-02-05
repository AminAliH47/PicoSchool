$("input[required], select[required]").attr("oninvalid", "this.setCustomValidity('لطفا این فیلد را پر کنید')");
$("input[required], select[required]").attr("oninput", "setCustomValidity('')");
$("textarea[required], select[required]").attr("oninvalid", "this.setCustomValidity('لطفا این فیلد را پر کنید')");
$("textarea[required], select[required]").attr("oninput", "setCustomValidity('')");
//let csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
// Sidebar Section
(function ($) {
    let $allPanels = $(".nested").hide();
    let $elements = $(".treeview-animated-element");
    $(".closed").click(function () {
        $this = $(this);
        $target = $this.siblings(".nested");
        $pointer = $this.children(".fa-angle-right");

        $this.toggleClass("open");
        $pointer.toggleClass("down");

        !$target.hasClass("active") ? $target.addClass("active").slideDown() : $target.removeClass("active").slideUp();

        return false;
    });

    $elements.click(function () {
        $this = $(this);
        $this.hasClass("opened") ? $this.removeClass("opened") : ($elements.removeClass("opened"), $this.addClass("opened"));
    });
})(jQuery);

var mediaQuery = window.matchMedia("(min-width: 768px)");
if (mediaQuery.matches) {
    document.getElementById("mySidenav").style.width = "260px";
} else {
    document.getElementById("mySidenav").style.width = "0";
}
/* Set the width of the side navigation to 250px */
function openNav() {
    let mySidenav = document.getElementById("mySidenav");
    let wrapper = document.getElementById("wrapper");
    let NavTogglerMo = document.getElementById("NavTogglerMo");

    if (mySidenav.style.width == "0px") {
        mySidenav.style.width = "260px";
        if (mediaQuery.matches) {
            document.getElementById("wrapper").style.marginRight = "260px";
        }
        wrapper.classList.add("sidebar-collapsed");
        NavTogglerMo.classList.remove("fa-bars");
        NavTogglerMo.classList.add("fa-times");
    } else if (mySidenav.style.width == "260px") {
        mySidenav.style.width = "0";
        if (mediaQuery.matches) {
            document.getElementById("wrapper").style.marginRight = "0";
        }
        wrapper.classList.remove("sidebar-collapsed");
        NavTogglerMo.classList.add("fa-bars");
        NavTogglerMo.classList.remove("fa-times");
    }
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("wrapper").style.marginRight = "0";
}
//=============================

// Search in users name
function search_users() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("UsersDropdown");
    button = div.getElementsByTagName("button");
    for (i = 0; i < button.length; i++) {
        txtValue = button[i].textContent || button[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            button[i].style.display = "";
        } else {
            button[i].style.display = "none";
        }
    }
}
// Make new Notice
var notice_writer_id = "";
var notice_writer = document.getElementsByClassName("Notice_writer");
$(".noticeWr").click(function () {
    var id = this.id.slice(2);
    notice_writer[0].innerText = this.innerText;
    notice_writer[1].innerText = this.innerText;
    notice_writer_id = id;
    notice_writer[1].name = id;
});
function submit_notice() {
    var notice_title = document.getElementById("notice_title");
    var notice_description = document.getElementById("notice_description");
    if ((notice_title.value == "" && notice_description.value == "") || notice_description.value == "" || notice_title.value == "") {
        alert("لطفا فیلد های مورد نیاز رو پر کنید");
    } else {
        $.ajax({
            url: "/manager/add-notice/",
            method: "POST",
            data: {
                writer: notice_writer_id,
                title: $("#notice_title").val(),
                description: $("#notice_description").val(),
                csrfmiddlewaretoken: csrf,
            },
            beforeSend: function () {
                $("#notices_modal").modal("hide");
            },
            success: function (data) {
                window.location.reload();
            },
            error: function (data) {
                alert("مشکلی پیش آمده");
            },
        });
    }
}

// Delete Notice
$(".delete_notice").click(function init() {
    var id = this.name;

    if (!confirm("آیا از حذف اعلان اطمینان دارید؟")) {
    } else {
        $.ajax({
            url: "/manager/delete-notice/",
            method: "POST",
            data: {
                id: id,
                csrfmiddlewaretoken: csrf,
            },
            beforeSend: function () {
                $("#delete_nortice_modal").modal("hide");
            },
            success: function (data) {
                alert("با موفقیت حذف شد");
                window.location.reload();
            },
            error: function (data) {
                alert("مشکلی پیش آمده");
            },
        });
    }
    return (ENI = id);
});

var ENI = null;
$(".edit_notice").click(function () {
    var id = this.name;
    var ENB = document.getElementById(id);
    var Enotice_title2 = document.getElementById("Enotice_title2");
    var Enotice_description2 = document.getElementById("Enotice_description2");
    var Enotice_writer2 = document.getElementsByClassName("Notice_writer")[1];
    var Enotice_title = ENB.getElementsByTagName("h6")[0];
    var Enotice_description = ENB.getElementsByTagName("p")[0];
    var Enotice_writer = ENB.getElementsByTagName("span")[1];
    Enotice_writer2.innerText = Enotice_writer.innerText;
    Enotice_title2.value = Enotice_title.innerText;
    Enotice_description2.value = Enotice_description.innerText;
    ENI = id;
    $("#edit_notice_modal").modal("show");
});

function edit_notice() {
    var Notice_writer = document.getElementsByClassName("Notice_writer")[1];
    var writer = Notice_writer.innerText.slice(0, 2);
    var Enotice_title2 = document.getElementById("Enotice_title2");
    var Enotice_description2 = document.getElementById("Enotice_description2");

    if ((Enotice_title2.value == "" && Enotice_description2.value == "") || Enotice_description2.value == "" || Enotice_title2.value == "") {
        alert("لطفا فیلد های مورد نیاز رو پر کنید");
    } else {
        $.ajax({
            url: "/manager/edit-notice/",
            method: "POST",
            data: {
                id: ENI,
                writer: writer,
                title: $("#Enotice_title2").val(),
                description: $("#Enotice_description2").val(),
                csrfmiddlewaretoken: csrf,
            },
            beforeSend: function () {
                $("#notices_modal").modal("hide");
            },
            success: function (data) {
                alert("با موفقیت ویرایش شد");
                window.location.reload();
            },
            error: function (data) {
                alert("مشکلی پیش آمده");
            },
        });
    }
}

$("#change_event_desc").click(function () {
    const textarea_ = document.getElementById("eventDesc");
    var description;
    if (textarea_.value) description = textarea_.value;
    else description = textarea_.innerText;
    $.ajax({
        type: "post",
        url: "/manager/update-event-desc/",
        data: {
            id: document.getElementById("event_id").value,
            description: description,
            csrfmiddlewaretoken: csrf,
        },
        success: function () {
            $("#exampleModalCenter").modal("hide");
            window.location.reload();
        },
        error: function () {
            alert("مشکلی پیش آمده است");
        },
    });
});
$("#delete_event").click(function () {
    if (confirm("آیا از حذف این رویداد اطمینان دارید؟")) {
        $.ajax({
            type: "post",
            url: "/manager/delete-event/",
            data: {
                id: document.getElementById("event_id").value,
                csrfmiddlewaretoken: csrf,
            },
            success: function () {
                $("#exampleModalCenter").modal("hide");
                window.location.reload();
            },
            error: function () {
                alert("مشکلی پیش آمده است");
            },
        });
    }
});
// Filter Selections
var GradeDropdown = document.getElementById("GradeDropdown");
var gradeSC = document.getElementById("gradeSC");
$(".grade").click(function () {
    if (this.innerText == "همه") gradeSC.value = null;
    else gradeSC.value = this.innerText;
    GradeDropdown.innerText = this.innerText;
});

var MajorDropdown = document.getElementById("MajorDropdown");
var majorSC = document.getElementById("majorSC");
$(".major").click(function () {
    if (this.innerText == "همه") majorSC.value = null;
    else majorSC.value = this.innerText;
    MajorDropdown.innerText = this.innerText;
});

$(".MajorDP").click(function () {
    let Major_dropdown = document.getElementsByClassName("Major_dropdown")[0];
    Major_dropdown.innerText = this.innerText;
    let id_major = document.getElementById("id_major");
    id_major.value = this.id.slice(3);
});

$(".GradeDP").click(function () {
    let Grade_dropdown = document.getElementsByClassName("Grade_dropdown")[0];
    Grade_dropdown.innerText = this.innerText;
    let id_grade = document.getElementById("id_grade");
    id_grade.value = this.id.slice(3);
});

function filter() {
    var keyword = document.getElementById("search").value;
    var select = document.getElementById("id_parent");
    for (var i = 0; i < select.length; i++) {
        var txt = select.options[i].text;
        if (txt.substring(0, keyword.length).toLowerCase() !== keyword.toLowerCase() && keyword.trim() !== "") {
            $(select.options[i]).attr("disabled", "disabled").hide();
        } else {
            $(select.options[i]).removeAttr("disabled").show();
        }
    }
}
function filter2() {
    var keyword = document.getElementById("search_cs").value;
    var select = document.getElementById("id_student_class");
    for (var i = 0; i < select.length; i++) {
        var txt = select.options[i].text;
        if (txt.substring(0, keyword.length).toLowerCase() !== keyword.toLowerCase() && keyword.trim() !== "") {
            $(select.options[i]).attr("disabled", "disabled").hide();
        } else {
            $(select.options[i]).removeAttr("disabled").show();
        }
    }
}

// Change Password Section
function submit_change_password() {
    let user_id = $("#user_id").val();
    let password1 = $("#password1").val();
    let password2 = $("#password2").val();
    if (password1 == "" || password2 == "") {
        alert("لطفا فیلد های مورد نیاز رو پر کنید");
    } else {
        $.ajax({
            method: "POST",
            url: "/manager/user/" + user_id + "/password/",
            data: {
                password1: password1,
                password2: password2,
                csrfmiddlewaretoken: csrf,
            },
            beforeSend: function () {},
            success: function (data) {
                if (data.hasOwnProperty("error")) {
                    if (data.error == true) {
                        let validateError = document.getElementById("validateError");
                        validateError.style.display = "";
                        validateError.innerText = data.message;
                    }
                } else {
                    window.location.href = "/manager/password-done/";
                }
            },
            error: function (jqXHR, exception) {
                alert(jqXHR.responseText);
            },
        });
    }
}
//var user_memory = navigator.deviceMemory;
//console.log(user_memory);
//if (user_memory >= 8) {
//    alert("good");
//} else{
//    alert("not bad");
//}

function create_emp_form() {
    var emp_from_organ = document.getElementById("emp_from_organ");
    var emp_from_student = document.getElementById("emp_from_student");
    $.ajax({
        method: "POST",
        url: "/student/create-emp-form/",
        data: {
            stu_id: emp_from_student.value,
            organ: emp_from_organ.value,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function () {
            $("#EMPFormModal").modal("hide");
        },
        success: function () {
            window.location.reload();
        },
        error: function () {
            alert("مشکلی پیش آمده");
        },
    });
}

$(".statusEMP").click(function () {
    let statusForm = document.getElementById("statusForm");
    statusForm.innerText = this.innerText;
    statusForm.classList.remove("btn-success");
    statusForm.classList.remove("btn-warning");
    statusForm.classList.remove("btn-danger");
    if (this.innerText == "بررسی شده") {
        statusForm.classList.add("btn-success");
    } else if (this.innerText == "در انتظار بررسی") {
        statusForm.classList.add("btn-warning");
    } else if (this.innerText == "رد شده") {
        statusForm.classList.add("btn-danger");
    }
    $.ajax({
        method: "POST",
        url: window.location.href,
        data: {
            status: this.innerText,
            emp_form_id: document.getElementById("emp_form_id").value,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function () {},
        success: function () {
            window.location.reload();
        },
        error: function () {
            alert("مشکلی پیش آمده");
        },
    });
});
function loadFile(event) {
    var image = document.getElementById("img_output");
    image.src = URL.createObjectURL(event.target.files[0]);
    var files = $("#img_form")[0].files;
    let formData = new FormData();

    formData.append("file", files[0]);
    formData.append("emp_form_id", document.getElementById("emp_form_id").value);
    formData.append("csrfmiddlewaretoken", csrf);

    $.ajax({
        type: "POST",
        url: "/manager/upload-emp-form/",
        contentType: false,
        processData: false,
        data: formData,
        beforeSend: function () {},
        success: function () {
            window.location.reload();
        },
        error: function () {
            alert("مشکلی پیش آمده است");
        },
    });
}
function ImagetoPrint(source) {
    return (
        "<html><head><scri" + "pt>function step1(){\n" + "setTimeout('step2()', 10);}\n" + "function step2(){window.print();window.close()}\n" + "</scri" + "pt></head><body onload='step1()'>\n" + "<img src='" + source + "' /></body></html>"
    );
}

function PrintImage(source) {
    var Pagelink = "about:blank";
    var pwa = window.open(Pagelink, "_new");
    pwa.document.open();
    pwa.document.write(ImagetoPrint(source));
    pwa.document.close();
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrf = getCookie('csrftoken');