//adding animation on full load to the header section
$(window).on('load',function () {
    $('.header-section').addClass('animate__fadeInUp');
});

$('.dataItemClearMessage').hide();

// Declaring all the variables
var mainCounter = $('#mainmenucounter').val();
var data1 = $('#data1');
var data2 = $('#data2');
var data3 = $('#data3');
var data4 = $('#data4');
var data5 = $('#data5');
var data6 = $('#data6');

// Main Menu Data fields handling for data selection
function mainMenuDataFields(fieldValue){
    var mainCounter = $('#mainmenucounter').val();
    var mainMenuValue = $('#mainMenuText').val();

if(mainCounter==0){
    $('#data-placeholder1').hide();
    $('#sd1').html(fieldValue);
    $('#mainMenuText').val(fieldValue);
}
else if(mainCounter==1){
    $('#data-placeholder2').hide();
    $('#sd2-1').html(fieldValue);
    $('#mainMenuText').val(fieldValue);
}
else if(mainCounter==2){
    $('#data-placeholder3').hide();
    $('#sd3-1').html(fieldValue);
    $('#mainMenuText').val(fieldValue);
}
else if(mainCounter==3){
    $('#data-placeholder4').hide();
    $('#sd4-1').html(fieldValue);
    $('#mainMenuText').val(fieldValue);
}
else if(mainCounter==4){
    $('#data-placeholder5').hide();
    $('#sd5-1').html(fieldValue);
    $('#mainMenuText').val(fieldValue);
}
else if(mainCounter==5){
    $('#data-placeholder6').hide();
    $('#sd6-1').html(fieldValue);
    $('#mainMenuText').val(fieldValue);
}
else {
    $('.openMaximumDataModal').click();
    }
}

// Show message for unchecking
function showUncheckMessage(id){
    if (data1.val() == id || data2.val() == id || data3.val() == id || data4.val() == id || data5.val() == id || data6.val() == id){
        $('.dataItemClearMessage').show();
    }
}


// Sub Menu Data fields handling for data selection
function subMenuDataFields(fieldValue) {
    var mainCounter = $('#mainmenucounter').val();
    var subMenuValue = $('#subMenuText').val();
    var mainMenuValue2 = $('#mainMenuText').val();

if(mainCounter==0){
    $('#data-placeholder1').hide();
    $('#sd1').html(mainMenuValue2);
    $('#sd2').html(" - "+fieldValue);
    $('#subMenuText').val(fieldValue);
}
else if(mainCounter==1){
    $('#data-placeholder2').hide();
    $('#sd2-1').html(mainMenuValue2);
    $('#sd2-2').html(" - "+fieldValue);
    $('#subMenuText').val(fieldValue);
}
else if(mainCounter==2){
    $('#data-placeholder3').hide();
    $('#sd3-1').html(mainMenuValue2);
    $('#sd3-2').html(" - "+fieldValue);
    $('#subMenuText').val(fieldValue);
}
else if(mainCounter==3){
    $('#data-placeholder4').hide();
    $('#sd4-1').html(mainMenuValue2);
    $('#sd4-2').html(" - "+fieldValue);
    $('#subMenuText').val(fieldValue);
}
else if(mainCounter==4){
    $('#data-placeholder5').hide();
    $('#sd5-1').html(mainMenuValue2);
    $('#sd5-2').html(" - "+fieldValue);
    $('#subMenuText').val(fieldValue);
}
else if(mainCounter==5){
    $('#data-placeholder6').hide();
    $('#sd6-1').html(mainMenuValue2);
    $('#sd6-2').html(" - "+fieldValue);
    $('#subMenuText').val(fieldValue);
}
else {
    $('.openMaximumDataModal').click();
}
}

