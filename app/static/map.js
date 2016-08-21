(function() {
    var nzLatLon = {lat: -40.9006, lng: 174.8860};
    var markers = [];

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: nzLatLon
    });

    var remove_markers = function () {
        for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(null);
        }
    }


    var get_markers = function (region) {
        remove_markers();
        $.getJSON('/region/' + region, function (data) {
            for (i = 0; i < data.length; i++) {

                var item = data[i];
                var mkr = new google.maps.Marker({
                    position: item.location,
                    map: map,
                    title: item.name
                });

                mkr.addListener('click', function (ev) {
                    map.setZoom(10);
                    map.setCenter(this.getPosition());
                });

                markers.push(mkr);
            }
        });
    }

    get_markers('Nelson');
})()