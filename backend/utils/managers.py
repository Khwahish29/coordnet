"""
The soft delete managers in this file are copied from model_utils, because their version wasn't
playing nicely with mypy.
"""

import warnings

from django.db import models


class SoftDeletableQuerySet(models.QuerySet):
    """
    QuerySet for SoftDeletableModel. Instead of removing instance sets
    its ``is_removed`` field to True.
    """

    def delete(self) -> None:  # type: ignore[override]
        """
        Soft delete objects from queryset (set their ``is_removed`` field to True)
        TODO: - Collect and return the number of objects deleted even for a soft delete.
              - Allow for hard delete.
        """
        self.update(is_removed=True)


class SoftDeletableManager(models.Manager):
    """
    Manager that limits the queryset by default to show only not removed
    instances of model.
    """

    _queryset_class = SoftDeletableQuerySet

    def __init__(self, _emit_deprecation_warnings: bool = False):
        self.emit_deprecation_warnings = _emit_deprecation_warnings
        super().__init__()

    def get_queryset(self) -> models.QuerySet:
        """
        Return queryset limited to not removed entries.
        """

        if self.emit_deprecation_warnings:
            warning_message = (
                "{0}.objects model manager will include soft-deleted objects in an "
                "upcoming release; please use {0}.available_objects to continue "
                "excluding soft-deleted objects. See "
                "https://django-model-utils.readthedocs.io/en/stable/models.html"
                "#softdeletablemodel for more information."
            ).format(self.model.__class__.__name__)
            warnings.warn(warning_message, DeprecationWarning, stacklevel=1)

        return self._queryset_class(
            model=self.model, using=self._db, hints=getattr(self, "_hints", None)
        ).filter(is_removed=False)
