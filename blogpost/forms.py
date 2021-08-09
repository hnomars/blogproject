from django import forms
from .models import SRMModel, StPointModel, MonitorModel, StPointNameModel, ExerciseModel
import django.utils

#活動量の数値の範囲
value_range1 = (('',''),('0','0'),('1','1'),('2','2'),('3','3'))
#気分の数値の範囲
value_range2 = (('',''),('-5','-5'),('-4','-4'),('-3','-3'),('-2','-2'),('-1','-1'),('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))

CONDITION = [
    ("焦り",'焦り'),
    ("不安",'不安'),
    ("恐怖",'恐怖'),
    ("睡眠不足",'睡眠不足'),
    ("生活リズム",'生活リズム'),
    ("イライラ",'イライラ'),
    ("他人の仕事",'他人の仕事'),
    ("不要な共感",'不要な共感'),
    ("過食",'過食'),
    ("疲れ",'疲れ'),
    ("怒り",'怒り'),
    ("我慢",'我慢'),
    ("会話不足",'会話不足'),
    ]

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
        from .models import StPointModel, StPointNameModel
        points = StPointNameModel.objects.all().values_list('point')
        pointslist = []
        for i in range(len(points)):
            pointslist.append(points[i][0])

        for i in range(30-len(pointslist)):
            pointslist.append(0)

        model = StPointModel
        fields = '__all__'
        widgets = {
            'point_date': forms.DateInput(attrs={"type":"date"}),
            'point1' : forms.Select(choices=[(pointslist[0], 'Yes'), (0, 'No')]),
            'point2' : forms.Select(choices=[(pointslist[1], 'Yes'), (0, 'No')]),
            'point3' : forms.Select(choices=[(pointslist[2], 'Yes'), (0, 'No')]),
            'point4' : forms.Select(choices=[(pointslist[3], 'Yes'), (0, 'No')]),
            'point5' : forms.Select(choices=[(pointslist[4], 'Yes'), (0, 'No')]),
            'point6' : forms.Select(choices=[(pointslist[5], 'Yes'), (0, 'No')]),
            'point7' : forms.Select(choices=[(pointslist[6], 'Yes'), (0, 'No')]),
            'point8' : forms.Select(choices=[(pointslist[7], 'Yes'), (0, 'No')]),
            'point9' : forms.Select(choices=[(pointslist[8], 'Yes'), (0, 'No')]),
            'point10' : forms.Select(choices=[(pointslist[9], 'Yes'), (0, 'No')]),
            'point11' : forms.Select(choices=[(pointslist[10], 'Yes'), (0, 'No')]),
            'point12' : forms.Select(choices=[(pointslist[11], 'Yes'), (0, 'No')]),
            'point13' : forms.Select(choices=[(pointslist[12], 'Yes'), (0, 'No')]),
            'point14' : forms.Select(choices=[(pointslist[13], 'Yes'), (0, 'No')]),
            'point15' : forms.Select(choices=[(pointslist[14], 'Yes'), (0, 'No')]),
            'point16' : forms.Select(choices=[(pointslist[15], 'Yes'), (0, 'No')]),
            'point17' : forms.Select(choices=[(pointslist[16], 'Yes'), (0, 'No')]),
            'point18' : forms.Select(choices=[(pointslist[17], 'Yes'), (0, 'No')]),
            'point19' : forms.Select(choices=[(pointslist[18], 'Yes'), (0, 'No')]),
            'point20' : forms.Select(choices=[(pointslist[19], 'Yes'), (0, 'No')]),
            'point21' : forms.Select(choices=[(pointslist[20], 'Yes'), (0, 'No')]),
            'point22' : forms.Select(choices=[(pointslist[21], 'Yes'), (0, 'No')]),
            'point23' : forms.Select(choices=[(pointslist[22], 'Yes'), (0, 'No')]),
            'point24' : forms.Select(choices=[(pointslist[23], 'Yes'), (0, 'No')]),
            'point25' : forms.Select(choices=[(pointslist[24], 'Yes'), (0, 'No')]),
            'point26' : forms.Select(choices=[(pointslist[25], 'Yes'), (0, 'No')]),
            'point27' : forms.Select(choices=[(pointslist[26], 'Yes'), (0, 'No')]),
            'point28' : forms.Select(choices=[(pointslist[27], 'Yes'), (0, 'No')]),
            'point29' : forms.Select(choices=[(pointslist[28], 'Yes'), (0, 'No')]),
            'point30' : forms.Select(choices=[(pointslist[29], 'Yes'), (0, 'No')]),
        }

class St_Form(forms.ModelForm):
    class Meta:
        model = StPointModel
        fields = '__all__'
        widgets = {
            'point_date': forms.DateInput(attrs={"type":"date"})
        }

class Moni_Form(forms.ModelForm):
    class Meta:
        model = MonitorModel
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={"type":"date"}),
            'time': forms.TimeInput(attrs={"type":"time"})
        }

class St_Form(forms.ModelForm):
    class Meta:
        model = StPointModel
        fields = '__all__'
        widgets = {
            'point_date': forms.DateInput(attrs={"type":"date"})
        }

class Exer_Form(forms.ModelForm):
    class Meta:
        model = ExerciseModel
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={"type":"date"}),
            'time': forms.TimeInput(attrs={"type":"time"}),
            'strespoint_1': forms.NumberInput(attrs={'rows':2, 'cols':2}),
            'strespoint_2': forms.NumberInput(attrs={'rows':2, 'cols':2}),
        }