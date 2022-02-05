//CKEDITOR.replace( 'content', {
//    language: 'fa',
//    skin: 'office2013',
//    height: 70,
//    width: 'auto',
//    toolbar: [
//        ['Copy','Cut','Paste', '-',
//        'Bold', 'Italic', 'Underline', 'Strike', 'SpecialChar', '-',
//        'Styles', 'Format', 'Font', 'FontSize', '-',
//        'TextColor', 'BGColor', '-',
//        'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
//        'JustifyRight', 'JustifyBlock', '-',
//        'Image','-',
//        'RemoveFormat', 'Preview'
//        ]
//    ],
//});

$(".add_question").click(function () {});
$(".qus_type").click(function () {
    document.getElementById("QuestionTypeDP").innerText = this.innerText;
    if (this.innerText == "تشریحی") {
        document.getElementById("MultiQuestion").style.display = "none";
        document.getElementById("make_qus").style.display = "";
    } else if (this.innerText == "چهار گزینه ای") {
        document.getElementById("MultiQuestion").style.display = "";
        document.getElementById("make_qus").style.display = "";
    }
});
$("#make_qus").click(function () {
//    Create question for main quiz
    const contentData = CKEDITOR.instances.id_text.getData();
    const item = document.getElementById("id_text");
    const question_type = document.getElementById("QuestionTypeDP").innerText;
    const question_text = (item.value = contentData);
    const quiz_id = document.getElementById("quiz_id").value;
    const qus_id = Date.now();
    if (question_text == "") {
        alert("لطفا عنوان سوال را بنویسید");
    } else {
        if (question_type == "تشریحی") {
            let formData = new FormData();
            formData.append("qus_id", qus_id);
            formData.append("quiz_id", quiz_id);
            formData.append("question_type", question_type);
            formData.append("question_text", question_text);
            formData.append("csrfmiddlewaretoken", csrf);
            $.ajax({
                type: "POST",
                url: window.location.href,
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
        } else if (question_type == "چهار گزینه ای") {
            const answers = document.getElementsByClassName("Answer");
            const correct_answers = document.getElementsByClassName("CorrectAnswer");

            let formData = new FormData();
            formData.append("qus_id", qus_id);
            formData.append("quiz_id", quiz_id);
            formData.append("question_type", question_type);
            formData.append("question_text", question_text);
            formData.append("csrfmiddlewaretoken", csrf);

            $.ajax({
                type: "POST",
                url: window.location.href,
                contentType: false,
                processData: false,
                data: formData,
                beforeSend: function () {},
                success: function () {},
                error: function () {
                    alert("مشکلی پیش آمده است");
                },
            });
            setTimeout(function () {
                for (let i = 0; i < answers.length; i++) {
                    let fd = new FormData();
                    fd.append("answer_text", answers[i].value);
                    fd.append("qus_id", qus_id);
                    fd.append("csrfmiddlewaretoken", csrf);

                    if (correct_answers[i].value == answers[i].id) {
                        if (correct_answers[i].checked) fd.append("correct", true);
                        else fd.append("correct", false);
                    }
                    $.ajax({
                        type: "POST",
                        url: "/quiz/create-answers/",
                        contentType: false,
                        processData: false,
                        data: fd,
                        beforeSend: function () {},
                        success: function () {
                            //                        window.location.reload();
                        },
                        error: function () {
                            alert("مشکلی پیش آمده است");
                        },
                    });
                }
                setTimeout(function () {
                    window.location.reload();
                }, 1000);
            }, 300);
        }
    }
});
$(".delete-qus").click(function () {
    id = this.dataset.id;
    if (confirm("آیا از حذف این سوال اطمینان دارید؟")) {
        $.ajax({
            type: "POST",
            url: "/quiz/list/",
            data: {
                id: id,
                csrfmiddlewaretoken: csrf,
            },
            beforeSend: function () {},
            success: function () {
                window.location.reload();
            },
            error: function () {
                alert("مشکلی پیش آمده است");
            },
        });
    }
});
const qus_answers = document.getElementById("answers");
const id_question_type = document.getElementById("id_question_type");
if (id_question_type) id_question_type.disabled = true;
if (qus_answers) {
    const qus_type = document.getElementById("id_question_type");
    if (qus_type.value == "چهار گزینه ای") qus_answers.style.display = "";
}

$("#edit_question").click(function () {
    const contentData = CKEDITOR.instances.id_text.getData();
    let item = document.getElementById("id_text");
    let question_text = (item.value = contentData);
    const qus_id = this.dataset.id;
    const formData = new FormData();
    formData.append("qus_id", qus_id);
    formData.append("question_text", question_text);
    formData.append("csrfmiddlewaretoken", csrf);
    $.ajax({
        type: "POST",
        url: "/quiz/questions-update/",
        contentType: false,
        processData: false,
        data: formData,
        beforeSend: function () {},
        success: function () {
            //            window.location.reload();
        },
        error: function () {
            alert("مشکلی پیش آمده است");
        },
    });
    let answers = document.getElementsByClassName("Answer");
    let correct_answers = document.getElementsByClassName("CorrectAnswer");
    setTimeout(function () {
        for (let i = 0; i < answers.length; i++) {
            const fd = new FormData();
            fd.append("answer_text", answers[i].value);
            fd.append("answer_id", answers[i].id);
            fd.append("csrfmiddlewaretoken", csrf);

            if (correct_answers[i].value == answers[i].id) {
                if (correct_answers[i].checked) fd.append("correct", true);
                else fd.append("correct", false);
            }
            $.ajax({
                type: "POST",
                url: "/quiz/answers-update/",
                contentType: false,
                processData: false,
                data: fd,
                beforeSend: function () {},
                success: function () {
                    //                        window.location.reload();
                },
                error: function () {
                    alert("مشکلی پیش آمده است");
                },
            });
        }
        setTimeout(function () {
            window.location.reload();
        }, 1000);
    }, 300);
});

$(".start-quiz-btn").click(function () {
    const pk = this.dataset.pk;
    const name = this.dataset.quiz;
    const difficulty = this.dataset.difficulty;
    const time = this.dataset.time;
    const uuid = this.dataset.uuid;
    const modal_body = document.getElementById("quiz-modal-body");
    const startBtn = document.getElementById("start-button");
    const url = window.location.href;
    modal_body.innerHTML = `
        <div class="h3 mb-3"> آیا میخواهید آزمون "<b>${name}</b>" را اجرا کنید؟ </div>
        <div class="text-muted">
            <ul>
                <li class="mb-3"> سختی: <b class="text-primary">${difficulty}</b> </li>
                <li class="mb-3"> زمان: <b class="text-primary">${time} دقیقه</b> </li>
            </ul>
        </div>
    `;
    $("#start-button").click(function () {
        window.location.href = "/quiz/detail/" + pk + "/" + uuid + "/" + "?qus=1";
    });
});
$(".submit-answer").click(function () {
    const type = this.dataset.type;
    const id = this.dataset.id;
    const url = this.dataset.url;

    if (type == "تشریحی") {
        const textBox = document.getElementsByName(id)[0].value;
        $.ajax({
            type: "post",
            url: window.location.href,
            data: {
                id: id,
                answer_test: textBox,
                type: type,
                csrfmiddlewaretoken: csrf,
            },
            success: function () {
                window.location.href = url;
            },
            error: function () {
                alert("مشکلی پیش آمده است");
            },
        });
    } else if (type == "چهار گزینه ای") {
        const multiAns = document.getElementById("multiAns");
        const input = multiAns.getElementsByTagName("INPUT");
        let correct = "";
        for (let i = 0; i < input.length; i++) {
            if (input[i].checked) {
                correct = input[i].dataset.pk;
            }
        }
        $.ajax({
            type: "post",
            url: window.location.href,
            data: {
                id: id,
                type: type,
                correct: correct,
                csrfmiddlewaretoken: csrf,
            },
            success: function () {
                window.location.href = url;
            },
            error: function () {
                alert("مشکلی پیش آمده است");
            },
        });
    }
});

$(".end-quiz").click(function () {
    const type = this.dataset.type;
    const id = this.dataset.id;
    const url = this.dataset.url;
    const uuid = this.dataset.uuid;
    const pk = this.dataset.pk;

    if (type == "تشریحی") {
        const textBox = document.getElementsByName(id)[0].value;
        $.ajax({
            type: "post",
            url: "/quiz/create-result/",
            data: {
                id: id,
                answer_test: textBox,
                type: type,
                // send data for make result
                uuid: uuid,
                pk: pk,
                csrfmiddlewaretoken: csrf,
            },
            success: function () {
                window.location.href = "/quiz/result/list/";
            },
            error: function () {
                alert("مشکلی پیش آمده است");
            },
        });
    } else if (type == "چهار گزینه ای") {
        const multiAns = document.getElementById("multiAns");
        const input = multiAns.getElementsByTagName("INPUT");
        var correct = "";
        for (let i = 0; i < input.length; i++) {
            if (input[i].checked) {
                correct = input[i].dataset.pk;
            }
        }
        $.ajax({
            type: "post",
            url: "/quiz/create-result/",
            data: {
                id: id,
                correct: correct,
                type: type,
                // send data for make result
                uuid: uuid,
                pk: pk,
                csrfmiddlewaretoken: csrf,
            },
            success: function () {
                window.location.href = "/quiz/result/list/";
            },
            error: function () {
                alert("مشکلی پیش آمده است");
            },
        });
    }
});

$(".text-answer").change(function () {
    const id = this.name;
    const type = this.dataset.type;
    const answer_text = this.value;
    $.ajax({
        type: "post",
        url: "/quiz/get-question/",
        data: {
            id: id,
            type: type,
            answer_text: answer_text,
            csrfmiddlewaretoken: csrf,
        },
        success: function () {},
        error: function () {
            alert("مشکلی پیش آمده است");
        },
    });
});
$(".multi-answer").change(function () {
    const id = this.name;
    const type = this.dataset.type;
    const correct = this.dataset.pk;
    $.ajax({
        type: "post",
        url: "/quiz/get-question/",
        data: {
            id: id,
            type: type,
            correct: correct,
            csrfmiddlewaretoken: csrf,
        },
        success: function () {},
        error: function () {
            alert("مشکلی پیش آمده است");
        },
    });
});
$(".end-quiz-2").click(function () {
    const uuid = this.dataset.uuid;
    const pk = this.dataset.pk;
    $.ajax({
        type: "post",
        url: "/quiz/create-result-2/",
        data: {
            // send data for make result
            uuid: uuid,
            pk: pk,
            csrfmiddlewaretoken: csrf,
        },
        success: function () {
            window.location.href = "/quiz/result/list/";
        },
        error: function () {
            alert("مشکلی پیش آمده است");
        },
    });
});
$.ajax({
    type: "GET",
    url: "/quiz/answers/",
    success: function (response) {
        var data = response;
        let id, answer_text, correct, type, qus_id_;
        const qus = document.getElementsByClassName("qus_id");

        for (let i = 0; i < data.length; i++) {
            id = data[i].id;
            type = data[i].type;
            for (let j = 0; j < qus.length; j++) {
                quiz_id_ = qus[j].value;
                if (type == "تشریحی") {
                    answer_text = data[i].answer_text;
                    if (id == quiz_id_) {
                        const new_qus = document.getElementsByName(id);
                        for (let l = 0; l < new_qus.length; l++) {
                            new_qus[l].innerText = answer_text;
                        }
                    }
                } else if (type == "چهار گزینه ای") {
                    correct = data[i].correct;
                    if (id == quiz_id_) {
                        const new_qus = document.getElementsByName(id);
                        var ans_pk;
                        for (let l = 0; l < new_qus.length; l++) {
                            const ans = document.getElementsByClassName("ans" + id);
                            for (let k = 0; k < ans.length; k++) {
                                ans_pk = ans[k].dataset.pk;
                                if (correct == ans_pk) {
                                    ans[k].checked = true;
                                }
                            }
                        }
                    }
                }
            }
        }
    },
});

let time = document.getElementById("time").value;
//if (time) {
//    time = time.value;
//}
let timer_box = document.getElementById("timer_box");

let quiz_pk = document.getElementById("quiz_pk").value;
//if (quiz_pk) {
//    quiz_pk = quiz_pk.value;
//}else {
//    quiz_pk = 0;
//}
let quiz_uuid = document.getElementById("quiz_uuid").value;
//if (quiz_uuid) {
//    quiz_uuid = quiz_uuid.value;
//}else {
//    quiz_uuid = 0;
//}

time = time * 60;
document.addEventListener("DOMContentLoaded", function (event) {
    if (sessionStorage.getItem("counter")) {
        if (sessionStorage.getItem("counter") <= 0) {
            var value = time;
        } else {
            var value = sessionStorage.getItem("counter");
        }
    } else {
        var value = time;
    }

    var counter = function () {
        if (value <= 0) {
            sessionStorage.removeItem("counter");
            value = time;
            $.ajax({
                type: "post",
                url: "/quiz/create-result-2/",
                data: {
                    // send data for make result
                    uuid: quiz_uuid,
                    pk: quiz_pk,
                    csrfmiddlewaretoken: csrf,
                },
                success: function () {
                    window.location.href = "/quiz/result/list/";
                },
                error: function () {
                    alert("مشکلی پیش آمده است");
                },
            });
        } else {
            value = parseInt(value) - 1;
            sessionStorage.setItem("counter", value);
        }
        if (value <= 60) {
            timer_box.style.color = "#dc3545";
        } else {
            timer_box.style.color = "#6c757d";
        }

        var minutes = Math.floor(value / 60);
        var seconds = value - minutes * 60;
        var displayMin;
        var displaySec;

        if (minutes.toString().length < 2) displayMin = "0" + minutes;
        else displayMin = minutes;

        if (seconds.toString().length < 2) displaySec = "0" + seconds;
        else displaySec = seconds;

        timer_box.innerHTML = `<b>${displayMin}:${displaySec}</b>`;
    };

    var interval = setInterval(function () {
        counter();
    }, 1000);
});
