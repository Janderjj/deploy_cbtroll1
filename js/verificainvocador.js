function getinvocador(){



    $(document).ready(function () {
        $.ajax({ 
            type: 'GET', 
            url: 'http://example/functions.php', 
            data: { get_param: 'value' }, 
            success: function (data) { 
                var names = data
                $('#cand').html(data);
            }
        });
    });


}