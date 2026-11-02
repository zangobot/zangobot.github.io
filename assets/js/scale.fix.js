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



    if (/Mobi|Android/i.test(navigator.userAgent)) {
        initialize();

        document.addEventListener("touchstart", gestureStart, false);
        document.addEventListener("touchend", gestureEnd, false);

        // --- start: shrink logo on scroll (mobile) ---
        var headerImg = document.querySelector('header img');
        if (headerImg) {
            headerImg.style.transition = 'transform 0.2s ease-out';
            window.addEventListener('scroll', function() {
                var y = window.scrollY;
                // Scale down to minimum 0.5 when scrolled 300px
                var scale = Math.max(0.5, 1 - y / 300);
                headerImg.style.transform = 'scale(' + scale + ')';
            });
        }
        // --- end: shrink logo on scroll (mobile) ---
    }
})(document);
