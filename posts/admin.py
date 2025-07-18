from django.contrib import admin

from posts.models import AdsTxt, Contact, Post, PostCategory, PostComments, RobotsTxt, Subscribe

# Register your models here.


class PostComponentsInline(admin.StackedInline):
    model = PostComments
    classes = ("collapse",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        # "seo_title",
        # "seo_description",
        "slug",
        "image",
        "created",
        "updated",
    )
    list_display_links = (
        "title",
        "slug",
    )
    readonly_fields = (
        "created",
        "updated",
    )
    search_fields = (
        "title",
        "slug",
        "created",
        "updated",
    )
    prepopulated_fields = {"slug": ("title",)}
    list_filter = (
        "created",
        "updated",
    )
    list_editable = (
        "status",
        # "seo_title",
        # "seo_description",
        "image",
    )
    exclude = ("user",)
    inlines = [
        PostComponentsInline,
    ]

    def save_model(self, request, obj, form, change):
        if not change or not obj.user_id:
            obj.user = request.user
        return super().save_model(request, obj, form, change)


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "created",
        "updated",
    )
    list_display_links = (
        "name",
        "slug",
    )
    readonly_fields = (
        "created",
        "updated",
    )
    search_fields = (
        "name",
        "slug",
        "created",
        "updated",
    )
    prepopulated_fields = {"slug": ("name",)}
    list_filter = (
        "created",
        "updated",
    )


@admin.register(PostComments)
class PostCommentsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "updated",
    )
    readonly_fields = (
        "created",
        "updated",
    )
    search_fields = (
        "id",
        "created",
        "updated",
    )
    list_filter = (
        "created",
        "updated",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "created",
        "updated",
    )
    list_display_links = (
        "name",
        "email",
    )
    readonly_fields = (
        "created",
        "updated",
    )
    search_fields = (
        "name",
        "email",
        "message",
        "created",
        "updated",
    )
    list_filter = (
        "created",
        "updated",
    )


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "created",
        "updated",
    )
    list_display_links = (
        "name",
        "email",
    )
    readonly_fields = (
        "created",
        "updated",
    )
    search_fields = (
        "name",
        "email",
        "created",
        "updated",
    )
    list_filter = (
        "created",
        "updated",
    )


@admin.register(RobotsTxt)
class RobotsTxtAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created",
        "updated",
    )
    list_display_links = ("title",)
    readonly_fields = (
        "created",
        "updated",
    )
    search_fields = (
        "title",
        "created",
        "updated",
    )
    list_filter = (
        "created",
        "updated",
    )


@admin.register(AdsTxt)
class AdsTxtAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created",
        "updated",
    )
    list_display_links = ("title",)
    readonly_fields = (
        "created",
        "updated",
    )
    search_fields = (
        "title",
        "created",
        "updated",
    )
    list_filter = (
        "created",
        "updated",
    )
