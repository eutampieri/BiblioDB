function getUrl(url){
	var webrequest = new XMLHttpRequest();
	webrequest.open('GET', url, false);
	webrequest.send(null);
	return webrequest.responseText;
}
function getMobileOS() {
  var userAgent = navigator.userAgent || navigator.vendor || window.opera;

  if( userAgent.match( /iPad/i ) || userAgent.match( /iPhone/i ) || userAgent.match( /iPod/i ) || ("standalone" in window.navigator) &&!window.navigator.standalone )
  {
	return 'iOS';

  }
  else if( userAgent.match( /Android/i ) )
  {

	return 'Android';
  }
  else
  {
	return 'unknown';
  }
}
function getOS(){
	if(getMobileOS()=="unknown"){
		 if(navigator.userAgent.indexOf("Chrome") != -1 ) 
		{
			return 'Chrome-'+navigator.platform.replace(/\s+/g, '');
		}
		else if(navigator.userAgent.indexOf("Opera") != -1 )
		{
		 return 'Opera-'+navigator.platform.replace(/\s+/g, '');
		}
		else if(navigator.userAgent.toLowerCase().indexOf("opr") != -1 )
		{
		 return 'Opera-'+navigator.platform.replace(/\s+/g, '');
		}
		else if(navigator.userAgent.toLowerCase().indexOf("trident") != -1 )
		{
		 return 'IE-'+navigator.platform.replace(/\s+/g, '');
		}
		else if(navigator.userAgent.indexOf("Firefox") != -1 ) 
		{
			 return 'Firefox-'+navigator.platform.replace(/\s+/g, '');
		}
		else if((navigator.userAgent.indexOf("MSIE") != -1 ) || (!!document.documentMode == true )) //IF IE > 10
		{
		  return 'IE-'+navigator.platform.replace(/\s+/g, '');
		}  
		else 
		{
		   return 'unknown-on-'+navigator.platform.replace(/\s+/g, '');
		}
	}
	else{
		return getMobileOS()
	}
}
function generateUUID() {
	var d = new Date().getTime();
	var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
		var r = (d + Math.random()*16)%16 | 0;
		d = Math.floor(d/16);
		return (c=='x' ? r : (r&0x3|0x8)).toString(16);
	});
	return uuid;
}
function setCookie(cname, cvalue, exdays) {
	var d = new Date();
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	var expires = "expires="+d.toUTCString();
	if (exdays==-1){
		document.cookie = cname + "=" + cvalue;+"; expires=Fri, 31 Dec 2038 23:59:59 GMT;"
	}
	else{
		document.cookie = cname + "=" + cvalue + "; " + expires;
	}
}

function getCookie(cname) {
	var name = cname + "=";
	var ca = document.cookie.split(';');
	for(var i=0; i<ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1);
		if (c.indexOf(name) == 0) return c.substring(name.length, c.length).replace("=","");
	}
	return "";
}

function checkCookie(name) {
	var user = getCookie(name);
	if (user != "") {
		return true;
	}
	else {
		return false;
	}
}