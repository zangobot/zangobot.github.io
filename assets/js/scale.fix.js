(function(document) {
    var metas = document.getElementsByTagName('meta'),
        changeViewportContent = function(content) {
            for (var i = 0; i < metas.length; i++) {
                if (metas[i].name == "viewport") {
                    metas[i].content = content;
                }
            }
        },
        initialize = function() {
            changeViewportContent("width=device-width, minimum-scale=1.0, maximum-scale=1.0");
        },
        gestureStart = function() {
            changeViewportContent("width=device-width, minimum-scale=0.25, maximum-scale=1.6");
        },
        gestureEnd = function() {
            initialize();
        };



    if (/Mobi|Android|iPhone/i.test(navigator.userAgent)) {
        initialize();

        document.addEventListener("touchstart", gestureStart, false);
        document.addEventListener("touchend", gestureEnd, false);

        // --- start: reduce logo size on mobile ---
        var headerImg = document.querySelector('header img');
        if (headerImg) {
            headerImg.style.maxWidth = '50%';
        }
        // --- end: reduce logo size on mobile ---
    }
})(document);
