//let csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

$('#submit-btn').click(function(){
    const option = document.getElementById('option_text').value
    const poll = document.getElementById('poll_id').value

    if (option){
        $.ajax({
        type: "post",
        url: window.location.href,
        data: {
            option: option,
            poll: poll,
            csrfmiddlewaretoken: csrf,
        },
        success: function(){
            window.location.reload();
        },
        error: function(){
            alert("مشکلی پیش آمده است")
        }
    })
    }else{
        alert("لطفا فیلد مورد نیاز رو پر کنید")
    }
})

$('#vote-btn').click(function(){
    const option = document.getElementsByName('poll');
    for (let i = 0; i < option.length; i++){
        if (option[i].checked){
            $.ajax({
                type: "post",
                url: window.location.href,
                data: {
                    option: option[i].value,
                    csrfmiddlewaretoken: csrf,
                },
                success: function(response){
                    const pk = response.pk;
                    window,location.href = "/poll/result/" + pk + "/"
                },
                error: function(){
                    alert("مشکلی پیش آمده است")
                }
            })
            break;
        }
    }
})