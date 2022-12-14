# Generated by Django 4.1 on 2022-08-13 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='職業名')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'm_occupation',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='決済方法')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'm_payment_methods',
            },
        ),
        migrations.CreateModel(
            name='Payment_status',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'm_payment_status',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='決済状況')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'm_payment_situations',
            },
        ),
        migrations.CreateModel(
            name='Stock_status',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'm_stock_status',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=30, null=True, verbose_name='氏名')),
                ('fullname_kana', models.CharField(blank=True, max_length=30, null=True, verbose_name='氏名カナ')),
                ('pw', models.CharField(blank=True, max_length=30, null=True, verbose_name='パスワード')),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='メール')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='電話')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='年齢')),
                ('prefecture_id', models.CharField(blank=True, max_length=5, null=True, verbose_name='都道府県')),
                ('line_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='LINE')),
                ('discord_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='ディスコードユーザー名')),
                ('discord_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='ディスコードID')),
                ('fx', models.PositiveIntegerField(blank=True, null=True, verbose_name='FXサロン生')),
                ('afiliate_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='紹介者')),
                ('role_state', models.BooleanField(blank=True, null=True, verbose_name='認証状態')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='備考欄')),
                ('join_date', models.DateField(blank=True, null=True, verbose_name='入会日')),
                ('resigned_at', models.DateField(blank=True, null=True, verbose_name='退会日')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='削除日時')),
                ('occupation_id', models.ForeignKey(db_column='occupation_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api_rest_framework.occupation')),
                ('payment_id', models.ForeignKey(db_column='payment_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api_rest_framework.payment')),
                ('payment_status_id', models.ForeignKey(db_column='payment_status_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api_rest_framework.payment_status')),
                ('status_id', models.ForeignKey(db_column='status_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api_rest_framework.status')),
                ('stock', models.ForeignKey(db_column='stock', null=True, on_delete=django.db.models.deletion.CASCADE, to='api_rest_framework.stock_status')),
            ],
            options={
                'db_table': 't_customers',
            },
        ),
    ]
