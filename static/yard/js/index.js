var selected_scale = 0 ;
$(document).ready(function() {
    websocketStart('GET WEIGHT');
    var img_loading1 = $("#img_loading1");
    var img_loading2 = $("#img_loading2");
    var img_loading3 = $("#img_loading3");
    img_loading1.hide();
    img_loading2.hide();
    img_loading3.hide();
    // Initialize select2
    $("#id_customer").select2({
        tags: true
    });
    $('#clear_customer').click(function() {
        $('#id_customer_name').val(0).trigger('change');
        $('.kunden').val("")
        event.preventDefault()
    });

    $("#id_vehicle").select2({
        tags: true
    });
    $('#clear_vehicle').click(function() {
        $('#id_vehicle').val(0).trigger('change');
        $('.fahrzeuge').val("")
        event.preventDefault()
    });
    $("#id_supplier").select2({
        tags: true
    });
    $('#clear_supplier').click(function() {
        $('#id_supplier').val(0).trigger('change');
        $('.lieferanten').val("")
        event.preventDefault()
    });
    $("#id_article").select2({
        tags: true
    });
    $('#clear_article').click(function() {
        $('#id_article').val(0).trigger('change');
        $('.artikel').val("")
        event.preventDefault()
    });
    $("#id_ident").select2({
        tags: true
    });
    $('#clear_ident').click(function() {
        $('#id_ident').val(0).trigger('change');
        $('.artikel').val("")
        $('.lieferanten').val("")
        $('.fahrzeuge').val("")
        $('.kunden').val("")
        event.preventDefault()
    });

    $('#id_scale2_tab').click(function(event) {
        event.preventDefault();
        selected_scale = 1 ;
        alert("Reading weight from Scale 2");
        sendRequest('GET WEIGHT1');
        });

        $('#id_scale1_tab').click(function(event) {
        event.preventDefault();
        selected_scale = 0 ;
        alert("Reading weight from Scale 1");
        sendRequest('GET WEIGHT');
        });

    $('#btn-firstweight').click(function(event) {
        event.preventDefault();
        var get_weight_nm = true;
//        weight = $("#id_weight").text();
//        date = $("#id_date").val();
//        time = $("#id_time").val();
//        alibi_num = $("#id_alibi_num").val();
//        date_time = date.concat(" ", time, ":00").replaceAll(".", "/")
//        date_time = Date(date_time.toString())
//        date_time = new Date(date_time.toString()).toISOString()

        $("#trans-flag").val(0);
        $('#stat_vehicle_weight').val(true);
//        $('#firstweight').val(weight);
//        $('#alibi_firstw').val(alibi_num);
//        date_time = date_time.replace('T', ' ')
//        date_time = date_time.replace('Z', '');
//        $('#datetime_firstw').val(date_time);

        if(selected_scale == 0)
        {
            sendRequest('GET WEIGHTNM');
        }
        else if(selected_scale == 1)
        {
            sendRequest('GET WEIGHTNM1');
        }
        web_socket.onmessage = function(event) {
        try {
            retval = JSON.parse(event.data);
            if (retval.msg_type == 'weightnm' && get_weight_nm == true) {
                console.log("scale NM", retval);

                date = retval.date;
                time = retval.time;

                date_time = date.concat(" ", time, ":00").replaceAll(".", "/")
                date_time = Date(date_time.toString())
                date_time = new Date(date_time.toString()).toISOString()
                date_time = date_time.replace('T', ' ')
                date_time = date_time.replace('Z', '');
                $('#datetime_firstw').val(date_time);
                $('#alibi_firstw').val(retval.alibi_nr);
                $('#firstweight').val(retval.weight);
            }
            else if (retval.msg_type == 'weight') {
                console.log("scale again", retval);
                weight_field = $("#id_weight");
                weight_field.text(retval.weight);

            } else if (event.data == "NO CONNECTION") {
                alert("Connection Problem");
            }
        }
        catch(err) {
            alert("Error in fetching json")
        }

        get_weight_nm = false;
    };

//Code for load all images on first weight click
//        var img_loading1 = $("#img_loading1");
//        var img_loading2 = $("#img_loading2");
//        var img_loading3 = $("#img_loading3");
//        img_loading1.show();
//        img_loading2.show();
//        img_loading3.show();
//
//        sendRequest('GET IMAGE');
//        web_socket.onmessage = function(event) {
//
//        try {
//            retval = JSON.parse(event.data);
//            if (retval.msg_type == 'image')
//            {
//                img_loading1.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//                img_loading2.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//                img_loading3.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//
////                img_loading1.val(retval.image_data)
////                img_loading2.val(retval.image_data)
////                img_loading3.val(retval.image_data)
//                $('#id_img_loading1').attr("value", "data: image/jpeg;base64, " + retval.image_data);
//                $('#id_img_loading2').attr("value", "data: image/jpeg;base64, " + retval.image_data);
//                $('#id_img_loading3').attr("value", "data: image/jpeg;base64, " + retval.image_data);
//            }
//            else if (retval.msg_type == 'weight') {
//
//                weight_field = $("#id_weight");
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                weight_field.text(retval.weight);
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);
//
//            } else if (event.data == "NO CONNECTION") {
//                alert("Connection Problem");
//            }
//        }
//        catch(err) {
//            alert("Error in fetching json")
//        }
//     }
    });

    $('#btn-secondweight').click(function(event) {
        event.preventDefault();
        var get_weight_nm = true;
        // popup
                var title = "Transcations";
                var body = "Transcation List";
                $("#MyPopup .modal-title").html(title);
                $("#MyPopup .modal-body").html(body);
                // $("#MyPopup").show()
                 // $('#my-modal').modal({
                 //      show: 'True'
                 //  }); 
                $("#btnClosePopup").click(function () {
                    $("#MyPopup").modal("hide");
                });
                 $("#MyPopup .modal-body").load("transcation_popup/");
                $("#MyPopup").modal();
        // popup end

//        weight = $("#id_weight").text();
//        date = $("#id_date").val();
//        time = $("#id_time").val();
//        alibi_num = $("#id_alibi_num").val();
//        date_time = date.concat(" ", time, ":00").replaceAll(".", "/")
//        date_time = Date(date_time.toString())
//        date_time = new Date(date_time.toString()).toISOString()
//        $('#secondweight').val(weight);
//        // calculate net weight
//        first_weight = $('#firstweight').val();
//        second_weight = $('#secondweight').val();
//        net_weight = Math.abs(second_weight - first_weight)
//        $("#netweight").val(net_weight);
//        var gmtDateTime = new Date(date_time).toISOString()
//        date_time = date_time.replace('T', ' ')
//        date_time = date_time.replace('Z', '');
//        $('#datetime_secondw').val(date_time);
//        $('#alibi_secondw').val(alibi_num);
        $("#trans-flag").val(1);

        if(selected_scale == 0)
        {
            sendRequest('GET WEIGHTNM');
        }
        else if(selected_scale == 1)
        {
            sendRequest('GET WEIGHTNM1');
        }

        web_socket.onmessage = function(event) {
        try {
            retval = JSON.parse(event.data);
            if (retval.msg_type == 'weightnm' && get_weight_nm == true) {
                console.log("scale NM", retval);

                date = retval.date;
                time = retval.time;

                date_time = date.concat(" ", time, ":00").replaceAll(".", "/")
                date_time = Date(date_time.toString())
                date_time = new Date(date_time.toString()).toISOString()
                date_time = date_time.replace('T', ' ')
                date_time = date_time.replace('Z', '');
                $('#datetime_secondw').val(date_time);
                $('#alibi_secondw').val(retval.alibi_nr);
                $('#secondweight').val(retval.weight);

                first_weight = $('#firstweight').val();
                second_weight = $('#secondweight').val();
                net_weight = Math.abs(second_weight - first_weight)
                $("#netweight").val(net_weight);
        }
        else if (retval.msg_type == 'weight') {
                console.log("scale again", retval);
                weight_field = $("#id_weight");
                weight_field.text(retval.weight);

            } else if (event.data == "NO CONNECTION") {
                alert("Connection Problem");
            }
        }
        catch(err) {
            alert("Error in fetching json")
        }

        get_weight_nm = false;
    };

// Code for fetching all images when second weight click
//        var img_loading1 = $("#img_loading1");
//        var img_loading2 = $("#img_loading2");
//        var img_loading3 = $("#img_loading3");
//        img_loading1.show();
//        img_loading2.show();
//        img_loading3.show();
//
//        sendRequest('GET IMAGE');
//        web_socket.onmessage = function(event) {
//
//        try {
//            retval = JSON.parse(event.data);
//            if (retval.msg_type == 'image')
//            {
//                console.log("Image",retval);
//                img_loading1.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//                img_loading2.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//                img_loading3.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//
//                $('#id_img_loading1').attr("value", "data: image/jpeg;base64, " + retval.image_data);
//                $('#id_img_loading2').attr("value", "data: image/jpeg;base64, " + retval.image_data);
//                $('#id_img_loading3').attr("value", "data: image/jpeg;base64, " + retval.image_data);
//            }
//            else if (retval.msg_type == 'weight') {
//                console.log("scale again", retval);
//
//                weight_field = $("#id_weight");
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                weight_field.text(retval.weight);
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);
//
//            } else if (event.data == "NO CONNECTION") {
//                alert("Connection Problem");
//            }
//        }
//        catch(err) {
//            alert("Error in fetching json")
//        }
//     }

    });
    $('#btn-netweight').click(function(event) {
        // calculate net weight
        first_weight = $('#firstweight').val();
        second_weight = $('#secondweight').val();
        net_weight = Math.abs(second_weight - first_weight)
        $("#netweight").val(net_weight);
        event.preventDefault();
    });

    $('#id_capture_image1').click(function(event) {

        event.preventDefault();
        var img_loading1 = $("#img_loading1");
        var img_loading2 = $("#img_loading2");
        var img_loading3 = $("#img_loading3");
        img_loading1.show();
//        img_loading2.show();
//        img_loading3.show();

        sendRequest('GET IMAGE1');
        web_socket.onmessage = function(event) {

        try {
            retval = JSON.parse(event.data);
            if (retval.msg_type == 'image')
            {
                console.log("Image",retval);
                img_loading1.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//                img_loading2.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//                img_loading3.attr("src", "data: image/jpeg;base64, " + retval.image_data);

                $('#id_img_loading1').attr("value", "data: image/jpeg;base64, " + retval.image_data);
//                $('#id_img_loading2').attr("value", "data: image/jpeg;base64, " + retval.image_data);
//                $('#id_img_loading3').attr("value", "data: image/jpeg;base64, " + retval.image_data);
            }
            else if (retval.msg_type == 'weight') {
                console.log("scale again", retval);

                weight_field = $("#id_weight");
                weight_field.text(retval.weight);
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);

            } else if (event.data == "NO CONNECTION") {
                alert("Connection Problem");
            }
        }
        catch(err) {
            alert("Error in fetching json")
        }
     }
    });
    $('#id_capture_image2').click(function(event) {

        event.preventDefault();
        var img_loading2 = $("#img_loading2");
        img_loading2.show();

        sendRequest('GET IMAGE2');
        web_socket.onmessage = function(event) {

        try {
            retval = JSON.parse(event.data);
            if (retval.msg_type == 'image')
            {
                console.log("Image",retval);
                img_loading2.attr("src", "data: image/jpeg;base64, " + retval.image_data);

                $('#id_img_loading2').attr("value", "data: image/jpeg;base64, " + retval.image_data);
            }
            else if (retval.msg_type == 'weight') {
                console.log("scale again", retval);

                weight_field = $("#id_weight");
                weight_field.text(retval.weight);
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);

            } else if (event.data == "NO CONNECTION") {
                alert("Connection Problem");
            }
        }
        catch(err) {
            alert("Error in fetching json")
        }
     }
    });

    $('#id_capture_image3').click(function(event) {

        event.preventDefault();
        var img_loading3 = $("#img_loading3");
        img_loading3.show();

        sendRequest('GET IMAGE3');
        web_socket.onmessage = function(event) {

        try {
            retval = JSON.parse(event.data);
            if (retval.msg_type == 'image')
            {
                console.log("Image",retval);
                img_loading3.attr("src", "data: image/jpeg;base64, " + retval.image_data);

                $('#id_img_loading3').attr("value", "data: image/jpeg;base64, " + retval.image_data);
            }
            else if (retval.msg_type == 'weight') {
                console.log("scale again", retval);

                weight_field = $("#id_weight");
                weight_field.text(retval.weight);
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);

            } else if (event.data == "NO CONNECTION") {
                alert("Connection Problem");
            }
        }
        catch(err) {
            alert("Error in fetching json")
        }
     }
    });

    $('#read_camera').click(function(event) {
        event.preventDefault();

        sendRequest('GET PLATE');
        web_socket.onmessage = function(event) {
            retval = JSON.parse(event.data);
            if (retval.msg_type == 'plate') {
                console.log("plate", retval);
                var existing_plate = false
                $("#id_vehicle option").each(function() {
                    if (retval.license_plate == $(this).text()) {
                        $("#id_vehicle").val($(this).val()).trigger('change');
                        existing_plate = true
                        $('.fahrzeuge').removeClass('loading')
                    }

                });
                if (existing_plate == false) {
                    var cameRead = $("<option selected='selected'></option>").text(retval.license_plate);
                    $("#id_vehicle").append(cameRead).trigger('change');
                    $('.fahrzeuge').removeClass('loading')
                }
            } else if (retval.msg_type == 'weight') {
                console.log("scale again", retval);

                weight_field = $("#id_weight");
                weight_field.text(retval.weight);
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);

            } else if (event.data == "NO CONNECTION") {
                alert("Connection Problem");
            }
        };




        //   if (websocket.readyState != WebSocket.CLOSED) {
        //     websocket.onclose = function () {websocket.close();}; // disable onclose handler first
        //    // Do your stuff...
        // }
        // var bufferedAmount = web_socket.bufferedAmount;
        // alert(bufferedAmount);
        // clearTimeout(sendRequest);
        // websocketStart(1);
        // clearTimeout(sendRequest);
        // web_socket = new WebSocket('ws://localhost:9002/');
        // web_socket.onopen = function(event){
        // sendRequest('GET PLATE'); }
        // web_socket.onmessage = function(event) {
        //   // retval = JSON.parse(event.data);
        //   console.log("NUMBER",event.data);
        //   clearTimeout(sendRequest);
        //   clearTimeout(websocketStart())
        //   websocketStart();
        // };
    });
    $('#read_camera2').click(function(event) {
        event.preventDefault();

        sendRequest('GET PLATE');
        web_socket.onmessage = function(event) {
            retval = JSON.parse(event.data);
            if (retval.msg_type == 'plate') {
                console.log("plate", retval);
                $("#license_plate2").val(retval.license_plate)

            } else if (retval.msg_type == 'weight') {
                console.log("scale again", retval);

                weight_field = $("#id_weight");
                date_field = $("#id_date");
                time_field = $("#id_time");
                alibi_num_field = $("#id_alibi_num");
                weight_field.text(retval.weight);
                date_field.val(retval.date);
                time_field.val(retval.time);
                alibi_num_field.val(retval.alibi_nr);

            } else if (event.data == "NO CONNECTION") {
                alert("Connection Problem");
            }
        };
    });

    $('#btn-index-save').click(function(event) {
        var customer = document.forms["myForm"]["id_customer"].value;
         if (customer == 0) {
            alert("Please select a customer to continue");
            return false;
          }

        var velicle = document.forms["myForm"]["id_vehicle"].value;
         if (velicle == 0) {
            alert("Please select a vehicle to continue");
            return false;
          }

        var material = document.forms["myForm"]["id_article"].value;
         if (material == 0) {
            alert("Please select a Material to continue");
            return false;
          }

        var lieferanten = document.forms["myForm"]["id_supplier"].value;
         if (lieferanten == 0) {
            alert("Please select a Supplier to continue");
            return false;
          }

        var article_price = document.forms["myForm"]["article_price"].value;
         if (article_price == 0) {
            alert("Please enter Article Price!");
            return false;
          }
        var veh_weight = document.forms["myForm"]["vehicle_weight"].value;
         if (veh_weight == 0) {
            alert("Please enter Vehicle Weight!");
            return false;
          }
        // event.preventDefault();
//        $('#form_home').append('<input type="text" name="image_loading1" value="'+$('#img_loading1').attr('src')+'" />');
//        $('#form_home').append('<input type="text" name="image_loading2" value="'+$('#img_loading2').attr('src')+'" />');
//        $('#form_home').append('<input type="text" name="image_loading3" value="'+$('#img_loading3').attr('src')+'" />');
        var form = $('#form_home');
        form.attr('target', '')
        form.submit();
    });

    $('#btn-print').click(function(event) {
       var customer = document.forms["myForm"]["id_customer"].value;
         if (customer == 0) {
            alert("Please select a customer to continue");
            return false;
          }

        var velicle = document.forms["myForm"]["id_vehicle"].value;
         if (velicle == 0) {
            alert("Please select a vehicle to continue");
            return false;
          }

        var material = document.forms["myForm"]["id_article"].value;
         if (material == 0) {
            alert("Please select a Material to continue");
            return false;
          }

        var lieferanten = document.forms["myForm"]["id_supplier"].value;
         if (lieferanten == 0) {
            alert("Please select a Supplier to continue");
            return false;
          }

        var article_price = document.forms["myForm"]["article_price"].value;
         if (article_price == 0) {
            alert("Please enter Article Price!");
            return false;
          }
        var veh_weight = document.forms["myForm"]["vehicle_weight"].value;
         if (veh_weight == 0) {
            alert("Please enter Vehicle Weight!");
            return false;
          }
//        $('#form_home').append('<input type="text" name="image_loading1" value="'+$('#img_loading1').attr('src')+'" />');
//        $('#form_home').append('<input type="text" name="image_loading2" value="'+$('#img_loading2').attr('src')+'" />');
//        $('#form_home').append('<input type="text" name="image_loading3" value="'+$('#img_loading3').attr('src')+'" />');
        $('#form_home').append('<input type="hidden" name="print_button" value="print"/>');
        var image_not_required, netweight_not_required;
        var image1 = $('#img_loading1').attr('src')
        var image2 = $('#img_loading2').attr('src')
        var image3 = $('#img_loading3').attr('src')
        if (image1 == "/static/yard/images/loading.gif" || image2 == "/static/yard/images/loading.gif"
        || image3 == "/static/yard/images/loading.gif"){
            var txt;
                var r = confirm("Images are not loaded Do you want to continue without all images?");
                if (r == true) {
                   event.preventDefault();
                       image_not_required = true;
                } else {
                  image_not_required = false;
                  return false;
                }
        }
        else
        {
            image_not_required = true;

        }
        net_weight = $('#netweight').val();
        if(parseFloat(net_weight) == 0)
        {
            var r = confirm("Nettogewicht ist 0, möchten Sie den Vorgang Fortsetzen?");
                if (r == true) {
                   event.preventDefault();
                        netweight_not_required = true;
                } else {
                  netweight_not_required = false;
                  return false;
                }
        }
        else
        {
            netweight_not_required = true;
        }
        if(image_not_required  && netweight_not_required )
        {
            var form = $('#form_home');
            form.submit();
        }
        else
        {
            return false;
        }
        event.preventDefault();
//        var form = $('#form_home');
//        // form.attr('target', '')
//        form.submit();

    });
