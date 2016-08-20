function initMap() {
    var nzLatLon = {lat: -40.9006, lng: 174.8860};
    var markers = [];

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: nzLatLon
    });

    var marker = new google.maps.Marker({
        position: nzLatLon,
        map: map,
        title: 'Hello World!'
    });


    marker.addListener('click', function() {
        map.setZoom(8);
        map.setCenter(marker.getPosition());
    });


    $.getJSON('data.json', function (json) {
        for (var key in json) {
            if (json.hasOwnProperty(key)) {
                var item = json[key];
                markers.push({
                    name: item.name,
                    safe: item.safe,
                    reason: item.reason,
                    location: item.location
                });
            }
        }
    });


}