let my_map = L.map("us3");
const drawnItems = L.featureGroup();
var drawControlEditOnly = new L.Control.Draw({
  edit: {
    featureGroup: drawnItems,
  },
  draw: false,
});

var drawControlFull = new L.Control.Draw({
  edit: {
    featureGroup: drawnItems,
  },
  draw: {
    polyline: false,
    circle: false,
    marker: false,
    rectangle: true,
  },
});

let showMap = (position) => {
  if (position) {
    my_map.setView([position.coords.latitude, position.coords.longitude], 13);
    const marker = L.marker(
      [position.coords.latitude, position.coords.longitude],
      10
    ).addTo(my_map);
    var popup = marker.bindPopup("<b>Your Current Location</b>");
  } else {
    my_map.setView([36.97912, -121.89939], 1);
  }

  var osm = L.tileLayer("http://tile.openstreetmap.org/{z}/{x}/{y}.png"),
    googleSat = L.tileLayer(
      "http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
      {
        maxZoom: 20,
        subdomains: ["mt0", "mt1", "mt2", "mt3"],
      }
    );
  var baseMaps = {
    OpenStreetMap: osm,
    MapQuestImagery: googleSat,
  };
  osm.addTo(my_map);

  drawnItems.addTo(my_map);
  L.control
    .layers(
      baseMaps,
      { drawlayer: drawnItems },
      { position: "topright", collapsed: false }
    )
    .addTo(my_map);

  if ($("#long_lat").attr("value") !== "") {
    my_map.addControl(drawControlFull);
  } else {
    my_map.addControl(drawControlFull);
  }
  var searchControl = new L.esri.Controls.Geosearch().addTo(my_map);
  my_map.on("draw:created", function (e) {
    var area_layer = e.layer;
    area_layer.addTo(drawnItems);
    drawControlFull.remove(my_map);
    drawControlEditOnly.addTo(my_map);
    // polygons.addLayer(area_layer);
    console.log(area_layer);
    $("#long_lat").attr("value", JSON.stringify(area_layer._latlngs[0]));
    var seeArea = L.GeometryUtil.geodesicArea(area_layer.getLatLngs()[0]);
    $("#id_area").attr("value", (seeArea / 10000).toFixed(4));
    console.log(seeArea);
  });

  my_map.on("draw:deleted", function (e) {
    drawnItems.clearLayers();
    drawControlEditOnly.remove(my_map);
    drawControlFull.addTo(my_map);

    $("#long_lat").attr("value", "");
  });
};

let drawShape = (js_obj) => {
  var latlngs = [];
  js_obj.forEach((val) => {
    latlngs = [...latlngs, [val["lat"], val["lng"]]];
  });
  var polygon = L.polygon(latlngs);
  polygon.addTo(drawnItems);
};

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showMap, show_map);
  }
}

function show_map() {
  showMap();
}
