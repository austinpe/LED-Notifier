// ==UserScript==
// @author          Paulo Da Silva
// @name            Song Status Updater
// @version         1.0
// @description     Periodically Update Song status
// @namespace       GroovesharkRemote
// @include         http://grooveshark.com/#/*
// ==/UserScript==

var GroovesharkRemote = function() {

	GroovesharkRemote = {};

	GroovesharkRemote.init = function() {
        setInterval("GroovesharkRemote.updateInfo()", 2000);
	};

    GroovesharkRemote.updateInfo = function() {			
        var currentSong = Grooveshark.getCurrentSongStatus();
        request = new XMLHttpRequest();
        request.open("POST","http://localhost:2020/updateInfo",true);
        request.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        request.send(JSON.stringify(currentSong));	
		console.log('hi')
	};
	
	GroovesharkRemote.init();
};

addFunction = function(func, exec) {
	var script = document.createElement("script");
	script.textContent = (exec ? "(" : "") + func.toString() + (exec ? ")();" : "");
	document.body.appendChild(script);
}

addFunction(GroovesharkRemote, true);
