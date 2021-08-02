# Generated by Django 3.2 on 2021-07-18 21:37

import datetime
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('postdate', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('business', 'ビジネス'), ('Life', '生活'), ('other', 'その他')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MonitorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, help_text='日付')),
                ('time', models.TimeField(default=django.utils.timezone.now, help_text='時間')),
                ('event', models.CharField(help_text='きっかけ', max_length=100)),
                ('think', models.CharField(help_text='考え', max_length=100)),
                ('action', models.CharField(help_text='行動', max_length=100)),
                ('emotion', models.CharField(help_text='気持ち', max_length=200)),
                ('body', models.CharField(help_text='身体感覚', max_length=100)),
                ('stress', models.CharField(choices=[('1', '焦り'), ('2', '睡眠不足'), ('3', '生活リズム'), ('4', 'イライラ'), ('5', '他人の仕事'), ('6', '不要な共感'), ('7', '過食'), ('8', '疲れ'), ('9', '怒り'), ('10', '我慢'), ('11', '会話不足')], max_length=50)),
                ('strespoint', models.CharField(help_text='行動', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SRMModel',
            fields=[
                ('SRM_date', models.DateField(default=django.utils.timezone.localtime, help_text='日付', primary_key=True, serialize=False)),
                ('action_time1', models.TimeField(blank=True, default=datetime.time(21, 0), help_text='昨就寝の時間', null=True)),
                ('action_value1', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='昨就寝の活動量 0～3', null=True)),
                ('action_time2', models.TimeField(blank=True, default=datetime.time(4, 30), help_text='起床の時間', null=True)),
                ('action_value2', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='起床の活動量 0～3', null=True)),
                ('action_time3', models.TimeField(blank=True, default=datetime.time(6, 30), help_text='接触の時間', null=True)),
                ('action_value3', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='接触の活動量 0～3', null=True)),
                ('action_time4', models.TimeField(blank=True, default=datetime.time(9, 0), help_text='集団の時間', null=True)),
                ('action_value4', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='集団の活動量 0～3', null=True)),
                ('action_time5', models.TimeField(blank=True, default=datetime.time(18, 30), help_text='夕食の時間', null=True)),
                ('action_value5', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='夕食の活動量 0～3', null=True)),
                ('action_time6', models.TimeField(blank=True, default=datetime.time(12, 0), help_text='#6の時間', null=True)),
                ('action_value6', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='#6の活動量 0～3', null=True)),
                ('action_time7', models.TimeField(blank=True, default=datetime.time(12, 0), help_text='#7の時間', null=True)),
                ('action_value7', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='#7の活動量 0～3', null=True)),
                ('action_time8', models.TimeField(blank=True, default=datetime.time(12, 0), help_text='#8の時間', null=True)),
                ('action_value8', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='#8の活動量 0～3', null=True)),
                ('action_time9', models.TimeField(blank=True, default=datetime.time(12, 0), help_text='#9の時間', null=True)),
                ('action_value9', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='#9の活動量 0～3', null=True)),
                ('action_time10', models.TimeField(blank=True, default=datetime.time(12, 0), help_text='#10の時間', null=True)),
                ('action_value10', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3)], help_text='#10の活動量 0～3', null=True)),
                ('mood_value', models.IntegerField(blank=True, choices=[(-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None, help_text='気分の値 -5～5', null=True)),
                ('ivent', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SRMOptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SRM_name3', models.CharField(blank=True, default='接触', max_length=20, null=True)),
                ('SRM_name4', models.CharField(blank=True, default='集団', max_length=20, null=True)),
                ('SRM_name5', models.CharField(blank=True, default='夕食', max_length=20, null=True)),
                ('SRM_name6', models.CharField(blank=True, max_length=20, null=True)),
                ('SRM_name7', models.CharField(blank=True, max_length=20, null=True)),
                ('SRM_name8', models.CharField(blank=True, max_length=20, null=True)),
                ('SRM_name9', models.CharField(blank=True, max_length=20, null=True)),
                ('SRM_name10', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StPointModel',
            fields=[
                ('point_date', models.DateField(default=django.utils.timezone.now, help_text='日付', primary_key=True, serialize=False)),
                ('point1', models.IntegerField(default=0)),
                ('point2', models.IntegerField(default=0)),
                ('point3', models.IntegerField(default=0)),
                ('point4', models.IntegerField(default=0)),
                ('point5', models.IntegerField(default=0)),
                ('point6', models.IntegerField(default=0)),
                ('point7', models.IntegerField(default=0)),
                ('point8', models.IntegerField(default=0)),
                ('point9', models.IntegerField(default=0)),
                ('point10', models.IntegerField(default=0)),
                ('point11', models.IntegerField(default=0)),
                ('point12', models.IntegerField(default=0)),
                ('point13', models.IntegerField(default=0)),
                ('point14', models.IntegerField(default=0)),
                ('point15', models.IntegerField(default=0)),
                ('point16', models.IntegerField(default=0)),
                ('point17', models.IntegerField(default=0)),
                ('point18', models.IntegerField(default=0)),
                ('point19', models.IntegerField(default=0)),
                ('point20', models.IntegerField(default=0)),
                ('point21', models.IntegerField(default=0)),
                ('point22', models.IntegerField(default=0)),
                ('point23', models.IntegerField(default=0)),
                ('point24', models.IntegerField(default=0)),
                ('point25', models.IntegerField(default=0)),
                ('point26', models.IntegerField(default=0)),
                ('point27', models.IntegerField(default=0)),
                ('point28', models.IntegerField(default=0)),
                ('point29', models.IntegerField(default=0)),
                ('point30', models.IntegerField(default=0)),
                ('sumpoint', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StPointNameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode', models.CharField(max_length=30)),
                ('category', models.CharField(blank=True, choices=[('1', '焦り'), ('2', '睡眠不足'), ('3', '生活リズム'), ('4', 'イライラ'), ('5', '他人の仕事'), ('6', '不要な共感'), ('7', '過食'), ('8', '疲れ'), ('9', '怒り'), ('10', '我慢'), ('11', '会話不足')], max_length=20, verbose_name='分類')),
                ('point', models.IntegerField(default=30, help_text='1～100', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='WordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
                ('category', models.TextField(blank=True, choices=[('always', 'いつでも'), ('Sad', '悲しい時に送る言葉'), ('Sleepless', '眠っていない'), ('high', '躁度が高い'), ('low', '躁度が低い'), ('angry', 'イライラしている'), ('hurry', '焦っている')], verbose_name='どんな時にかけたい言葉ですか？')),
            ],
        ),
    ]
