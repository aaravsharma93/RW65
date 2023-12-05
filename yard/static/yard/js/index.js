var selected_scale = 0 ;
var img = 0;

$(document).ready(function() {
    // websocketStart('GET WEIGHT');
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
    $("#sp_cust").select2({
        tags: true
    });
    $("#sp_veh").select2({
        tags: true
    });
    $("#sp_sup").select2({
        tags: true
    });
    $("#sp_art").select2({
        tags: true
    });

    $("#id_ident").select2({
        tags: true
    });
    $('#clear_ident').click(function(e) {
        e.preventDefault()
        $('#id_ident').val(0).trigger('change');
        $('.artikel').val("")
        $('.lieferanten').val("")
        $('.fahrzeuge').val("")
        $('.kunden').val("")
        $('.container').val('')
        $('#secondweight').val("0000")
        $("#status").val('')
        $("#netweight").val("0000")
        $("#firstweight").val("0000")
        $("#trans-flag").val("");
        $("#alibi_firstw").val("0000")
        $("#alibi_secondw").val("0000")
        value = $("#btn-firstweight").prop('disabled'); 
            if (value == true){
                $("#btn-firstweight").prop('disabled',false);
                $('#stat_vehicle_weight').val(0);
                $("#btn_tara").text("Ohne");
                $("#firstweight").val("0000");
                $("#firstweight").prop('readonly',true)
                $("#firstweight").css('pointer-events','none')
            }

        value2 = $("#btn-secondweight").prop('disabled');
            if (value2 == true){
                $("#btn-secondweight").prop('disabled',false);
                $('#stat_vehicle_second_weight').val(0);
                $("#firstweight").val("0000");
                $("#secondweight").prop('readonly',true)
                $("#secondweight").css('pointer-events','none')
            } 

        resetImageCont();

    
    });


    // $("#firstweight").change(function(){
    //     first_weight = $('#firstweight').val();
    //     second_weight = $('#secondweight').val();
    //     net_weight = Math.abs(second_weight - first_weight)
    //     $("#netweight").val(net_weight);
    // })

    // $("#secondweight").change(function(){
    //     first_weight = $('#firstweight').val();
    //     second_weight = $('#secondweight').val();
    //     net_weight = Math.abs(second_weight - first_weight)
    //     $("#netweight").val(net_weight);
    // })



    $("#firstweight").keyup(function(){
        first = $(this).val();
        second = $("#secondweight").val();
        container_weight = $("#contr_weight").val();
        final_weight = Math.abs(second - first)
        if ($("#contr_on").val() == "true"){
            net_weight = Math.abs(final_weight - container_weight);
            $("#netweight").val(net_weight);
        } else {
            net_weight = final_weight;
            $("#netweight").val(net_weight);
        }
        currentdate = new Date();
        date_time = currentdate.getFullYear()+"-"+(currentdate.getMonth()+1)+"-"+currentdate.getDate()+" "+currentdate.getHours()+":"+currentdate.getMinutes()+":"+currentdate.getSeconds()+".000"
        $('#datetime_firstw').val(date_time);
      })
      
      $("#secondweight").keyup(function(){
        first = $("#firstweight").val();
        second = $(this).val();
        container_weight = $("#contr_weight").val();
        final_weight = Math.abs(second - first)
        if ($("#contr_on").val() == "true"){
            net_weight = Math.abs(final_weight - container_weight);
            $("#netweight").val(net_weight);
        } else {
            net_weight = final_weight;
            $("#netweight").val(net_weight);
        }
        currentdate = new Date();
        date_time = currentdate.getFullYear()+"-"+(currentdate.getMonth()+1)+"-"+currentdate.getDate()+" "+currentdate.getHours()+":"+currentdate.getMinutes()+":"+currentdate.getSeconds()+".000"
        $('#datetime_secondw').val(date_time);
      })

    $('#id_scale2_tab').click(async function(event) {
        event.preventDefault();
        selected_scale = 1 ;
        alert("Reading weight from Scale 2");
        await sendRequest('GET WEIGHT1');
        });

        $('#id_scale1_tab').click(async function(event) {
        event.preventDefault();
        selected_scale = 0 ;
        alert("Reading weight from Scale 1");
        await sendRequest('GET WEIGHT');
        });

    $('#btn-firstweight').click(async function(event) {
        event.preventDefault();
        ew = $("#btn_ew_input").val()
        var velicle = document.forms["myForm"]["id_vehicle"].value;
        if (ew == '0' && velicle == 0 ){
                alert(`Sie können noch nicht wiegen!
Bitte wählen Sie ein Fahrzeug aus.`);
                return false;
            } else {



        var get_weight_nm = true;
//        weight = $("#id_weight").text();
//        date = $("#id_date").val();
//        time = $("#id_time").val();
//        alibi_num = $("#id_alibi_num").val();
//        date_time = date.concat(" ", time, ":00").replaceAll(".", "/")
//        date_time = Date(date_time.toString())
//        date_time = new Date(date_time.toString()).toISOString()

        $("#trans-flag").val(0);
      //  $('#stat_vehicle_weight').val(true);



//        $('#firstweight').val(weight);
//        $('#alibi_firstw').val(alibi_num);
//        date_time = date_time.replace('T', ' ')
//        date_time = date_time.replace('Z', '');
//        $('#datetime_firstw').val(date_time);
        let response;
        try {

            if (selected_scale == 0) {
                response = await sendRequest('GET WEIGHTNM');
            } else if (selected_scale == 1) {
                response = await sendRequest('GET WEIGHTNM1');
            }
        }catch(err){
            alert("NO CONNECTION");
        }
        
        try {
            retval = response;
            if (retval.msg_type == 'weightnm' || get_weight_nm == true) {

                date = retval.date;
                time = retval.time;

                datee = date.split('.')
                date_time = "20"+datee[2]+"-"+datee[1]+"-"+datee[0]+" "+time+":00.000"

                cap = $("#auto_capture").val()
                if(cap == 'true'){
                    $(".capture").click();
                }

                // date_time = date.concat(" ", time, ":00").replaceAll(".", "-")
                // date_time = Date(date_time.toString())
                // date_time = new Date(date_time.toString()).toISOString()
                // date_time = date_time.replace('T', ' ')
                // date_time = date_time.replace('Z', '')
                $('#datetime_firstw').val(date_time);
                $('#alibi_firstw').val(retval.alibi_nr);
                $('#firstweight').val(retval.weight);
                tara = $("#btn_tara").text();
                if (tara == "Mit"){
                    first_weight = $('#firstweight').val();
                    second_weight = $('#secondweight').val();
                    net_weight = Math.abs(second_weight - first_weight)
                    $("#netweight").val(net_weight);
                    setTimeout(()=> {$("#btn-print").click()},1000);
                } else {
                    fw_1 = $("#fw_cam_1").val()
                    fw_2 = $("#fw_cam_2").val()
                    fw_3 = $("#fw_cam_3").val()
                    if( fw_1 == 'true'){
                        $("#id_capture_image1").click();
                    }
                    if( fw_2 == 'true'){
                        $("#id_capture_image2").click();
                    }
                    if( fw_3 == 'true'){
                        $("#id_capture_image3").click();
                    }
                    function save(){
                        if(img == 1){
                            $("#btn-index-save").click()
                        } else {
                           setTimeout(()=>{
                            save()
                           },1000); 
                        }
                    }
                    
                
                if( fw_1 == 'true' || fw_2 == 'true' || fw_3 == 'true'){
                    save()
                } else {
                        setTimeout(()=> {
                                $("#btn-index-save").click()
                    },1000);
                }
                }
            }
            else if (retval.msg_type == 'weight') {
                
                weight_field = $("#id_weight");
                weight_field.text(retval.weight);

            }
        }
        catch(err) {
            alert("Bitte versuche es erneut")
        }
        

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
    }
    });

    $("#btn-hofliste").click(function(){
        // popup
        var title = "Suchen in der Hofliste";
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
         $("#MyPopup .modal-body").load("/transcation_popup/");
        $("#MyPopup").modal();
        // popup end
    });


    $('#btn-secondweight').click(async function(event) {
        event.preventDefault();
        ew = $("#btn_ew_input").val()
        fw = $('#select_from_hofliste').val();
        var velicle = document.forms["myForm"]["id_vehicle"].value;
        if (ew == '0' && fw =='0' && velicle == 0){
                alert(`Sie können noch nicht wiegen!
Bitte wählen Sie ein Fahrzeug aus.`);
                return false;
            } else {
            

        var get_weight_nm = true;
        // // popup
        //         var title = "Transcations";
        //         var body = "Transcation List";
        //         $("#MyPopup .modal-title").html(title);
        //         $("#MyPopup .modal-body").html(body);
        //         // $("#MyPopup").show()
        //          // $('#my-modal').modal({
        //          //      show: 'True'
        //          //  }); 
        //         $("#btnClosePopup").click(function () {
        //             $("#MyPopup").modal("hide");
        //         });
        //          $("#MyPopup .modal-body").load("transcation_popup/");
        //         $("#MyPopup").modal();
        // // popup end

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
        try {
         if(selected_scale == 0)
        {
           response = await sendRequest('GET WEIGHTNM');
        }
        else if(selected_scale == 1)
        {
            response = await sendRequest('GET WEIGHTNM1');
        }
        } catch (e) {
            alert("Connection Problem");
        }
        try {
            retval = response;
            if (retval.msg_type == 'weightnm' || get_weight_nm == true) {
                

                date = retval.date;
                time = retval.time;
                datee = date.split('.')
                date_time = "20"+datee[2]+"-"+datee[1]+"-"+datee[0]+" "+time+":00.000"

                // date_time = date.concat(" ", time, ":00").replaceAll(".", "-")
                // date_time = Date(date_time.toString())
                // date_time = new Date(date_time.toString()).toISOString()
                // date_time = date_time.replace('T', ' ')
                // date_time = date_time.replace('Z', '')
                $('#datetime_secondw').val(date_time);
                $('#alibi_secondw').val(retval.alibi_nr);
                $('#secondweight').val(retval.weight);

                first_weight = $('#firstweight').val();
                second_weight = $('#secondweight').val();
                container_weight = $("#contr_weight").val();
                final_weight = Math.abs(second_weight - first_weight)
                if ($("#contr_on").val() == "true"){
                    net_weight = Math.abs(final_weight - container_weight);
                    $("#netweight").val(net_weight);
                } else {
                    net_weight = final_weight;
                    $("#netweight").val(net_weight);
                }
                

                    sw_1 = $("#sw_cam_1").val()
                    sw_2 = $("#sw_cam_2").val()
                    sw_3 = $("#sw_cam_3").val()
                    if( sw_1 == 'true'){
                        $("#id_capture_image1").click();
                    }
                    if( sw_2 == 'true'){
                        $("#id_capture_image2").click();
                    }
                    if( sw_3 == 'true'){
                        $("#id_capture_image3").click();
                    }
                        function print(){
                            if(img == 1){
                                conf = confirm("Möchten Sie Drucken ??")
                                    if (conf ==true){
                                        $("#btn-print").click();
                                    } else if (conf==false){
                                                    if(confirm("Möchten Sie in Lieferscheinen speichern")){
                                                        $("#btn-index-save").click();
                                                        }
                                                    }
                            } else {
                                setTimeout(()=>{
                                    print()
                                },1000);
                            }
                                    }
                    if(sw_1 == 'true' || sw_2 == 'true' || sw_3 == 'true'){
                            print()
                    } else {
                        setTimeout(()=>{ 
                                conf = confirm("Möchten Sie Drucken ??")
                                    if (conf ==true){
                                        $("#btn-print").click();
                                    } else if (conf==false){
                                                    if(confirm("Möchten Sie in Lieferscheinen speichern")){
                                                        $("#btn-index-save").click();
                                                        }
                                                    }
                                                },1000);
                    }
        }
        else if (retval.msg_type == 'weight') {
               
                weight_field = $("#id_weight");
                weight_field.text(retval.weight);

            }
        }

        catch(err) {
            alert("Bitte versuche es erneut")
        }

        get_weight_nm = false;
    
    }

    });

    $("#btn_tara").click(function(){
        btn= $("#btn_tara").text();
        status = $("#status").val();
        
        if (btn == "Ohne" ){
            if (status == '') {
                alert("Please Select Richtung")
            } else if (status == '0'){
                    $("#status").prop('required',true);
                    $("#btn_tara").text("Mit");
                    $("#btn_hand").prop('disabled',true);
                    $('#stat_vehicle_second_weight').val(1);
                    $("#btn-secondweight").prop('disabled',true);
                    $("#tara_date").val("1");
                    $("#secondweight").val($("#vehicle_weight").val());
                    // first_weight = $('#firstweight').val();
                    // second_weight = $('#secondweight').val();
                    // net_weight = Math.abs(second_weight - first_weight)
                    // $("#netweight").val(net_weight);
                    $("#vehicle_weight").keyup(function(){
                        $("#secondweight").val(this.value);
                        // first_weight = $('#firstweight').val();
                        // second_weight = $('#secondweight').val();
                        // net_weight = Math.abs(second_weight - first_weight)
                        // $("#netweight").val(net_weight);
                    })
                    $("#btn-firstweight").prop('disabled',false);

            } else if (status == '1'){
                    $("#status").prop('required',true);
                    $("#btn_tara").text("Mit");
                    $("#btn_hand").prop('disabled',true);
                    $('#stat_vehicle_weight').val(1);
                    $("#btn-firstweight").prop('disabled',true);
                    $("#tara_date").val("0");
                    $("#firstweight").val($("#vehicle_weight").val());
                    // first_weight = $('#firstweight').val();
                    // second_weight = $('#secondweight').val();
                    // net_weight = Math.abs(second_weight - first_weight)
                    // $("#netweight").val(net_weight);
                    $("#vehicle_weight").change(function(){
                        $("#firstweight").val(this.value);
                        // first_weight = $('#firstweight').val();
                        // second_weight = $('#secondweight').val();
                        // net_weight = Math.abs(second_weight - first_weight)
                        // $("#netweight").val(net_weight);
                    })
                    $("#vehicle_weight").keyup(function(){
                        $("#firstweight").val(this.value);
                        // first_weight = $('#firstweight').val();
                        // second_weight = $('#secondweight').val();
                        // net_weight = Math.abs(second_weight - first_weight)
                        // $("#netweight").val(net_weight);
                    })
                    $("#btn-secondweight").prop('disabled',false);
            
            } else {
                $("#status").prop('required',true);
                $("#btn_tara").text("Mit");
                $("#btn_hand").prop('disabled',true);
                $('#stat_vehicle_weight').val(1);
                $("#btn-firstweight").prop('disabled',true);
                $("#tara_date").val("0");
                $("#firstweight").val($("#vehicle_weight").val());
                // first_weight = $('#firstweight').val();
                // second_weight = $('#secondweight').val();
                // net_weight = Math.abs(second_weight - first_weight)
                // $("#netweight").val(net_weight);
                $("#vehicle_weight").change(function(){
                    $("#firstweight").val(this.value);
                    // first_weight = $('#firstweight').val();
                    // second_weight = $('#secondweight').val();
                    // net_weight = Math.abs(second_weight - first_weight)
                    // $("#netweight").val(net_weight);
                })
                $("#vehicle_weight").keyup(function(){
                    $("#firstweight").val(this.value);
                    // first_weight = $('#firstweight').val();
                    // second_weight = $('#secondweight').val();
                    // net_weight = Math.abs(second_weight - first_weight)
                    // $("#netweight").val(net_weight);
                })

            }
        } else {
            $("#status").prop('required',false);
            $("#btn-firstweight").prop('disabled',false);
            $("#btn-secondweight").prop('disabled',false);
            $("#tara_date").val("0");
            $('#stat_vehicle_weight').val(0);
            $("#btn_tara").text("Ohne");
            $("#btn_hand").prop('disabled',false);
            $("#firstweight").val("0000");
            $("#secondweight").val("0000");
        }


       
    })


    $("#btn_tarawagung").click(async function(event) {
    //    event.preventDefault();
        var get_weight_nm = true;
        $("#trans-flag").val(0);

        let response;
        try {

            if (selected_scale == 0) {
                response = await sendRequest('GET WEIGHTNM');
            } else if (selected_scale == 1) {
                response = await sendRequest('GET WEIGHTNM1');
            }
        }catch(err){
            alert("NO CONNECTION");
        }
        try {
            retval = response;
            if (retval.msg_type == 'weightnm' || get_weight_nm == true) {
                $("#vehicle_weight").val(retval.weight);
                value = $("#btn-firstweight").prop('disabled');
                if (value == true){
                    date = retval.date;
                    time = retval.time;
                    datee = date.split('.')
                    date_time = "20"+datee[2]+"-"+datee[1]+"-"+datee[0]+" "+time+":00.000"
                    $('#datetime_firstw').val(date_time);
                    $("#firstweight").val(retval.weight);
                }
                weight = $("#vehicle_weight").val();
                licence_plate = $("#id_vehicle").val();
                licence_plate2 = $("#license_plate2").val();
                forwarder = $("#vehicle_forwarder").val();
                mydata = {'weight':weight, 'licence_plate':licence_plate, 'licence_plate2':licence_plate2, 'forwarder':forwarder }
                $.ajax({
                    type:'GET',
                    url:"/vehicle_save/",
                    data:mydata,
                    success:function(result){
                        j = result.status
                        if (j == 1){
                            alert(`Die Wägung wurde erfolgreich durchgeführt.
Gewiecht : ${weight} kg`);
                        }
                        else{
                            alert("error")
                        }
                    }
                })
                //setTimeout(()=> {$("#btn-index-save").click()},1000);
            }
            else if (retval.msg_type == 'weight') {
                
                weight_field = $("#id_weight");
                weight_field.text(retval.weight);

            }
        }
        catch(err) {
            alert("Bitte versuche es erneut")
        }
    });



    $("#btn_hand").click(function(){
        $("#trans-flag").val(0);
        value1 = $("#btn-firstweight").prop('disabled');
        value2 = $("#btn-secondweight").prop('disabled');


        if (value1 == true){
            $("#btn-firstweight").prop('disabled',false);
            $('#stat_vehicle_weight').val(0);
            $("#firstweight").prop('readonly',true)
            $("#btn_hand").text("Handeingabe")
            $("#btn_tara").prop('disabled',false);
            $("#firstweight").css('pointer-events','none')
        } else {
            $("#btn-firstweight").prop('disabled',true);
            $('#stat_vehicle_weight').val(2);
            $("#firstweight").prop('readonly',false)
            $("#btn_hand").text("Automatik")
            $("#btn_tara").prop('disabled',true);
            $("#firstweight").css('pointer-events','all')
        }

        if (value2 == true){
            $("#btn-secondweight").prop('disabled',false);
            $('#stat_vehicle_second_weight').val(0);
            $("#secondweight").prop('readonly',true)
        } else {
            $("#btn-secondweight").prop('disabled',true);
            $('#stat_vehicle_second_weight').val(2);
            $("#secondweight").prop('readonly',false)
            $("#secondweight").css('pointer-events','all')

        }
    })

    $('#btn-netweight').click(function(event) {
        // calculate net weight
        first_weight = $('#firstweight').val();
        second_weight = $('#secondweight').val();
        net_weight = Math.abs(second_weight - first_weight)
        $("#netweight").val(net_weight);
        event.preventDefault();
    });

    $('#id_capture_image1').click(async function(event) {

        event.preventDefault();
        var img_loading1 = $("#img_loading1");
        var img_loading2 = $("#img_loading2");
        var img_loading3 = $("#img_loading3");
        img_loading1.show();
//        img_loading2.show();
//        img_loading3.show();
        let response
        try {
            response = await sendRequest('GET IMAGE');
        }catch (e){
            alert("Connection Problem");
        }
        try {
            retval = response;
            if (retval.msg_type == 'image')
            {
                img_loading1.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//                img_loading2.attr("src", "data: image/jpeg;base64, " + retval.image_data);
//                img_loading3.attr("src", "data: image/jpeg;base64, " + retval.image_data);

                $('#id_img_loading1').attr("value", retval.image_data);
                  img = 1;

            }
            else if (retval.msg_type == 'weight') {
               

                weight_field = $("#id_weight");
                weight_field.text(retval.weight);
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);

            }
        }
        catch(err) {
            alert("Bitte versuche es erneut")
        }
    });
    $('#id_capture_image2').click(async function(event) {

        event.preventDefault();
        var img_loading2 = $("#img_loading2");
        img_loading2.show();
        let response;
        try {
            response = await sendRequest('GET IMAGE1');
        }catch (e) {
            console.log(e)
            alert("Connection Problem");
        }

        try {
            retval = response;
            if (retval.msg_type == 'image')
            {
                img_loading2.attr("src", "data: image/jpeg;base64, " + retval.image_data);

                $('#id_img_loading2').attr("value", retval.image_data);
                img = 1;
            }
            else if (retval.msg_type == 'weight') {
            

                weight_field = $("#id_weight");
                weight_field.text(retval.weight);
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);

            }
        }
        catch(err) {
            alert("Bitte versuche es erneut")
        }
    });

    $('#id_capture_image3').click(async function(event) {

        event.preventDefault();
        var img_loading3 = $("#img_loading3");
        img_loading3.show();
        let response;
        try {
            response = await sendRequest('GET IMAGE2');
        }catch (e) {
            console.log(e)
            alert("Connection Problem");
        }

        try {
            retval = response;
            if (retval.msg_type == 'image')
            {
               
                img_loading3.attr("src", "data: image/jpeg;base64, " + retval.image_data);

                $('#id_img_loading3').attr("value", retval.image_data);
                 img = 1;
            }
            else if (retval.msg_type == 'weight') {
                

                weight_field = $("#id_weight");
                weight_field.text(retval.weight);
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);

            }
            }catch(err) {
            alert("Bitte versuche es erneut")
        }
    });

    $('#read_camera').click(async function(event) {
        event.preventDefault();
        let response;
        try {
             response = await sendRequest('GET PLATE');
        }catch (e) {
            console.log(e);
            alert("Connection Problem");
        }
        retval = response;
        if (retval.msg_type == 'plate') {
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
            weight_field = $("#id_weight");
            weight_field.text(retval.weight);
//                date_field = $("#id_date");
//                time_field = $("#id_time");
//                alibi_num_field = $("#id_alibi_num");
//                date_field.val(retval.date);
//                time_field.val(retval.time);
//                alibi_num_field.val(retval.alibi_nr);

            } else if (response.data == "NO CONNECTION") {
                alert("Connection Problem");
            }
        });




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
    $('#read_camera2').click(async function(event) {
        event.preventDefault();
        let response;
        try {
            response =await sendRequest('GET PLATE');
        }catch (e) {
            console.log(e);
            alert("Connection Problem");
        }
            retval = response;
            if (retval.msg_type == 'plate') {
                $("#license_plate2").val(retval.license_plate)

            } else if (retval.msg_type == 'weight') {
             

                weight_field = $("#id_weight");
                date_field = $("#id_date");
                time_field = $("#id_time");
                alibi_num_field = $("#id_alibi_num");
                weight_field.text(retval.weight);
                date_field.val(retval.date);
                time_field.val(retval.time);
                alibi_num_field.val(retval.alibi_nr);

            }
    });

    $("#btn_ew").click(function(){
        input = $("#btn_ew_input").val()
        if (input == '0'){
            $(this).removeClass('btn-dark').addClass('btn-success')
            $("#btn_ew_input").val('1')
        } else if (input == '1'){
            $(this).removeClass('btn-success').addClass('btn-dark')
            $("#btn_ew_input").val('0')
        }
    })

    $('#btn-index-save').click(function(event) {
        // var customer = document.forms["myForm"]["id_customer"].value;
        //  if (customer == 0) {
        //     alert("Please select a customer to continue");
        //     return false;
        //   }
//         ew = $("#btn_ew_input").val()
//         if (ew == '0'){
//             var velicle = document.forms["myForm"]["id_vehicle"].value;
//                 if (velicle == 0) {
//                     alert(`Sie können noch nicht wiegen!
//  Bitte wählen Sie ein Fahrzeug aus.`);
//                     return false;
//                 }
//         }
        // var material = document.forms["myForm"]["id_article"].value;
        //  if (material == 0) {
        //     alert("Please select a Material to continue");
        //     return false;
        //   }

        // var lieferanten = document.forms["myForm"]["id_supplier"].value;
        //  if (lieferanten == 0) {
        //     alert("Please select a Supplier to continue");
        //     return false;
        //   }

        // var article_price = document.forms["myForm"]["article_price"].value;
        //  if (article_price == 0) {
        //     alert("Please enter Article Price!");
        //     return false;
        //   }
        // var veh_weight = document.forms["myForm"]["vehicle_weight"].value;
        //  if (veh_weight == 0) {
        //     alert("Please enter Vehicle Weight!");
        //     return false;
        //   }




        
        
//        $('#form_home').append('<input type="text" name="image_loading1" value="'+$('#img_loading1').attr('src')+'" />');
//        $('#form_home').append('<input type="text" name="image_loading2" value="'+$('#img_loading2').attr('src')+'" />');
//        $('#form_home').append('<input type="text" name="image_loading3" value="'+$('#img_loading3').attr('src')+'" />');
        var form = $('#form_home');
        form.attr('target', '')
        form.submit();
    });

    $('#btn-print').click(function(event) {
    //    var customer = document.forms["myForm"]["id_customer"].value;
    //      if (customer == 0) {
    //         alert("Please select a customer to continue");
    //         return false;
    //       }
           
        //         var velicle = document.forms["myForm"]["id_vehicle"].value;
        //         if (velicle == 0) {
        //             alert(`Sie können noch nicht wiegen!
        // Bitte wählen Sie ein Fahrzeug aus.`);
        //             return false;
        //         }   
        // var material = document.forms["myForm"]["id_article"].value;
        //  if (material == 0) {
        //     alert("Please select a Material to continue");
        //     return false;
        //   }

        // var lieferanten = document.forms["myForm"]["id_supplier"].value;
        //  if (lieferanten == 0) {
        //     alert("Please select a Supplier to continue");
        //     return false;
        //   }

        // var article_price = document.forms["myForm"]["article_price"].value;
        //  if (article_price == 0) {
        //     alert("Please enter Article Price!");
        //     return false;
        //   }
        // var veh_weight = document.forms["myForm"]["vehicle_weight"].value;
        //  if (veh_weight == 0) {
        //     alert("Please enter Vehicle Weight!");
        //     return false;
        //   }
//        $('#form_home').append('<input type="text" name="image_loading1" value="'+$('#img_loading1').attr('src')+'" />');
//        $('#form_home').append('<input type="text" name="image_loading2" value="'+$('#img_loading2').attr('src')+'" />');
//        $('#form_home').append('<input type="text" name="image_loading3" value="'+$('#img_loading3').attr('src')+'" />');
        $('#form_home').append('<input type="hidden" name="print_button" value="print"/>');
        var image_not_required, netweight_not_required;
        var image1 = $('#img_loading1').attr('value')
        var image2 = $('#img_loading2').attr('value')
        var image3 = $('#img_loading3').attr('value')
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
            var r = confirm("Nettogewicht ist 0, Mochten Sie den Vorgang Fortsetzen?");
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
            $("#form_home").prop('target','_blank')
            form.submit();
            setTimeout(()=> { 
                $("#clear_ident").click();
                location.reload(); } ,2000);
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
            var title = "Kunden Suchen";
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
            var title = "Artikel Suchen";
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
            var title = "Fahrzeug Suchen";
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
            var title = "Baustelle Suchen";
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
var timeout = 3000;

async function sendRequest(request_msg) {
    // console.log(request_msg)
    let url = `/scale_data/?cmd=${request_msg}`;
    const result = await $.ajax({
        url: url,
        type: 'GET',
    });
    return result;
    // web_socket.send(request_msg)
    // if (request_msg == 'GET WEIGHT' && selected_scale == 0) {
    //     setTimeout(function() {
    //         sendRequest(request_msg);
    //     }, timeout);
    // }
    // else if (request_msg == 'GET WEIGHT1' && selected_scale == 1)
    // {
    //     setTimeout(function() {
    //             sendRequest(request_msg);
    //         }, timeout);
    // }

}
//var selected_scale = "Scale1"
//$("input[type=radio][name=scale]").change(function() {
//    selected_scale = $(this).val()
//    // websocketStart();
//});

// web_socket = new WebSocket('ws://localhost:9001/')
// var websock;
// if (web_socket.readyState == 0){
//     websock = 0;
// } else {
//     websock = 1;
// }
// console.log(websock);

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
            weight_field.text(retval.weight);
//            date_field.val(retval.date);
//            time_field.val(retval.time);
//            alibi_num_field.val(retval.alibi_nr);
        }

    };
}