//    $('#btn-image-capture').click(function(event) {
//        window.open('/captured_image/', '_self');
//        event.preventDefault();
//    });

  // customer advanced search popup  start

  $("#customerPopup").click(function(){
            var title = "Search Customer";
            var body = "customers list";
            $("#MyPopup .modal-title").html(title);
            $("#MyPopup .modal-body").html(body);
            // $("#MyPopup").show()
             // $('#my-modal').modal({
             //      show: 'True'
             //  }); 
            $("#btnClosePopup").click(function () {
                $("#MyPopup").modal("hide");
            });
             $("#MyPopup .modal-body").load("customer_popup/");
    $("#MyPopup").modal();
  });

  // customer advanced search popup end  

  // materialPopup advanced search popup  start

  $("#materialPopup").click(function(){
            var title = "Search Material";
            var body = "Material list";
            $("#MyPopup .modal-title").html(title);
            $("#MyPopup .modal-body").html(body);
            // $("#MyPopup").show()
             // $('#my-modal').modal({
             //      show: 'True'
             //  }); 
            $("#btnClosePopup").click(function () {
                $("#MyPopup").modal("hide");
            });
             $("#MyPopup .modal-body").load("material_popup/");
    $("#MyPopup").modal();
  });

  // materialPopup advanced search popup end  

  // vehiclePopup advanced search popup  start

  $("#vehiclePopup").click(function(){
            var title = "Search Vehicle";
            var body = "Vehicle list";
            $("#MyPopup .modal-title").html(title);
            $("#MyPopup .modal-body").html(body);
            // $("#MyPopup").show()
             // $('#my-modal').modal({
             //      show: 'True'
             //  }); 
            $("#btnClosePopup").click(function () {
                $("#MyPopup").modal("hide");
            });
             $("#MyPopup .modal-body").load("vehicle_popup/");
    $("#MyPopup").modal();
  });
  // vehiclePopup advanced search popup end  

  // supplierPopup advanced search popup  start

  $("#supplierPopup").click(function(){
            var title = "Search Supplier";
            var body = "Supplier list";
            $("#MyPopup .modal-title").html(title);
            $("#MyPopup .modal-body").html(body);
            // $("#MyPopup").show()
             // $('#my-modal').modal({
             //      show: 'True'
             //  }); 
            $("#btnClosePopup").click(function () {
                $("#MyPopup").modal("hide");
            });
             $("#MyPopup .modal-body").load("supplier_popup/");
    $("#MyPopup").modal();
  });
  // supplierPopup advanced search popup end  
 $('img').on('click', function () {
        var image = $(this).attr('src');
        $('#myModal').on('show.bs.modal', function () {
            $(".img-responsive").attr("src", image);
        });
    });

});

