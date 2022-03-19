jQuery(document).ready(function($){

	$('.divo').on({
		mouseover: function(){
			$(this).css({
				transform: "scale(1.1)",
				transition: "0.4s",
				background: "silver"
			})
		},
		mouseout: function(){
			$(this).css({
				transform: "scale(1)",
				transition: "1s",
				background: "unset"
			})
		}
	})



	$(window).scroll(function(event){
		if($(this).scrollTop() > 350){
			$('section').css({
				filter: "brightness(40%)",
				transition: ".5s"
			})
			$('#up').css({
				"display": "block",
				opacity: "1"
			})
			$('#news').animate({
				marginLeft: "0%"
			},1000)

		}else{
			$('section').css("filter", "brightness(100%)")
			$('#up').css({
				display: "none",
				opacity: "0"
			});
		}
	});

	$('#up').click(function(event){
		$('html, body').animate({
			scrollTop: 0
		},800)
	});

	$('.serv_button button').click(function(event){
		$('#more').slideToggle(1000);

	});





	













})