function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue();
    var location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_prices";

    $.post(url, {
        area: parseFloat(sqft),
        bhk: bhk,
        region: location
    }, function(data, status) {
        console.log(data);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Rupees</h2>";
        console.log(status);
    });

    // Highlight location on the map
    highlightLocation(location);
}

function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var locations = data.region;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                uiLocations.append(opt);
            }
        }
    });

    // Initialize the map
    initializeMap();
}

function initializeMap() {
    var map = L.map('map', {
        zoomControl: false, // Remove zoom control buttons
        attributionControl: false // Remove attribution control
    }).setView([19.0760, 72.8777], 11); // Coordinates for Mumbai

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        noWrap: true, // Prevent map gridlines
        bounds: [[-90, -180], [90, 180]] // Map boundaries to remove gridlines
    }).addTo(map);

    window.map = map; // Store map in the global scope to access it later
}

function highlightLocation(location) {
    var locationsCoordinates = {
        "Andheri": [19.1197, 72.8468],
        "Bandra": [19.0544, 72.8402],
        "Borivali": [19.2288, 72.8543],
        // Add more locations with their coordinates
    };

    var coordinates = locationsCoordinates[location];
    if (coordinates) {
        window.map.setView(coordinates, 13); // Zoom into the selected location

        // Remove existing markers
        if (window.currentMarker) {
            window.map.removeLayer(window.currentMarker);
        }

        // Add a new marker
        window.currentMarker = L.marker(coordinates).addTo(window.map)
            .bindPopup(location)
            .openPopup();
    }
}

window.onload = onPageLoad;
