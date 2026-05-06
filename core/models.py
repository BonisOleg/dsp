from django.db import models


# ── CMS: badge colour choices ────────────────────────────────────────────────

BADGE_COLOUR_CHOICES = [
    ("default", "Синій"),
    ("green", "Зелений"),
    ("amber", "Жовтий"),
    ("brown", "Коричневий"),
]


# ── CMS: Site-wide settings (singleton) ─────────────────────────────────────

class SiteSettings(models.Model):
    """Singleton — зберігає весь редагований контент сайту (крім продуктів і галереї)."""

    # Header
    header_name = models.CharField("Назва компанії", max_length=100, default="ФАНЕРА  ДВП")
    header_tagline = models.CharField("Підзаголовок хедера", max_length=100, default="Фанера · ДВП · ДСП")
    header_phone = models.CharField(
        "Телефон хедера (для посилання tel:)", max_length=30, default="+380976962409",
        help_text="Формат: +380976962409",
    )

    # Hero
    hero_title = models.CharField("Заголовок Hero", max_length=200, default="Будівельні плити та фанера у Рівному")
    hero_subtitle = models.CharField("Підзаголовок Hero", max_length=300, default="Гурт та роздріб з 1997 року · Індивідуальні ціни")

    # About — stats
    about_year = models.CharField("Рік заснування", max_length=10, default="1997")
    about_experience = models.CharField("Років досвіду", max_length=10, default="28+")
    about_product_count = models.CharField("Видів продукції", max_length=10, default="4")
    about_text_1 = models.TextField("Текст «Про нас» 1", default="")
    about_text_2 = models.TextField("Текст «Про нас» 2", default="")

    # CTA banner
    cta_title = models.CharField("CTA заголовок", max_length=200, default="Готові до співпраці?")
    cta_description = models.CharField("CTA опис", max_length=300, default="Розкажіть про вашу потребу — підберемо оптимальну позицію та ціну")

    # Contacts
    contact_address = models.CharField("Адреса", max_length=200, default="вул. Будівельників, 7, м. Рівне")
    contact_phone_1 = models.CharField(
        "Телефон 1 (для посилання tel:)", max_length=30, default="+380976962409",
        help_text="Формат: +380976962409",
    )
    contact_phone_1_display = models.CharField(
        "Телефон 1 (відображення)", max_length=30, default="097 696 24 09",
    )
    contact_phone_2 = models.CharField(
        "Телефон 2 (для посилання tel:)", max_length=30, default="+380505072334",
        help_text="Формат: +380505072334",
    )
    contact_phone_2_display = models.CharField(
        "Телефон 2 (відображення)", max_length=30, default="050 507 23 34",
    )
    contact_email = models.EmailField("E-mail", default="")
    contact_cta_title = models.CharField("Заголовок CTA-контактів", max_length=100, default="Готові до співпраці")

    # Footer
    footer_copyright = models.CharField(
        "Текст копірайту (без року)", max_length=200,
        default="ФАНЕРА  ДВП · Рівне",
    )

    # Meta
    meta_description = models.CharField("Meta description", max_length=300, default="")

    class Meta:
        verbose_name = "Налаштування сайту"
        verbose_name_plural = "Налаштування сайту"

    def __str__(self) -> str:
        return "Налаштування сайту"

    def save(self, *args, **kwargs) -> None:
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls) -> "SiteSettings":
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ── CMS: Products ────────────────────────────────────────────────────────────

class Product(models.Model):
    """Картка продукту у секції «Продукція»."""

    code = models.CharField("Код (ФК / ФСФ / ДВП…)", max_length=20)
    name = models.CharField("Назва", max_length=200)
    badge_colour = models.CharField("Колір бейджу", max_length=20, choices=BADGE_COLOUR_CHOICES, default="default")
    image = models.ImageField("Фото (завантажити)", upload_to="products/", blank=True, null=True)
    image_static = models.CharField(
        "Шлях до статичного фото (fallback)",
        max_length=200, blank=True,
        help_text="Напр.: img/products/fk.png — використовується якщо не завантажено фото.",
    )
    order = models.PositiveSmallIntegerField("Порядок", default=0)
    is_visible = models.BooleanField("Видимий", default=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
        ordering = ["order"]

    def __str__(self) -> str:
        return f"{self.code} — {self.name}"


class ProductSpec(models.Model):
    """Рядок характеристик продукту."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specs")
    label = models.CharField("Характеристика", max_length=100)
    value = models.TextField("Значення")
    order = models.PositiveSmallIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"
        ordering = ["order"]

    def __str__(self) -> str:
        return f"{self.product.code}: {self.label}"


# ── CMS: Gallery ─────────────────────────────────────────────────────────────

class GalleryImage(models.Model):
    """Фото у секції «Галерея»."""

    image = models.ImageField("Фото (завантажити)", upload_to="gallery/", blank=True, null=True)
    image_static = models.CharField(
        "Шлях до статичного фото (fallback)",
        max_length=200, blank=True,
        help_text="Напр.: img/gallery/fk-1.png — використовується якщо не завантажено фото.",
    )
    alt_text = models.CharField("Alt текст", max_length=200, blank=True)
    caption = models.CharField("Підпис під фото", max_length=200)
    lightbox_caption = models.CharField("Підпис Lightbox", max_length=200, blank=True)
    badge_label = models.CharField("Мітка бейджу", max_length=20, blank=True)
    badge_colour = models.CharField("Колір бейджу", max_length=20, choices=BADGE_COLOUR_CHOICES, default="default")
    order = models.PositiveSmallIntegerField("Порядок", default=0)
    is_visible = models.BooleanField("Видима", default=True)

    class Meta:
        verbose_name = "Фото галереї"
        verbose_name_plural = "Галерея"
        ordering = ["order"]

    def __str__(self) -> str:
        return self.caption


# ── Forms / leads (existing) ─────────────────────────────────────────────────

class CallbackRequest(models.Model):
    """Заявка на зворотний дзвінок."""

    name = models.CharField("Ім'я", max_length=100)
    phone = models.CharField("Телефон", max_length=30)
    message = models.TextField("Повідомлення", blank=True)
    created_at = models.DateTimeField("Отримано", auto_now_add=True)
    is_processed = models.BooleanField("Оброблено", default=False)

    class Meta:
        verbose_name = "Заявка на дзвінок"
        verbose_name_plural = "Заявки на дзвінок"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.name} — {self.phone} ({self.created_at:%d.%m.%Y %H:%M})"


class ContactMessage(models.Model):
    """Повідомлення від клієнта через форму 'Написати'."""

    name = models.CharField("Ім'я", max_length=100)
    email = models.EmailField("E-mail")
    message = models.TextField("Повідомлення")
    created_at = models.DateTimeField("Отримано", auto_now_add=True)
    is_processed = models.BooleanField("Оброблено", default=False)

    class Meta:
        verbose_name = "Повідомлення"
        verbose_name_plural = "Повідомлення"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.name} <{self.email}> ({self.created_at:%d.%m.%Y %H:%M})"
