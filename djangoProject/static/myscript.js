/// the response_json_object is sent to the html and then inside the html the js receives it through its catcher called getJSON() and passes it to the typeles parameter called data
/// data then gets chopped via data.events[0].name


$(document).ready(function() {
    /// print('hellooooooooo static javascript!');
    
    $.ajax({
	console.log(data);
    });

    $.getJSON('/hello', function(data) {
	$('#event-list').append('<li>' + data.events[0].name + '</li>'); 
    });

});



