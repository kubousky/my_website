//* JQuerry iguala height de .c a la de .flex-fill */
jQuery(function($){
    var mainHeight = $('.flex-fill').height();          
    $('.c').css('height', mainHeight );

});
// refresh page on browser resize
$(window).on('resize',function(){location.reload();
});

