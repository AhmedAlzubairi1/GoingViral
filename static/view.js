var dateSet=false
var reviewSet=false
var t;
var undoStack=[]
$(document).ready(function(){
    //console.log(id)

    display(currentAnime)
   $("#editButton").click(function(){

    var newRow=$("<div class='row'>")

        var nextUserInput=$("<input id = 'reviewBox' placeholder='Insert Review Here' type = 'text'/>")
        newRow.append(nextUserInput)

        $("#review").append(newRow)
       reviewSet=true
       $(".submitButtons").css("visibility","visible")
       
   })
   $("#editDate").click(function(){
       dateSet=true
       var currentDate= $("#date").html()
       console.log(currentDate)
       $("#date").empty()
       var userInput=$("<input id = 'dateInput' placeholder='Insert Date Here' type = 'text'/>")
       userInput.val(currentDate)
       t=userInput
       $("#date").html(userInput)
       userInput.focus()
       $(".submitButtons").css("visibility","visible")
})
$("#submitChanges").click(function(){
console.log("SubmitButton")
if(reviewSet && dateSet){
var newDate=t.val().trim()

var insertedReview=$("#reviewBox").val()
    var reviewJSON;
    reviewJSON={
        "id":id,
        "combo":0
    }

    if(newDate.length!=0 && insertedReview.trim().length!=0){
        reviewJSON={
            "id":id,
            "review":insertedReview,
            "year":newDate,
            "combo":3

        }
    console.log(3)

    }
    else if(insertedReview.trim().length!=0){
        reviewJSON={
            "id":id,
            "review":insertedReview,
            "combo":1

        }
        console.log(1)

    }
    else if(newDate.length!=0){
        reviewJSON={
            "id":id,
            "year":newDate,
            "combo":2

        }
        console.log(2)

    }
    
    $.ajax({
        type: "POST",
        url: "/add_review",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(reviewJSON), 
        success: function(result){
            location.reload(true);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}
else if (dateSet){
    var newDate=t.val().trim()
    var reviewJSON;
    reviewJSON={
        "id":id,
        "year":newDate,
        "combo":2
    }
    console.log(2)

    if(newDate.length!=0){
        $.ajax({
            type: "POST",
            url: "/add_review",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(reviewJSON), 
            success: function(result){
                location.reload(true);
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });      

    }
    else{
        location.reload(true);
    }


}
else if (reviewSet && $("#reviewBox").val().length!=0){
    console.log("hiii")
    console.log($("#reviewBox").val())
    var  reviewJSON={
        "id":id,
        "review":$("#reviewBox").val(),
        "combo":1

    }
    console.log(reviewJSON)
    console.log(1)

    $.ajax({
        type: "POST",
        url: "/add_review",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(reviewJSON), 
        success: function(result){
            location.reload(true);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}
else{
    location.reload(true);
}



})
$("#discardChanges").click(function(){
    location.reload(true);
})

$("#undo").click(function(){

    var data_to_save= [id,undoStack.pop()]

    $.ajax({
        type: "POST",
        url: "/undo",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save), //"{\"name\":\"bob\"}" this is saying data would be this assuming name is bob. In short, we always send data by Json stringifying it
        success: function(result){
            if(undoStack.length<=0){
               
                $("#undo").css("visibility","hidden")

            }

            showReviews(result["reviewList"])
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });


})

})

function display(anime){
    $("#title").text(anime["title"])
    $("#animePic").attr("src",anime["image"])
    $("#animePic").attr("alt",anime["title"])
    $("#info").text(anime["info"])
    $("#date").text(anime["year"])
    showReviews(anime["reviews"])

}
function deleteButton(element){

    var numberVersion=parseInt(element.id)
    //numberVersion-=1
    var data_to_save = [id,numberVersion]
    console.log(numberVersion)
    undoStack.push(numberVersion)
    $("#undo").css("visibility","visible")
    $.ajax({
        type: "POST",
        url: "/delete_review",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save), //"{\"name\":\"bob\"}" this is saying data would be this assuming name is bob. In short, we always send data by Json stringifying it
        success: function(result){
            showReviews(result["reviewList"])
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
    



}


function showReviews(reviewList){
    console.log(reviewList)
    var count=1
    var actual=0
    $("#review").empty()
    for(i in reviewList){
        if(!reviewList[i][1]){
            var newRow=$("<div class='row'>")
            var deleteButtonColumn=$("<div class='col-md-3'>")
            var deleterTrigger ="onclick='deleteButton(this)'"
            var deleteButton= $("<button id=" + actual+" "+ deleterTrigger+ " >")
            deleteButton.text("X")
            deleteButton.addClass("deleteButton")
            deleteButtonColumn.html(deleteButton)


            newRow.text(count + ". " + reviewList[i][0])
            newRow.append(deleteButton)
            count++
    
            $("#review").append(newRow)

        }
        actual+=1

    }

}


