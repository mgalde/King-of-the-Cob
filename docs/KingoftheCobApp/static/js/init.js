
$(document).ready(function() {
    "use strict";

    /**************************************************************************
                 SKILL BAR
    **************************************************************************/

    $(".determinate").each(function(){
      var width = $(this).text();
      $(this).css("width", width)
        .empty()
        .append(width + "Complete");
    });


    var wow = new WOW({ mobile: false });
    wow.init();
});
