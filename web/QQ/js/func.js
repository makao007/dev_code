//登录，发送用户名和密码去认证
function to_login () {
    var inputs = $('login_panel_body').getElementsByTagName('input');
    var username = inputs[0].value.trim();
    var password = inputs[1].value.trim();
}

function to_login_after() {
}

function to_register () {
    var inputs = $('register_panel_body');


//根据id，返回该元素
function to_element (elem) {
    return (typeof elem == 'string') ? $(elem) : elem;
}

//使用某个元素在中间位置
function to_middle (elem) {
    elem = to_element(elem);
    if (elem){
        elem.style.left = ( parseInt(document.body.clientWidth) - parseInt(elem.clientWidth) ) / 2;
        elem.style.top  = ( parseInt(document.body.clientHeight)- parseInt(elem.clientHeight)) / 2;
    }
}


//显示某个元素
function show_it (elem) {
    elem = to_element(elem);
    elem.style.zIndex  = ++ global_max_zindex ;
    elem.style.display = "block";
}

// 显示注册面板
function show_register() {
    show_it ('register_panel');
    to_middle ('register_panel');
}

// 显示找回密码面板
function show_forgot_password () {
    show_it ('find_password');
    to_middle ('find_password');
}
