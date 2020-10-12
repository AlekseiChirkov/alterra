// Modal window
var modal = document.getElementById("contacts-block");
var btn = document.getElementById("contacts");
var service = document.getElementById("service");
var portfolio = document.getElementById("portfolio");


btn.onclick = function() {
  modal.style.display = "block";
}

service.onclick = function() {
    modal.style.display = "none";
}

portfolio.onclick = function() {
    modal.style.display = "none";
}


// Video background
var vid = document.getElementById("video");
vid.playbackRate = 0.7;

setTimeout(function(){
    document.getElementById("video").play();
}, 8000);


// Burger menu
$(document).ready(function(){
	$('.header__burger').click(function(event){
		$('.header__burger, .header__menu').toggleClass('active');
		$('body').toggleClass('lock');
	});
});


