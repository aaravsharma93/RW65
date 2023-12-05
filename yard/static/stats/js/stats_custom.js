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
       $("#vehicle_id").val(result.vehicle).trigger('change');
       $("#id_vehicle").val($(".vehicleName"+id).text());
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
        $("#id_vehicle_second_weight_flag").val(result.vehicle_second_weight_flag);
        $("#id_trans_flag").val(result.trans_flag);
        $("#id_article_price").val(result.price_per_item);
        $("#load_images_btn").val(id);

        if (result.vehicle_weight_flag == 2 ){
          $("#id_first_weight").prop('readonly',false)
        } else{
          $("#id_first_weight").prop('readonly',true)
        }
        if (result.vehicle_second_weight_flag == 2 ){
          $("#id_second_weight").prop('readonly',false)
        } else {
          $("#id_second_weight").prop('readonly',true)
        }
    }
  })
}

$( "#load_images_btn" ).click(function() {

    $("#MyPopupImg").modal();

    $.ajax({
      type: "GET",
      url: "../view_images_base64/"+ this.value,
      success: function (result) {
          let image_ele = ''
        if(result.status==false){
          image_ele = '<h4>'+ result.msg + '</h4>'
        }
        else{
            if(result.image1 !== ""){
                let image1 = `<img id="image1" class="trans_img" src="/media/${result.image1}" width="200px">`
                image_ele += image1
            }
            if(result.image2!==""){
                let image2 = `<img id="image3" class="trans_img" src="/media/${result.image2}" width="200px">`
                image_ele += image2
            }
            if(result.image3 !== ""){
                let image3 = `<img id="image3" class="trans_img" src="/media/${result.image3}" width="200px">`
                image_ele += image3
            }
        }
        $("#MyPopupImg .modal-body center").html(image_ele);
        $('.trans_img').on('click', function () {
                $('#MyPopupImg').modal('hide');
                var image = $(this).attr('src');
                 $('#MyModal').on('show.bs.modal', function () {
                    $(".img-responsive").attr("src", image);
                });
                $('#MyModal').modal('show');
            });
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
    const send_email = async (trans_id) =>{
        const url = "/stats/send_deliverynotes/"+trans_id
        let response = await $.ajax(url,{
            type:"GET"
        });
        return response
    }

    $('#send_email_btn').click(async function (event) {
        event.preventDefault();
        var trans_id = $('#form_delivery_note').find('input[name="id"]').attr("value");
        console.log(trans_id);
        try {
            let response = await send_email(trans_id);
            console.log(response);
            alert(response.status);
        }catch (e) {
            console.log(e);
            if(e.status == 404){
                alert(e.responseJSON.status);
            }
            else {
                alert(e.toString());
            }
        }
    });


   $('#cancel_delivery_note').click(function (event) {
    event.preventDefault()
    $('#div_delivery_form').hide()
   var form = $('#form_delivery_note')[0];
   form.reset();
  });


});

$("#id_first_weight").change(function(){
  $("#id_vehicle_weight_flag").val(2);
  currentdate = new Date();
  date_time = currentdate.getFullYear()+"-"+(currentdate.getMonth()+1)+"-"+currentdate.getDate()+" "+currentdate.getHours()+":"+currentdate.getMinutes()+":"+currentdate.getSeconds()+".000"
  $('#id_firstw_date_time').val(date_time);
})

$("#id_second_weight").change(function(){
  $("#id_vehicle_second_weight_flag").val(2);
  currentdate = new Date();
  date_time = currentdate.getFullYear()+"-"+(currentdate.getMonth()+1)+"-"+currentdate.getDate()+" "+currentdate.getHours()+":"+currentdate.getMinutes()+":"+currentdate.getSeconds()+".000"
  $('#id_secondw_date_time').val(date_time);
})

$("#sitelistdelete").click(function(e){
  if (!confirm("Do you want to delete")){
    return false;
  }
})

