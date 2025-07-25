from django.db import models

# Create your models here.


class CoreModel(models.Model):
  """
  INFO: This Model was develop for sorting the information, just add this format into the top of your model.
  order = "your_column_name"
  """

  order = "id"

  class Meta:
    abstract = True

  def __init_subclass__(cls, **kwargs):
    super().__init_subclass__(**kwargs)

    if not hasattr(cls, "Meta"):

      class Meta:
        pass

      cls.Meta = Meta

      if not hasattr(cls.Meta, "ordering"):
        cls.Meta.ordering = [f"{cls.order}"]


class CoreModelDescending(models.Model):
  """
  INFO: This Model was develop for sorting the information in descending order, just add this format into the top of your model.
  order = "your_column_name"
  """

  order = "id"

  class Meta:
    abstract = True

  def __init_subclass__(cls, **kwargs):
    super().__init_subclass__(**kwargs)
    if not hasattr(cls, "Meta"):

      class Meta:
        pass

      cls.Meta = Meta
    if not hasattr(cls.Meta, "ordering"):
      cls.Meta.ordering = [f"-{cls.order}"]