var weight_field;
var web_socket;
var timeout = 1000;

function sendRequest(request_msg) {
    web_socket.send(request_msg)
    if (request_msg == 'GET WEIGHT' && selected_scale == 0) {
        setTimeout(function() {
            sendRequest(request_msg);
        }, timeout);
    }
    else if (request_msg == 'GET WEIGHT1' && selected_scale == 1)
    {
        setTimeout(function() {
                sendRequest(request_msg);
            }, timeout);
    }

}
//var selected_scale = "Scale1"
//$("input[type=radio][name=scale]").change(function() {
//    selected_scale = $(this).val()
//    // websocketStart();
//});

web_socket = new WebSocket('ws://localhost:9001/')

function websocketStart(request_msg) {
    weight_field = $("#id_weight");
    date_field = $("#id_date");
    time_field = $("#id_time");
    alibi_num_field = $("#id_alibi_num");
    // if (selected_scale =="scale1"){

    // }else{

    // web_socket = new WebSocket('ws://localhost:9003/');
    // }

    web_socket.onopen = function(event) {
        //setTimeout(function(){ sendRequest(); }, timeout);
        sendRequest(request_msg);
    }
    web_socket.onmessage = function(event) {
        retval = JSON.parse(event.data);
        if (retval.msg_type == 'weight') {
            console.log("scale", retval);
            weight_field.text(retval.weight);
//            date_field.val(retval.date);
//            time_field.val(retval.time);
//            alibi_num_field.val(retval.alibi_nr);
        }

    };
}



