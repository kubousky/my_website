//* JQuerry iguala height de .c a la de .flex-fill */
jQuery(function($){
    var mainHeight = $('.flex-fill').height();          
    $('.c').css('height', mainHeight );

});

if ('http://jakub-parcheta.herokuapp.com/' == window.location.href ||'http://localhost:8000/' == window.location.href){
// refresh page when resize browser
$(window).on('resize',function(){location.reload();});
}
