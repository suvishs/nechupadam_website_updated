$(document).ready(function(){
    $('.ssc').slick({
      slidesToShow: 4,
    slidesToScroll: 1,
    dots: true,
    autoplay: true,
    autoplaySpeed: 1000,
    });
    $(".menu-toggle").click(function () {
      $(".mobile-menu").toggleClass("open");
      $(".mobile-menu").css("left","0")
  });
  $(".close-button").click(function () {
    $(".mobile-menu").removeClass("open");
    $(".mobile-menu").css("left","-300px")
  });
  $('.has-submenu').click(function(e) {
    e.preventDefault();
    $('.has-submenu').not(this).find('.submenu').slideUp();
    $(this).find('.submenu').slideToggle();
    $('.submenu').css("display","block")
    $('.dropdown-icon').toggleClass("rotate");
    $(document).click(function(e) {
      if (!$('.has-submenu').is(e.target) && $('.has-submenu').has(e.target).length === 0) {
        $('.submenu').slideUp();
        $('.has-submenu').removeClass('active');
      }
    });
  });
  $('.has-submenus').click(function(e) {
    e.preventDefault();
    $('.has-submenus').not(this).find('.submenus').slideUp();
    $(this).find('.submenus').slideToggle();
    $('.submenus').css("display","block")
    $('.dropdown-icons').toggleClass("rotates");
    $(document).click(function(e) {
      if (!$('.has-submenus').is(e.target) && $('.has-submenus').has(e.target).length === 0) {
        $('.submenus').slideUp();
        $('.has-submenus').removeClass('active');
      }
    });
  });

  // Prevent submenu click from propagating to the parent
  $('.submenu').click(function(e) {
    e.stopPropagation();
  });
  });

  $('.autoplay').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1000,
  });

// fade in grid items  ==================================

$(document).on("scroll", function () {
  var pageTop = $(document).scrollTop()
  var pageBottom = pageTop + $(window).height()
  var tags = $(".fadein")

  for (var i = 0; i < tags.length; i++) {
    var tag = tags[i]

    if ($(tag).offset().top < pageBottom) {
      $(tag).addClass("visible")
    } else {
      $(tag).removeClass("visible")
    }
  }
});