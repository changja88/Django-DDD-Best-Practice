from django.db import models


class AddressLevel1Entity(models.Model):
    name = models.CharField("도/광역시", max_length=16, blank=False, null=False)
    order = models.PositiveIntegerField("노출 순위", blank=False, null=True)

    class Meta:
        app_label = "address"
        db_table = "address_level1"
        verbose_name = "[address_level1] 1단계 주소 정보 - 도/광역시/특별시"
        verbose_name_plural = "[address_level1] 1단계 주소 정보 - 도/광역시/특별시"

    def __str__(self) -> str:
        return f"[id: {self.id}] [name: {self.name}]"
