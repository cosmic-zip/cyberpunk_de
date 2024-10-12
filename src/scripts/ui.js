$(document).ready(function () {
  $("#main_apps_menu").click(function () {
    $("#sidebar").toggle();
  });
});

$(document).ready(function () {
  $("#show-desktop").click(function () {
    $(".app").hide();
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

// Taskbar wallpaper switch
$(document).ready(function () {
  function sys_switch_desktop(number) {
    const images = [
      "url(wallpapers/wp1.jpg)",
      "url(wallpapers/wp2.jpg)",
      "url(wallpapers/wp3.jpg)",
      "url(wallpapers/wp4.jpg)",
      "url(wallpapers/wp5.jpg)",
      "url(wallpapers/wp6.jpg)",
    ];

    if (number >= 1 && number <= images.length) {
      $("body").css("background-image", images[number - 1]);
    } else {
      console.log("Invalid number. Please provide a number between 1 and " + images.length);
    }
  }

  // Attach click event to taskbar buttons
  $(".taskbar-btn").on("click", function () {
    const number = $(this).data("number");
    sys_switch_desktop(number);
  });
});

var __EVAL = (s) => eval(`void (__EVAL = ${__EVAL}); ${s}`);
jQuery(function ($, undefined) {
  $("#term_demo").terminal(
    function (command) {
      if (command !== "") {
        try {
          var result = __EVAL(command);
          if (result !== undefined) {
            this.echo(new String(result));
          }
        } catch (e) {
          this.error(new String(e));
        }
      }
    },
    {
      greetings: "",
      name: "witch",
      height: 800,
      prompt: "[witch_craft] ❆ [localnet] $ ",
    },
  );
});
