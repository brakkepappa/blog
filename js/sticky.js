// When the user scrolls the page, execute myFunction 
window.onscroll = function() {myFunction()};

// Get the timebar
var timebar = document.getElementByClass("timebar");

// Get the offset position of the timebar
var sticky = timebar.offsetTop;

// Add the sticky class to the timebar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    timebar.classList.add("sticky")
  } else {
    timebar.classList.remove("sticky");
  }
} 
