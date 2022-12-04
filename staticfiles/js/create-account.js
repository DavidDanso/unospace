/////////////////////// Pre-load Animation //////////////////
// var tll = gsap.timeline();
// tll.from(".animate-this", {
//   duration: 1,
//   y: -30,
//   opacity: 0,
//   stagger: 1,
//   delay: 0.3,
// });
// TweenMax.from(".is-animated", 1, {
//   delay: 0.6,
//   opacity: 0,
//   ease: Expo.easeInOut,
// });
// //text animation
// const textrev = gsap.timeline();
// textrev.from(".line span", 1.8, {
//   y: 200,
//   ease: "power4.out",
//   delay: 0.3,
//   skewY: 10,
//   stagger: {
//     amount: 0.4,
//   },
// });
////////////////////// End Pre-load Animation /////////////////

/////////////////////// Navigation //////////////////
$(document).ready(function () {
  //
  $(".nav-link").click(function () {
    $(".navbar-collapse").collapse("hide");
  });

  //
  $(window).scroll(function () {
    var sc = $(window).scrollTop();
    if (sc > 0) {
      $("#mainNavv").addClass("navbar-shrink");
    } else {
      $("#mainNavv").removeClass("navbar-shrink");
    }
  });
});

// password eye toggle
$(".toggle-password").click(function () {
  $(this).toggleClass("fa-eye fa-eye-slash");
  var input = $($(this).attr("toggle"));
  if (input.attr("type") == "password") {
    input.attr("type", "text");
  } else {
    input.attr("type", "password");
  }
});

// Smooth Scrolling ==========================================================-->
$(document).ready(function () {
  // Add smooth scrolling to all links
  $("a").on("click", function (event) {
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $("html, body").animate(
        {
          scrollTop: $(hash).offset().top,
        },
        800,
        function () {
          // Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash = hash;
        }
      );
    } // End if
  });
});
// Select all links with hashes
$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function (event) {
    // On-page links
    if (
      location.pathname.replace(/^\//, "") ==
        this.pathname.replace(/^\//, "") &&
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $("[name=" + this.hash.slice(1) + "]");
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $("html, body").animate(
          {
            scrollTop: target.offset().top,
          },
          1000,
          function () {
            // Callback after animation
            // Must change focus!
            var $target = $(target);
            $target.focus();
            if ($target.is(":focus")) {
              // Checking if the target was focused
              return false;
            } else {
              $target.attr("tabindex", "-1"); // Adding tabindex for elements not focusable
              $target.focus(); // Set focus again
            }
          }
        );
      }
    }
  });
