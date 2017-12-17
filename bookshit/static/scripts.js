$(document).ready(function() {

    $("#target").click(function () {
        console.log("Handler for .click() called.");
    });

    $("#other").click(function () {
        $("#target").click();
    });
});
