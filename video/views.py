from django.shortcuts import render
from django.http import HttpResponse
from video import models
# Create your views here.

row_temp = "<tr> \
    <td>{id}</td> \
    <td>{date}</td> \
    <td>{title}</td> \
    <td>{intro}</td> \
    <td>{link}</td> \
    <td>{url}</td> \
    <td><a class=\"waves-effect deep-orange lighten-1 btn detail-btn\" href=\"#\" value=\"{value}\">查看详情</td>\
</tr>"

disk_share_temp = "链接：{link} 提取码：{code} 复制这段内容后打开百度网盘手机App，操作更方便哦--来自百度网盘超级会员V2的分享"

def video(request):
    context = {}
    context['ip'] = get_ip(request)
    context['rows'] = get_video_list()
    return render(request, 'video.html', context)

def get_record_row(r):
    disk_link = "暂无" if r.vid_baidu_url is None else "<a class=\"waves-effect blue-grey darken-3 btn disk-btn\" data-clipboard-text=\"" \
                            +disk_share_temp.format(link=r.vid_baidu_url,code=r.vid_code) \
                            +"\" data-clipboard-action=\"copy\">复制分享链接</a>"

    bili_link = "暂无" if r.vid_bili_url is None else "<a class=\"waves-effect blue-grey darken-3 btn bili-btn\" href=\"{}\" \
                            target=\"view_window\">b站观看</a>".format(r.vid_bili_url)

    values = "vid_date=%s&vid_title=%s&vid_intro=%s&vid_cap_trans=%s \
                &vid_dial_trans=%s&vid_axis_prd=%s&vid_cover_prd=%s&vid_sup_prd=%s" % \
                (r.vid_date, r.vid_title, r.vid_intro, r.vid_cap_trans, \
                    r.vid_dial_trans, r.vid_axis_prd, r.vid_cover_prd, r.vid_sup_prd)

    return row_temp.format(id = r.id,
                           date = r.vid_date,
                           title = r.vid_title,
                           intro = r.vid_intro,
                           link = disk_link,
                           url = bili_link,
                           value = values)

def get_video_list():
    records = query_all()
    rows = []
    for i in records:
        rows.append(get_record_row(i))
    return rows

def query_all():
    record_list = models.video.objects.order_by('-vid_date').all()
    return record_list

def get_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for#.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
