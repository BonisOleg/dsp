from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline

from .models import (
    CallbackRequest,
    ContactMessage,
    GalleryImage,
    Product,
    ProductSpec,
    SiteSettings,
)


# ── Actions ───────────────────────────────────────────────────────────────────

@admin.action(description="Позначити як оброблені")
def mark_processed(modeladmin, request, queryset):
    queryset.update(is_processed=True)


@admin.action(description="Зняти позначку «оброблено»")
def mark_unprocessed(modeladmin, request, queryset):
    queryset.update(is_processed=False)


# ── CMS: SiteSettings (Singleton) ────────────────────────────────────────────

@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    compressed_fields = True

    fieldsets = (
        ("Хедер", {
            "fields": ("header_name", "header_tagline", "header_phone"),
        }),
        ("Hero-секція", {
            "fields": ("hero_title", "hero_subtitle"),
        }),
        ("Секція «Про нас»", {
            "fields": (
                "about_year", "about_experience", "about_product_count",
                "about_text_1", "about_text_2",
            ),
        }),
        ("CTA-банер", {
            "fields": ("cta_title", "cta_description"),
        }),
        ("Контакти", {
            "fields": (
                "contact_address",
                "contact_phone_1", "contact_phone_1_display",
                "contact_phone_2", "contact_phone_2_display",
                "contact_email", "contact_cta_title",
            ),
        }),
        ("Футер", {
            "fields": ("footer_copyright",),
        }),
        ("Заголовки секцій", {
            "fields": (
                "section_about_title",
                "section_products_title",
                "section_gallery_title",
                "section_contacts_title",
            ),
        }),
        ("Статистика — мітки", {
            "fields": ("stat_year_label", "stat_experience_label", "stat_products_label"),
        }),
        ("Кнопки та CTA", {
            "fields": ("cta_btn_label",),
        }),
        ("SEO", {
            "fields": ("page_title", "meta_description"),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj, _ = SiteSettings.objects.get_or_create(pk=1)
        return self.change_view(request, str(obj.pk), extra_context=extra_context)


# ── CMS: Products ─────────────────────────────────────────────────────────────

class ProductSpecInline(TabularInline):
    model = ProductSpec
    extra = 1
    fields = ("label", "value", "order")
    ordering = ("order",)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    compressed_fields = True
    list_display = ("code", "name", "badge_colour", "image_preview_thumb", "order", "is_visible")
    list_editable = ("order", "is_visible")
    list_filter = ("is_visible", "badge_colour")
    search_fields = ("code", "name")
    inlines = [ProductSpecInline]
    readonly_fields = ("image_preview_large",)
    fieldsets = (
        ("Основне", {
            "fields": ("code", "name", "badge_colour", "order", "is_visible"),
        }),
        ("Фото", {
            "fields": ("image_preview_large", "image", "image_static"),
            "description": (
                "Завантажте нове фото або залиште поле порожнім — тоді відображатиметься "
                "стандартне статичне фото з поля «Шлях до статичного фото»."
            ),
        }),
    )

    @admin.display(description="Фото")
    def image_preview_thumb(self, obj: Product) -> str:
        if obj.image:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;">', obj.image.url)
        if obj.image_static:
            return format_html('<span style="color:#aaa;font-size:11px">static</span>')
        return "—"

    @admin.display(description="Поточне фото")
    def image_preview_large(self, obj: Product) -> str:
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:220px;max-width:100%;border-radius:6px;'
                'box-shadow:0 2px 8px rgba(0,0,0,.15);">',
                obj.image.url,
            )
        if obj.image_static:
            from django.templatetags.static import static
            return format_html(
                '<img src="{}" style="max-height:220px;max-width:100%;border-radius:6px;'
                'box-shadow:0 2px 8px rgba(0,0,0,.15);opacity:.8;" title="Статичне фото (fallback)">',
                static(obj.image_static),
            )
        return format_html('<span style="color:#aaa">Фото не завантажено</span>')


# ── CMS: Gallery ──────────────────────────────────────────────────────────────

@admin.register(GalleryImage)
class GalleryImageAdmin(ModelAdmin):
    compressed_fields = True
    list_display = ("caption", "badge_label", "badge_colour", "image_preview_thumb", "order", "is_visible")
    list_editable = ("order", "is_visible")
    list_filter = ("is_visible", "badge_colour")
    search_fields = ("caption", "badge_label", "alt_text")
    readonly_fields = ("image_preview_large",)
    fieldsets = (
        ("Фото", {
            "fields": ("image_preview_large", "image", "image_static"),
            "description": (
                "Натисніть «Обрати файл» щоб завантажити нове фото. "
                "Після збереження воно одразу відобразиться на сайті. "
                "Поле «Шлях до статичного фото» — резервне, якщо завантаженого фото немає."
            ),
        }),
        ("Підписи та мітки", {
            "fields": ("caption", "lightbox_caption", "alt_text", "badge_label", "badge_colour"),
        }),
        ("Відображення", {
            "fields": ("order", "is_visible"),
        }),
    )

    @admin.display(description="Фото")
    def image_preview_thumb(self, obj: GalleryImage) -> str:
        if obj.image:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;">', obj.image.url)
        if obj.image_static:
            return format_html('<span style="color:#aaa;font-size:11px">static</span>')
        return "—"

    @admin.display(description="Поточне фото")
    def image_preview_large(self, obj: GalleryImage) -> str:
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:260px;max-width:100%;border-radius:6px;'
                'box-shadow:0 2px 8px rgba(0,0,0,.15);">',
                obj.image.url,
            )
        if obj.image_static:
            from django.templatetags.static import static
            return format_html(
                '<img src="{}" style="max-height:260px;max-width:100%;border-radius:6px;'
                'box-shadow:0 2px 8px rgba(0,0,0,.15);opacity:.8;" title="Статичне фото (fallback)">',
                static(obj.image_static),
            )
        return format_html('<span style="color:#aaa">Фото не завантажено</span>')


# ── Leads ──────────────────────────────────────────────────────────────────────

@admin.register(CallbackRequest)
class CallbackRequestAdmin(ModelAdmin):
    list_display = ("name", "phone", "short_message", "created_at", "is_processed")
    list_filter = ("is_processed",)
    search_fields = ("name", "phone", "message")
    list_editable = ("is_processed",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
    actions = [mark_processed, mark_unprocessed]

    @admin.display(description="Повідомлення")
    def short_message(self, obj: CallbackRequest) -> str:
        if not obj.message:
            return "—"
        text = obj.message[:60]
        return format_html("{}{}", text, "…" if len(obj.message) > 60 else "")


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ("name", "email", "short_message", "created_at", "is_processed")
    list_filter = ("is_processed",)
    search_fields = ("name", "email", "message")
    list_editable = ("is_processed",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
    actions = [mark_processed, mark_unprocessed]

    @admin.display(description="Повідомлення")
    def short_message(self, obj: ContactMessage) -> str:
        text = obj.message[:60]
        return format_html("{}{}", text, "…" if len(obj.message) > 60 else "")
