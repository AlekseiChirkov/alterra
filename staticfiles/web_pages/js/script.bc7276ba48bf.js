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


// Modal window
var modal = document.getElementById("contacts-block");
var btn = document.getElementById("contacts");

btn.onclick = function() {
  modal.style.display = "block";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}