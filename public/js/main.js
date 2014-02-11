$( document ).ready(function() {
  $('.flipper').on('click', function() {
    document.querySelector('.flip-container').classList.toggle('enter');
    document.querySelector('.container').classList.toggle('visible');
    document.querySelector('.vertical.flip-container').classList.toggle('flip'); 
    document.querySelector('.bottom.separator').classList.toggle('opened');
    document.querySelector('.top.separator').classList.toggle('opened');
    document.querySelector('body').classList.toggle('opened');
    $("html, body").animate({ scrollTop: 0 }, "slow");
  });
});
