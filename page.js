$(document).ready(function() {
    $('.demo').click(function(e) {
        e.preventDefault();
        alert('Function disabled in demo.');
    });

    window.addEventListener("orientationchange", updateOrientation);
});


function updateOrientation(e) {
    switch (e.orientation) {
        case 0:
            // Do your thing
            break;

        case -90:
            // Do your thing
            break;

        case 90:
            // Do your thing
            break;

        default:
            break;
    }
}


function scan() {
    cordova.plugins.barcodeScanner.scan(
        function(result) {
            /* 
            alert("We got a barcode\n" +
                "Result: " + result.text + "\n" +
                "Format: " + result.format + "\n" +
                "Cancelled: " + result.cancelled);
			*/

            window.open('http://64.186.38.68:3010/ccda', '_self', 'location=yes');
        },
        function(error) {
            alert("Scanning failed: " + error);
        }
    );
}
