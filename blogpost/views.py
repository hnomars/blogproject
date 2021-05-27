from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView, UpdateView, TemplateView, FormView
from .models import BlogModel, SRMModel, SRMOptionModel, WordModel, StPointModel ,StPointNameModel
from .forms import SRMForm
import os
import openpyxl
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.views import generic
import csv
import urllib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

import matplotlib
#バックエンドを指定
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse

# 以下追加モジュール

class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = {'title','content','category'}
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = {'title','content','category'}
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class AllList(ListView):
    template_name = 'alllist.html'
    model = BlogModel

class AllUpdate(UpdateView):
    template_name = 'allupdate.html'
    model = BlogModel
    fields = {'title','content','category'}
    success_url = reverse_lazy('alllist')

class SRMList(ListView):
    template_name = 'SRM/SRMlist.html'
    model = SRMModel
    
    paginate_by = 5
    
    def get_queryset(self):
        SRM = SRMModel.objects.order_by('-SRM_date')
        return SRM

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['players'] = '勇者', '戦士', '魔法使い', '忍者'
        context['message'] = 'Welcome my BBS'
        context['categolys'] = list(BlogModel.objects.all().values_list('title', flat=True))#.order_by("id")
        context['SRMoptions'] = list(SRMOptionModel.objects.all())
        context['SRMname'] = 'SRMoptions.0.SRM_name1','SRMoptions.0.SRM_name2','SRMoptions.0.SRM_name3','SRMoptions.0.SRM_name4','SRMoptions.0.SRM_name5','SRMoptions.0.SRM_name6','SRMoptions.0.SRM_name7','SRMoptions.0.SRM_name8','SRMoptions.0.SRM_name9','SRMoptions.0.SRM_name10'
        return context

class SRMDetail(DetailView):
    template_name = 'SRM/SRMdetail.html'
    model = SRMModel
    SRMfields = {"BlogModel":'title'}

class SRMUpdate(UpdateView):
    template_name = 'SRM/SRMupdate.html'
    model = SRMModel
    fields = "__all__"

    success_url = reverse_lazy('Top')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['SRMOptionlist'] = SRMOptionModel.objects.all()
        
        return context

class SRMCreate(CreateView):
    template_name = 'SRM/SRMcreate.html'
    model = SRMModel
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['SRMOptionlist'] = SRMOptionModel.objects.all()        
        return context
    success_url = reverse_lazy('Top')

class SRM_opupdate(UpdateView):
    template_name = 'options/SRM_opupdate.html'
    model = SRMOptionModel
    fields = "__all__"
    success_url = reverse_lazy('Options')


class SRM_OpList(ListView):
    template_name = 'options/SRM_oplist.html'
    model = SRMOptionModel

posted_data = {"text": "",
               "select_part": []}

class Top(TemplateView):
    template_name = 'top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['players'] = '勇者', '戦士', '魔法使い', '忍者'
        date_format = "%Y-%m-%d"
        today = timezone.datetime.today()
        context['todaydate'] = today
        context['todaystr'] = today.strftime(date_format)
        context['message'] = 'Welcome my BBS'
        context['categolys'] = list(BlogModel.objects.all().values_list('title', flat=True))#.order_by("id")
        context['SRMoptions'] = list(SRMOptionModel.objects.all())
        context['srmtest'] = list(SRMModel.objects.all())
        srmmodellist = list(SRMModel.objects.all())        
        context['SRMmodels'] = [str(i) for i in srmmodellist]
        context['SRMname'] = 'SRMoptions.0.SRM_name1','SRMoptions.0.SRM_name2','SRMoptions.0.SRM_name3','SRMoptions.0.SRM_name4','SRMoptions.0.SRM_name5','SRMoptions.0.SRM_name6','SRMoptions.0.SRM_name7','SRMoptions.0.SRM_name8','SRMoptions.0.SRM_name9','SRMoptions.0.SRM_name10'
        context['word'] = list(WordModel.objects.all().values_list('word', flat=True))
        
        stmodellist = list(SRMModel.objects.all())
        context['St_models'] = [str(i) for i in stmodellist]

        return context

def signupview(request):
    if request.method == "POST":
        username_data = request.POST['username_data']
        password_data = request.POST["password_data"]
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html',{'error':'このユーザーは既に登録されています'})
    else:
        return render(request, "signup.html",{})            
    return render(request, "signup.html",{})

def loginview(request):
    if request.method == "POST":
        username_data = request.POST['username_data']
        password_data = request.POST["password_data"]
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect("Top")
        else:
            return redirect("login")
    return render(request, "login.html")

def logoutview(request):
    logout(request)
    return redirect("login")

class St_List(ListView):
    template_name = 'stpoint/st_list.html'
    model = StPointModel
    paginate_by = 7

    def get_queryset(self):
        StPoint = StPointModel.objects.order_by('-point_date')
        return StPoint

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['stcategolys'] = list(StPointModel.objects.all())
        context['stNames'] = list(StPointNameModel.objects.all())
        return context
    
