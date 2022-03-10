# Generated by Django 2.0.5 on 2019-11-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asesoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Automaquillaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Informes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colores', models.CharField(blank=True, choices=[('a', 'a) Colores neutros + no se combinarlos prefiero solo usar neutros'), ('b', 'b) Es muy raro que utilice algún otro color aparte de los neutros'), ('c', 'c) Colores neutros + colores pastel o colores claros + colores alegres y vivos '), ('d', 'd) Colores neutros + me gustan los obscuros + no me da miedo el rojo ni los colores brillantes'), ('e', 'e) No hay un limite en el color, me gustan todos y seria capaz de usarlos todos'), ('f', 'f) Prefiero utilizar negro todo el tiempo o colores que estén de moda  ')], max_length=250)),
                ('accesorios', models.CharField(blank=True, choices=[('a', 'a) Es muy raro que utilice accesorios, a veces aretes, alguna pulsera o la bolsa pero casi no los utilizo'), ('b', 'b) Me gusta la joyeria clásica, accesorios minimalistas, de preferencia de marca, accesorios con perlas o un solo material como oro, plata, o pedreria'), ('c', 'c) Entre más accesorios mejor, me gustan las bolsas, los collares, las pulsera, pero tienen que ser accesorios muy femeninos'), ('d', 'd) Me encantan los accesorios pero estos deben ser grandes, que se noten, me gusta que complementen mi look, grandes, vistosos y entre más brillen mejor'), ('e', 'e) Me gusta que mi look luzca totalmente diferente a los demás mis accesorios son vintage, de formas irregulares, me gusta usar muchos me atrevo a usar diferentes. '), ('f', 'f) Los accesorios deben lucir fuertes, exagerados, muy elegante, en tendencia o vanguardistas')], max_length=250)),
                ('siento', models.CharField(blank=True, choices=[('a', 'a) Fachosa por que me siento muy simple'), ('b', 'b) Anticuada suelen decirme que luzco más grande'), ('c', 'c) Demasiado femenina o aniñada'), ('d', 'd) Muy exagerada y atrevida'), ('e', 'e) Ridícula, que no combine bien las prendas, uso muchos colores y estilos al mismo tiempo'), ('f', 'f) Muy bien vestida, muy arreglada me mencionan que luzco enojada o dominante')], max_length=250)),
                ('ropa', models.CharField(blank=True, choices=[('a', 'a) Entre más cómoda mejor, no me gusta que este muy pegada'), ('b', 'b) Me gusta sentirme cómoda pero debo lucir arreglada, me gusta que se vea perfecta, procuro que no tenga arrugas y este en perfecto estado'), ('c', 'c) Me fijo mucho en los detalles, como esta hecha, prefiero que tenga estampados, me gusta que sea muy suave'), ('d', 'd) Me gusta que luzca mi cuerpo, prefiero la ropa muy ajustada y si muestra algo de piel mejor'), ('e', 'e) Diferente, no me gusta verme nada similar a los demás, tengo que ser creativa'), ('f', 'f) Me gusta que se vea imponente, sofisticada y la gente me respete con la ropa que uso y lucir siempre muy arreglada')], max_length=250)),
                ('personalidad', models.CharField(blank=True, choices=[('a', 'a) Divertida, no me considero una persona complicada, soy muy adaptable'), ('b', 'b) Tengo una personalidad más cuadrada, me gusta seguir las reglas, soy perfeccionista'), ('c', 'c) Soy muy amable y gentil, me gusta ayudar a los demás soy sociable y sensible'), ('d', 'd) Tengo una personalidad fuerte, me gusta sentirme atractiva, cuido mucho mi aspecto fisico'), ('e', 'e) Creativa, espontánea, no me gusta seguir reglas, ocurrente'), ('f', 'f) Tengo una personalidad fuerte, soy perfeccionista y me gusta socializar con personas que y conozco, me gusta que el reconocimiento de la gente luzca segura de mi misma')], max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('correo', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Valido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(default=1, max_length=1)),
                ('codigo', models.CharField(max_length=4)),
                ('correo', models.CharField(max_length=250)),
            ],
        ),
    ]
