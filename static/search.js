
function display_search_results(results){

    $("search-results").empty()
    if (results.length == 0){
      console.log("hi")
      let no_results = $("<div> No results found! Try looking on the official <a class='toast-link' href='https://www.webtoons.com/en/'>Webtoon</a> site.</div>")
      $("#search-results").append(no_results)
    } else {
      $.each(results, function(i, result){
        let new_row = $("<div class = 'row'> </div>")
        let img_col = $("<div class='col-md-3'> <a href='/view/" +result["id"]+ "'><img src='"+result["image"]+ "' height='200px' width='auto' alt='search result cover image'> </a>")
        let info_col = $("<div class='col-md-9'>")
  
        let title = $("<div class = 'search-result-title'>")
        let title_accented = addAccents(result["title"], search_string)
        title.append(title_accented)

        if (result["complete"] == "true"){
          title.append($("<img class ='icon check' src = 'https://www.venzagroup.com/wp-content/uploads/transparent-green-checkmark-md.png' alt='check icon' width='20px' height='auto'></img>"))
        } else {
          title.append($("<img class ='icon check' src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Eo_circle_green_letter-x.svg/480px-Eo_circle_green_letter-x.svg.png' alt='x icon' width='20px' height='auto'></img>"))

        }
  
        let author = $("<div class = 'search-result-author'>")
        let author_accented = addAccents(result["author"], search_string)
        author.append(author_accented)
  
        let summary = $("<div class = 'search-result-summary'>")
        let j = result["summary"].indexOf(search_string)      
        let temp = result["summary"].substring(j-30,j+220)
        let summary_accented = addAccents(result["summary"].substring(j-30,j+220), search_string)
  
  
        summary_accented = "..." + summary_accented + "...";
        summary.append(summary_accented)
  
  
    
      info_col.append(title)
      info_col.append(author)
      info_col.append(summary)
      new_row.append(img_col)
      new_row.append(info_col)
      $("#search-results").append(new_row)
  
      })
    }

  
  }

  function addAccents(string, search_string){
    //search-result-accent
    let x = string.toLowerCase()
    let y = search_string.toLowerCase()
    let index = x.indexOf(y);
    //get indices of string that match

    while (index != -1){
      x = x.slice(0, index) + "<span class='search-result-accent'>" + x.slice(index, index+search_string.length) + "</span>" + x.slice(index+search_string.length)
      string = string.slice(0, index) + "<span class='search-result-accent'>" + string.slice(index, index+search_string.length) + "</span>" + string.slice(index+search_string.length)
      
      index += ("<span class='search-result-accent'>").length
      index += search_string.length
      index = x.indexOf(y, index);
    }


    return string

  }
  
  $(document).ready(function(){
    display_search_results(search_results)
  })