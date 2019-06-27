$(function(){
    $('#btnSingUp').click(function(){
        $.ajax({
            url: '/singup',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
                console.log(response)
            },
            error: function(response) {
                console.log(response)
            }
        });
    });
});