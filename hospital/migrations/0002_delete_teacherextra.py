from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeacherExtra',
        ),
    ]