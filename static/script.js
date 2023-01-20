
$(document).ready(function() {
    $(document).on("click", "#all_offers tbody tr", function() {
        // alert($(this).find("td:eq(0)").text());

        $.post("/user", {userID: $(this).find("td:eq(0)").text()})
        window.location.href = "/user"
    });

    $(document).on("click", "#all_requests tbody tr", function() {
        // alert($(this).find("td:eq(0)").text());

        $.post("/user", {userID: $(this).find("td:eq(0)").text()})
        window.location.href = "/user"
    });

    $(document).on("click", "#my_offering tbody tr", function() {
        // alert($(this).find("td:eq(0)").text());

        $.post("/user", {userID: $(this).find("td:eq(0)").text()})
        window.location.href = "/user"
    });

    $('.btn-primary.offer').click(function(e){
        // alert( $(this).closest("tr")   // Finds the closest row <tr> 
        // .find(".hide")     // Gets a descendent with class="nr"
        // .text());
        $.post("/", {offerID: $(this).closest("tr").find(".hide").text()})
        e.stopPropagation();
        window.location.href = "/"
    });

    $('.btn-primary.request').click(function(e){
        // alert( $(this).closest("tr")   // Finds the closest row <tr> 
        // .find(".hide")     // Gets a descendent with class="nr"
        // .text());
        $.post("/", {requestID: $(this).closest("tr").find(".hide").text()})
        e.stopPropagation();
        window.location.href = "/"
    });



    $(document).on("click", "#my_request tbody tr", function() {
        // alert($(this).find("td:eq(0)").text());

        $.post("/user", {userID: $(this).find("td:eq(0)").text()})
        window.location.href = "/user"
    });

    $(document).on("click", "#potential_offer tbody tr", function() {
        // alert($(this).find("td:eq(0)").text());

        $.post("/user", {userID: $(this).find("td:eq(0)").text()})
        window.location.href = "/user"
    });

    $(document).on("click", "#potential_request tbody tr", function() {
        // alert($(this).find("td:eq(0)").text());

        $.post("/user", {userID: $(this).find("td:eq(0)").text()})
        window.location.href = "/user"
    });
});