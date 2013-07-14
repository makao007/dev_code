#coding:utf-8
import urllib
import os

def down_file (url):
    filename = os.path.split(url)[1]
    urllib.urlretrieve(url,filename)
    print 'downloading... %s' % url

def down_files (urls):
    for url in urls:
        down_file(url)

def make_url(url_template,x,y):
    urls = []
    for i in x:
        for j in y:
            urls.append (url_template % (i,j))
    return urls

def down_sogou_map (x,y) :
    down_files (make_url ('http://p2.go2map.com/seamless1/0/174/716/7/1/%d_%d.png',x,y))

def save_file (filename,content):
    w = open(filename,'w')
    w.write(content)
    w.close()

def make_html (html_template, map_template,x, y,z,width,height):
    map_records = []
    for i,left in enumerate (x):
        for j,top in enumerate(y[::-1]):
            map_records.append (map_template % (width,height,width*i,height*j,width,height,left,top))
    html_content = html_template % (''.join(map_records))
    save_file ('map.html',html_content)

    

def make_map (x,y,z=0):
    html_template = '''

<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Simple Map</title>
    <style type="text/css" media="screen">
        #map{border:1px solid #333; width:800px; height:600px; overflow:hidden; position:relative; cursor:move;}
    </style>
</head>
<body>
    <h3>this is a simple Map</h3>
    <hr/>
    <div id="map">
    %s
    </div>

<script type="text/javascript">
/**
 * 
 * 
 * new Dragdrop({
 * 		target 	 拖拽元素 HTMLElemnt 必选
 * 		bridge	 指定鼠标按下哪个元素时开始拖拽，实现模态对话框时用到 
 * 		dragable 是否可拖拽	(true)默认
 * 		dragX 	 true/false false水平方向不可拖拽 (true)默认
 * 		dragY	 true/false false垂直方向不可拖拽 (true)默认
 * 		area 	 [minX,maxX,minY,maxY] 指定拖拽范围 默认任意拖动
 * 		callback 移动过程中的回调函数
 * });
 * source: http://www.nowamagic.net/librarys/veda/detail/1316 
 * demo
 * 		dragdrop_0.6.html
 */
Dragdrop = function(window){
	var doc = window.document;
	var E = {
		on : function(el, type, fn){
			el.addEventListener ?
				el.addEventListener(type, fn, false) :
			el.attachEvent ?
				el.attachEvent("on" + type, fn) :
			el['on'+type] = fn;
		},
		un : function(el,type,fn){
			el.removeEventListener ?
				el.removeEventListener(type, fn, false) :
			el.detachEvent ?
				el.detachEvent("on" + type, fn) :
			el['on'+type] = null;
		},
		evt : function(e){
			return e || window.event;
		}
	};
	return function(opt){
		
		var conf = null, defaultConf, diffX, diffY;
		function Config(opt){
			this.target = opt.target;
			this.bridge = opt.bridge;
			this.dragable = opt.dragable != false;
			this.dragX = opt.dragX != false;
			this.dragY = opt.dragY != false;
			this.area  = opt.area;
			this.callback = opt.callback;
		}	
		function Dragdrop(opt){
			if(!opt){return;}
			conf = new Config(opt);
			defaultConf = new Config(opt);
			conf.bridge ?
				E.on(conf.bridge,'mousedown',mousedown) :
				E.on(conf.target,'mousedown',mousedown);
		}
		Dragdrop.prototype = {
			dragX : function(){
				conf.dragX = true;
				conf.dragY = false;
			},
			dragY : function(b){
				conf.dragY = true;
				conf.dragX = false;
			},
			dragAll : function(){
				conf.dragX = true;
				conf.dragY = true;
			},
			setArea : function(a){
				conf.area = a;
			},
			setBridge : function(b){
				conf.bridge = b;
			},
			setDragable : function(b){
				conf.dragable = b;
			},
			reStore : function(){
				conf = new Config(defaultConf);
				conf.target.style.top = '0px';
				conf.target.style.left = '0px';
			},
			getDragX : function(){
				return conf.dragX;
			},
			getDragY : function(){
				return conf.dragY;
			}
		}
		function mousedown(e){
			e = E.evt(e);
			var el = conf.target;
			el.style.position = 'absolute';
			el.style.cursor = 'move';
			if(el.setCapture){ //IE
				E.on(el, "losecapture", mouseup);
				el.setCapture();
				e.cancelBubble = true;
			}else if(window.captureEvents){ //标准DOM
				e.stopPropagation();
				E.on(window, "blur", mouseup);
				e.preventDefault();
			}
			pre_position_x = e.clientX ;
			pre_position_y = e.clientY ;
			E.on(doc,'mousemove',mousemove);
			E.on(doc,'mouseup',mouseup);
		}
		function mousemove(e){
			var el = conf.target, e = E.evt(e), moveX = e.clientX - pre_position_x, moveY = e.clientY - pre_position_y;
			var minX, maxX, minY, maxY;
			if(conf.area){
				minX = conf.area[0];
				maxX = conf.area[1];
				minY = conf.area[2];
				maxY = conf.area[3];
				moveX < minX && (moveX = minX); // left 最小值
				moveX > maxX && (moveX = maxX); // left 最大值
				moveY < minY && (moveY = minY); // top 最小值
				moveY > maxY && (moveY = maxY); // top 最大值
			}
			if(conf.dragable){
				//conf.dragX && (el.style.left = moveX + 'px');
				//conf.dragY && (el.style.top =  moveY + 'px');
                var imgs = el.children;
                for (var i=0;i< el.children.length;i++) {
                    var t = el.children[i];
                    t.style.left= moveX+ t.offsetLeft + "px";
                    t.style.top = moveY+ t.offsetTop + "px";
                }

				if(conf.callback){
					var obj = {moveX:moveX,moveY:moveY};
					conf.callback.call(conf,obj);
				}
			}
		}
		function mouseup(e){
			var el = conf.target;
			el.style.cursor = 'default';
			E.un(doc,'mousemove',mousemove);
			E.un(doc,'mouseup',mouseup);
			if(el.releaseCapture){ //IE
				E.un(el, "losecapture", mouseup);
				el.releaseCapture();
			}
			if(window.releaseEvents){ //标准DOM
				E.un(window, "blur", mouseup);
			}
		}
		return new Dragdrop(opt);
		
	}
		
}(this);
var $ = function (name) { return document.getElementById(name) };
var drag = new Dragdrop({target:$('map')});
drag.dragAll();
</script>	
</body>
</html>

'''
    map_template = '''<img style="width: %dpx; height: %dpx; position: absolute; left: %dpx; top: %dpx; z-index: 0; border: 0px; visibility: visible;" width="%d" height="%d" name="MAPTILEIMAGE" src="%d_%d.png">'''
    width = 256
    height = 256
    make_html (html_template, map_template,x, y, z , width, height)


x = range(1580,1590)
y = range(330,340)
down_sogou_map(x,y)
make_map (x,y)


