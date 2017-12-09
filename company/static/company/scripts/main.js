$(document).ready(function(){

  function get_calendar(service_code) {
      $.ajax({
        url : "/clients/email_check/", // the endpoint
        type : "POST", // http method
        data : {'service_code' : service_code,
      "date_start" : new Date().toLocaleString(),
      "date_finish" :
 }, // data sent with the post request
        success : function(response) {
            console.log(response.email);
            if ( response.email == true ){
              OnOffEmailForm();
            }
            else{
              alert("Klient nie podal adresu e-mail!");
            }
        },
    });
  };

});
