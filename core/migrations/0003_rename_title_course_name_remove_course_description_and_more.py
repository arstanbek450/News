# Generated by Django 4.2.4 on 2023-08-06 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_course_lesson_user_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('russian_word', models.CharField(max_length=100)),
                ('english_word', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course')),
            ],
        ),
    ]
