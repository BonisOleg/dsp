"""Data migration: seed CMS with default content matching the original static site."""
from django.db import migrations


ABOUT_TEXT_1 = (
    "Нашими партнерами є відомі фірми та підприємці в Україні. Чітко дотримуємось "
    "домовленостей. Готові до співпраці з надійними суб'єктами підприємницької "
    "діяльності та фізичними особами. Практикуємо індивідуальний підхід до "
    "ціноутворення."
)

ABOUT_TEXT_2 = (
    "Пропонуємо плити для будівництва та виготовлення меблів. Реалізуємо товар "
    "гуртом та вроздріб за прийнятними договірними цінами. Оперативно здійснюємо "
    "відвантаження продукції."
)

PRODUCTS = [
    {
        "code": "ФК",
        "name": "Фанера клеєна",
        "badge_colour": "green",
        "image_static": "img/products/fk.png",
        "order": 1,
        "specs": [
            ("Розміри", "1525 × 1525 мм\n2500 × 1250 мм", 1),
            ("Товщина", "4 · 6 · 8 · 10 · 12 · 15 · 18 мм", 2),
            ("Порода", "Береза, вільха", 3),
            ("Сортність", "1/2 · 2/2 · 2/3 · 2/4 · 3/4 · 4/4", 4),
            ("Обробка", "Шліфована з 2-х сторін\nШліфована з 1-ї сторони\nНе шліфована", 5),
        ],
    },
    {
        "code": "ФСФ",
        "name": "Фанера вологостійка ламінована",
        "badge_colour": "default",
        "image_static": "img/products/fsf.png",
        "order": 2,
        "specs": [
            ("Розмір", "2500 × 1250 мм", 1),
            ("Товщина", "9 · 12 · 15 · 18 · 21 мм", 2),
        ],
    },
    {
        "code": "ДВП",
        "name": "Деревоволокниста плита",
        "badge_colour": "amber",
        "image_static": "img/products/dvp.png",
        "order": 3,
        "specs": [
            ("Розміри", "2750 × 1700 мм\n2440 × 1220 мм", 1),
            ("Товщина", "2,5 · 3,0 · 3,2 мм", 2),
        ],
    },
    {
        "code": "ДВПО",
        "name": "ДВП оздоблена (біла)",
        "badge_colour": "amber",
        "image_static": "img/products/dvpo.png",
        "order": 4,
        "specs": [
            ("Розмір", "2745 × 1700 мм", 1),
            ("Товщина", "2,5 · 3,2 мм", 2),
        ],
    },
    {
        "code": "ДСП",
        "name": "Деревостружкова плита",
        "badge_colour": "brown",
        "image_static": "img/products/dsp.png",
        "order": 5,
        "specs": [
            ("Розмір", "2750 × 1830 мм", 1),
            ("Товщина", "16 · 18 мм", 2),
        ],
    },
]

