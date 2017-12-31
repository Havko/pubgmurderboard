$(document).foundation()
function compare(a,b) {
    if (a.total_kills < b.total_kills)
      return 1;
    if (a.total_kills > b.total_kills)
      return -1;
    return 0;
  }
var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://uprbu535he.execute-api.us-east-1.amazonaws.com/prod/players",
    "method": "GET",
    "headers": {

    }
  }
  
  $.ajax(settings).done(function (response) {
    var sorted_order = response.sort(compare);
    //console.log(sorted_order);
    for (var i = 0; i < sorted_order.length; i++){
        $('#leaderboard').append('<tr><td class="tabledata">'+sorted_order[i].player_id+'</td><td class="tabledata">'+sorted_order[i].total_kills+'</td></tr>');
    }
  });


  
