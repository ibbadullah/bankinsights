// JS logics options disabling and enabling
$('.bankSearchBtn').css('display','none');
$('#option0').click(function () {
   $('.top-options').attr('disabled','disabled');
   $('.bankSearchBtn').css('display','none');
   $('#singleusbank1').val('');
   $('#singleusbank2').val('0');
   $('#singleusBankDiv').hide();
});
$('#option1').click(function () {
   $('.top-options').attr('disabled','disabled');
    $('#select-top-options1').removeAttr('disabled','disabled');
    $('#select-top-options1').attr('required','required');
    $('.bankSearchBtn').css('display','none');
    $('#singleusbank1').val('');
    $('#singleusbank2').val('0');
    $('#singleusBankDiv').hide();
});
$('#option2').click(function () {
   $('.top-options').attr('disabled','disabled');
    $('#branchlocation').removeAttr('disabled','disabled');
    $('#branchlocation2').removeAttr('disabled','disabled');
    $('#select-top-options2').removeAttr('disabled','disabled');
    $('.bankSearchBtn').css('display','none');
    $('#singleusbank1').val('');
    $('#singleusbank2').val('0');
    $('#singleusBankDiv').hide();
});
$('#option3').click(function () {
   $('.top-options').attr('disabled','disabled');
    $('#select-top-options3').removeAttr('disabled','disabled');
    $('.bankSearchBtn').css('display','none');
    $('#singleusbank1').val('');
    $('#singleusbank2').val('0');
    $('#singleusBankDiv').hide();
});
$('#option4').click(function () {
   $('.top-options').attr('disabled','disabled');
   $('#singleusbank1').removeAttr('disabled','disabled');
   $('#singleusbank2').removeAttr('disabled','disabled');
   $('.bankSearchBtn').css('display','block');
});
$('#option5').click(function () {
   $('.periodselect').attr('disabled','disabled');
   $('#period1').removeAttr('disabled','disabled');
});
$('#option6').click(function () {
   $('.periodselect').attr('disabled','disabled');
   $('#period2').removeAttr('disabled','disabled');
});