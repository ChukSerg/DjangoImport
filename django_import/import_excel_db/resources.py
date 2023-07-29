from import_export import resources, widgets
from import_export.fields import Field
from .models import Boards, Cities, Surfaces, Materials


class BoardsResource(resources.ModelResource):
    city = Field(
            column_name='Город',
            attribute='city',
            widget=widgets.ForeignKeyWidget(Cities, 'name'))
    surface = Field(
            column_name='Тип поверхности',
            attribute='surface',
            widget=widgets.ForeignKeyWidget(Surfaces, 'type'))
    light = Field(attribute='light', column_name='Осв')
    side = Field(attribute='side', column_name='Сторона')
    address = Field(attribute='address', column_name='Адрес')
    in_code = Field(attribute='in_code', column_name='Вн. код')
    latitude = Field(attribute='latitude', column_name='Широта')
    longitude = Field(attribute='longitude', column_name='Долгота')
    scheme = Field(attribute='scheme', column_name='фото/схема')
    price = Field(attribute='price', column_name='Прайс С НДС')
    digital = Field(attribute='digital', column_name='Диджтал кол-во показов')
    grp = Field(attribute='grp', column_name='GRP')
    ots = Field(attribute='ots', column_name='OTS')
    code_espar = Field(attribute='code_espar', column_name='Код Эспар')
    sales_july = Field(attribute='sales_july', column_name='Июль 2023')
    sales_august = Field(attribute='sales_august', column_name='Август 2023')
    sales_september = Field(attribute='sales_september',
                            column_name='Сентябрь 2023')
    sales_october = Field(attribute='sales_october',
                          column_name='Октябрь 2023')
    sales_november = Field(attribute='sales_november',
                           column_name='Ноябрь 2023')
    sales_december = Field(attribute='sales_december',
                           column_name='Декабрь 2023')
    material = Field(attribute='material',
                     column_name='Материал носителя',
                     widget=widgets.ForeignKeyWidget(Materials, 'description'))
    products = Field(attribute='products',
                     column_name='Ограничения по продукту')
    district = Field(attribute='district', column_name='Городской Округ')
    technic = Field(attribute='technic', column_name='Тех. требования')
    price_montage = Field(attribute='price_montage',
                          column_name='Монтаж. Прайс  с НДС')
    price_remontage = Field(attribute='price_remontage',
                            column_name='Переклейка. Прайс с НДС')
    permission_to = Field(attribute='permission_to',
                          column_name='Разрешение ПО',
                          widget=widgets.DateWidget(format='%d.%m.%Y'))
    description = Field(attribute='description', column_name='Примечание')

    def before_import_row(self, row, **kwargs):
        city_name = row['Город']
        Cities.objects.get_or_create(name=city_name)
        surface_name = row['Тип поверхности']
        Surfaces.objects.get_or_create(type=surface_name)
        material_name = row['Материал носителя']
        Materials.objects.get_or_create(description=material_name)

    class Meta:
        model = Boards
        import_id_fields = ('in_code',)
        fields = ('city', 'surface', 'light', 'side', 'address',
                  'in_code', 'latitude', 'longitude', 'scheme',
                  'price', 'digital', 'grp', 'ots', 'code_espar',
                  'sales_july', 'sales_august', 'sales_september',
                  'sales_october', 'sales_november', 'sales_december',
                  'material', 'products', 'district', 'technic',
                  'price_montage', 'price_remontage', 'permission_to',
                  'description')
        use_bulk = True
        batch_size = 1000
        skip_unchanged = True