GALLERY = [
    {
        "image_static": "img/gallery/fk-3.png",
        "alt_text": "Фанера клеєна ФК — берізка, шліфована поверхня",
        "caption": "Фанера клеєна берізка/вільха",
        "lightbox_caption": "Фанера клеєна ФК — берізка/вільха",
        "badge_label": "ФК",
        "badge_colour": "green",
        "order": 1,
    },
    {
        "image_static": "img/gallery/fk-1.png",
        "alt_text": "Фанера ФК берізка/вільха, паковання з маркуванням виробника",
        "caption": "ФК — відвантаження від виробника",
        "lightbox_caption": "Фанера клеєна ФК — відвантаження з виробництва",
        "badge_label": "ФК",
        "badge_colour": "green",
        "order": 2,
    },
    {
        "image_static": "img/gallery/fk-2.png",
        "alt_text": "Фанера ФК на складі, стопки на піддонах",
        "caption": "ФК на складі",
        "lightbox_caption": "Фанера клеєна ФК — зберігання на складі",
        "badge_label": "ФК",
        "badge_colour": "green",
        "order": 3,
    },
    {
        "image_static": "img/gallery/fsf-1.png",
        "alt_text": "Фанера ФСФ ламінована чорна, стопки листів",
        "caption": "Фанера ламінована ФСФ (чорна)",
        "lightbox_caption": "Фанера ламінована ФСФ — чорна, двостороннє покриття",
        "badge_label": "ФСФ",
        "badge_colour": "default",
        "order": 4,
    },
    {
        "image_static": "img/gallery/fsf-2.png",
        "alt_text": "ФСФ антиковзна фактура поверхні — шестикутний рельєф",
        "caption": "ФСФ — антиковзна поверхня",
        "lightbox_caption": "Фанера ФСФ — антиковзна поверхня (сітка)",
        "badge_label": "ФСФ",
        "badge_colour": "default",
        "order": 5,
    },
    {
        "image_static": "img/gallery/dvp-1.png",
        "alt_text": "ДВП деревоволокниста плита — стопки листів",
        "caption": "Деревоволокниста плита (ДВП)",
        "lightbox_caption": "ДВП — деревоволокниста плита",
        "badge_label": "ДВП",
        "badge_colour": "amber",
        "order": 6,
    },
    {
        "image_static": "img/gallery/dvp-2.png",
        "alt_text": "ДВП відвантаження у вантажівці",
        "caption": "ДВП — відвантаження",
        "lightbox_caption": "ДВП — відвантаження, завантажений транспорт",
        "badge_label": "ДВП",
        "badge_colour": "amber",
        "order": 7,
    },
    {
        "image_static": "img/gallery/dvp-3.png",
        "alt_text": "ДВП завантаження у вантажівці",
        "caption": "ДВП — доставка",
        "lightbox_caption": "ДВП — доставка, завантажений транспорт",
        "badge_label": "ДВП",
        "badge_colour": "amber",
        "order": 8,
    },
    {
        "image_static": "img/gallery/dvpo-1.png",
        "alt_text": "ДВПО біла — гладка ламінована поверхня",
        "caption": "ДВП оздоблена (ДВПО) біла",
        "lightbox_caption": "ДВПО — ДВП оздоблена біла",
        "badge_label": "ДВПО",
        "badge_colour": "amber",
        "order": 9,
    },
    {
        "image_static": "img/gallery/dvpo-2.png",
        "alt_text": "ДВПО оздоблена біла з маркуванням розмірів",
        "caption": "ДВПО біла 2.75×1.7 м",
        "lightbox_caption": "ДВПО біла 2.75×1.7 м — стандартний аркуш",
        "badge_label": "ДВПО",
        "badge_colour": "amber",
        "order": 10,
    },
    {
        "image_static": "img/gallery/dsp-1.png",
        "alt_text": "ДСП деревостружкова плита — стопка листів",
        "caption": "Деревостружкова плита (ДСП)",
        "lightbox_caption": "ДСП — деревостружкова плита",
        "badge_label": "ДСП",
        "badge_colour": "brown",
        "order": 11,
    },
]


def seed_forward(apps, schema_editor):
    SiteSettings = apps.get_model("core", "SiteSettings")
    Product = apps.get_model("core", "Product")
    ProductSpec = apps.get_model("core", "ProductSpec")
    GalleryImage = apps.get_model("core", "GalleryImage")

    SiteSettings.objects.get_or_create(
        pk=1,
        defaults={
            "header_name": "ФАНЕРА  ДВП",
            "header_tagline": "Фанера · ДВП · ДСП",
            "header_phone": "+380976962409",
            "hero_title": "Будівельні плити та фанера у Рівному",
            "hero_subtitle": "Гурт та роздріб з 1997 року · Індивідуальні ціни",
            "about_year": "1997",
            "about_experience": "28+",
            "about_product_count": "4",
            "about_text_1": ABOUT_TEXT_1,
            "about_text_2": ABOUT_TEXT_2,
            "cta_title": "Готові до співпраці?",
            "cta_description": "Розкажіть про вашу потребу — підберемо оптимальну позицію та ціну",
            "contact_address": "вул. Будівельників, 7, м. Рівне",
            "contact_phone_1": "+380976962409",
            "contact_phone_1_display": "097 696 24 09",
            "contact_phone_2": "+380505072334",
            "contact_phone_2_display": "050 507 23 34",
            "contact_email": "tmuzicko@gmail.com",
            "contact_cta_title": "Готові до співпраці",
            "footer_copyright": "ФОП Музичко Михайло Васильович · Рівне",
            "meta_description": (
                "ФОП Музичко М.В. — фанера, ДВП, ДСП у Рівному. "
                "Гурт та роздріб. Тел. 097 696 24 09"
            ),
        },
    )

    for p_data in PRODUCTS:
        specs = p_data.pop("specs")
        product, created = Product.objects.get_or_create(
            code=p_data["code"],
            defaults=p_data,
        )
        if created:
            for label, value, order in specs:
                ProductSpec.objects.create(
                    product=product,
                    label=label,
                    value=value,
                    order=order,
                )

    for g_data in GALLERY:
        GalleryImage.objects.get_or_create(
            image_static=g_data["image_static"],
            defaults=g_data,
        )


def seed_reverse(apps, schema_editor):
    SiteSettings = apps.get_model("core", "SiteSettings")
    Product = apps.get_model("core", "Product")
    GalleryImage = apps.get_model("core", "GalleryImage")
    SiteSettings.objects.filter(pk=1).delete()
    Product.objects.all().delete()
    GalleryImage.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_cms_models"),
    ]

    operations = [
        migrations.RunPython(seed_forward, seed_reverse),
    ]
