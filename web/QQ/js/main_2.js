//这用于实现具体的功能
//

//修改个人签名
function update_signed (text) {
    console.log (text);
}

//头像跳动
function icon_jump (elem,color) {
    var i = 0;
    function jump (elem,i) {
        var offset = (i % 2 ==0 ) ? -1 : 1;
        elem.style.top = elem.clientTop + offset;
    }
    function flash(elem,i) {
        var color  = (i % 2 ==0 ) ? 'white': '#E5E5E5';
        elem.style.background = color;
    }
    return setInterval (function () { 
        jump (elem, i); 
        if ( color==1 ) 
            flash (elem,i); 
        i++;
    }, 300); 
}

// panel 的操作，最大化，最小化，隐藏
function op_panel (elem, o_type) {
    var temp = elem.parentElement.parentElement.parentElement;
    var x_y = [['700px','600px'], ['360px','400px']];
    if (temp) {
        switch (o_type) {
            case 1:
                temp.style.display = "none";
                break;
            case 2:
                temp.style.width = x_y[0][0];
                temp.style.height = x_y[0][1];
                elem.onclick = function () {op_panel(elem, 4)} ;
                break;
            case 3:
                temp.style.display = "none";
                break;
            case 4:
                temp.style.width = x_y[1][0];
                temp.style.height = x_y[1][1];
                elem.onclick = function () { op_panel(elem, 2) };
        }
    }
}

/*
var aa = $('chat_panel_body').getElementsByTagName('li')[0];
var ia = icon_jump (aa, 0);
aa.onclick = function () {
    window.clearInterval (ia);
}

var bb = $('stat_panel_sum').getElementsByTagName('li')[0];
var ib = icon_jump (bb, 1);
bb.onclick = function () {
    window.clearInterval (ib);
}
*/



