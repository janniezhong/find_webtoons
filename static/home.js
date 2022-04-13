function displayPopularList(data){
    //empty old data
    $("#popularimg").empty()
    $("#populartext").empty()

    //insert all new data
    $.each(data, function(i, datum){
        if (i < 3){
            let new_popular_img = $("<div class = 'col-md-4'> <a href='/view/"+ datum["id"]+"'> <img src='" + datum["image"] + "' alt= 'popular webtoon cover art' class ='more_img'> </a> </div>")
            $("#popularimg").append(new_popular_img)

            let new_label_div = $("<div class = 'col-md-4 more_text'> </div>")
            let new_label_span=$("<span> <a class = 'more_link' href='/view/"+ datum["id"]+"'>" +"<b>" + datum["title"]+ "</b>"+"</a> <i>by " + datum["author"]+" </i></span>")
            $(new_label_div).append(new_label_span)
            $("#populartext").append(new_label_div)
        }

    })
}

 
$(document).ready(function(){
    //when the page loads, display all the names
    displayPopularList(most_popular)

})