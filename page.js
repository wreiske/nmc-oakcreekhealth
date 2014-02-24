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
            var jqxhr = $.ajax("https://dev.nomoreclipboard.com/mobile/check.php?qrcode=" + result.text)
                .done(function(data) {
                    if (data.pat_id != "") {
                        window.open('http://64.186.38.68:3010/ccda#' + data.pat_id, '_self', 'location=yes');
                    } else {
                        alert('Invalid promo code.');
                    }
                })
                .fail(function() {
                    alert("Promo code is invalid or network unavailable.");
                });
        },
        function(error) {
            alert("Scanning failed: " + error);
        }
    );
}