// Sub in Menu Data fields handling for data selection
function subinMenuDataFields(id,label) {
    var mainCounter = $('#mainmenucounter').val();
    var mainMenuValue = $('#mainMenuText').val();
    var subMenuValue = $('#subMenuText').val();
    // preventing selection from duplication
    $('.data-item-checklist').click(function () {
        $(this).prop('checked', true);
        $(this).addClass('disable'); // disableing the selected checkbox
    });
    if (toString(data1.val()) == toString(id)){
        //window.alert("Please a data item can only be selected once. If you want to remove any data item please make the selection again by clicking the Clear Selected Data button.")
    }
        if(mainCounter==0){
            data1.val(id);
            $('#mainmenucounter').val(1)
            $('#data-placeholder1').hide();
            $('#sd1').html(mainMenuValue);
            $('#sd2').html(" - "+subMenuValue);
            $('#sd3').html(" - "+label);
            }
        else if(mainCounter==1){
            // Adding value to the input fields
            data2.val(id);
            $('#mainmenucounter').val(2);
            $('#data-placeholder2').hide();
            $('#sd2-1').html(mainMenuValue);
            $('#sd2-2').html(" - "+subMenuValue);
            $('#sd2-3').html(" - "+label);
        }
        else if(mainCounter==2){
            data3.val(id);
            $('#mainmenucounter').val(3)
            $('#data-placeholder3').hide();
            $('#sd3-1').html(mainMenuValue);
            $('#sd3-2').html(" - "+subMenuValue);
            $('#sd3-3').html(" - "+label);
        }
        else if(mainCounter==3){
            data4.val(id);
            $('#mainmenucounter').val(4)
            $('#data-placeholder4').hide();
            $('#sd4-1').html(mainMenuValue);
            $('#sd4-2').html(" - "+subMenuValue);
            $('#sd4-3').html(" - "+label);
        }
        else if(mainCounter==4){
            data5.val(id);
            $('#mainmenucounter').val(5)
            $('#data-placeholder5').hide();
            $('#sd5-1').html(mainMenuValue);
            $('#sd5-2').html(" - "+subMenuValue);
            $('#sd5-3').html(" - "+label);
        }
        else if(mainCounter==5){
            data6.val(id);
            $('#mainmenucounter').val(6)
            $('#data-placeholder6').hide();
            $('#sd6-1').html(mainMenuValue);
            $('#sd6-2').html(" - "+subMenuValue);
            $('#sd6-3').html(" - "+label);
            $('.data-item-checklist').addClass('disable');
        }
        else {
            $('.openMaximumDataModal').click();
            }

}

// Sub in Menu 4 and 7 Data fields handling for data selection
function subinMenuDataFields47(id,label) {
    var mainCounter = $('#mainmenucounter').val();
    var mainMenuValue = $('#mainMenuText').val();
    var subMenuValue = $('#subMenuText').val('');
    // preventing selection from duplication
    $('.data-item-checklist').click(function () {
        $(this).prop('checked', true);
        $(this).addClass('disable'); // disableing the selected checkbox
    });
    if (data1.val() == id || data2.val() == id || data3.val() == id || data4.val() == id || data5.val() == id || data6.val() == id){
       // return window.alert("Please a data item can only be selected once. If you want to remove any data item please make the selection again by clicking the Clear Selected Data button.")
    }
    else {
        if(mainCounter==0){
            data1.val(id);
            $('#mainmenucounter').val(1);
            $('#data-placeholder1').hide();
            $('#sd1').html(mainMenuValue);
            $('#sd2').html("");
            $('#sd3').html(" - "+label);
            }
        else if(mainCounter==1){
            // Adding value to the input fields
            data2.val(id);
            $('#mainmenucounter').val(2);
            $('#data-placeholder2').hide();
            $('#sd2-1').html(mainMenuValue);
            $('#sd2-2').html("");
            $('#sd2-3').html(" - "+label);
        }
        else if(mainCounter==2){
            data3.val(id);
            $('#mainmenucounter').val(3)
            $('#data-placeholder3').hide();
            $('#sd3-1').html(mainMenuValue);
            $('#sd3-2').html("");
            $('#sd3-3').html(" - "+label);
        }
        else if(mainCounter==3){
            data4.val(id);
            $('#mainmenucounter').val(4)
            $('#data-placeholder4').hide();
            $('#sd4-1').html(mainMenuValue);
            $('#sd4-2').html("");
            $('#sd4-3').html(" - "+label);
        }
        else if(mainCounter==4){
            data5.val(id);
            $('#mainmenucounter').val(5)
            $('#data-placeholder5').hide();
            $('#sd5-1').html(mainMenuValue);
            $('#sd5-2').html("");
            $('#sd5-3').html(" - "+label);
        }
        else if(mainCounter==5){
            data6.val(id);
            $('#mainmenucounter').val(6)
            $('#data-placeholder6').hide();
            $('#sd6-1').html(mainMenuValue);
            $('#sd6-2').html("");
            $('#sd6-3').html(" - "+label);
            $('.data-item-checklist').addClass('disable');
        }
        else {
            $('.openMaximumDataModal').click();
            }
    }

}