function resetImageCont(){
    var img_loading1 = $("#img_loading1");
    img_loading1.removeAttr("src");
    $('#id_img_loading1').removeAttr("value");

    var img_loading2 = $("#img_loading2");
    img_loading2.removeAttr("src");
    $('#id_img_loading2').removeAttr("value");

    var img_loading3 = $("#img_loading3");
    img_loading3.removeAttr("src");
    $('#id_img_loading3').removeAttr("value");
}


function loadTranscationDetails(id) {
    resetImageCont();
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
        $('#id_container').val(result.container).trigger('change');
        $("#status").val(result.status)
        $("#select_from_hofliste").val('1');
        $('#firstweight').val(result.first_weight).delay( 800 );
        $('#alibi_firstw').val(result.firstw_alibi_nr);
        $('#datetime_firstw').val(result.firstw_date_time);
        console.log("Test Time");
        if (result.combination_id != null){
            $("#id_ident").val(result.combination_id).trigger('change');
        }
        $("#id_transaction_id").val(id);     
        // calculate net weight
        first_weight = $('#firstweight').val();
        second_weight = $('#secondweight').val();
        net_weight = Math.abs(second_weight - first_weight)
        $("#netweight").val(net_weight);

        if(result.images.image1){
            var img_loading1 = $("#img_loading1");
            img_loading1.show();
            img_loading1.attr("src", "data: image/jpeg;base64, " + result.images.image1);
            $('#id_img_loading1').attr("value", result.images.image1);
        }
        if(result.images.image2){
            let img_loading2 = $("#img_loading2");
            img_loading2.show();
            img_loading2.attr("src", "data: image/jpeg;base64, " + result.images.image2);
            $('#id_img_loading2').attr("value", result.images.image2);
        }
        if(result.images.image3){
            let img_loading3 = $("#img_loading3");
            img_loading3.show();
            img_loading3.attr("src", "data: image/jpeg;base64, " + result.images.image3);
            $('#id_img_loading3').attr("value", result.images.image3);
        }
    }

  });
}

