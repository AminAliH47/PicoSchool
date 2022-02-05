let result_pk = document.getElementById("result_pk").dataset.pk;
$.ajax({
    type: "GET",
    url: "/quiz/result-data/" + result_pk + "/",
    success: function (response) {
        var data = response.data;
        var type;
        var answer_text;
        var correct;
        var id;

        for (let i = 0; i < data.length; i++) {
            type = data[i].type;
            id = data[i].id;
            if (type == "تشریحی") {
                const qus_id = document.getElementsByName("qus_id");
                answer_text = data[i].answer_text;
                for (let j = 0; j < qus_id.length; j++) {
                    const id_ = qus_id[j].value;
                    if (id_ == id) {
                        document.getElementById("box" + id_).innerText = answer_text;
                    }//else{
                        //document.getElementById('not-answered').style.display = "";
                    //}
                }
            } else if (type == "چهار گزینه ای") {

                correct = data[i].correct;
                const answer = document.getElementsByClassName("answer");
                const is_superuser = document.getElementById("user_role").dataset.is_superuser;
                const is_teacher = document.getElementById("user_role").dataset.is_teacher;
                for (let i = 0; i < answer.length; i++) {
                    const pk = answer[i].dataset.pk;
                    const correct_ = document.getElementById(pk);
                    ans_correct = answer[i].dataset.correct;

                    if (is_superuser == "True" || is_teacher == "True") {
                        if (pk == correct) {
                            answer[i].checked = true;
                            if (!ans_correct) {
                                answer[i].classList.add("result-ans-incorrect");
                                document.getElementById("lbl" + pk).classList.add("text-danger");
                            }
                        }

                        if (correct_.value && ans_correct) {
                            if (ans_correct == correct_.value) {
                                answer[i].classList.add("result-ans-correct");
                            } else {
                                answer[i].classList.add("result-ans-incorrect");
                            }
                        }
                    } else {
                        if (pk == correct) {
                            answer[i].checked = true;
                        }
                    }

                }
            }
        }
    },
});

$('#printResultBtn').click(function(){
            var divContents = document.getElementById("printResult").innerHTML;
            var a = window.open('', '', 'height=900, width=700');
            a.document.write('<html>');
            a.document.write('<body dir="rtl">');
            a.document.write(divContents);
            a.document.write('</body></html>');
            a.document.close();
            a.print();
            a.close();
})