// clear selected data
$('.clear-all-form').click(function () {
  // clearing everything
  $('.bankSearchBtn').css('display','none');
  $('#mainmenucounter').val(0);
  data1.val('');
  data2.val('');
  data3.val('');
  data4.val('');
  data5.val('');
  data6.val('');
  $('p').removeClass('menu-active-class');
  $('#sd1').html('');
  $('#sd2').html('');
  $('#sd3').html('');
  $('#sd2-1').html('');
  $('#sd2-2').html('');
  $('#sd2-3').html('');
  $('#sd3-1').html('');
  $('#sd3-2').html('');
  $('#sd3-3').html('');
  $('#sd4-1').html('');
  $('#sd4-2').html('');
  $('#sd4-3').html('');
  $('#sd5-1').html('');
  $('#sd5-2').html('');
  $('#sd5-3').html('');
  $('#sd6-1').html('');
  $('#sd6-2').html('');
  $('#sd6-3').html('');
  $('.data-placeholder').show();
  $('.sub-menu-wrapper').hide();
  $('.sub-in-menu-wrapper').hide();
  $('.data-item-checklist').prop('checked', false);
  $('.data-item-checklist').removeClass('disable');
  $('.top-options').attr('disabled','disabled');
  $('.periodselect').attr('disabled','disabled');
  $('.dataItemClearMessage').hide();
});


// clear selected data
$('.clear-select-data').click(function () {
  // clearing everything
  $('#mainmenucounter').val(0);
  data1.val('');
  data2.val('');
  data3.val('');
  data4.val('');
  data5.val('');
  data6.val('');
  $('p').removeClass('menu-active-class');
  $('#sd1').html('');
  $('#sd2').html('');
  $('#sd3').html('');
  $('#sd2-1').html('');
  $('#sd2-2').html('');
  $('#sd2-3').html('');
  $('#sd3-1').html('');
  $('#sd3-2').html('');
  $('#sd3-3').html('');
  $('#sd4-1').html('');
  $('#sd4-2').html('');
  $('#sd4-3').html('');
  $('#sd5-1').html('');
  $('#sd5-2').html('');
  $('#sd5-3').html('');
  $('#sd6-1').html('');
  $('#sd6-2').html('');
  $('#sd6-3').html('');
  $('.data-placeholder').show();
  $('.sub-menu-wrapper').hide();
  $('.sub-in-menu-wrapper').hide();
  $('.data-item-checklist').prop('checked', false);
  $('.data-item-checklist').removeClass('disable');
  $('.dataItemClearMessage').hide();
});

// drop down menu js logics
$(document).ready(function () {
    // Main menu logic
    $('#mainmenu1').click(function () {
      $('.mainmenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-menu-wrapper').hide();
      $('#sm1').show();
      $('.sub-in-menu-wrapper').hide();
    })
    $('#mainmenu2').click(function () {
      $('.mainmenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-menu-wrapper').hide();
      $('#sm2').show();
      $('.sub-in-menu-wrapper').hide();
    })
    $('#mainmenu3').click(function () {
      $('.mainmenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-menu-wrapper').hide();
      $('#sm3').show();
      $('.sub-in-menu-wrapper').hide();
    })
    $('#mainmenu4').click(function () {
      $('.mainmenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-menu-wrapper').hide();
      $('#sm4').show();
      $('.sub-in-menu-wrapper').hide();
    })
    $('#mainmenu5').click(function () {
      $('.mainmenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-menu-wrapper').hide();
      $('#sm5').show();
      $('.sub-in-menu-wrapper').hide();
    })
    $('#mainmenu6').click(function () {
      $('.mainmenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-menu-wrapper').hide();
      $('#sm6').show();
      $('.sub-in-menu-wrapper').hide();
    })
    $('#mainmenu7').click(function () {
      $('.mainmenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-menu-wrapper').hide();
      $('#sm7').show();
      $('.sub-in-menu-wrapper').hide();
    })

});

// Sub in menu logic
$(document).ready(function () {
    $('#sm1submenu1').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu1').show();
    })
    $('#sm1submenu2').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu2').show();
    })
    $('#sm1submenu3').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu3').show();
    })
    $('#sm1submenu4').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu4').show();
    })
    $('#sm1submenu5').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu5').show();
    })
    $('#sm1submenu6').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu6').show();
    })
    $('#sm1submenu7').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu7').show();
    })
    $('#sm2submenu1').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu8').show();
    })
    $('#sm2submenu2').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu9').show();
    })
    $('#sm2submenu3').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu10').show();
    })
    $('#sm2submenu4').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu11').show();
    })
    $('#sm2submenu5').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu12').show();
    })
    $('#sm3submenu1').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu13').show();
    })
    $('#sm3submenu2').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu14').show();
    })
    $('#sm3submenu3').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu15').show();
    })
    $('#sm3submenu4').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu16').show();
    })
    $('#sm3submenu5').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu17').show();
    })
    $('#sm5submenu1').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu18').show();
    })
    $('#sm5submenu2').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu19').show();
    })
    $('#sm6submenu1').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu20').show();
    })
    $('#sm6submenu2').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu21').show();
    })
    $('#sm6submenu3').click(function () {
      $('.submenuitem').removeClass('menu-active-class');
      $(this).addClass('menu-active-class');
      $('.sub-in-menu-wrapper').hide();
      $('#subinmenu22').show();
    })

})

