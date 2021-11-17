$(document).ready(function () {
    // Timeout function to close alert messages after 3 seconds
    // Taken from the Code Institute 'I Think Therefore I Blog' walkthrough
    setTimeout(function () {
        let messages = $("#msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2000);

    // Modal launch script, url for the confirm delete button taken from data-delete-url attribute
    // Adapted from https://stackoverflow.com/questions/54806538/
    $(".manage-delete").click(function () {
        let del_url = $(this).data('delete-url');
        $("#manage-delete").attr("href", del_url);
        $("#booking-delete-modal").modal();
    });
});