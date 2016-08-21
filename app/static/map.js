function initMap() {
    var nzLatLon = {lat: -40.9006, lng: 174.8860};
    var markers = [];

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: nzLatLon
    });



    /*var marker = new google.maps.Marker({
        position: nzLatLon,
        map: map,
        title: "Hello"
    })*/


    $.getJSON('data.json', function (data) {
        for (i = 0; i < data.length; i++)
        {
            var item = data[i];
            var mkr = new google.maps.Marker({
                position: item.location,
                map: map,
                title: item.name
            });
            mkr.addListener('click', function (ev) {
                console.log(mkr)
                map.setZoom(10);
                map.setCenter(this.getPosition());
            });

            markers.push(mkr);
        }
    });
}