class St_Create(CreateView):
    template_name = 'stpoint/st_create.html'
    model = StPointModel
    fields = "__all__"
    success_url = reverse_lazy('St_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['stcategolys'] = list(StPointModel.objects.all())
        context['stNames'] = list(StPointNameModel.objects.all())
        return context    

class St_Update(UpdateView):
    template_name = 'stpoint/st_update.html'
    model = StPointModel
    fields = "__all__"

    success_url = reverse_lazy('Top')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['stcategolys'] = list(StPointModel.objects.all())
        context['stNames'] = list(StPointNameModel.objects.all())
        return context  

class Options(TemplateView):
    template_name = 'options/op_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        
        return context  
    
class St_Oplist(ListView):
    template_name = 'options/st_oplist.html'
    model = StPointNameModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['stcategolys'] = list(StPointModel.objects.all())
        context['stNames'] = list(StPointNameModel.objects.all())
        return context

class St_Opupdate(UpdateView):
    template_name = 'options/st_opupdate.html'
    model = StPointNameModel
    fields = "__all__"
    success_url = reverse_lazy('St_oplist')

class St_Opcreate(CreateView):
    template_name = 'options/st_opcreate.html'
    model = StPointNameModel
    fields = "__all__"
    success_url = reverse_lazy('St_oplist')

class Word_List(ListView):
    template_name = 'options/word_list.html'
    model = WordModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['stcategolys'] = list(StPointModel.objects.all())
        context['stNames'] = list(StPointNameModel.objects.all())
        return context

class Word_Create(CreateView):
    template_name = 'options/word_create.html'
    model = WordModel
    fields = "__all__"
    success_url = reverse_lazy('Word_list')

class Word_Update(UpdateView):
    template_name = 'options/word_update.html'
    model = WordModel
    fields = "__all__"

    success_url = reverse_lazy('Word_list')

""" def alllist(request):
    data = BlogModel.objects.all()
    params = {'message': 'メンバーの一覧', 'data': data}
    return render(request, 'alllist.html', params)
 """
class Excel(ListView):
    template_name = 'excel.html'
    model = BlogModel
    success_url = reverse_lazy('excel')

    def ExcelExport(self, response):
        template_name = 'delete.html'
        model = BlogModel
        """
        Excel output from template
        """
        # Excelのテンプレートファイルの読み込み
        wb = openpyxl.load_workbook('C:/Users/hnoma/OneDrive/ドキュメント/djangotest.xlsx')

        sheet = wb['Sheet1']
        sheet['C2'] = 'XXX'
        sheet['E2'] = 'new'

        # Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s' % 'report.xlsx'

        # データの書き込みを行なったExcelファイルを保存する
        wb.save(response)

        # 生成したHttpResponseをreturnする
        return response

class Index(generic.ListView):
    """
    役職テーブルの一覧表作成
    """
    model = SRMModel
    template_name = 'csvdownload/list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_name'] = 'csvdownload'
        return ctx

def csvExport(request):
    """
    役職テーブルを全件検索して、CSVファイルを作成してresponseに出力します。
    """
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    filename = urllib.parse.quote((u'ueforiapp.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)
    
    SRM_head = [i for i in SRMOptionModel.objects.all()]
    writer.writerow(
        SRM_head.SRM_name1, SRM_head.SRM_name2,SRM_head.SRM_name3,SRM_head.SRM_name4,SRM_head.SRM_name5,
        SRM_head.SRM_name6,SRM_head.SRM_name7,SRM_head.SRM_name8,SRM_head.SRM_name9,SRM_head.SRM_name10,
        "気分", "出来事")
    # for post in SRMModel.objects.all():
    #     writer.writerow([post.pk, post.name])
    return response

#グラフ作成

class SRMglaph(TemplateView):
    template_name = 'SRM/SRMcreate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context['stcategolys'] = list(StPointModel.objects.all())
        context['stNames'] = list(StPointNameModel.objects.all())
        return context

def setPlt():
    x_dt = SRMModel.objects.all().values_list('SRM_date').order_by('-SRM_date')[:14]

    print("test")
    print(x_dt)
    x =[]
    for i in range(len(x_dt)):
        x.append(x_dt[i][0].strftime('%m/%d'))
    
    y_val = SRMModel.objects.all().values_list('action_value1',"action_value2","action_value3","action_value4","action_value5","action_value6","action_value7","action_value8","action_value9","action_value10").order_by('-SRM_date')[:14]
    y = [i for i in y_val]

    print(y)
    y_sum =[]
    for i in range(len(y)):
        y_sum.append(sum([0 if j is None else j for j in y[i]])) 
    print(y_sum)

    plt.bar(x, y_sum, color='#00d5ff')
    plt.title(r"$\bf{activelevel 14days nearly}$", color='#3407ba')
    plt.xlabel("date")
    plt.ylabel("activelevel")

# SVG化
def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数
def get_svg(request):
    setPlt()  
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response