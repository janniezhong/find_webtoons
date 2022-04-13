function displayReviewList(reviews) {
    //empty old data
    $("#reviews_list").empty()
    let charCount = 0;
    const maxCount = 350;
    $.each(reviews, function (i, review) {
        let new_review;
        if (charCount + review.length <= maxCount) {
            new_review = $("<li>")
            $(new_review).append(review)

            charCount += review.length
            if (!(charCount <= maxCount - 75)) {
                $(new_review).append("... <button class='see_more' id='review' type='button'>See More</button>")
                $("#reviews_list").append(new_review)
                return false;
            }
            $("#reviews_list").append(new_review)

        } else {
            new_review = $("<li>")
            $(new_review).append(review.substring(0, maxCount - charCount))
            $(new_review).append("... <button class='see_more' id='review' type='button'>See More</button>")
            $("#reviews_list").append(new_review)
            return false;
        }
    })

}

function getMoreLikeThis(id){
    let id_to_get = {"id": id}

    $.ajax({
        type: "POST",
        url: "/get_more_like_this",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(id_to_get),
        success: function(result){
            moreLikeThis=result["more_like_this"]
            displayMoreLikeThis(moreLikeThis)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

function displayMoreLikeThis(more){
    $("#morelikethisimg").empty()
    $("#morelikethistext").empty()

    $.each(more,function(i, webtoon){
        if (i < 3){
            let new_more = $("<div class = 'col-md-4'> <a href='/view/"+ webtoon["id"]+"'> <img src='" + webtoon["image"] + "' class ='more_img' alt = 'more like this cover art'> </a> </div>")
            $("#morelikethisimg").append(new_more)

            let new_labels = $("<div class = 'col-md-4 more_text'> <a class = 'more_link' href='/view/"+ webtoon["id"]+"'>" +webtoon["title"]+"</a></div>")
            $("#morelikethistext").append(new_labels)

        }
    })

}

$(document).ready(function () {
    //when the page loads, display
    displayReviewList(item_info["reviews"])
    getMoreLikeThis(item_info["id"])





    // modal stuff

    $("#summary.see_more").click(function () {
        $(".see_more_modal").addClass("active")
        $("#modal-summary").empty()
        $("#modal-summary").append("<p>" + item_info["summary"])
    })
    $("#review.see_more").click(function () {
        $("#full_reviews_list").empty()
        $.each(item_info["reviews"], function (i, review) {
            let new_review = $("<li>");
            $(new_review).append(review)
            $("#full_reviews_list").append(new_review)
        })
        $(".see_more_modal").addClass("active")
    })
    $("#close-modal").click(function () {
        $(".see_more_modal").removeClass("active")
        $("#modal-summary").empty()
        $("#full_reviews_list").empty()

    })
})
