# Generated by Django 5.2.1 on 2025-06-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mainpageinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalstatistics',
            name='salary_graph',
        ),
        migrations.RemoveField(
            model_name='generalstatistics',
            name='salary_table',
        ),
        migrations.RemoveField(
            model_name='generalstatistics',
            name='vacancy_graph',
        ),
        migrations.RemoveField(
            model_name='generalstatistics',
            name='vacancy_table',
        ),
        migrations.AddField(
            model_name='generalstatistics',
            name='salary_by_city',
            field=models.ImageField(blank=True, null=True, upload_to='charts/', verbose_name='Уровень зарплат по городам'),
        ),
        migrations.AddField(
            model_name='generalstatistics',
            name='salary_dynamics',
            field=models.ImageField(blank=True, null=True, upload_to='charts/', verbose_name='Динамика уровня зарплат по годам'),
        ),
        migrations.AddField(
            model_name='generalstatistics',
            name='top_skills',
            field=models.ImageField(blank=True, null=True, upload_to='charts/', verbose_name='ТОП-20 навыков по годам'),
        ),
        migrations.AddField(
            model_name='generalstatistics',
            name='vacancies_dynamics',
            field=models.ImageField(blank=True, null=True, upload_to='charts/', verbose_name='Динамика количества вакансий по годам'),
        ),
        migrations.AddField(
            model_name='generalstatistics',
            name='vacancies_share_by_city',
            field=models.ImageField(blank=True, null=True, upload_to='charts/', verbose_name='Доля вакансий по городам'),
        ),
    ]
