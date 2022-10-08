$(document).ready (function () {
    $("#reset").click(function () {
        document.getElementById("meaning").innerHTML = '';
    });
});


function playTrack () {
        var myAudio = document.getElementById("myTune");
        myAudio.play();
        $("#play").hide();
        $("#pause").show();
        }
function pauseTrack () {
        var myAudio = document.getElementById("myTune");
        myAudio.pause();
        $("#play").show();
        $("#pause").hide();
        }
$(document).ready (function () {
    $("#play").bind ("click", playTrack);
    $("#pause").bind ("click", pauseTrack);
});