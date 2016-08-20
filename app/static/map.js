function initMap() {
    var nzLatLon = {lat: -40.9006, lng: 174.8860};
    var markers = [];

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: nzLatLon
    });


    // marker.addListener('click', function() {
    //     map.setZoom(8);
    //     map.setCenter(marker.getPosition());
    // });

    /*var marker = new google.maps.Marker({
        position: nzLatLon,
        map: map,
        title: "Hello"
    })*/


    $.getJSON('data.json', function (json) {
        for (var key in json) {
            if (json.hasOwnProperty(key)) {
                var item = json[key];
                var mkr = new google.maps.Marker({
                    position: item.location,
                    map: map,
                    title: item.name
                });
                markers.push(mkr);
            }
        }
    });
}