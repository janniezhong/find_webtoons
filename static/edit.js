function submitValidation() {
    // sanitize inputs

    let error_list = []
    let title = $("#title").val().trim()
    let author = $("#author").val().trim()
    let summary = $("#summary").val().trim()
    let rating = $("#rating").val().trim()
    let complete = $("#complete").val().trim()
    let image = $("#image").val().trim()
    let ep1 = $("#ep1").val().trim()
    let ex_art = $("#ex-art").val().trim()
    let reviews = $("#reviews").val().trim()
    let more_titles = $("#more-titles").val().trim()


    if (title.length <= 0) {
        error_list.push("Title must not be whitespace or empty")
    }

    if (author.length <= 0) {
        error_list.push("Author must not be whitespace or empty")
    }

    if (summary.length <= 0) {
        error_list.push("Summary must not be whitespace or empty")
    }

    if (rating.length <= 0) {
        error_list.push("Rating must not be whitespace or empty")
    } else {
        rating = parseFloat(rating);

        if (isNaN(rating)){
            error_list.push("Rating must be a number")

        } else if (rating < 0 || rating > 10){
            error_list.push("Rating must between 0 and 10")
        }
        
    }

    if (complete.length <= 0) {
        error_list.push("Complete must not be whitespace or empty")
    } else if (complete == "yes"){
        complete = "true"
    } else if (complete =="no"){
        complete = "false"
    } else {
        error_list.push("Complete must be yes or no")
    }

    if (image.length <= 0) {
        error_list.push("Cover Art URL must not be whitespace or empty")
    } else {
        let url;
        try {
            url = new URL(image);
        } catch (_) {
            error_list.push("Cover Art URL is not a valid URL")
        }
    }

    if (ep1.length <= 0) {
        error_list.push("First episode URL must not be whitespace or empty")
    } else {
        let url;
        try {
            url = new URL(ep1);
        } catch (_) {
            error_list.push("First episode URL is not a valid URL")
        }
    }


    let ex_art_list = []
    if (ex_art.length <= 0) {
        error_list.push("Example Art URLs must not be whitespace or empty")
    } else {
        ex_art_list = ex_art.split(/\r?\n/)
        ex_art_list.forEach(element => {
            let url;
            try {
                url = new URL(element);
            } catch (_) {
                error_list.push("An example art URL is not a valid URL")
                return;
            }
        })
    }

    let reviews_list = []
    if (reviews.length <= 0) {
        error_list.push("Reviews must not be whitespace or empty")
    } else {
        reviews_list = reviews.split(/\r?\n/)
        reviews_list= reviews_list.map(element => {
            return element.trim();
        });
        reviews_list = reviews_list.filter(element => {
            return element !== '';
        });
    }

    let more_titles_list = []
    if (more_titles.length <= 0) {
        error_list.push("More Titles must not be whitespace or empty")
    } else {
        more_titles_list = more_titles.split(",")
        more_titles_list=more_titles_list.map(element => {
            return element.trim();
          });
        more_titles_list = more_titles_list.filter(element => {
            return element !== '';
          });
    }

    // if valid, go on to submitForm
    if (error_list.length == 0) {
        submitForm(title, author, summary, rating, complete, image, ep1, ex_art_list, reviews_list, more_titles_list);

    } else {
        // if not, pop up modal and show errors

        $("#errors_list").empty()
        $.each(error_list, function (i, error) {
            let new_error = $("<li>");
            $(new_error).append(error)
            $("#errors_list").append(new_error)
        })
        $(".error-modal").addClass("active")

    }
}

function submitForm(title, author, summary, rating, complete, image, ep1, ex_art_list, reviews_list, more_titles_list) {
    // ajax to submit form

    console.log("hi there!" + complete)
    let new_data = {
        "id": item_info["id"],
        "title":title,
        "author": author,
        "summary": summary,
        "rating": rating,
        "complete": complete,
        "image":image,
        "ep1": ep1,
        "art_img": ex_art_list,
        "reviews": reviews_list,
        "more_like_this": more_titles_list
    }

    $.ajax({
        type: "POST",
        url: "/edit_data",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_data),
        success: function(result){
            id= result["id"]
            window.location.href="/view/"+id
            console.log("success!")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

function preload_info(item_info){
    $("#title").val(item_info["title"])
    $("#author").val(item_info["author"])
    $("#rating").val(item_info["rating"])
    $("#summary").val(item_info["summary"])
    console.log(item_info["complete"])
    if (item_info["complete"] == "true"){
        $("#complete").val("yes")
    } else {
        $("#complete").val("no")
    }
    $("#image").val(item_info["image"])
    $("#ep1").val(item_info["ep1"])

    let exArtList = item_info["art_img"]
    let exarttext = ""
    for (let i = 0; i < exArtList.length; i++){
        exarttext+=exArtList[i]
        exarttext+="\n"
    }
    $("#ex-art").val(exarttext.trim())


    let reviewsList = item_info["reviews"]
    let reviews = ""
    for (let i = 0; i < reviewsList.length; i++){
        reviews+=reviewsList[i]
        reviews+="\n"
    }
    $("#reviews").val(reviews.trim())

    let more_like_this = ""
    console.log(more_titles)
    for (let i = 0; i < more_titles.length; i++){
        more_like_this+=more_titles[i]
        more_like_this+=", "
    }
    $("#more-titles").val(more_like_this.trim())
}

$(document).ready(function () {
    //when the page loads, display
    preload_info(item_info)
    $(".edit-submit-button").click(function () {
        submitValidation()
    })

    $(".toast").toast({
        delay: 20000
    }); 


    $(".edit-modal-yes-button").click(function(){
        window.location.href="/view/"+ item_info["id"]
    })

    $(".edit-modal-no-button").click(function(){
        $(".discard-modal").removeClass("active")
    })

    // modal stuff

    $("#close-modal").click(function () {
        $(".error-modal").removeClass("active")
    })

    $(".edit-cancel-button").click(function(){
        $(".discard-modal").addClass("active")
    })
})
