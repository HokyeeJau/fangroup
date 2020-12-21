$(function(){
    // get all parameters translation
    var decode_name = {
        "vid_data": "日期",
        "vid_title": "标题",
        "vid_intro": "介绍",
        "vid_cap_trans": "字幕",
        "vid_dial_trans": "对白",
        "vid_axis_prd": "打轴",
        "vid_cover_prd": "精效",
        "vid_sup_prd": "压制"
    };
    $(".pop_main").hide();
    // $("#bg").hide();

    $("td").find('.detail-btn').bind('click', function(){
        // 准备数据
        var values = $(this).attr("value");
        var values_list = values.split("&");
        var details = {};
        for (var i = 0; i < values_list.length; i++){
            var single_pair = values_list[i].split("=");
            details[single_pair[0]] = single_pair[1];
            $("#"+single_pair[0]).text(single_pair[1]);
        }

        //显示弹窗的主界面
        // $("#bg").show();
        $('.pop_main').show();
        //设置animate动画初始值
        $('.pop_con').css({'top':0,'opacity':0});
        $('.pop_con').animate({'top':'50%','opacity':1})
    });

        //取消按钮和关闭按钮添加事件
    $('.cancel').click(function(){
        $('.pop_con').animate({'top':0,'opacity':0},function(){
            //隐藏弹窗的主界面
            $('.pop_main').hide()
        })
    });

    $("td").find(".disk-btn").bind('click', function(){
        var clipboard = new ClipboardJS(this);
        clipboard.on('success', function(e) {
            console.info('Action:', e.action);
            console.info('Text:', e.text);
            console.info('Trigger:', e.trigger);
            e.clearSelection();
        });
        clipboard.on('error', function(e) {
            console.error('Action:', e.action);
            console.error('Trigger:', e.trigger);
        });
    });
});
