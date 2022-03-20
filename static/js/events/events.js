$(document).ready(function() {
  const allEventsTab = new bootstrap.Tab(document.querySelector("#allevents-tab"));


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + '=') {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      }
    
      $.ajaxSetup({
        beforeSend: function (xhr, settings) {
          if (
            !(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))
          ) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
          }
        },
      });
  // Ajax call handling create event
      $('body').on('click', '.createEvent', function(e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/create/",
          success: function (response) {
            // $('.modalBody').html(response);
            // $('.modal-title').html("Create Event");
            // $('#id_tags').select2({
            //   maximumSelectionLength: 3,
            // });
    
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
    // Ajax call handling update event
      $('body').on('click', '.updateEvent', function(e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/update_event/"+$(this).attr('id'),
          success: function (response) {
            $('.modalBody').html(response);
            $('.modal-title').html("Update Event");
            $('#id_tags').select2({
              maximumSelectionLength: 3,
            });
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });

      // Ajax call handling delete event
      $('body').on('click', '.deleteEvent', function(e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/delete_event/"+$(this).attr('id'),
          success: function (response) {
            $('.modalBody').html(response);
            $('.modal-title').html("Delete Event");
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });

      // Ajax call handling get request of showing attendees list
      $('body').on('click', '.attendees-list', function(e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/event/"+ $(this).attr('id'),
          success: function (response) {
            $('.modalBody').html(response);
            $('.modal-title').html("Attendees List");
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      
      // Ajax call handling search and redirecting to all events tab
      $('.search-input').change(function (e) {
        e.preventDefault();
        var input = $(this).val();
        $.ajax({
            type: 'GET',
            url: "/search/",
            data: { "data": input },
            success: function (response) {

                $('#allevents').html(response);
            },
            error: function (response) {
                console.log('error', response);
            },
            complete: function () {
                allEventsTab.show();
            }
        });
    });

      // Ajax call handling all events fetch
      $('#allevents-tab').click(function (e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/all_events/",
          success: function (response) {
            $('#allevents').html(response);
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });

       // Ajax call handling created events fetch
      $('#myevents-tab').click(function (e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/created/",
          success: function (response) {
            $('#myevents').html(response);
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });

       // Ajax call handling favorite events fetch
      $('#fav-tab').click(function (e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/favourite/",
          success: function (response) {
            $('#fav').html(response);
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });

       // Ajax call handling attending events fetch
      $('#attending-tab').click(function (e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/attending/",
          success: function (response) {
            $('#attending').html(response);
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });

      // Ajax call handling attending button fetch
      $('body').on('click', '.attend-btn', function(e) {
        const csrftoken = getCookie('csrftoken');
        e.preventDefault();
        let event = $(this).val();
        // GET AJAX request
        $.ajax({
          type: 'POST',
          headers: { 'X-CSRFToken': csrftoken },
          url: "/attend_event/",
          data: {
            event: event,
          },
          success: function (response) {
            $(e.currentTarget).html(response.status);
            $(e.currentTarget).closest(".d-flex").find(".attendees-list").html(response.attendees_list);
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      // Ajax call handling favourite events fetch
      $('body').on('click', '.favourite', function(e) {
        const csrftoken = getCookie('csrftoken');
        e.preventDefault();e
        let event = $(this).attr('id');
        $.ajax({
          type: 'POST',
          headers: { 'X-CSRFToken': csrftoken },
          url: "/mark_favourite/",
          data: {
            event: event,
          },
          success: function (response) {
            if (response.status == 'favourite') {
              $(e.currentTarget).html(
                '<i class="fas fa-star" style="color: #ffc300"></i>'
              );
            } else {
              $(e.currentTarget).html('<i class="far fa-star"></i>');
            }
          },
          error: function (response) {
            console.log('error', response);
          },
        });
    });
    
     
    });
