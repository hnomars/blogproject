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
    actions = ["昨就寝","起床","接触","集団","帰宅","夕食","#7","#8","#9","#10"]
    action_times = ["action" + str(i) +"_time" for i in range(len(actions))]  
    default_times = [time(21,00,00,0),time(4,30,00,0),time(6,30,00,0),time(9,00,00,0),time(17,30,00,0),time(18,30,00,0),time(12,00,00,0),time(12,00,00,0),time(12,00,00,0),time(12,00,00,0)]
    default_values = [2,0,2,2,2,2,0,0,0,0]
    action_values = ["action" + str(i) +"_value" for i in range(len(actions))]  
    #活動量の数値の範囲
    value_range1 =  ((0,0),(1,1),(2,2),(3,3))
    #気分の数値の範囲
    value_range2 = ((-5,-5),(-4,-4),(-3,-3),(-2,-2),(-1,-1),(0,0),(1,1),(2,2),(3,3),(4,4),(5,5))

    i = 0

    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    SRM_date = models.DateField(primary_key=True, default=timezone.localtime, help_text="日付")  #db_index=True

    action_time1 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value1 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time2 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value2 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time3 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value3 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time4 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value4 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time5 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value5 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time6 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value6 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time7 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value7 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time8 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value8 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time9 = models.TimeField(default=default_times[i], blank=True, null=True, help_text=actions[i] + "の時間")
    action_value9 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")
    i += 1
    action_time10 = models.TimeField(default=default_times[i] , blank=True, null=True, help_text=actions[i] + "の時間")
    action_value10 = models.IntegerField(default=default_values[i], choices=value_range1, blank=True, null=True, help_text=actions[i] +"の活動量 0～3")

    day = models.CharField(max_length=20, blank=True, null=True)

    mood_value = models.IntegerField(choices=value_range2, default=None, blank=True, null=True, help_text="気分の値 -5～5")
    ivent = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        self.title = str(self.SRM_date)
        return self.title

SITUATION = [
    ('いつでも','いつでも'),
    ('不安','不安'),
    ('恐怖','恐怖'),
    ('悲しい時に送る言葉','悲しい時に送る言葉'),
    ('眠っていない','眠っていない'),
    ('躁度が高い','躁度が高い'),
    ('躁度が低い','躁度が低い'),
    ("ストレス値高い","ストレス値高い"),
    ('イライラしている','イライラしている'),
    ('焦っている','焦っている'),
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
    ('オーバーワーク','オーバーワーク'),
    ('ストレス行動・現象','ストレス行動・現象'),
    ('我慢','我慢'),
    ('時間管理','時間管理'),
    ('気持ちのゆとり','気持ちのゆとり'),
    ('焦り','焦り'),
    ('生活リズム','生活リズム'),
    ('怒り','怒り'),
    ('不調','不調'),
    ('不安','不安'),
    ('恐怖','恐怖'),
    ("疲れ",'疲れ'),
    ("不要な共感",'不要な共感'),
    ("他人の仕事",'他人の仕事'),
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
    pointlist = list(StPointNameModel.objects.all().values_list('point', flat=True).order_by("id"))
    add0 = 30 - len(pointlist)
    for i in range(add0):
        pointlist.append(0)
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
    sumpoint = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.sumpoint = self.point1*self.pointlist[0]+self.point2*self.pointlist[1]+self.point3*self.pointlist[2]+self.point4*self.pointlist[3]+self.point5*self.pointlist[4]+self.point6*self.pointlist[5]+self.point7*self.pointlist[6]+self.point8*self.pointlist[7]+self.point9*self.pointlist[8]+self.point10*self.pointlist[9]+self.point11*self.pointlist[10]+self.point12*self.pointlist[11]+self.point13*self.pointlist[12]+self.point14*self.pointlist[13]+self.point15*self.pointlist[14]+self.point16*self.pointlist[15]+self.point17*self.pointlist[16]+self.point18*self.pointlist[17]+self.point19*self.pointlist[18]+self.point20*self.pointlist[19]+self.point21*self.pointlist[20]+self.point22*self.pointlist[21]+self.point23*self.pointlist[22]+self.point24*self.pointlist[23]+self.point25*self.pointlist[24]+self.point26*self.pointlist[25]+self.point27*self.pointlist[26]+self.point28*self.pointlist[27]+self.point29*self.pointlist[28]+self.point30*self.pointlist[29]

        #self.sumpoint = self.point1*self.pointlist[0]+self.point2+self.point3+self.point4+self.point5+self.point6+self.point7+self.point8+self.point9+self.point10+self.point11+self.point12+self.point13+self.point14+self.point15+self.point16+self.point17+self.point18+self.point19+self.point20+self.point21+self.point22+self.point23+self.point24+self.point25+self.point26+self.point27+self.point28+self.point29+self.point30
        super().save(*args, **kwargs)
        print(self.sumpoint)

    def __str__(self):
        self.title = str(self.point_date)
        return self.title

class MonitorModel(models.Model):
    date = models.DateField(default=timezone.now, help_text="日付") #unique_for_date=True
    time = models.TimeField(default=timezone.now, blank=True, null=True, help_text="時間") #unique_for_date=True
    event = models.CharField(max_length=100, blank=True, null=True, help_text="きっかけ")
    think = models.CharField(max_length=100, blank=True, null=True, help_text="考え")
    action = models.CharField(max_length=100, blank=True, null=True, help_text="行動")
    emotion = models.CharField(max_length=200, blank=True, null=True, help_text="気持ち")
    body = models.CharField(max_length=100, blank=True, null=True, help_text="身体感覚")
    stress = models.CharField(
        max_length= 50,
        choices = CONDITION, blank=True, null=True,
    )
    strespoint =  models.CharField(max_length=100, blank=True, null=True, help_text="行動")

class ExerciseModel(models.Model):
    falls = [("なし",'なし'),("①",'①'),("②",'②')]
    date = models.DateField(default=timezone.now, help_text="記録した日付") #unique_for_date=True
    time = models.TimeField(default=timezone.now, blank=True, null=True, help_text="記録した時間") #unique_for_date=True
    think = models.TextField(max_length=100, blank=True, null=True, help_text="浮かんだ考え心のつぶやき")
    stress_1 = models.CharField(
        max_length= 30,
        choices = CONDITION, blank=True, null=True, default='なし',
    )
    strespoint_1 =  models.IntegerField(blank=True, null=True, default=0, help_text="気持ちの強さ１")
    stress_2 = models.CharField(
        max_length= 10,
        choices = CONDITION, blank=True, null=True, default='なし',
    )
    strespoint_2 =  models.IntegerField(blank=True, null=True, default=0, help_text="気持ちの強さ２（あれば）")
    
    fall = models.CharField(default='なし', max_length=5, blank=True, null=True, choices = falls, help_text="考えの落とし穴")
    evidence = models.TextField(max_length=100, blank=True, null=True, help_text="その根拠")
    opposite = models.TextField(max_length=200, blank=True, null=True, help_text="気持ち")
    stress_3 = models.CharField(
        max_length= 10,
        choices = CONDITION, blank=True, null=True, default='なし',
    )
    strespoint_3 =  models.IntegerField(blank=True, null=True, default=0, help_text="気持ちの強さ１")
    stress_4 = models.CharField(
        max_length= 10,
        choices = CONDITION, blank=True, null=True, default='なし',
    )
    strespoint_4 =  models.IntegerField(blank=True, null=True, default=0, help_text="気持ちの強さ２（あれば）")
    

