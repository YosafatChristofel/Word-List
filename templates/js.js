let word = "sample_word";  // You would dynamically set this based on user actions.

function get_examples() {
    $("#example-list").empty();
    $.ajax({
        type: "GET",
        url: `/api/get_exs?word_give=${word}`,
        success: function (response) {
            response.examples.forEach(function(ex, index) {
                $("#example-list").append(`<li id="ex-${index}">${ex.example}&nbsp;&nbsp;&nbsp;<a href="javascript:delete_ex(${index})">delete</a></li>`);
            });
        }
    });
}

function add_ex() {
    let new_ex = $('#new-example').val();
    $.ajax({
        type: "POST",
        url: `/api/save_ex`,
        contentType: 'application/json',
        data: JSON.stringify({
            word_give: word,
            example: new_ex
        }),
        success: function (response) {
            $('#new-example').val('');  // Clear the input after saving
            get_examples();  // Refresh the list
        }
    });
}

function delete_ex(id) {
    $.ajax({
        type: "POST",
        url: `/api/delete_ex`,
        contentType: 'application/json',
        data: JSON.stringify({
            word: word,
            id: id
        }),
        success: function (response) {
            get_examples();  // Refresh the list
        }
    });
}
