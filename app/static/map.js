(function() {
    var nzLatLon = {lat: -40.9006, lng: 174.8860};
    var markers = [];

    var select = $('.select2');
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 5,
        center: nzLatLon
    });

    var remove_markers = function () {
        for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(null);
        }
    };
    
    var get_regions = function () {
        $.getJSON('/region', function (data) {
            for (i = 0; i < data.length; i++) {

                var region = data[i];
                var new_option = '<option value="' + region + '">' + region + '</option>';
                select.append(new_option);

            }
        });
    };

    var get_markers = function (region) {
        remove_markers();
        $.getJSON(/*'/region/' + region*/'data.json', function (data) {
            for (i = 0; i < data.length; i++) {

                var item = data[i];

                var icon = item.safe ? 'green' : 'red';

                var mkr = new google.maps.Marker({
                    position: item.location,
                    map: map,
                    title: item.name,
                    icon: 'http://maps.google.com/mapfiles/ms/icons/' + icon + '-dot.png'
                });
                markers.push(mkr);
                addListeners(mkr, item.safe, item.reasons)
            }
        });
    };

    function addListeners(marker, safe, reason) {
        var infoWindow = new google.maps.InfoWindow({
            content: safe ? 'This place is safe to swim!' : 'This place is not safe to swim because ' + reason
        });
        var map = marker.get('map');
        marker.addListener('click', function () {
            infoWindow.open(map, marker);
            map.setZoom(15);
            map.setCenter(marker.getPosition());
        })
    }

    select.change(function(){
        $('option:selected', select).each(function() {
            var region = $(this).attr('value');
            get_markers(region);
        });
    });
    get_regions();
    get_markers('Nelson');
})();