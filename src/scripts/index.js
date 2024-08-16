$(document).ready(function () {
  $("#main_apps_menu").click(function () {
    $("#sidebar").toggle();
  });
});

$(document).ready(function () {
  function updateClock() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();

    // Add leading zeros  if necessary
    hours = hours < 10 ? "0" + hours : hours;
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;

    var timeString = hours + ":" + minutes + ":" + seconds;

    $("#clock").text(timeString);
  }

  updateClock(); // Initial call to display time immediately
  setInterval(updateClock, 1000); // Update time every second
});
