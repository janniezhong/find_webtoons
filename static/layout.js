$(document).ready(function(){
    $("#search").on("submit", function(event) {

        let input = $("#searchinput").val().trim()

        // alert("_" + input+"_");
    
        if (input.length == 0){
            event.preventDefault();
            $("#searchinput").val("")
            $("#searchinput").focus()
        }
     });
})