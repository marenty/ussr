function resignation(id_resources_usage){
  $.ajax({
      url : "/services/service_resignation/", // the endpoint
      type : "POST", // http method
      data : {'id_resources_usage' : id_resources_usage}, // data sent with the post request

      // handle a successful response
      success : function(response) {
        $('#resignation-message').html(response);
      },

  });
}

function OnOffResignationWindow()
{
  if (document.getElementById('reservation-resignation-box').style.display == "block") {
      document.getElementById('reservation-resignation-box').style.display = "none";
  }
  else {
    document.getElementById('reservation-resignation-box').style.display = "block";
  }
}

function show_confirmation_window(chosen){

  OnOffResignationWindow();

  $('#confirm-button').click(function(e){
    e.preventDefault();
    console.log(chosen);
    resignation(chosen);
    OnOffResignationWindow();
  });

  $('#decline-button').click(function(e){
    e.preventDefault();
    OnOffResignationWindow();
    console.log('Declined')
    $( "#confirm-button" ).unbind();
    $( "#decline-button" ).unbind();
  });
}

$(document).ready(function() {

  $('.resignation-button').click(function(e){
    e.preventDefault();
    var chosen = this.value;
    show_confirmation_window(chosen);
  });


});
