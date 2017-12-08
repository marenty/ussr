function OnOffEditClientForm()
{
  if (document.getElementById('edit-client-box').style.display == "block") {
      document.getElementById('edit-client-box').style.display = "none";
      $( '#client-edit-form').remove();
  }
  else {
    document.getElementById('edit-client-box').style.display = "block";
  }
}

function OnOffEmailForm()
{
  if (document.getElementById('email-box').style.display == "block") {
      document.getElementById('email-box').style.display = "none";
  }
  else {
    document.getElementById('email-box').style.display = "block";
  }
}


$(document).ready(function() {


  $( '#client-form' ).submit(function( event ){
      event.preventDefault();
      console.log("form submitted!");
      document.getElementById('client-form').style.color = "blue";
      create_client();
  });

  $( document ).on('click', '#client-edit-button', function( event ){
      event.preventDefault();
      console.log("edit form submitted!");
      console.log($("#client-edit-form").serialize());
      console.log($('#client-edit-button').val());
      edit_client($('#client-edit-button').val());
  });


  function edit_client(id) {
    console.log("edit post is working!") // sanity check
    console.log($("#client-edit-form").serialize());
    console.log(id)
    $.ajax({
        url : "/clients/edit_client/", // the endpoint
        type : "POST", // http method
        data : $('#client-edit-form').serialize() + "&id=" + id,

        // handle a successful response
        success : function(response) {
            $('#body').html(response);
            console.log("success"); // another sanity check
        },

    });
  }

  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });


function create_client() {
    console.log("create post is working!") // sanity check
    console.log($("#client-form").serialize());
    $.ajax({
        url : "/clients/create_client/", // the endpoint
        type : "POST", // http method
        data : $('#client-form').serialize(), // data sent with the post request

        // handle a successful response
        success : function(response) {
            $('#client-form').trigger("reset");
            $('#body').html(response);
            console.log("success"); // another sanity check
        },

    });
};

$( '#client-table-form' ).submit(function( event ){
    event.preventDefault();
    console.log("DELETE");
    delete_client();
});

$( '.edit-button' ).click(function( event ){
    event.preventDefault();
    console.log($(this).val());
    edit_client_form_genertion($(this));
});

$( '.email-button' ).click(function( event ){
    event.preventDefault();
    let id = $(this).val();
    email_check(id);
    $( '#email-form' ).submit(function( event ){
      event.preventDefault();
      send_mail(id)
      $( '#email-form' ).off("submit");
    });

});

function email_check(id) {
    $.ajax({
      url : "/clients/email_check/", // the endpoint
      type : "POST", // http method
      data : {'id' : id }, // data sent with the post request
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

function send_mail(id) {
  $.ajax({
    url : "/clients/send_email/", // the endpoint
    type : "POST", // http method
    data : $('#email-form').serialize() + "&id=" + id,

    success : function(response) {
        console.log(response);
        $('#email-form').trigger("reset");
        OnOffEmailForm();

    },
});
};

function delete_client() {
    console.log("Delete") // sanity check
    console.log($("#client-table-form").serialize());
    $.ajax({
        url : "/clients/delete_clients/", // the endpoint
        type : "POST", // http method
        data : $('#client-table-form').serialize(), // data sent with the post request

        // handle a successful response
        success : function(response) {
            $('#client-form').trigger("reset");
            $('#body').html(response);
            console.log("success"); // another sanity check
        },

    });
};

function edit_client_form_genertion(id) {
    console.log("Edit") // sanity check
    console.log(id.val());
    $.ajax({
        url : "/clients/edit_client_form/", // the endpoint
        async: false ,
        type : "POST", // http method
        data : {"id" : id.val()}, // data sent with the post request

        // handle a successful response
        success : function(response) {
            $('#edit-client-form-box').append(response);
            console.log(response); // another sanity check
            OnOffEditClientForm();
        },

    });
};

});