$("#s_on").click(async function(){
    $(this).removeClass('btn-secondary').addClass('btn-success')
    $("#s_off").removeClass('btn-danger').addClass('btn-secondary')
    m = 1;
    n = m+1;
    try {
    cmd = await sendRequest('OUT'+n+' OFF');
        } catch(error) {
            alert ("connection error")
        }
        if (cmd.state == 'good'){
            try{
            cmd1 = await sendRequest('OUT'+m+' ON');
                } catch (error) {
                    alert('Connection error')
                }
            if (cmd1.state == 'good'){
                alert("open")
            }
            else{
                alert('Try Again')
            }

    } else {
        alert("Try Again")
    }
})

$("#s_off").click(async function(){
    $(this).removeClass('btn-secondary').addClass('btn-danger')
    $("#s_on").removeClass('btn-success').addClass('btn-secondary')
    m=2;
    n=m-1;
    try {
    cmd = await sendRequest('OUT'+n+' OFF');
    } catch(error) {
        alert ("connection error")
    }
    if (cmd.state == 'good'){
        try{
        cmd1 = await sendRequest('OUT'+m+' ON');
            } catch (error) {
                alert('Connection error')
            }
        if (cmd1.state == 'good'){
            alert("Close")
        }
        else{
            alert('Try Again')
        }

    } else {
        alert("Try Again")
    }
})

