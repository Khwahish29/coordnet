import uuid

from django.db import models

from utils import managers

try:
    from django_stubs_ext.db.models import TypedModelMeta
except ImportError:
    # Django-Stubs is not installed in production, since it is only used for
    # type checking.
    TypedModelMeta = object  # type: ignore[misc,assignment]

SOFT_DELETION_FIELD_NAME = "is_removed"


class BaseModel(models.Model):
    """
    Base model for all models in the project.

    This model provides the following fields:
    - public_id: UUID field that is used as the primary key in the API.
    - created_at: DateTime field that is set to the current time when the object is created.
    - updated_at: DateTime field that is set to the current time when the object is updated.
    """

    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(TypedModelMeta):
        abstract = True
        indexes = [models.Index(fields=["public_id"])]


class SoftDeletableBaseModel(BaseModel):
    """
    Base model for all soft-deletable models in the project.

    This model provides the following fields:
    - public_id: UUID field that is used as the primary key in the API.
    - created_at: DateTime field that is set to the current time when the object is created.
    - updated_at: DateTime field that is set to the current time when the object is updated.
    - is_removed: Boolean field that is used to soft-delete objects, this is provided by
                  `SoftDeletableModel`.

    TODO: pgtrigger also supports soft-deletion, either add it or replace model_utils.
    """

    is_removed = models.BooleanField(default=False)

    objects = managers.SoftDeletableUnfilteredManager()
    available_objects = managers.SoftDeletableManager()
    all_objects = models.Manager()

    def delete(  # type: ignore[override]
        self, using: str | None = None, soft: bool = True, keep_parents: bool = False
    ) -> tuple[int, dict[str, int]] | None:
        """
        Soft delete object (set its ``is_removed`` field to True).
        Actually delete object if setting ``soft`` to False.
        TODO: - collect and return the number of objects deleted even for a soft delete.
        """
        if soft:
            self.is_removed = True
            self.save(using=using, update_fields=["is_removed"])
            return None
        else:
            return super().delete(using=using, keep_parents=keep_parents)

    class Meta(TypedModelMeta):
        abstract = True
        indexes = [models.Index(fields=["public_id"])]
