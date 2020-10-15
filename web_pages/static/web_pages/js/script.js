// Modal window


var contacts_modal = document.getElementById("contacts-block");
var contacts_open = document.getElementById("contacts");

contacts_open.onclick = function() {
    if (contacts_modal.style.display === "none") {
        contacts_modal.style.display = "block";
    } else {
        contacts_modal.style.display = "none";
    }
}

var useful_modal = document.getElementById("useful-block");
var useful_open = document.getElementById("useful");

useful_open.onclick = function() {
    if (useful_modal.style.display === "none") {
        useful_modal.style.display = "flex";
    } else {
        useful_modal.style.display = "none";
    }
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


