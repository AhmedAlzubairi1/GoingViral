var current_player = 1;
var isDraw = false;
var atpEffect = false;
var gameEnd = false;
var t = null;
var coinfection = false;
$(document).ready(function () {
  $("#draw_button").click(function () {
    //First check if game is still on
    if (gameEnd) {
      $("#notification_text").html(
        "Game has already ended, to continue please refresh the page"
      );
      return;
    }
    //I should draw based on the current player
    if (!isDraw) {
      console.log("draw");
      $.ajax({
        type: "POST",
        url: "/draw",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(current_player), //"{\"name\":\"bob\"}" this is saying data would be this assuming name is bob. In short, we always send data by Json stringifying it
        success: function (result) {
          //sales=sales,clients=clients, current_id=current_id
          //var all_data = result["data"] //Doing result["bob"] would read bob data
          //var currentID=result["lastID"]
          console.log("success");
          //Now i make sure they cant draw anymore by setting isDraw to true, then i add to their card and reload the hand
          isDraw = true;

          $("#notification_text").html(result["drawnCard"]["name"] + " Drawn!");

          if (current_player == 1) {
            playerOne["hand"].push(result["drawnCard"]);
            loadhand(playerOne["hand"]);
          } else {
            playerTwo["hand"].push(result["drawnCard"]);
            loadhand(playerTwo["hand"]);
          }
        },
        error: function (request, status, error) {
          console.log("Error");
          console.log(request);
          console.log(status);
          console.log(error);
        },
      });
    } else {
      $("#notification_text").html(
        "Card already drawn, can't draw again until next turn."
      );
    }
  });

  $("#turn_button").click(function () {
    //First check if game is still on
    if (gameEnd) {
      $("#notification_text").html(
        "Game has already ended, to continue please refresh the page"
      );
      return;
    }
    // First check if I have drew already
    if (!isDraw) {
      $("#notification_text").html("You must draw first!");
      return;
    }
    //Next check if user has an immediate
    if (current_player == 1) {
      if (immediateExist(playerOne)) {
        $("#notification_text").html(
          "ERROR. You must play all your immediate cards first!"
        );
        return;
      }
    } else {
      if (immediateExist(playerTwo)) {
        $("#notification_text").html(
          "ERROR. You must play all your immediate cards first!"
        );
        return;
      }
    }
    //I should draw based on the current player
    // I need to also do an ajax call to update the player info
    if (coinfection == false) {
      if (current_player == 1) {
        isDraw = false;
        current_player = 2;
        loadhand(playerTwo["hand"]);
        $("#notification_text").html(
          "Player 1 Turn End, Player 2 Turn Start. Draw Card!"
        );
        $("#player_text").html("Player 2");
        $("#virus_image").attr("src", playerTwo["virusImage"]);
        $("#stage_image").attr("src", playerTwo["stageImage"]);
        //Now I need to update the backend side
        updatePlayer(playerOne, 1, true);
      } else {
        isDraw = false;
        current_player = 1;
        loadhand(playerOne["hand"]);
        $("#notification_text").html(
          "Player 2 Turn End, Player 1 Turn Start. Draw Card!"
        );
        $("#player_text").html("Player 1");
        $("#virus_image").attr("src", playerOne["virusImage"]);
        $("#stage_image").attr("src", playerOne["stageImage"]);
        // Now I need to update the backend side
        updatePlayer(playerTwo, 2, true);
      }
    }
    // just in case the user used coinfection, i don't want to go to next player's turn
    else {
      coinfection = false;
      if (current_player == 2) {
        isDraw = false;
        current_player = 2;
        loadhand(playerTwo["hand"]);
        $("#notification_text").html(
          "Coinfection used, player 2 starts new turn"
        );
        $("#player_text").html("Player 2");
        $("#virus_image").attr("src", playerTwo["virusImage"]);
        $("#stage_image").attr("src", playerTwo["stageImage"]);
      } else {
        isDraw = false;
        current_player = 1;
        loadhand(playerOne["hand"]);
        $("#notification_text").html(
          "Coinfection used, player 1 starts new turn"
        );
        $("#player_text").html("Player 1");
        $("#virus_image").attr("src", playerOne["virusImage"]);
        $("#stage_image").attr("src", playerOne["stageImage"]);
      }
    }
  });

  $("#stage_button").click(function () {
    //First check if game is still on
    if (gameEnd) {
      $("#notification_text").html(
        "Game has already ended, to continue please refresh the page"
      );
      return;
    }
    // First check that the user drew first
    if (!isDraw) {
      $("#notification_text").html("You must draw first!");
      return;
    }

    //Then check if he doesn't have an immidiate
    if (current_player == 1) {
      if (immediateExist(playerOne)) {
        $("#notification_text").html(
          "ERROR. You must play all your immediate cards first!"
        );
        return;
      }
    } else {
      if (immediateExist(playerTwo)) {
        $("#notification_text").html(
          "ERROR. You must play all your immediate cards first!"
        );
        return;
      }
    }

    //Evolve to next Stage
    /*
        I need to send in the current player I am looking at. I should check if I can upgrade my atp count as such.
        Note: siece I update the back end at everty turn, maybe I don't need to change the info yet. I can just set it aside. 
        */
    var player = null;
    if (current_player == 1) {
      player = {
        player: playerOne,
        number: 1,
      };
    } else {
      player = {
        player: playerTwo,
        number: 2,
      };
    }

    $.ajax({
      type: "POST",
      url: "/nextStage",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(player),
      success: function (result) {
        // First I update the player and then
        if (result["upGraded"] == true) {
          $("#notification_text").html("Going to next stage!");
          $("#atp_text").html("0");
        } else {
          $("#notification_text").html("Can't go to next stage!");
        }
        if (current_player == 1) {
          playerOne = result["player"];
          $("#stage_image").attr("src", playerOne["stageImage"]);
          if (playerOne["stage"] == 5) {
            gameEnd = true;
            $("#notification_text").html(
              "GAME END, YOU WON!. Refresh page to play again"
            );
          }
        } else {
          playerTwo = result["player"];
          $("#stage_image").attr("src", playerTwo["stageImage"]);
          if (playerTwo["stage"] == 5) {
            gameEnd = true;
            $("#notification_text").html(
              "GAME END, YOU WON!. Refresh page to play again"
            );
          }
        }
      },
      error: function (request, status, error) {
        console.log("Error");
        console.log(request);
        console.log(status);
        console.log(error);
      },
    });
  });
});

