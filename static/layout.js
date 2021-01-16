var isNumber=true
var lastSearch=""
var onSearch=false;
var currentList=[]




/*

$(document).ready(function(){
    //init()
    $("#clientBox").autocomplete({ 
        source: animeList
    });

})
*/

$(document).ready(function(){
    $("#submitButton").click(function(){

        //newPostAttempt()
        searchAnime($("#clientBox").val())


    })
    $("#clientBox").keyup(function(event){
        if($("#clientBox").val().length!=0){

            $("#clientBox").removeClass()
            
            $("#clientWarn").text("")
           // $("#clientBox").attr("placeholder", "Client")
        }
        if (event.keyCode==13){
            console.log("entered")
            searchAnime($("#clientBox").val())      
                 // alert("pressing enter")
        }
        

    })

})
/*
function deleteButton(element){

    var numberVersion=parseInt(element.id)
    var data_to_save = numberVersion
    $.ajax({
        type: "POST",
        url: "/delete_anime",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save), //"{\"name\":\"bob\"}" this is saying data would be this assuming name is bob. In short, we always send data by Json stringifying it
        success: function(result){
 //sales=sales,clients=clients, current_id=current_id
            //var all_data = result["data"] //Doing result["bob"] would read bob data
 
            if(onSearch){
                refresh()

            }



            
 
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
    



}

*/


function start (listOfCards){
    console.log("Reading cards")
    $("#baseHTML").empty()
    var dis=$("<div class='container' id='display'>")
    var newRow=$("<div class='row'>")
    for (i in listOfCards){
        if(i%3==0){
            newRow=$("<div class='row'>")
        }
        var colum=$("<div class='col-md-4'>")
        var card=$("<div class='card' style='width: 9rem;'>")
        var hyperLink=$("<a href='/view/"+ listOfCards[i].id.toString() + "'" +">")
        var imgTag=$("<img src='"+ listOfCards[i].image.toString() + "' class ='card-img-top' alt='"+listOfCards[i].title.toString()+"' >")
        hyperLink.html(imgTag)
        var cardBody= $("<div class='card-body'> <p class='card-text'>"+ listOfCards[i].title.toString() + "</p> </div>")
        card.append(hyperLink)
        card.append(cardBody)
        colum.append(card)
        newRow.append(colum)
        
        if(i%3==2 || i==(listOfCards.length-1)){
            dis.append(newRow)
            dis.append($("<br>"))
        }




    }
    $("#baseHTML").append(dis)

}




function updateDatabase(requestedAnime){
     //console.log("requested anime on updatedatabse")
     //console.log(requestedAnime)
    
    $.ajax({
        async:false,
        type: "POST",
        url: "/search",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(requestedAnime), //"{\"name\":\"bob\"}" this is saying data would be this assuming name is bob. In short, we always send data by Json stringifying it
        success: function(result){
 //sales=sales,clients=clients, current_id=current_id
            //var all_data = result["data"] //Doing result["bob"] would read bob data
            currentList=result["requestList"]
            //console.log(currentList)
            //console.log("printed the current list, now printing results")
            console.log("leaving")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}
function searchAnime(requestedAnime){
    onSearch=true;
    
    updateDatabase(requestedAnime)

    //I SHOULD TRY TO MAKE SURE TO RECIEVE UPDATED SEARCH ANIME LISTS RIGHT HERE
    //$("#logs").empty()
    //No, sales is the whole animeList
    var found=false
    
    //console.log("Current List after getting it is :")
    //console.log(currentList)
    console.log(currentList)
    if(currentList.length !=0)
        $("#baseHTML").empty()
    for(i in currentList){
        
            //console.log("found")
            found=true
            
            

        start(currentList)

        
    }
    console.log("in if")
    if (!found){
        console.log("Not FOund")
        $("#clientWarn").text("0 Results")
        $("#clientBox").addClass("warning")
        $("#clientBox").focus()

    }
    else{
        lastSearch=requestedAnime
        $("#clientBox").val("")
        console.log("Displaying results")
        $("#clientWarn").text("" + currentList.length+  " Results")

    }


}
