var global_max_zindex = 10;

function all_panel () {
    var temp = document.body.children;
    for (var i=0; i< temp.length; i++) {
        var elem = temp[i];
        if ( (elem.nodeType==1) && (elem.nodeName.toLowerCase()=="div") && 
                (elem.className.toLowerCase()=="panel") )
            elem.onclick = function () { this.style.zIndex = global_max_zindex ++; } ;
        var first_child = elem.children[0];
        if ( first_child && first_child.className.toLowerCase() =='panel_title' )
            move (first_child, elem);
    }
}

all_panel();
