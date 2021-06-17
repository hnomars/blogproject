from django.db import models
from django.db.models.fields import AutoField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import time

# Create your models here.
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

CATEGORY = (('business','ビジネス'),('Life','生活'),('other','その他'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length= 50,
        choices = CATEGORY
    )
    def __str__(self):
        return self.title

class SRMOptionModel(models.Model):
    # CATEGORY = (("00","-"),("01","起床"),("02","接触"))#"起床","接触","集団","夕食","就寝"
    # Char_set = models.CharField(max_length=20, choices = CATEGORY)
    title = "SRM_option"
    SRM_name1 = "就寝"
    SRM_name2 = "起床"
    SRM_name3 = models.CharField(default = "接触", max_length=20, blank=True, null=True)
    SRM_name4 = models.CharField(default = "集団", max_length=20, blank=True, null=True)
    SRM_name5 = models.CharField(default = "夕食", max_length=20, blank=True, null=True)
    SRM_name6 = models.CharField(max_length=20,blank=True, null=True)
    SRM_name7 = models.CharField(max_length=20,blank=True, null=True)
    SRM_name8 = models.CharField(max_length=20,blank=True, null=True)
    SRM_name9 = models.CharField(max_length=20,blank=True, null=True)
    SRM_name10 = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.title

class SRMModel(models.Model):
    actions = ["昨就寝","起床","接触","集団","夕食","#6","#7","#8","#9","#10"]
    action_times = ["action" + str(i) +"_time" for i in range(len(actions))]  
    default_times = [time(21,00,00,0),time(4,30,00,0),time(6,30,00,0),time(9,00,00,0),time(18,30,00,0),time(12,00,00,0),time(12,00,00,0),time(12,00,00,0),time(12,00,00,0),time(12,00,00,0)]
    action_values = ["action" + str(i) +"_value" for i in range(len(actions))]  
    #活動量の数値の範囲
    value_range1 =  ((0,0),(1,1),(2,2),(3,3))
    #気分の数値の範囲
    value_range2 = ((-5,-5),(-4,-4),(-3,-3),(-2,-2),(-1,-1),(0,0),(1,1),(2,2),(3,3),(4,4),(5,5))

    i = 0

    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    SRM_date = models.DateField(primary_key=True, default=timezone.localtime, help_text="日付")  #db_index=True

    action_time1 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value1 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time2 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value2 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time3 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value3 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time4 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value4 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time5 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value5 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time6 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value6 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time7 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value7 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time8 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value8 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time9 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value9 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time10 = models.TimeField(default=default_times[i] , blank=True, null=True, help_text=actions[i] + "の時間")
    action_value10 = models.IntegerField(choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")

    mood_value = models.IntegerField(choices=value_range2, default=None, blank=True, null=True, help_text="気分の値 -5～5")
    ivent = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        self.title = str(self.SRM_date)
        return self.title

SITUATION = [
    ('always','いつでも'),
    ('Sad','悲しい時に送る言葉'),
    ('Sleepless','眠っていない'),
    ('high','躁度が高い'),
    ('low','躁度が低い'),
    ('angry','イライラしている'),
    ('hurry','焦っている'),
    ]

class WordModel(models.Model):
    word = models.TextField()
    category = models.TextField(
        verbose_name="どんな時にかけたい言葉ですか？",
        choices=SITUATION,
        blank=True
        )
    def __str__(self):
        return self.word

CONDITION = [
    ("1",'焦り'),
    ("2",'睡眠不足'),
    ("3",'生活リズム'),
    ("4",'イライラ'),
    ("5",'他人の仕事'),
    ("6",'不要な共感'),
    ("7",'過食'),
    ("8",'疲れ'),
    ("9",'怒り'),
    ("10",'我慢'),
    ("11",'会話不足'),
    ]

class StPointNameModel(models.Model):
    episode = models.CharField(max_length=30)
    category = models.CharField(
        verbose_name="分類",
        choices=CONDITION,
        max_length=20,
        blank=True
        )
    point = models.IntegerField(default=30, validators=[MinValueValidator(1), MaxValueValidator(100)], help_text="1～100")
    def __str__(self):
        return self.episode
    
class StPointModel(models.Model):
    point_date = models.DateField(default=timezone.now, primary_key=True, help_text="日付") #unique_for_date=True
    point1 = models.BooleanField(default=False)
    point2 = models.BooleanField(default=False)
    point3 = models.BooleanField(default=False)
    point4 = models.BooleanField(default=False)
    point5 = models.BooleanField(default=False)
    point6 = models.BooleanField(default=False)
    point7 = models.BooleanField(default=False)
    point8 = models.BooleanField(default=False)
    point9 = models.BooleanField(default=False)
    point10 = models.BooleanField(default=False)
    point11 = models.BooleanField(default=False)
    point12 = models.BooleanField(default=False)
    point13 = models.BooleanField(default=False)
    point14 = models.BooleanField(default=False)
    point15 = models.BooleanField(default=False)
    point16 = models.BooleanField(default=False)
    point17 = models.BooleanField(default=False)
    point18 = models.BooleanField(default=False)
    point19 = models.BooleanField(default=False)
    point20 = models.BooleanField(default=False)
    point21 = models.BooleanField(default=False)
    point22 = models.BooleanField(default=False)
    point23 = models.BooleanField(default=False)
    point24 = models.BooleanField(default=False)
    point25 = models.BooleanField(default=False)
    point26 = models.BooleanField(default=False)
    point27 = models.BooleanField(default=False)
    point28 = models.BooleanField(default=False)
    point29 = models.BooleanField(default=False)
    point30 = models.BooleanField(default=False)

class MonitorModel(models.Model):
    datetime = models.DateTimeField(default=timezone.now, primary_key=True, help_text="日付") #unique_for_date=True
    event = models.CharField(max_length=100 ,help_text="きっかけ")
    think = models.CharField(max_length=100 ,help_text="考え")
    action = models.CharField(max_length=100 ,help_text="行動")
    emotion = models.CharField(max_length=200 ,help_text="気持ち")
    body = models.CharField(max_length=100 ,help_text="身体感覚")
    stress = models.CharField(
        max_length= 50,
        choices = CONDITION
    )
    strespoint =  models.CharField(max_length=100 ,help_text="行動")
    def __str__(self):
        return self.title