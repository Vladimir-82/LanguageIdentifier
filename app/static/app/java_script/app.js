$(document).ready (function () {
    $("#reset").click(function () {
        document.getElementById("meaning").innerHTML = '';
    });
});
$(document).ready (function () {
    $("#play").click(function () {
    var myAudio = document.getElementById("myTune");
        if (myAudio.paused) {
        myAudio.play();
        } else {
            myAudio.pause();
                }
    });
});