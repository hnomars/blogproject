from django import template
from blogpost.models import SRMModel, SRMOptionModel
register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムtタグとして登録する

@register.simple_tag
def SRM_check():
    n = len(SRMModel.objects.all())
    if n >= 14:
        n = 14
    check = []
    ops = SRMOptionModel.objects.all()[0]
    print(ops.SRM_name7)
    for i in SRMModel.objects.all().filter(action_value1=None)[:n]:
        check.append(str(i.SRM_date)[5:])
    for i in SRMModel.objects.all().filter(action_value2=None)[:n]:
        check.append(str(i.SRM_date)[5:])
    if ops.SRM_name3  != "":
        for i in SRMModel.objects.all().filter(action_value3=None)[:n]:
            check.append(str(i.SRM_date)[5:])
    if ops.SRM_name4  != "":
        for i in SRMModel.objects.all().filter(action_value4=None)[:n]:
            check.append(str(i.SRM_date)[5:])
    if ops.SRM_name5  != "":
        for i in SRMModel.objects.all().filter(action_value5=None)[:n]:
            check.append(str(i.SRM_date)[5:])
    if ops.SRM_name6  != "":
        for i in SRMModel.objects.all().filter(action_value6=None)[:n]:
            check.append(str(i.SRM_date)[5:])
    if ops.SRM_name7  != "":
        for i in SRMModel.objects.all().filter(action_value7=None)[:n]:
            check.append(str(i.SRM_date)[5:])
    if ops.SRM_name8  != "":
        for i in SRMModel.objects.all().filter(action_value8=None)[:n]:
            check.append(str(i.SRM_date)[5:])
    if ops.SRM_name9  != "":
        for i in SRMModel.objects.all().filter(action_value9=None)[:n]:
            check.append(str(i.SRM_date)[5:])
    if ops.SRM_name10  != "":
        for i in SRMModel.objects.all().filter(action_value10=None)[:n]:
            check.append(str(i.SRM_date)[5:])
    for i in SRMModel.objects.all().filter(mood_value=None)[:n]:
        check.append(str(i.SRM_date)[5:])
    for i in SRMModel.objects.all().filter(ivent=None)[:n]:
        check.append(str(i.SRM_date)[5:])
    check = sorted(list(set(check)))
    check2 = ""
    for i in check:
        check2 += i + ", "
    if check2 != "":
        return "未入力があります　：" + check2
    else:
        return ""

# テンプレートの呼び方
# {% load rrandom_tags %}

# <!-- num1=3, num2=4のとき、HTML上には12が表示される -->
# <span>掛け算:{% randomtag num1 num2 %}</span>