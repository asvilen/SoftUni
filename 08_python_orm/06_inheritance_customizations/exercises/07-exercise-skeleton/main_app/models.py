from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class BaseCharacter(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100)
    description = models.TextField()


class Mage(BaseCharacter):
    elemental_power = models.CharField(max_length=100)
    spellbook_type = models.CharField(max_length=100)


class Assassin(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    assassination_technique = models.CharField(max_length=100)


class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    demon_slaying_ability = models.CharField(max_length=100)


class TimeMage(Mage):
    time_magic_mastery = models.CharField(max_length=100)
    temporal_shift_ability = models.CharField(max_length=100)


class Necromancer(Mage):
    raise_dead_ability = models.CharField(max_length=100)


class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(max_length=100)
    venomous_bite_ability = models.CharField(max_length=100)


class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(max_length=100)


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(max_length=100)
    retribution_ability = models.CharField(max_length=100)


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(max_length=100)


class UserProfile(models.Model):
    username = models.CharField(
        max_length=70,
        unique=True,
    )
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)


class Message(models.Model):
    sender = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    receiver = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True

    def reply_to_message(self, reply_content: str):
        message = Message(
            sender=self.receiver,
            receiver=self.sender,
            content=reply_content,
        )

        message.save()
        return message

    def forward_message(self, receiver: UserProfile):
        message = Message(
            sender=self.receiver,
            receiver=receiver,
            content=self.content,
        )
        message.save()
        return message


class StudentIDField(models.PositiveIntegerField):
    def to_python(self, id_number):
        try:
            return int(id_number)
        except ValueError:
            raise ValueError(
                "Invalid input for student ID"
            )

    def get_prep_value(self, id_number):
        cleaned_id = self.to_python(id_number)

        if cleaned_id <= 0:
            raise ValidationError("ID cannot be less than or equal to zero")

        return cleaned_id


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = StudentIDField()


class MaskedCreditCardField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super().__init__(*args, **kwargs)

    def to_python(self, card_number):
        if not isinstance(card_number, str):
            raise ValidationError(
                "The card number must be a string"
            )
        if not card_number.isdigit():
            raise ValidationError(
                "The card number must contain only digits"
            )
        if len(card_number) != 16:
            raise ValidationError(
                "The card number must be exactly 16 characters long"
            )
        return f"****-****-****-{card_number[-4:]}"

    def get_prep_value(self, card_number):
        return self.to_python(card_number)


class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField()

