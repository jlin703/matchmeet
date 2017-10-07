const berkeleyLat = 37.8719;
const berkeleyLong = -122.2585;

function createMap(pos) {
    console.log(pos);
    var map = null;
    var initLat;
    var initLong;
    if (pos) {
        initLat = pos.coords.latitude;
        initLong = pos.coords.longitude;
    } else {
        initLat = berkeleyLat;
        initLong = berkeleyLong;
    }

    console.log(initLat);
    map = L.Wrld.map("map", "230f0e3aff3e146b4a87f3ebf4fcb306", {
        center: [initLat, initLong],
        zoom: 16
    });
    var latlng = L.latLng(berkeleyLat, berkeleyLong);
    map.precache(latlng, 50);

    // obtain events from ruby in JSON
    var result = '[{"lat":37.8719, "long":-122.2585}, {"lat":37.8750, "long":-122.2600}]';
    eventLst = JSON.parse(result);
    for (var i = 0; i < eventLst.length; i++) {
        var e = eventLst[i];
        console.log(e);
        var lat = e.lat;
        var long = e.long;
        var marker = L.marker([lat, long], {
            title: "Transamerica Pyramid",
            opacity: 0.8
        }).bindTooltip("Event name", {
            permanent: true,
            direction: 'top',
            offset: L.point(0, -50),
            classname: "event_marker"
        }).bindPopup("This is the Transamerica Pyramid")//.openPopup()
        .on('mouseover', function (e) {
            this.openPopup();
        })
        .on('mouseout', function (e) {
            this.closePopup();
        })
        .addTo(map);
    }
}

var main = function() {
    // if (navigator.geolocation) {
    //     console.log("ask geolocation permis");
    //     navigator.geolocation.getCurrentPosition(createMap, createMap);
    // } else {
    //     createMap(null);
    // }
    createMap(null);
};


main();