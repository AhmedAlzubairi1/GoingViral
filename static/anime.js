$(document).ready(function(){

        function start (listOfCards){
            $("#display").empty()
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
                    $("#display").append(newRow)
                    $("#display").append($("<br>"))
                }


            }
 
        }

        start(cards)



})