function updatePlayer(player, number) {
  var playerInfo = {
    player: player,
    number: number,
  };
  $.ajax({
    type: "POST",
    url: "/update",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(playerInfo),
    success: function (result) {
      if (number == 1) {
        playerOne = result["player"];
      } else {
        playerTwo = result["player"];
      }
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
}
// This is to update the screen with the requested player info

function loadhand(hand) {
  // I first empty what I have
  //<button type="button" id="0" onclick="hold(0)" class="extraButton">Click here to Hold instead</button>

  $("#hand").empty();
  for (card in hand) {
    // Then put everything in order from the hand. I should have the id be the index of the lcoation in the hand

    var newRow = $(
      "<img alt='Bootstrap Image Preview' id = '" +
        card +
        "' src='" +
        hand[card]["image"].toString() +
        "' onclick='playCard(" +
        card +
        ")' width='250' height='400' class='d-inline-block align-top' />"
    );
    $("#hand").append(newRow);
    if (hand[card]["name"].endsWith("Rapid Growth")) {
      newRow = $(
        "<button type='button' id = '" +
          card +
          "' onclick='hold(" +
          card +
          ")' class='extraButton'>"
      );
      newRow.html("Click here to Hold instead");
      $("#hand").append(newRow);
    }
    $("#hand").append($("<br><br>"));
  }
}
function immediateExist(player) {
  for (i in player["hand"]) {
    if (player["hand"][i]["immediate"]) {
      return true;
    }
  }
  return false;
}
function hold(index) {
  if (current_player == 1) {
    playerOne["hand"][index]["immediate"] = false;
  } else {
    playerTwo["hand"][index]["immediate"] = false;
  }
}
function playCard(index) {
  // Here I would play the card located at index value
  // Hardest piece of my code

  player = null;
  if (current_player == 1) {
    player = playerOne;
  } else {
    player = playerTwo;
  }
  if (immediateExist(player) && !player["hand"][index]["immediate"]) {
    $("#notification_text").html(
      "ERROR. You must play all your immediate cards first!"
    );
    return;
  }
  //First i remove the card and store it
  card = player["hand"][index];
  player["hand"].splice(index, 1);

  // Then I call the card associated with it
  if (card["name"].endsWith("ATP")) {
    playATP(player, card);
  } else if (card["name"].endsWith("Antibiotic")) {
    playAntibiotic(index, player, card);
  } else if (card["name"].endsWith("Antiviral")) {
    playAntiviral(index, player, card);
  } else if (card["name"].endsWith("Coinfection")) {
    playCoinfection(index, player, card);
  } else if (card["name"].endsWith("Fever")) {
    playFever(index, player, card);
  } else if (card["name"].endsWith("Gene Exchange")) {
    playGeneExchange(index, player, card);
  } else if (card["name"].endsWith("No Vaccine")) {
    playNoVaccine(index, player, card);
  } else if (card["name"].endsWith("Quarantine")) {
    playQuarantine(index, player, card);
  } else if (card["name"].endsWith("Rapid Growth")) {
    playRapidGrowth(index, player, card);
  } else if (card["name"].endsWith("Resistance")) {
    playATP(player, card);
  } else if (card["name"].endsWith("Hospitalization")) {
    playTreatement(index, player, card, "ebola");
  } else if (card["name"].endsWith("Bed Rest")) {
    playTreatement(index, player, card, "flu");
  }
}

function playATP(player, card) {
  player["atp"] += card["atp"];
  $("#atp_text").html(player["atp"]);
  $("#notification_text").html("Increasing ATP!");
  loadhand(player["hand"]);
}
function playAntibiotic(index, player, card) {
  $.ajax({
    type: "POST",
    url: "/draw2",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(current_player),
    success: function (result) {
      player["hand"].push(result["cards"][0]);
      player["hand"].push(result["cards"][1]);
      loadhand(player["hand"]);
      $("#notification_text").html(
        "Antibiotic activated, drawing 2 cards! Drew:  " +
          result["cards"][0]["name"] +
          " and " +
          result["cards"][1]["name"]
      );
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
}
function playAntiviral(index, player, card) {
  $("#notification_text").html(
    "Antiviral Activated, other player's hand has been discarded!"
  );
  if (player["player"] == 1) {
    playerTwo["hand"] = [];
    loadhand(playerOne["hand"]);
    updatePlayer(playerTwo, 2);
  } else {
    playerOne["hand"] = [];
    loadhand(playerTwo["hand"]);
    updatePlayer(playerOne, 1);
  }
}
function playCoinfection(index, player, card) {
  $("#notification_text").html(
    "Coinfection Activated, draw 1 card and skip other player"
  );
  $.ajax({
    type: "POST",
    url: "/draw",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(current_player), //"{\"name\":\"bob\"}" this is saying data would be this assuming name is bob. In short, we always send data by Json stringifying it
    success: function (result) {
      if (current_player == 1) {
        playerOne["hand"].push(result["drawnCard"]);
        loadhand(playerOne["hand"]);
      } else {
        playerTwo["hand"].push(result["drawnCard"]);
        loadhand(playerTwo["hand"]);
      }
      coinfection = true;
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
}

function playFever(index, player, card) {
  $("#notification_text").html("Fever Activated, discard hand!");
  player["hand"] = [];
  loadhand(player["hand"]);
  if (player["player"] == 1) {
    updatePlayer(playerOne, 1);
  } else {
    updatePlayer(playerTwo, 2);
  }
}

function playGeneExchange(index, player, card) {
  console.log(playerOne);
  console.log(playerTwo);
  if (player["player"] == 1) {
    // I need to check if there is a possible card
    if (playerTwo["hand"].length != 0) {
      index = Math.floor(Math.random() * playerTwo["hand"].length);
      card = playerTwo["hand"][index];
      playerTwo["hand"].splice(index, 1);
      playerOne["hand"].push(card);
      $("#notification_text").html(
        "Gene Exchange Activated, took " + card["name"] + " From enemy player"
      );
    } else {
      $("#notification_text").html(
        "Wasted Gene Exchange card :(. Player didn't have any cards to take"
      );
    }
  } else {
    if (playerOne["hand"].length != 0) {
      index = Math.floor(Math.random() * playerOne["hand"].length);
      card = playerOne["hand"][index];
      playerOne["hand"].splice(index, 1);
      playerTwo["hand"].push(card);
      $("#notification_text").html(
        "Gene Exchange Activated, took " + card["name"] + " From enemy player"
      );
    } else {
      $("#notification_text").html(
        "Wasted Gene Exchange card :(. Player didn't have any cards to take"
      );
    }
  }
  console.log(playerOne);
  console.log(playerTwo);
  loadhand(player["hand"]);
  updatePlayer(playerOne, 1);
  updatePlayer(playerTwo, 2);
}
function playNoVaccine(index, player, card) {
  if (card["immediate"]) {
    // Card is immediate so I can set it to false first

    card["immediate"] = false;
    //Now I can add a card
    $.ajax({
      type: "POST",
      url: "/draw",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(current_player), //"{\"name\":\"bob\"}" this is saying data would be this assuming name is bob. In short, we always send data by Json stringifying it
      success: function (result) {
        //After adding the drawn card, i can add the updated no vaccine card
        $("#notification_text").html(
          "Activating No vaccine Immediate., hold card and drew:" +
            result["drawnCard"]["name"]
        );

        if (current_player == 1) {
          playerOne["hand"].push(result["drawnCard"]);
          playerOne["hand"].push(card);
          loadhand(playerOne["hand"]);
        } else {
          playerTwo["hand"].push(result["drawnCard"]);
          playerTwo["hand"].push(card);
          loadhand(playerTwo["hand"]);
        }
      },
      error: function (request, status, error) {
        console.log("Error");
      },
    });
  } else {
    console.log("helooooo");
    //In this case, I know that the user has already used the immediate, so i just leave it dropped and add the atp
    console.log(card);
    if (current_player == 1) {
      playATP(playerOne, card);
      loadhand(playerOne["hand"]);
    } else {
      playerATP(playerTwo, card);
      loadhand(playerTwo["hand"]);
    }
  }
}
function playQuarantine(index, player, card) {
  $.ajax({
    type: "POST",
    url: "/quarantine",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(player),
    success: function (result) {
      t = result;
      console.log(result["player"]);
      if (result["downGraded"] == true) {
        $("#notification_text").html(
          "Quarantine activated, lowering your stage!"
        );
      } else {
        $("#notification_text").html(
          "Quarantine activated, shuffling back into deck!"
        );
      }
      if (current_player == 1) {
        console.log();
        playerOne = result["player"];
        $("#stage_image").attr("src", playerOne["stageImage"]);
        loadhand(playerOne["hand"]);
      } else {
        playerTwo = result["player"];
        $("#stage_image").attr("src", playerTwo["stageImage"]);
        loadhand(playerTwo["hand"]);
      }
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
}

function playRapidGrowth(index, player, card) {
  if (card["immediate"]) {
    console.log("rapid growth imm");
    // Here i want to go to next stage
    //Save atp and just cap it to max to guarantee a next stage
    var initialATP = player["atp"];
    player["atp"] = 1000;
    playerJson = {
      player: player,
      number: player["player"],
    };
    $.ajax({
      type: "POST",
      url: "/nextStage",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(playerJson),
      success: function (result) {
        // First I update the player and then
        if (result["upGraded"] == true) {
          $("#notification_text").html("Going to next stage!");
          $("#atp_text").html("0");
        } else {
          $("#notification_text").html("Can't go to next stage!");
        }
        if (current_player == 1) {
          playerOne = result["player"];
          $("#stage_image").attr("src", playerOne["stageImage"]);
          if (playerOne["stage"] == 5) {
            gameEnd = true;
            $("#notification_text").html(
              "GAME END, YOU WON!. Refresh page to play again"
            );
          }
        } else {
          playerTwo = result["player"];
          $("#stage_image").attr("src", playerTwo["stageImage"]);
          if (playerTwo["stage"] == 5) {
            gameEnd = true;
            $("#notification_text").html(
              "GAME END, YOU WON!. Refresh page to play again"
            );
          }
        }
        player["atp"] = initialATP;
        loadhand(player["hand"]);
      },
      error: function (request, status, error) {
        console.log("Error");
        console.log(request);
        console.log(status);
        console.log(error);
      },
    });
  } else {
    console.log("rapid growth regg");

    playATP(player, card);
    loadhand(player["hand"]);
  }
}

function playTreatement(index, player, card, virus) {
  // I need to aslo make sure if player has resistance, they can stop it
  if (current_player == 1 && playerTwo["virus"].endsWith(virus)) {
    // I now can attack player 2
    //Check if player 2 has resistance
    var found = false;
    for (i in playerTwo["hand"]) {
      if (playerTwo["hand"][i]["name"].endsWith("Resistance")) {
        //Resitance has been found
        playerTwo["hand"].splice(i, 1);
        found = true;
      }
    }
    if (found) {
      //Found so oppoenent can drop it
      $("#notification_text").html(
        "Opponent has Resitance to cancel your Treatement card"
      );
    } else {
      //In this case, no resistance was found, so that means I can get player 2's strongest card
      if (playerTwo["hand"].length == 0) {
        $("#notification_text").html(
          "Oppenent has no cards, wasted your Treatement effect"
        );
      } else {
        //I consider no atp as 0 atp
        atp = 0;
        enemyIndex = 0;
        enemyCard = playerTwo["hand"][0];
        for (i in playerTwo["hand"]) {
          if (playerTwo["hand"][i]["atp"] > atp) {
            enemyIndex = i;
            atp = playerTwo["hand"][i]["atp"];
            enemyCard = playerTwo["hand"][i];
          }
        }
        //Now get rid of the card
        playerTwo["hand"].splice(enemyIndex, 1);
        playerOne["hand"].push(enemyCard);
        $("#notification_text").html(
          "Stole enemy " + enemyCard["name"] + " card from oponent"
        );
      }
    }
  } else if (current_player == 2 && playerOne["virus"].endsWith(virus)) {
    // I now can attack player 2
    //Check if player 2 has resistance
    var found = false;
    for (i in playerOne["hand"]) {
      if (playerOne["hand"][i]["name"].endsWith("Resistance")) {
        //Resitance has been found
        playerOne["hand"].splice(i, 1);
        found = true;
      }
    }
    if (found) {
      //Found so oppoenent can drop it
      $("#notification_text").html(
        "Opponent has Resitance to cancel your Treatement card"
      );
    } else {
      //In this case, no resistance was found, so that means I can get player 2's strongest card
      if (playerOne["hand"].length == 0) {
        $("#notification_text").html(
          "Oppenent has no cards, wasted your Treatement effect"
        );
      } else {
        //I consider no atp as 0 atp
        atp = 0;
        enemyIndex = 0;
        enemyCard = playerOne["hand"][0];
        for (i in playerOne["hand"]) {
          if (playerOne["hand"][i]["atp"] > atp) {
            enemyIndex = i;
            atp = playerOne["hand"][i]["atp"];
            enemyCard = playerOne["hand"][i];
          }
        }
        //Now get rid of the card
        playerOne["hand"].splice(enemyIndex, 1);
        playerTwo["hand"].push(enemyCard);
        $("#notification_text").html(
          "Stole enemy " + enemyCard["name"] + " card from oponent"
        );
      }
    }
  } else {
    $("#notification_text").html(
      "Wasted your card, no player has virus to match with your treatement"
    );
  }
  loadhand(player["hand"]);
  updatePlayer(playerOne, 1);
  updatePlayer(playerTwo, 2);
  // Now i can update everything. Load, and update players
}

/*
$.ajax({
    type: "POST",
    url: "/draw",                
    dataType : "json",
    contentType: "application/json; charset=utf-8",
    data : JSON.stringify(current_player),
    success: function(result){
    },
    error: function(request, status, error){
        console.log("Error");
        console.log(request)
        console.log(status)
        console.log(error)
    }
});
*/
