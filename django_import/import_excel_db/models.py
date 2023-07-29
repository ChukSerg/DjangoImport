from django.db import models


class Boards(models.Model):
    in_code = models.CharField(
        max_length=50,
    )
    city = models.ForeignKey('Cities', on_delete=models.CASCADE)
    surface = models.ForeignKey('Surfaces', on_delete=models.CASCADE)
    light = models.CharField(max_length=20)
    side = models.CharField(max_length=20)
    address = models.CharField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=13)
    longitude = models.DecimalField(max_digits=16, decimal_places=13)
    scheme = models.URLField()
    price = models.FloatField(null=True, blank=True)
    digital = models.PositiveIntegerField(null=True, blank=True)
    grp = models.FloatField(null=True, blank=True)
    ots = models.FloatField(null=True, blank=True)
    code_espar = models.CharField(max_length=10, null=True, blank=True)
    sales_july = models.CharField(max_length=400, null=True, blank=True)
    sales_august = models.CharField(max_length=400, null=True, blank=True)
    sales_september = models.CharField(max_length=400, null=True, blank=True)
    sales_october = models.CharField(max_length=400, null=True, blank=True)
    sales_november = models.CharField(max_length=400, null=True, blank=True)
    sales_december = models.CharField(max_length=400, null=True, blank=True)
    material = models.ForeignKey(
        'Materials',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    products = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    technic = models.URLField(null=True, blank=True)
    price_montage = models.PositiveIntegerField(null=True, blank=True)
    price_remontage = models.FloatField(null=True, blank=True)
    permission_to = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'г.%s, %s, сторона: %s' % (self.city, self.address, self.side)

    class Meta:
        verbose_name = 'Рекламный щит'
        verbose_name_plural = 'Рекламные щиты'
        models.UniqueConstraint(fields=['in_code', 'surface'],
                                name='code_surface')


class Cities(models.Model):
    name = models.CharField(
        max_length=50,
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self) -> str:
        return self.name


class Surfaces(models.Model):
    type = models.CharField(
        max_length=50,
    )

    class Meta:
        verbose_name = 'Поверхность'
        verbose_name_plural = 'Поверхности'

    def __str__(self) -> str:
        return self.type


class Materials(models.Model):
    description = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
