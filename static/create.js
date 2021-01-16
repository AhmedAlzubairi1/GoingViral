$(document).ready(function(){
    $("#title").keyup(function(event){
        $("#title").removeClass("warning")
        $("#title").attr("placeholder","Type Title Here")

    })

    $("#imageURL").keyup(function(event){
        $("#imageURL").removeClass("warning")
        $("#imageURL").attr("placeholder","Type Image URL Here")

    })

    $("#synposisBox").keyup(function(event){
        $("#synposisBox").removeClass("warning")
        $("#synposisBox").attr("placeholder","Type Synopsis Here")

    })
    $("#year").keyup(function(event){
        $("#year").removeClass("warning")
        $("#year").attr("placeholder","Type Year of Release Here")

    })

    function checkTitle(){
        var currentText=$("#title").val().trim()
        if(currentText.length==0){
            $("#title").val("")
            $("#title").attr("placeholder","Missing Text")
            $("#title").addClass("warning")
            return false

        }
        return true

    }
    function checkImage(){
        var currentText=$("#imageURL").val().trim()

        if(currentText.length==0){
            $("#imageURL").val("")
            $("#imageURL").attr("placeholder","Missing URL")
            $("#imageURL").addClass("warning")
            return false

        }

          //Source:https://forums.asp.net/t/2018312.aspx?How+to+check+an+image+url+is+exist+or+not+using+Jquery
         var returnValue=true
         var img = new Image();
         img.src = $("#imageURL").val();   
         if (img.height != 0) {

        } else {
             returnValue= false ;
         }
         
         if(!returnValue){
            $("#imageURL").val("")
            $("#imageURL").attr("placeholder","Invalid URL, not referncing Image")
            $("#imageURL").addClass("warning")
            return false

        }
         return returnValue

  //  return returnValue



    }

   
    function checkAbout(){
        var currentText=$("#synposisBox").val().trim()
        if(currentText.length==0){
            $("#synposisBox").val("")
            $("#synposisBox").attr("placeholder","Missing Text")
            $("#synposisBox").addClass("warning")
            return false

        }
        return true


    }
    function checkYear(){
        var currentText=$("#year").val().trim()
        if(currentText.length==0){
            $("#year").val("")
            $("#year").attr("placeholder","Missing Text")
            $("#year").addClass("warning")
            return false

        }
        else if (isNaN($("#year").val())){
            $("#year").val("")
            $("#year").attr("placeholder","Didn't insert a valid number")
            $("#year").addClass("warning")

            return false
        }
        return true



    }
    $("#create").click(function(){
       var a= checkTitle()
       var b=  checkImage()
       var c= checkAbout()
      var d=  checkYear()
        if(a && b && c && d){
            createAnime()
        }


    })


})

function createAnime(){
    var animeJSON={
        "id":current_id,
        "title":$("#title").val(),
        "image":$("#imageURL").val(),
        "info":$("#synposisBox").val(),
        "year":Number($("#year").val()),
        "reviews":[]
    }
    if($("#review").val().trim().length!=0){
        var temp=[$("#review").val()]
        animeJSON["reviews"]=temp

    }
    $.ajax({
        type: "POST",
        url: "/add_anime",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(animeJSON), //"{\"name\":\"bob\"}" this is saying data would be this assuming name is bob. In short, we always send data by Json stringifying it
        success: function(result){
 //sales=sales,clients=clients, current_id=current_id
            //var all_data = result["data"] //Doing result["bob"] would read bob data
            var currentID=result["lastID"]


            var url= "/view/"+currentID
            var notifyText= $("<b> New Item Successfully Creatd. </b>" + "<a href='"+ url + "'> See It Here </a>")
            $("#notify").append(notifyText)
            $("#title").val("")
            $("#imageURL").val("")
            $("#synposisBox").val("")
            $("#year").val("")
            $("#review").val("")
            $("#title").focus()



            
            /*
<div class="Notification center">
<b>New item successfully created.</b>
<a href="view/1">See It Here</a>
</div>
            
            var base_url = window.location.origin;
            var nextURL= base_url+url
            window.location.replace(nextURL)
        */
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });


}


/*

        var returnValue=true
            $.get($("#imageURL").val())
        .done(function() { 
            // Do something now you know the image exists.


        }).fail(function() { 
            // Image doesn't exist - do something else.
            $("#imageURL").val("")
            $("#imageURL").attr("placeholder","Invalid URL")
            $("#imageURL").addClass("warning")
            returnValue=false

        })
        return returnValue



*/
