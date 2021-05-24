from django import template
import random
from blogpost.models import WordModel, SRMModel, StPointModel
register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムtタグとして登録する
@register.simple_tag
def randomtag(value1,value2):
    words = WordModel.objects.values_list("word", flat=True)

    i = random.randint(0,len(words)-1)
    return  words[i] +str(i)

@register.simple_tag
def tfcheck(value1):
    if value1 == True:
        return "〇"
    else:
        return ""
    
@register.simple_tag
def tftest(value1):
    return "stNames."+ str(value1)

@register.simple_tag
def nullblank(value1):
    if value1 is not None:
        ans = value1
    else:
        ans = "－"
    return ans


# テンプレートの呼び方
# {% load rrandom_tags %}

# <!-- num1=3, num2=4のとき、HTML上には12が表示される -->
# <span>掛け算:{% randomtag num1 num2 %}</span>