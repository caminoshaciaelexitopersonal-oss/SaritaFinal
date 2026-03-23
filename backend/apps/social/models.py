import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone


class SocialConversation(models.Model):
    class ConversationType(models.TextChoices):
        DIRECT = "direct", "Directo"
        GROUP = "group", "Grupo"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation_type = models.CharField(max_length=20, choices=ConversationType.choices, default=ConversationType.DIRECT)
    title = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="social_conversations_created",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="SocialConversationMember",
        related_name="social_conversations",
    )

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title or f"Conversation {self.id}"


class SocialConversationMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(SocialConversation, on_delete=models.CASCADE, related_name="memberships")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="social_memberships")
    is_admin = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)
    last_seen_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("conversation", "user")
        ordering = ["-joined_at"]

    def __str__(self):
        return f"{self.user_id} in {self.conversation_id}"


class SocialMessage(models.Model):
    class MessageType(models.TextChoices):
        TEXT = "text", "Texto"
        EMOJI = "emoji", "Emoji"
        FILE = "file", "Archivo"
        VOICE = "voice", "Voz"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(SocialConversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="social_messages_sent")
    message_type = models.CharField(max_length=20, choices=MessageType.choices, default=MessageType.TEXT)
    content = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.message_type} by {self.sender_id}"


class SocialAttachment(models.Model):
    class AttachmentType(models.TextChoices):
        IMAGE = "image", "Imagen"
        VIDEO = "video", "Video"
        FILE = "file", "Archivo"
        AUDIO = "audio", "Audio"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.ForeignKey(SocialMessage, on_delete=models.CASCADE, related_name="attachments")
    attachment_type = models.CharField(max_length=20, choices=AttachmentType.choices, default=AttachmentType.FILE)
    file_url = models.URLField()
    mime_type = models.CharField(max_length=100, blank=True)
    size_bytes = models.PositiveBigIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["uploaded_at"]

    def __str__(self):
        return f"{self.attachment_type} {self.id}"


class SocialProfilePreference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="social_preference")
    bio = models.TextField(blank=True)
    interests = models.JSONField(default=list, blank=True)
    preferred_languages = models.JSONField(default=list, blank=True)
    preferred_destinations = models.JSONField(default=list, blank=True)
    visibility_enabled = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Preference {self.user_id}"


class SocialGiftCatalog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    icon_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["price"]

    def __str__(self):
        return f"{self.name} ({self.price})"


class SocialGiftTransaction(models.Model):
    class TransactionStatus(models.TextChoices):
        PENDING = "pending", "Pendiente"
        COMPLETED = "completed", "Completada"
        FAILED = "failed", "Fallida"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="social_gifts_sent")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="social_gifts_received")
    gift = models.ForeignKey(SocialGiftCatalog, on_delete=models.PROTECT, related_name="transactions")
    conversation = models.ForeignKey(
        SocialConversation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="gift_transactions",
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=TransactionStatus.choices, default=TransactionStatus.PENDING)
    external_reference = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender_id} -> {self.receiver_id} ({self.amount})"
