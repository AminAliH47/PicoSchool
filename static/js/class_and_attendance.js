$('.present').click(function(){
    let AttendanceStatus1 = document.getElementsByName('AttendanceStatus'+this.name)[0];
    let valAss = document.getElementsByName('val'+this.name)[0];
    AttendanceStatus1.classList.remove('btn-light');
    AttendanceStatus1.classList.remove('btn-success');
    AttendanceStatus1.classList.remove('btn-danger');
    AttendanceStatus1.classList.remove('btn-warning');
    AttendanceStatus1.classList.add('btn-success');
    AttendanceStatus1.innerText = this.innerText;
    $.ajax({
        method: 'POST',
        url: '/manager/change-att-status/',
        data: {
            ass_id: valAss.value,
            status: AttendanceStatus1.innerText,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function() {
        },
        success: function(data) {
        },
        error: function() {
            alert("مشکلی پیش آمده");
        },
    });
})
$('.absent').click(function(){
    let AttendanceStatus2 = document.getElementsByName('AttendanceStatus'+this.name)[0];
    let valAss = document.getElementsByName('val'+this.name)[0];
    AttendanceStatus2.classList.remove('btn-light');
    AttendanceStatus2.classList.remove('btn-success');
    AttendanceStatus2.classList.remove('btn-danger');
    AttendanceStatus2.classList.remove('btn-warning');
    AttendanceStatus2.classList.add('btn-danger');
    AttendanceStatus2.innerText = this.innerText;
    $.ajax({
        method: 'POST',
        url: '/manager/change-att-status/',
        data: {
            ass_id: valAss.value,
            status: AttendanceStatus2.innerText,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function() {
        },
        success: function(data) {
        },
        error: function() {
            alert("مشکلی پیش آمده");
        },
    });
})
$('.pLate').click(function(){
    let AttendanceStatus3 = document.getElementsByName('AttendanceStatus'+this.name)[0];
    let valAss = document.getElementsByName('val'+this.name)[0];
    AttendanceStatus3.classList.remove('btn-light');
    AttendanceStatus3.classList.remove('btn-success');
    AttendanceStatus3.classList.remove('btn-danger');
    AttendanceStatus3.classList.remove('btn-warning');
    AttendanceStatus3.classList.add('btn-warning');
    AttendanceStatus3.innerText = this.innerText;
     $.ajax({
        method: 'POST',
        url: '/manager/change-att-status/',
        data: {
            ass_id: valAss.value,
            status: AttendanceStatus3.innerText,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function() {
        },
        success: function(data) {
        },
        error: function() {
            alert("مشکلی پیش آمده");
        },
    });
})
//===================================
$('.present_cr').click(function(){
    let CrAttendanceStatus1 = document.getElementsByName('CrAttendanceStatus'+this.name)[0];
    CrAttendanceStatus1.classList.remove('btn-light');
    CrAttendanceStatus1.classList.remove('btn-success');
    CrAttendanceStatus1.classList.remove('btn-danger');
    CrAttendanceStatus1.classList.remove('btn-warning');
    CrAttendanceStatus1.classList.add('btn-success');
    CrAttendanceStatus1.innerText = this.innerText;
    $.ajax({
        method: 'POST',
        url: '/manager/add-att-status/',
        data: {
            att_id: CrAttendanceStatus1.id,
            stu_id: this.name,
            status: CrAttendanceStatus1.innerText,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function() {
        },
        success: function(data) {
            window.location.reload();
        },
        error: function() {
            alert("مشکلی پیش آمده");
        },
    });
})
$('.absent_cr').click(function(){
    let CrAttendanceStatus2 = document.getElementsByName('CrAttendanceStatus'+this.name)[0];
    CrAttendanceStatus2.classList.remove('btn-light');
    CrAttendanceStatus2.classList.remove('btn-success');
    CrAttendanceStatus2.classList.remove('btn-danger');
    CrAttendanceStatus2.classList.remove('btn-warning');
    CrAttendanceStatus2.classList.add('btn-danger');
    CrAttendanceStatus2.innerText = this.innerText;
    $.ajax({
        method: 'POST',
        url: '/manager/add-att-status/',
        data: {
            att_id: CrAttendanceStatus2.id,
            stu_id: this.name,
            status: CrAttendanceStatus2.innerText,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function() {
        },
        success: function(data) {
            window.location.reload();
        },
        error: function() {
            alert("مشکلی پیش آمده");
        },
    });
})
$('.pLate_cr').click(function(){
    let CrAttendanceStatus3 = document.getElementsByName('CrAttendanceStatus'+this.name)[0];
    CrAttendanceStatus3.classList.remove('btn-light');
    CrAttendanceStatus3.classList.remove('btn-success');
    CrAttendanceStatus3.classList.remove('btn-danger');
    CrAttendanceStatus3.classList.remove('btn-warning');
    CrAttendanceStatus3.classList.add('btn-warning');
    CrAttendanceStatus3.innerText = this.innerText;
     $.ajax({
        method: 'POST',
        url: '/manager/add-att-status/',
        data: {
            att_id: CrAttendanceStatus3.id,
            stu_id: this.name,
            status: CrAttendanceStatus3.innerText,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function() {
        },
        success: function(data) {
            window.location.reload();
        },
        error: function() {
            alert("مشکلی پیش آمده");
        },
    });
})

//==================================


$('.book_att').click(function(){
    if (confirm(" آیا از ساخت این لیست حضور و غیاب مطمئن هستید؟")){
        var csId = document.getElementById('csId');
        $.ajax({
        method: 'POST',
        url: '/manager/create-att/',
        data: {
            book_id: this.value,
            class_id: csId.value,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function() {
        },
        success: function() {
            window.location.reload();
        },
        error: function() {
            alert("مشکلی پیش آمده");
        },
    });
    }
})

function create_hw(){
    var hw_title = document.getElementById('hw_title');
    var hw_description = document.getElementById('hw_description');
    var hw_att = document.getElementById('hw_att');
        $.ajax({
        method: 'POST',
        url: '/manager/create-hw/',
        data: {
            hw_title: hw_title.value,
            hw_description: hw_description.value,
            hw_att: hw_att.value,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function() {
            $('#HWModal').modal('hide');
        },
        success: function() {
            window.location.reload();
        },
        error: function() {
            alert("مشکلی پیش آمده");
        },
    });
}

$('.SNote').change(function(){
        const ass_id = document.getElementsByName('ass'+this.name)[0];
        $.ajax({
        method: 'POST',
        url: '/manager/change-att-note/',
        data: {
            ass_id: ass_id.value,
            note: this.value,
            csrfmiddlewaretoken: csrf,
        },
        beforeSend: function() {
        },
        success: function(data) {
            window.location.reload();
        },
        error: function() {
            alert("مشکلی پیش آمده");
        },
    });
})