$("#tl_on").click(async function(){
    m = 3;
    n = m+1;
    try {
    cmd = await sendRequest('OUT'+n+' OFF');
        } catch(error) {
            alert ("connection error")
        }
        if (cmd.state == 'good'){
            try{
            cmd1 = await sendRequest('OUT'+m+' ON');
                } catch (error) {
                    alert('Connection error')
                }
            if (cmd1.state == 'good'){
                alert("Green")
            }
            else{
                alert('Try Again')
            }

    } else {
        alert("Try Again")
    }
})

$("#tl_off").click(async function(){ 
    m=4;
    n=m-1;
    try {
    cmd = await sendRequest('OUT'+n+' OFF');
    } catch(error) {
        alert ("connection error")
    }
    if (cmd.state == 'good'){
        try{
        cmd1 = await sendRequest('OUT'+m+' ON');
            } catch (error) {
                alert('Connection error')
            }
        if (cmd1.state == 'good'){
            alert("Red")
        }
        else{
            alert('Try Again')
        }

    } else {
        alert("Try Again")
    }
})

$("#id_container").change(function(){
    if(this.value != '0'){
       $("#contr_on").css('display','initial')
    } else {
       $("#contr_on").css('display','none')
       $("#contr_on").prop('checked',false)
    }
 })
 $('#contr_on').change(function(){
    if ($(this).prop('checked') == true){
       this.value = 'true' ;
    } else {
       this.value = 'false';
    }
 })
