// JavaScript script that adds, removes and clears LI elements
// from a list when the user clicks:
$(document).ready(() => {
    $("DIV#add_item").click( function () {
        var newItem = $("<li>Item</li>");
        $("ul.my_list").append(newItem);
    });
    $("DIV#remove_item").click( function () {
        $("ul.my_list li:last-child").remove();
    });
    $("DIV#clear_list").click( function () {
        $("ul.my_list").empty();
    });
});