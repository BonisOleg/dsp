from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_fix_brand_fanery_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='page_title',
            field=models.CharField(
                default='Фанера, ДВП, ДСП — Фанери | Рівне',
                max_length=200,
                verbose_name='Заголовок сторінки (тег <title>)',
            ),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='section_about_title',
            field=models.CharField(default='Про нас', max_length=100, verbose_name='Заголовок секції «Про нас»'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='section_products_title',
            field=models.CharField(default='Продукція', max_length=100, verbose_name='Заголовок секції «Продукція»'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='section_gallery_title',
            field=models.CharField(default='Галерея', max_length=100, verbose_name='Заголовок секції «Галерея»'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='section_contacts_title',
            field=models.CharField(default='Контакти', max_length=100, verbose_name='Заголовок секції «Контакти»'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='stat_year_label',
            field=models.CharField(default='рік заснування', max_length=50, verbose_name='Мітка під роком заснування'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='stat_experience_label',
            field=models.CharField(default='років досвіду', max_length=50, verbose_name='Мітка під досвідом'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='stat_products_label',
            field=models.CharField(default='видів продукції', max_length=50, verbose_name='Мітка під кількістю продукції'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='cta_btn_label',
            field=models.CharField(default="Зв'язатись з нами", max_length=100, verbose_name='Кнопка CTA-банеру'),
        ),
    ]
