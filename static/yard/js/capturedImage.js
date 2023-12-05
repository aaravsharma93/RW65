$(document).ready(function () {
captureWebsocketStart();

var btn_capture2 = $('#btn_capture2');
var btn_capture3 = $('#btn_capture3');
var img_loading2 = $("#img_loading2");
var img_loading3 = $("#img_loading3");

img_loading2.hide();
img_loading3.hide();
btn_capture2.hide();
btn_capture3.hide();

btn_capture2.click(function(event){
// Capture Top View
btn_capture2.hide();
img_loading2.show();
web_socket.send('GET IMAGE');
web_socket.onmessage = function(event) {

    try {
    retval = JSON.parse(event.data);
    if (retval.msg_type == 'image')
    {
        console.log("Image",retval);
        img_loading2.attr("src", "data: image/jpeg;base64, " + retval.image_data);
        btn_capture3.show();

    }
    }
    catch(err) {
    alert("Error in fetching json")
    }
 }

event.preventDefault();
});

btn_capture3.click(function(event){
// Capture Rear View
btn_capture3.hide();
img_loading3.show();
web_socket.send('GET IMAGE');
web_socket.onmessage = function(event) {

    try {
    retval = JSON.parse(event.data);
    if (retval.msg_type == 'image')
    {
        console.log("Image",retval);
        img_loading3.attr("src", "data: image/jpeg;base64, " + retval.image_data);
    }
    }
    catch(err) {
    alert("Error in fetching json")
    }
 }

event.preventDefault();
});

});

web_socket = new WebSocket('ws://localhost:9001/');
function captureWebsocketStart() {

    var img_loading1 = $("#img_loading1");
    var img_captured1 = $("#img_captured1");
    var btn_capture2 = $('#btn_capture2');

    web_socket.onopen = function(event){
	     web_socket.send('GET IMAGE');
	     img_loading1.show();
    }
   web_socket.onmessage = function(event) {
   try {
    retval = JSON.parse(event.data);
    if (retval.msg_type == 'image')
    {
        console.log("Image",retval);
        img_loading1.attr("src", "data: image/jpeg;base64, " + retval.image_data);
        btn_capture2.show();

    }
    }
    catch(err) {
    alert("Error in fetching json")
    }
 }
 }

