from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Book, Chapter, Illustration

@receiver(m2m_changed, sender=Book.tags.through)
def limit_book_tags(sender, instance, action, pk_set, **kwargs):
    """
    限制每本书最多只能绑定 6 个标签。
    适用于所有途径：API、Django Admin、ORM。
    """
    if action == "pre_add":
        current_count = instance.tags.count()
        add_count = len(pk_set)
        
        # 如果当前数量 + 准备新增的数量超过 6，则抛出验证错误
        if current_count + add_count > 6:
            raise ValidationError(f"一本书最多只能绑定 6 个标签！当前已有 {current_count} 个，尝试新增 {add_count} 个。")

@receiver(post_delete, sender=Book)
def auto_delete_cover_on_delete(sender, instance, **kwargs):
    """
    删除书籍时，自动删除 media 目录下的封面文件
    """
    if instance.cover:
        instance.cover.delete(save=False)

@receiver(post_save, sender=Chapter)
def update_word_count_on_save(sender, instance, created, **kwargs):
    """
    监听章节的保存事件 (post_save)
    保存章节时，增加书籍总字数。
    """
    if created:
        instance.book.word_count += len(instance.content)
        instance.book.save(update_fields=['word_count'])

@receiver(post_delete, sender=Chapter)
def update_word_count_on_delete(sender, instance, **kwargs):
    """
    监听章节的删除事件 (post_delete)
    删除章节时，减少书籍总字数。
    """
    book = instance.book
    if book.id: # 确保书籍实体还没被级联删除销毁
        book.word_count = max(0, book.word_count - len(instance.content))
        book.save(update_fields=['word_count'])

@receiver(post_save, sender=Illustration)
def update_illustration_count_on_save(sender, instance, created, **kwargs):
    """监听插图的新增"""
    if created:
        instance.book.illustration_count += 1
        instance.book.save(update_fields=['illustration_count'])

@receiver(post_delete, sender=Illustration)
def update_illustration_count_on_delete(sender, instance, **kwargs):
    """监听插图的删除"""
    book = instance.book
    if instance.image:
        instance.image.delete(save=False)
    if book.id:
        book.illustration_count = max(0, book.illustration_count - 1)
        book.save(update_fields=['illustration_count'])