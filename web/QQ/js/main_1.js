// 这里用于定义通用的函数
// 这里的函数 调用的次数较多

var $ = function (name) { return document.getElementById(name) };
var c = function (name) { return document.createElement(name)  };

function hide_panel(elem) {
    elem.parentElement.parentElement.style.display = "none";
}

// IE6 不支持数组的 indexOf 方法
if(!Array.prototype.indexOf){
    Array.prototype.indexOf = function(val){
       var value = this;
       for(var i =0; i < value.length; i++)
          if(value[i] == val) return i;
       return -1;
    };
}


//新建一个xmlhttprequest,为Ajax作准备
function xhr (){
    var xmlhttp;
    if (window.XMLHttpRequest) // code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    else // code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    return xmlhttp;
}

//ajax 用get的方法发送消息
function xhr_get(call_back, url){
    xmlhttp = xhr();
    xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
            call_back(xmlhttp.responseText);
    }
    url = encodeURI(url);
    url = encodeURI(url);
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
}

// 获取鼠标的坐标
var getMouseP=function (e){
	e = e || window.event;
	return (e.pageX || e.pageY)?{ x:e.pageX, y:e.pageY } : { x:e.clientX + document.body.scrollLeft - document.body.clientLeft, y:e.clientY + document.body.scrollTop  - document.body.clientTop };
};
    
move=function(o,t){
    o = (typeof o == 'string') ? $(o) : o;
    t = (typeof t == 'string') ? $(t) : t;
	o.onmousedown=function(ev){
		var mxy=getMouseP(ev);
		var by={x:mxy.x-(t.offsetLeft),y:mxy.y-(t.offsetTop)};
		o.style.cursor="move";
		document.onmousemove=function(ev){
			var mxy=getMouseP(ev);
			t.style.left=mxy.x-by.x+"px";
			t.style.top=mxy.y-by.y+"px";
		};
		document.onmouseup=function(){
			window.getSelection ? window.getSelection().removeAllRanges() : document.selection.empty();
			this.onmousemove=null;
		}
	}
}
