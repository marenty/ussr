function get_all_reservations(){
  $.ajax({
      url : "/services/get_all_future_reservations/", // the endpoint
      type : "POST", // http method
      data : {}, // data sent with the post request

      // handle a successful response
      success : function(response) {
          $('#service-table').empty();
          $('#service-table').html(response);
      },

  });

}

function get_all_past_reservations(){
  $.ajax({
      url : "/services/get_all_past_reservations/", // the endpoint
      type : "POST", // http method
      data : {}, // data sent with the post request

      // handle a successful response
      success : function(response) {
          $('#service-table').empty();
          $('#service-table').html(response);
      },

  });

}