/*##################################*/
// Bank city, state logic
$(document).ready(function(){
      /*$("#branchlocation").keypress(function(){
        var inputVal = $("#branchlocation").val();
        // setting value to none for hidden field in order to show search modal
        var inputVal2 = $("#branchlocation2");
        inputVal2.val("");
        $.ajax({
          type:'GET',
          url: "bankstates/"+inputVal,
          data: inputVal,
          beforeSend: function () {
            $('#dataloader').show();
          },
          success: (res)=>{
            $('#dataloader').hide();
            var bankbranchlocationDiv = document.getElementById('bankbranchlocationDiv');
            const data = res.data;
            bankbranchlocationDiv.innerHTML += "";
            if(Array.isArray(data)){
              bankbranchlocationDiv.innerHTML = "";
              // now displaying the search results
              data.forEach(items=>{
                bankbranchlocationDiv.innerHTML += `
                  <p class="data-item" onclick="setSearchValues('${items.city}','${items.state}')">${items.city}, ${items.state}</p>
                  `
              })
            }
            else {
              if($('.form-control').val().length > 0){
                bankbranchlocationDiv.innerHTML = '';
                bankbranchlocationDiv.innerHTML += `
                <span style="padding: 10px">${data}</span>
                `;
              }
            }
          },
          error: (err=>{
          })
        });
      });
      */

      // Hiding and showing the list wrapper
      setInterval(function () {
        // state city search field logic
        /* if($('#branchlocation2').val().length == 0){
                $('#bankbranchlocationDiv').show();
              }
        else if($('#branchlocation').val().length == 0){
                $('#bankbranchlocationDiv').hide();
              }
        else {
          $('#bankbranchlocationDiv').hide();
        } */

        // single us bank logic
        if($('#singleusbank2').val().length == 0){
                $('#singleusBankDiv').show();
              }
        else if($('#singleusbank1').val().length == 0){
                $('#singleusBankDiv').hide();
              }
        else {
          $('#singleusBankDiv').hide();
        }

      },1000)

});

/*
// Getting data from the forloop live search function for city and state
function setSearchValues(city, state) {
    var c = city;
    var s = state;

    var actualSearchField = document.getElementById('branchlocation');
    var hiddenSearchField = document.getElementById('branchlocation2');
    // storing value in the search input field
    actualSearchField.value = c + ", " + s;
    hiddenSearchField.value = c + ", " + s;
}
*/

// Getting data from the forloop live search function for bank name
function setBankName(bankname, rssid) {
    var bname = bankname;
    var rsid = rssid;

    var actualSearchField = document.getElementById('singleusbank1');
    var hiddenSearchField = document.getElementById('singleusbank2');
    // storing value in the search input field
    actualSearchField.value = bname;
    hiddenSearchField.value = rsid;
}



// logic for single us bank search
$(document).ready(function () {
  $(".bankSearchBtn").click(function (event) {
      event.preventDefault();
    var inputVal = $("#singleusbank1").val();
    var bankbranchlocationDiv = document.getElementById('singleusBankDiv');
    bankbranchlocationDiv.innerHTML = "";
    $('#dataloader2').show();
    // setting value to none for hidden field in order to show search modal
    var inputVal2 = $("#singleusbank2");
    inputVal2.val("");
    $.ajax({
      type: 'GET',
      url: "singleusbank/" + inputVal,
      data: {query:inputVal},
      success: (res) => {
        $('#dataloader2').hide();
        const data = res.data;
        if (Array.isArray(data)) {
          bankbranchlocationDiv.innerHTML = "";
          // now displaying the search results
          data.forEach(items => {
            bankbranchlocationDiv.innerHTML += `
                    <p class="data-item" onclick="setBankName('${items.bankname}','${items.rssid}')">${items.bankname}</p>
                    `
          })
        } else {
            bankbranchlocationDiv.innerHTML = '';
            bankbranchlocationDiv.innerHTML += `
                  <span style="padding: 10px">${data}</span>
                  `;
        }
      },
      error: (err => {
      })
    });
  });
})

// Preventing form from submitting when no data fields are selected.
$('form').submit(function (e) {
    var selectedData = $('#mainmenucounter').val();
    if (selectedData > 0 && $('.banks-radio').is(':checked') && $('.period').is(':checked')){
        $('.action-loader').css('display','block');
    }
    else {
        e.preventDefault();
        e.stopImmediatePropagation();
        $('.openValidationModal').click();
    }
});


