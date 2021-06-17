from django import forms
from .models import SRMModel, StPointModel
from django.utils import timezone

#活動量の数値の範囲
value_range1 = (('',''),('0','0'),('1','1'),('2','2'),('3','3'))
#気分の数値の範囲
value_range2 = (('',''),('-5','-5'),('-4','-4'),('-3','-3'),('-2','-2'),('-1','-1'),('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))

class SRMForm(forms.ModelForm):
    class Meta:
        model = SRMModel
        fields = ['SRM_date', 'action_time1', 'action_value1', 'action_time2', 'action_value2', 'action_time3', 'action_value3', 
            'action_time4', 'action_value4', 'action_time5', 'action_value5', 'action_time6', 'action_value6', 'action_time7', 'action_value7',
            'action_time8', 'action_value8', 'action_time9', 'action_value9', 'action_time10', 'action_value10', 'mood_value', 'ivent']
        widgets = {
            'SRM_date': forms.DateInput(attrs={"type":"date"}),
            'action_time1': forms.TimeInput(attrs={"type":"time"}),
            'action_time2': forms.TimeInput(attrs={"type":"time"}),
            'action_time3': forms.TimeInput(attrs={"type":"time"}),
            'action_time4': forms.TimeInput(attrs={"type":"time"}),
            'action_time5': forms.TimeInput(attrs={"type":"time"}),
            'action_time6': forms.TimeInput(attrs={"type":"time"}),
            'action_time7': forms.TimeInput(attrs={"type":"time"}),
            'action_time8': forms.TimeInput(attrs={"type":"time"}),
            'action_time9': forms.TimeInput(attrs={"type":"time"}),
            'action_time10': forms.TimeInput(attrs={"type":"time"}),  
        }

class St_Form(forms.ModelForm):
    class Meta:
        model = StPointModel
        fields = '__all__'
        widgets = {
            'point_date': forms.DateTimeInput(attrs={"type":"datetime-local"})
        }
    