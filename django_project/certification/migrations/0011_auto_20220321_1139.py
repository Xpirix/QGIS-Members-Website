# Generated by Django 2.2.18 on 2022-03-21 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_auto_20210308_0244'),
        ('certification', '0010_merge_20220212_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='certification.CertificateType'),
        ),
        migrations.CreateModel(
            name='HistoricalChecklist',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, db_index=True, null=True)),
                ('question', models.TextField(help_text='Checklist question for certification application form, e.g. Have you contributed to documentation?')),
                ('active', models.BooleanField(default=False)),
                ('show_text_box', models.BooleanField(default=False, help_text='Indicate whether the user should see a text box to add detail or not')),
                ('approved', models.BooleanField(default=False, help_text='Approval from project admin')),
                ('remarks', models.CharField(blank=True, help_text='Remarks regarding status of this checklist, i.e. Rejected, because lacks of information', max_length=500, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.Project')),
            ],
            options={
                'verbose_name': 'historical checklist',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True, unique=True)),
                ('question', models.TextField(help_text='Checklist question for certification application form, e.g. Have you contributed to documentation?')),
                ('active', models.BooleanField(default=False)),
                ('show_text_box', models.BooleanField(default=False, help_text='Indicate whether the user should see a text box to add detail or not')),
                ('approved', models.BooleanField(default=False, help_text='Approval from project admin')),
                ('remarks', models.CharField(blank=True, help_text='Remarks regarding status of this checklist, i.e. Rejected, because lacks of information', max_length=500, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project')),
            ],
        ),
    ]
