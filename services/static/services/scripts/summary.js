function submitreservation(){
  $.ajax({
      url : "/services/save_reservation/", // the endpoint
      type : "POST", // http method
      data : $('#reservation-form').serialize(), // data sent with the post request

      // handle a successful response
      success : function(response) {
          if (response == 'success'){
            $('#success-modal').modal('show');
            $('#success-modal-box').before('<p id = "summary-last-text">Rezerwacja sie udala</p>');
          }

          else if (response == 'fail') {
            $('#success-modal').modal('show');
            $('#Edit-Title').html('Przekroczyłeś limit');
            $('#success-modal-box').before('<p id = "summary-last-text">Przekroczyleś maksymalny czas możliwy do zarezerwowania.</p>');
          }
      },
      error : function() {
        $('#success-modal').modal('show');
        $('#Edit-Title').html('Błąd');
        $('#success-modal-box').before('<p id = "summary-last-text">Rezerwacja się nie udała. Spróbuj ponownie.</p>');
      }
  });
}

$(document).ready(function() {

  $('#select-service-group').change(function(){
    showSelectService(this.value);

  });

  $('#submit').click(function(){
    submitreservation()
  });

  $('#resignation').click(function(){
    window.location.replace("/services/reservation/");
  });

  $('#reservation-form').on('submit', function(e){
  e.preventDefault();
});

});
