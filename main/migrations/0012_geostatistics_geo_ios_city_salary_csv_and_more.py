# Generated by Django 5.2.1 on 2025-06-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_skillsstatistics_skills_top_ios_trend_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='geostatistics',
            name='geo_ios_city_salary_csv',
            field=models.FileField(blank=True, null=True, upload_to='csv/', verbose_name='CSV: Уровень зарплат по городам для выбранной профессии'),
        ),
        migrations.AddField(
            model_name='geostatistics',
            name='geo_ios_city_vacancy_share_csv',
            field=models.FileField(blank=True, null=True, upload_to='csv/', verbose_name='CSV: Доля вакансий по городам для выбранной профессии'),
        ),
    ]
