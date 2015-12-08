require(['/static/js/config.js'], function () {
  require(['jquery', 'bootstrap'], function($) {

	document.ready = function () {
		var transactions = $('#transactions');
		transactions.scrollTop(transactions[0].scrollHeight);

	};
	
	$('.void-line').each(function() {
		$(this).click(function() {
		alert($(this).data('id'))
		void_line($(this).data('id'));
	   	});
    	});

	$('.edit-line').each(function() {
		$(this).click(function() {
		alert('edit')
		void_line($(this).data('id'));
	   	});
    	});

 	function void_line(id) {
      	var csrf_token_input = $('#csrf_token').find('input'),
        post_args = {
          id: id
        };
      post_args[csrf_token_input.attr('name')] = csrf_token_input.attr('value');
      $.ajax({
        url: '/coffee/' + id + '/cancel/',
        data: post_args,
        type: 'POST',
        dataType: 'json'
      });
	};

	function edit_line(id) {
      	var csrf_token_input = $('#csrf_token').find('input'),
        post_args = {
          id: id
        };
      post_args[csrf_token_input.attr('name')] = csrf_token_input.attr('value');
      $.ajax({
        url: '/coffee/' + id + '/edit/',
        data: post_args,
        type: 'POST',
        dataType: 'json'
      });
	};


  });
});