function loadTranscationDetails(id) {
  $.ajax({
    type: "GET",
    url: "/transcation_detail/" + id,
    success: function (result) {
        $("#btnClosePopup").click();

        $('#trans_id').val(id);
        $('#id_supplier').val(result.supplier).trigger('change');
        $('#id_article').val(result.article).trigger('change');
        $('#id_vehicle').val(result.vehicle).trigger('change');
        $('#id_customer').val(result.customer).trigger('change');
        
        $('#firstweight').val(result.first_weight).delay( 800 );
        $('#alibi_firstw').val(result.firstw_alibi_nr);
        $('#datetime_firstw').val(result.firstw_date_time);
        console.log("Test Time");
        // calculate net weight
        first_weight = $('#firstweight').val();
        second_weight = $('#secondweight').val();
        net_weight = Math.abs(second_weight - first_weight)
        $("#netweight").val(net_weight);
    }

  });
}

$("#btn-firstweight").click(function(e) {
    e.preventDefault();
    $.ajax({
        type: "GET",
        url: "/scale_data/",    
        contentType: "application/json",
        dataType: 'json',
        data: { 
           
        },
        success: function(result) {
                document.getElementById("firstweight").value = result.weight
               // document.getElementById("firstweight").name = result.weight
                document.getElementById("datetime_firstw").value = result.datetime
               // document.getElementById("datetime_firstw").name = result.datetime
                document.getElementById("alibi_firstw").value = result.alibi_nr
                //document.getElementById("alibi_firstw").name = result.alibi_nr
               
        },
        error: function(result) {
           // alert('error');
        }
    });
});


$("#btn-secondweight").click(function(e) {
    e.preventDefault();
    $.ajax({
        type: "GET",
        url: "/scale_data/",    
        contentType: "application/json",
        dataType: 'json',
        data: { 
       
        },
        success: function(result) {

                document.getElementById("secondweight").value = result.weight
                //document.getElementById("secondweight").name = result.weight
                document.getElementById("datetime_secondw").value = result.datetime
                //document.getElementById("datetime_secondw").name = result.datetime
                document.getElementById("alibi_secondw").value = result.alibi_nr
               // document.getElementById("alibi_secondw").name = result.alibi_nr
                
          
        },
        error: function(result) {
            //alert('error');
        }
    });
});

//$('#btn-print').click(function (event) {
//  event.preventDefault();
//
//  var form = $('#form_home');
//  form.attr('target', '_blank')
//
//    var url ="/";
//
//    $.ajax({
//           type: "POST",
//           url: url,
//           data: form.serialize(), // serializes the form's elements.
//           success: function(data)
//           {
//               alert(data); // show response from the php script.
//           }
//         });
//  });

