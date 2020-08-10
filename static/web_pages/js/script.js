var vid = document.getElementById("video");
vid.playbackRate = 0.7;
setTimeout(function(){
    document.getElementById("video").play();
}, 8000);
$(document).ready(function(){
	$('.header__burger').click(function(event){
		$('.header__burger, .header__menu').toggleClass('active');
		$('body').toggleClass('lock');
	});
});