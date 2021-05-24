from django import forms
from .models import SRMModel

#活動量の数値の範囲
value_range1 = (('0','0'),('1','1'),('2','2'),('3','3'))
#気分の数値の範囲
value_range2 = (('-5','-5'),('-4','-4'),('-3','-3'),('-2','-2'),('-1','-1'),('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))

class SRMForm(forms.ModelForm):

    model = SRMModel

    action_time1 = forms.TimeField(
        label="TESTaction_range1",
        required =True,
        widget=forms.TimeInput(attrs={"type":"date"}),
        input_formats=['%H:%M']
    )

    action_value1 = forms.ChoiceField(
        label="TESTvalue_range1",
        widget = forms.Select,
        choices = value_range1,
        required =True,
    )
    
    text = forms.CharField(widget=forms.Textarea,
                           label="解析対象")

    select_part = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[("名詞", "名詞"), 
                 ("動詞", "動詞"), 
                 ("形容詞", "形容詞"), ],
        label="出力項目",
        error_messages={'required': '出力項目を選んでください'})

class MorpholyForm(forms.ModelForm):

    class Meta:
        model = SRMModel
        fields = ("action_time1", "action_value1")

    text = forms.CharField(widget=forms.Textarea,
                           label="解析対象")

    select_part = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[("名詞", "名詞"), 
                 ("動詞", "動詞"), 
                 ("形容詞", "形容詞"), ],
        label="出力項目",
        error_messages={'required': '出力項目を選んでください'})