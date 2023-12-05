var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}

/* This function is the alternate javascript function of loadDetails. and not using now */
function editFunction(lc_plate_1, lc_plate_2, lc_plate_3) {
  document.getElementById("id_license_plate1").value = lc_plate_1;
  document.getElementById("id_license_plate2").value = lc_plate_2;
  document.getElementById("id_license_plate3").value = lc_plate_3;
}

function loadUsersDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/users_details/" + id,
    success: function (result) {
      // document.getElementById("id_password1").disabled = true;
      document.getElementById("id").value = id;
      document.getElementById("id_name").value = result.name;
      document.getElementById("id_email").value = result.email;
      document.getElementById("id_password1").value = result.password;
      document.getElementById("id_yard").value = result.yard;
      document.getElementById("id_role").value = result.role;
    }
  })
}


function loadCustomerDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/customer_details/" + id,
    success: function (result) {
      document.getElementById("id").value = id;
      document.getElementById("id_firstname").value = result.firstname;
      document.getElementById("id_name").value = result.name;
      document.getElementById("id_description").value = result.description;
      document.getElementById("id_street").value = result.street;
      document.getElementById("id_pin").value = result.pin;
      document.getElementById("id_fax").value = result.fax;
      document.getElementById("id_place").value = result.place;
      document.getElementById("id_country").value = result.country;
      document.getElementById("id_website").value = result.website;
      document.getElementById("id_contact_person1_email").value = result.contact_person1_email;
      document.getElementById("id_contact_person2_email").value = result.contact_person2_email;
      document.getElementById("id_contact_person3_email").value = result.contact_person3_email;
      document.getElementById("id_contact_person1_phone").value = result.contact_person1_phone;
      document.getElementById("id_contact_person2_phone").value = result.contact_person2_phone;
      document.getElementById("id_contact_person3_phone").value = result.contact_person3_phone;
      document.getElementById("id_customer_type").value = result.customer_type;
      document.getElementById("id_classification").value = result.classification;
      document.getElementById("id_sector").value = result.sector;
      document.getElementById("id_company_size").value = result.company_size;
      document.getElementById("id_area").value = result.area;
      document.getElementById("id_warehouse").value = result.warehouse;
      document.getElementById("id_post_office_box").value = result.post_office_box;
      document.getElementById("id_salutation").value = result.salutation;
      document.getElementById("id_addition1").value = result.addition1;
      document.getElementById("id_addition2").value = result.addition2;
      document.getElementById("id_addition3").value = result.addition3;
      document.getElementById("id_diff_invoice_recipient").value = result.diff_invoice_recipient;
      document.getElementById("id_price_group").value = result.price_group;
      if (result.private_person==1){
      document.getElementById("id_private_person").checked = true;
      }
      else{
      document.getElementById("id_private_person").checked = false;
      }
      if (result.document_lock==1){
      document.getElementById("id_document_lock").checked = true;
      }
      else{
      document.getElementById("id_document_lock").checked = false;
      }
      if (result.payment_bock==1){
      document.getElementById("id_payment_bock").checked = true;
      }
      else{
      document.getElementById("id_payment_bock").checked = false;
      }
      document.getElementById("id_delivery_terms").value = result.delivery_terms;
      document.getElementById("id_special_discount").value = result.special_discount;
      document.getElementById("id_debitor_number").value = result.debitor_number;
      document.getElementById("id_dunning").value = result.dunning;
      document.getElementById("id_company").value = result.company;
      document.getElementById("id_perm_street").value = result.perm_street;
      document.getElementById("id_perm_pin").value = result.perm_pin;
      document.getElementById("id_perm_place").value = result.perm_place;
      document.getElementById("id_perm_country").value = result.perm_country;

      // $("#id_price_group").val(result.price_group).trigger('change');
    },
  })
}

function loadSupplierDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/supplier_detail/" + id,
    success: function (result) {
      document.getElementById("id").value = id;
      document.getElementById("id_supplier_name").value = result.supplier_name;
      document.getElementById("id_salutation").value = result.salutation;
      document.getElementById("id_first_name").value = result.first_name;
      document.getElementById("id_name").value = result.name;
      document.getElementById("id_street").value = result.street;
      document.getElementById("id_pin").value = result.pin;
      document.getElementById("id_fax").value = result.fax;
      document.getElementById("id_place").value = result.place;
      document.getElementById("id_country").value = result.country;
      document.getElementById("id_post_office_box").value = result.post_office_box;
      document.getElementById("id_contact_person1_email").value = result.contact_person1_email;
      document.getElementById("id_contact_person2_email").value = result.contact_person2_email;
      document.getElementById("id_contact_person3_email").value = result.contact_person3_email;
      document.getElementById("id_contact_person1_phone").value = result.contact_person1_phone;
      document.getElementById("id_contact_person2_phone").value = result.contact_person2_phone;
      document.getElementById("id_contact_person3_phone").value = result.contact_person3_phone;
      document.getElementById("id_website").value = result.website;
      document.getElementById("id_cost_centre").value = result.cost_centre;
      document.getElementById("id_warehouse").value = result.warehouse;
      document.getElementById("id_creditor_number").value = result.creditor_number;
      document.getElementById("id_addition1").value = result.addition1;
      document.getElementById("id_addition2").value = result.addition2;
      document.getElementById("id_addition3").value = result.addition3;
    }
  })
}


function loadForwardersDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/forwarders_detail/" + id,
    success: function (result) {
      document.getElementById("id").value = id;
      document.getElementById("id_name").value = result.name;
      document.getElementById("id_firstname").value = result.firstname;
      document.getElementById("id_second_name").value = result.second_name;
      document.getElementById("id_street").value = result.street;
      document.getElementById("id_pin").value = result.pin;
      document.getElementById("id_telephone").value = result.telephone;
      document.getElementById("id_place").value = result.place;
      document.getElementById("id_country").value = result.country;
    }
  })
}

function loadYardListDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/yard_list_detail/" + id,
    success: function (result) {
      document.getElementById("id").value = id;
      document.getElementById("id_name").value = result.name;
      document.getElementById("id_place").value = result.place;
      document.getElementById("id_country").value = result.country;
    }
  })
}

function loadArticleDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/article_detail/" + id,
    success: function (result) {
      document.getElementById("id").value = id;
      document.getElementById("id_name").value = result.name;
      document.getElementById("id_short_name").value = result.short_name;
      document.getElementById("id_description").value = result.description;
//      document.getElementById("id_entry_weight").value = result.entry_weight;
      // document.getElementById("id_balance_weight").value = result.balance_weight;
      // document.getElementById("id_outgoing_weight").value = result.outgoing_weight;
      document.getElementById("id_group").value = result.group;
      document.getElementById("id_vat").value = result.vat;
      document.getElementById("id_minimum_amount").value = result.minimum_amount;
      document.getElementById("id_price1").value = result.price1;
      document.getElementById("id_price2").value = result.price2;
      document.getElementById("id_price3").value = result.price3;
      document.getElementById("id_price4").value = result.price4;
      document.getElementById("id_price5").value = result.price5;
      document.getElementById("id_discount").value = result.discount;
      document.getElementById("id_avv_num").value = result.avv_num;
      document.getElementById("id_account").value = result.account;
      document.getElementById("id_cost_center").value = result.cost_center;
      document.getElementById("id_unit").value = result.unit;
      document.getElementById("id_min_quantity").value = result.min_quantity;
      document.getElementById("id_revenue_group").value = result.revenue_group;
      document.getElementById("id_revenue_account").value = result.revenue_account;
      document.getElementById("id_list_price_net").value = result.list_price_net;
      document.getElementById("id_ean").value = result.ean;
      document.getElementById("id_ware_house").value = result.ware_house;
      document.getElementById("id_supplier").value = result.supplier;
    }
  })
}

function loadBuildingSiteDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/building_site_detail/" + id,
    success: function (result) {
      document.getElementById("id").value = id;
      document.getElementById("id_name").value = result.name;
      document.getElementById("id_short_name").value = result.short_name;
      document.getElementById("id_place").value = result.place;
      document.getElementById("id_street").value = result.street;
      document.getElementById("id_pin").value = result.pin;
      document.getElementById("id_infotext").value = result.infotext;
    }
  })
}

function loadVehicleDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/vehicle_detail/" + id,
    success: function (result) {
      document.getElementById("id").value = id;
      document.getElementById("id_license_plate").value = result.license_plate;
      document.getElementById("id_license_plate2").value = result.license_plate2;
      document.getElementById("id_forwarder").value = result.forwarder;
      document.getElementById("id_group").value = result.group;
      document.getElementById("id_country").value = result.country;
      document.getElementById("id_telephone").value = result.telephone;
      document.getElementById("id_vehicle_weight").value = result.vehicle_weight;
      document.getElementById("id_vehicle_weight_id").value = result.vehicle_weight_id;
      document.getElementById("id_vehicle_type").value = result.vehicle_type;
      document.getElementById("id_cost_center").value = result.cost_center;
      document.getElementById("id_owner").value = result.owner;
      document.getElementById("id_driver_name").value = result.driver_name;
      document.getElementById("id_trailor_weight").value = result.trailor_weight;
    }
  })
}


// function autocompleteSearch(id_field, search_url, func_id) {
//   var search = $('#' + id_field).val()
//   var data = {
//     'search': search
//   };
//   $('#' + id_field).autocomplete({
//     source: function (request, response) {
//       $.ajax({
//         url: search_url,
//         type: "GET",
//         data: data,
//         success: function (data) {
//           response($.map(data.list, function (el) {
//             return {
//               label: el.label,
//               value: el.value
//             };
//           }));
//         }
//       });
//     },
//     select: function (event, ui) {
//       // Prevent value from being put in the input:
//       this.value = ui.item.label;
//       var id = ui.item.value;
//       if (func_id == "kunden") {
//         populateCustomerDetails(id);
//       } else if (func_id == "fahrzeuge") {
//         populateFahrzeugeDetails(id);
//       } else if (func_id == "lieferanten") {
//         populateSupplierDetails(id);
//       } else if (func_id == "artikel") {
//         populateArtikelDetails(id);
//       }
//       // Set the next input's value to the "value" of the item.
//       // $(this).next("input").val(ui.item.value);
//       event.preventDefault();
//     }
//   });
// }

function populateCustomerDetails(id) {
  $.ajax({
    type: "GET",
    url: "/customer_details/" + id,
    beforeSend: function (xhr) { 
      $('.kunden').addClass('loading')
      console.log('beforeSend');
    },
    success: function (result) {
      $("#customer_id").val(id);
      $("#customer_firstname").val(result.firstname);
      $("#customer_street").val(result.street);
      $("#customer_pin").val(result.pin);
      $("#customer_place").val(result.place);
      $("#customer_price_group").val(result.price_group);
      if (result.price_group==undefined){
        $("#customer_price_group").val('price1');
      }else{
      $("#customer_price_group").val(result.price_group);
      }
      $("#customer_price_group").trigger('change');

    },
    complete: function () {
      $('.kunden').removeClass('loading')
    },
  })
}

function populateVehicleDetails(id) {
  $.ajax({
    type: "GET",
    url: "/vehicle_detail/" + id,
    beforeSend: function (xhr) { 
      $('.fahrzeuge').addClass('loading')
      console.log('beforeSend');
    },
    success: function (result) {
      $("#vehicle_id").val(id);
      $("#vehicle_forwarder").val(result.forwarder);
      $("#license_plate2").val(result.license_plate2);
      $("#vehicle_weight").val(result.vehicle_weight);
      if(result.vehicle_weight == null)
      {
        $("#firstweight").val("0000");
      }
      else
      {
      var first_weight = $("#firstweight").val();
          if(first_weight =="0000")
          {
            $("#firstweight").val(result.vehicle_weight);
          }

      }

    },
    complete: function () {
      $('.fahrzeuge').removeClass('loading')
    },
  })
}

function populateSupplierDetails(id) {
  $.ajax({
    type: "GET",
    url: "/supplier_detail/" + id,
    beforeSend: function (xhr) { 
      $('.lieferanten').addClass('loading')
      console.log('beforeSend');
    },
    success: function (result) {
      $("#supplier_id").val(id);
//      $("#supplier_short_name").val(result.short_name);
      $("#supplier_street").val(result.street);
      $("#supplier_pin").val(result.pin);
      $("#supplier_firstname").val(result.first_name);
     $("#supplier_place").val(result.place);
    },
    complete: function () {
      $('.lieferanten').removeClass('loading')
    },
  })
}

