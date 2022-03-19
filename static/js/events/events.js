$(document).ready(function() {
  const allEventsTab = new bootstrap.Tab(document.querySelector("#allevents-tab"));
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
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
  
      $('body').on('click', '.createEvent', function(e) {
        e.preventDefault();
        // get the nickname
        var nick_name = $(this).val();
        // GET AJAX request
        $.ajax({
          type: 'GET',
          url: "/create/",
          success: function (response) {
            // if not valid user, alert the user
            $('.modalBody').html(response);
    
            console.log('display');
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      $('body').on('click', '.updateEvent', function(e) {
        e.preventDefault();
        // get the nickname
        var nick_name = $(this).val();
        // GET AJAX request
        $.ajax({
          type: 'GET',
          url: "/update_event/"+$(this).attr('id'),
          success: function (response) {
            // if not valid user, alert the user
            $('.modalBody').html(response);
    
            console.log('display');
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      $('body').on('click', '.deleteEvent', function(e) {
        e.preventDefault();
        // get the nickname
        var nick_name = $(this).val();
        // GET AJAX request
        $.ajax({
          type: 'GET',
          url: "/delete_event/"+$(this).attr('id'),
          success: function (response) {
            // if not valid user, alert the user
            $('.modalBody').html(response);
    
            console.log('display');
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      $('body').on('click', '.attendees-list', function(e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/event/"+ $(this).attr('id'),
          success: function (response) {
            $('.modalBody').html(response);
    
            console.log('display', $('.modalBody').html);
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      
      $('.search-input').change(function (e) {
        e.preventDefault();
        // get the nickname
        var nick_name = $(this).val();
        console.log('data', nick_name);
        // GET AJAX request
        $.ajax({
            type: 'GET',
            url: "/search/",
            data: { "data": nick_name },
            success: function (response) {

                $('#allevents').html(response);

                console.log('display', response);
            },
            error: function (response) {
                console.log('error', response);
            },
            complete: function () {
                allEventsTab.show();
            }
        });
    });

      
      $('#allevents-tab').click(function (e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/all_events/",
          success: function (response) {
            $('#allevents').html(response);
            console.log('all_events', response);
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      $('#myevents-tab').click(function (e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/created/",
          success: function (response) {
            $('#myevents').html(response);
            console.log('display');
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      $('#fav-tab').click(function (e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/favourite/",
          success: function (response) {
            $('#fav').html(response);
            console.log('display');
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      $('#attending-tab').click(function (e) {
        e.preventDefault();
        $.ajax({
          type: 'GET',
          url: "/attending/",
          success: function (response) {
            $('#attending').html(response);
            console.log('attending clicked');
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      $('body').on('click', '.attend-btn', function(e) {
        const csrftoken = getCookie('csrftoken');
        e.preventDefault();
        let event = $(this).val();
        console.log('data', event);
        // GET AJAX request
        $.ajax({
          type: 'POST',
          headers: { 'X-CSRFToken': csrftoken },
          url: "/attend_event/",
          data: {
            event: event,
          },
          success: function (response) {
            // if not valid user, alert the user
            console.log('attend_success,', response.status);
            $(e.currentTarget).html(response.status);
            $('.attendees-list').html(response.attendees_list);
          },
          error: function (response) {
            console.log('error', response);
          },
        });
      });
      $('body').on('click', '.favourite', function(e) {
        const csrftoken = getCookie('csrftoken');
        console.log('target', $(e.currentTarget));
        e.preventDefault();
        // get the nickname
        let event = $(this).attr('id');
        console.log('data', event);
        // GET AJAX request
        $.ajax({
          type: 'POST',
          headers: { 'X-CSRFToken': csrftoken },
          url: "/mark_favourite/",
          data: {
            event: event,
          },
          success: function (response) {
            if (response.status == 'favourite') {
              console.log('enterd');
              $(e.currentTarget).html(
                '<i class="fas fa-star" style="color: #ffc300"></i>'
              );
            } else {
              console.log('enterd2');
              $(e.currentTarget).html('<i class="far fa-star"></i>');
            }
          },
          error: function (response) {
            console.log('error', response);
          },
        });
    });
      // $('.favourite').click(function (e) {
      //   const csrftoken = getCookie('csrftoken');
      //   console.log('csrf token', csrftoken);
      //   e.preventDefault();
      //   // get the nickname
      //   let event = $(this).attr('id');
      //   console.log('data', event);
      //   // GET AJAX request
      //   $.ajax({
      //     type: 'POST',
      //     headers: { 'X-CSRFToken': csrftoken },
      //     url: "/mark_favourite/",
      //     data: {
      //       event: event,
      //     },
      //     success: function (response) {
      //       if (response.status == 'favourite') {
      //         console.log('enterd');
      //         $('.favourite').html(
      //           '<i class="fas fa-star" style="color: #ffc300"></i>'
      //         );
      //       } else {
      //         console.log('enterd2');
      //         $('.favourite').html('<i class="far fa-star"></i>');
      //       }
      //     },
      //     error: function (response) {
      //       console.log('error', response);
      //     },
      //   });
      // });
    });
