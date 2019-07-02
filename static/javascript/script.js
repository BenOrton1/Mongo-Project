$(document).ready(function() {
    console.log('this');
    if (($( document ).height()) < ($( window ).height())) {
        $('.footer').addclass('bottom');
    }
    
});
/*    $('#insertrecipes').on('submit', function(event) {
        $.ajax({
                data: {
                    name: $('#recipe_name_input').val()
                },
                type: 'POST',
                url: '/insertrecipe'
            })
            .done(function(data) {

                if (data.error) {
                    $('#errorAlert').text(data.error).show();
                    $('#successAlert').hide();
                }
                else {
                    $('#successAlert').text(data.output).show();
                    $('#errorAlert').hide();
                }
            });
        event.preventDefault();

    });
    /*
    1 select add ingredient form 
    2 prevent default
    3 store ingredient in array
    4 sent array to back end
    5 add new lines to array and update inner html
    6 remove ingedients from array
*/

