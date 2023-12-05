function loadDeliveryNoteDetails(id) {
$('#div_delivery_form').show();
window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
$('.errorlist').hide();
  $.ajax({
    type: "GET",
    url: "../deliverynote_detail/" + id,
    success: function (result) {
        $('#load_images_btn').show();
        $("#id").val(id);
        $("#id_vehicle").val(result.vehicle).trigger('change');
        $("#id_article").val(result.article).trigger('change');
        $("#id_delivery_customer").val(result.customer).trigger('change');
        $("#id_supplier").val(result.supplier).trigger('change');
        $("#id_first_weight").val(result.first_weight);
        $("#id_second_weight").val(result.second_weight);
        $("#id_net_weight").val(result.net_weight);
        $("#id_firstw_alibi_nr").val(result.firstw_alibi_nr);
        $("#id_firstw_date_time").val(result.firstw_date_time);
        $("#id_secondw_alibi_nr").val(result.secondw_alibi_nr);
        $("#id_secondw_date_time").val(result.secondw_date_time);
        $("#id_vehicle_weight_flag").val(result.vehicle_weight_flag);
        $("#id_trans_flag").val(result.trans_flag);
        $("#id_article_price").val(result.price_per_item);
        $("#load_images_btn").val(id);
    }
  })
}

$( "#load_images_btn" ).click(function() {

    $("#MyPopupImg").modal();
    $("#MyModal").modal();

    $.ajax({
      type: "GET",
      url: "../view_images_base64/"+ this.value,
      success: function (result) {
        if(result.status==false){
          data = '<h4>'+ result.msg + '</h4>'
        }
        else{
            data = '<img id="image1" src="'+ 
            result.image1 +'" width="200px"> <img id="image2" src="'+
            result.image2 +'" width="200px"> <img id="image3" src="'+ 
            result.image3 + '" width="200px">'
        }
        $("#MyPopupImg .modal-body center").html(data)
      }
    });
});

$("#btnClosePopup").click(function () {
  $("#MyPopupImg").modal("hide");
});

$(document).ready(function () {
  $('#load_images_btn').hide()
  $('#div_delivery_form').hide()
   $('#save_delivery_note').click(function (event) {
   var form = $('#form_delivery_note');
   form.attr('target', '')
   form.submit();
  });

//   $('#print_delivery_note').click(function (event) {
//   var form = $('#form_delivery_note');
//   form.attr('target', '_blank')
//   form.submit();
//  });

   $('#cancel_delivery_note').click(function (event) {
    event.preventDefault()
    $('#div_delivery_form').hide()
   var form = $('#form_delivery_note')[0];
   form.reset();
  });


});


