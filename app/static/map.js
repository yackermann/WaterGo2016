(function() {
    var nzLatLon = {lat: -40.9006, lng: 174.8860};
    var markers = [];

    var select = $('.select2');
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: nzLatLon
    });

    var get_regions = function () {
        $.getJSON('/region', function (data) {
            for (i = 0; i < data.length; i++) {

                var region = data[i];

                var new_option = '<option value="' + region + '">' + region + '</option>';
                select.append(new_option);

            }
        });
    }


    var get_markers = function (region) {
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
    get_regions();
    get_markers('Nelson');
})()