function populateArticleDetails(id) {
  $.ajax({
    type: "GET",
    url: "/article_detail/" + id,
    beforeSend: function (xhr) { 
      $('.artikel').addClass('loading')
      console.log('beforeSend');
    },
    success: function (result) {
      var price_group = document.getElementById("customer_price_group").value
      $("#article_id").val(id);
      $("#article_short_name").val(result.short_name);
      if (result.group==undefined){
        $("#article_group").val(1);
      }else{
      $("#article_group").val(result.group);
      }
      if (price_group == "price5"){
        $("#article_price").val(result.price5);
      }
      else if(price_group == "price2"){
         $("#article_price").val(result.price2);
      }
      else if(price_group == "price3"){
         $("#article_price").val(result.price3);
      }
      else if(price_group == "price4"){
         $("#article_price").val(result.price4);
      }
      else{
         $("#article_price").val(result.price1);
      }
    },
    complete: function () {
      $('.artikel').removeClass('loading')
    },
  })
}

function populateCombinationDetails(id) {
var id_ident = $("#id_ident option:selected").text()
  $.ajax({
    type: "GET",
    url: "/combination/" + id,
    beforeSend: function (xhr) {
    $("#id_selected_combi").val(id_ident)
      $('.artikel').addClass('loading')
      $('.lieferanten').addClass('loading')
      $('.fahrzeuge').addClass('loading')
       $('.kunden').addClass('loading')
      console.log('beforeSend');
    },
    success: function (result) {
    $("#id_customer").val(result.customer).trigger('change');
    $("#id_vehicle").val(result.vehicle).trigger('change');
    $("#id_supplier").val(result.supplier).trigger('change');
    $("#id_article").val(result.article).trigger('change');
    },
    complete: function () {
      $('.artikel').removeClass('loading')
      $('.lieferanten').removeClass('loading')
      $('.fahrzeuge').removeClass('loading')
      $('.kunden').removeClass('loading')
    },
  })
}
  function daily_close(){
    var txt;
  var r = confirm("Enforce Day Conclusion?");
  if (r == true) {
      $.ajax({
          type: "GET",
          url: "/stats/daily_closing/",
          beforeSend: function (xhr) {

          },
          success: function (result) {
              alert(result.msg)
          },
          complete: function () {
          },
        })
  } 
  else {
    txt = "You pressed Cancel!";
  }
 }

 function loadContainerDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/container_details/" + id,
    success: function (result) {
      document.getElementById("id").value = id;
      document.getElementById("id_name").value = result.name;
      document.getElementById("id_container_type").value = result.container_type;
      document.getElementById("id_group").value = result.group;
      document.getElementById("id_container_weight").value = result.container_weight;
      document.getElementById("id_volume").value = result.volume;
      document.getElementById("id_last_site").value = result.last_site;

    },
  })
}

function loadWarehouseDetails(id) {
  window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
  $.ajax({
    type: "GET",
    url: "/warehouse_detail/" + id,
    success: function (result) {
      document.getElementById("id").value = id;
      document.getElementById("id_name").value = result.name;
      document.getElementById("id_stock_designation").value = result.stock_designation;
      document.getElementById("id_stock_number").value = result.stock_number;
      if (result.stock_item==1){
      document.getElementById("id_stock_item").checked = true;
      }
      else{
      document.getElementById("id_stock_item").checked = false;
      }
      if (result.locked_warehouse==1){
      document.getElementById("id_locked_warehouse").checked = true;
      }
      else{
      document.getElementById("id_locked_warehouse").checked = false;
      }
      if (result.ordered==1){
      document.getElementById("id_ordered").checked = true;
      }
      else{
      document.getElementById("id_ordered").checked = false;
      }
      document.getElementById("id_production").value = result.production;
      document.getElementById("id_reserved").value = result.reserved;
      document.getElementById("id_available").value = result.available;
      document.getElementById("id_total_stock").value = result.total_stock;
      document.getElementById("id_store").value = result.store;
      document.getElementById("id_outsource").value = result.outsource;

    }
  })
}


$("#id_customer,#customer_price_group").change(function(){
 var id = document.getElementById("id_article").value
 if(id!=0){
    var price_group = document.getElementById("customer_price_group").value
    $.ajax({
      type: "GET",
      url: "/article_detail/" + id,
      beforeSend: function (xhr) { 
      },
      success: function (result) {
          if (price_group == "price5"){
            $("#article_price").val(result.price5);
          }
          else if(price_group == "price2"){
             $("#article_price").val(result.price2);
          }
          else if(price_group == "price3"){
             $("#article_price").val(result.price3);
          }
          else if(price_group == "price4"){
             $("#article_price").val(result.price4);
          }
          else{
             $("#article_price").val(result.price1);
          }
            },
    })
 }
});

$("select").selectize();