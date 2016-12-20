require([
  'jquery','bootstrap-tabs'
], function($,tabs) {
  'use strict';
$(document).ready(function(){
$('.collapse-control').on('click', function () {
var willshow = $(this).find('.hidden');
var willhide = $(this).find('.shown');
 willshow.removeClass('hidden').addClass('shown');
 willhide.removeClass('shown').addClass('hidden');
});
$('a[href^="http://mw4024.wicp.net:8089/"]').attr('target','_blank').attr('class','outputlink');

$(".nav-tabs a").mouseover(function (e) {
    e.preventDefault()
    $(this).tab('show')
  });
$(".nav-tabs").on("click","a",function (e) {
    e.preventDefault();
    var url = $(this).attr("data-js-target");
    window.location.href = url;
    return false;
  });	

});
});
