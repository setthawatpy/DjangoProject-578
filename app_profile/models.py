from django.db import models
from decimal import Decimal
# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=255, unique=True)               # ชื่อสินค้า 
    description = models.TextField(blank=True)                          # รายละเอียดสินค้า
    stock = models.IntegerField()                                       # จำนวนสินค้า
    weight = models.DecimalField(max_digits=10, decimal_places=2)       # น้ำหนักทอง
    price = models.DecimalField(max_digits=10, decimal_places=2)        # ราคา
    discount = models.DecimalField(max_digits=10, decimal_places=2)     # ค่ากำเหน็ด
    delivery = models.DecimalField(max_digits=10, decimal_places=2)     # ค่ากำเหน็ด
    available = models.BooleanField(default=True)                       # สถานะสินค้า
    create_datetime = models.DateTimeField(auto_now_add=True)           # วันที่เพิ่มสินค้า
    update_datetime = models.DateTimeField(auto_now=True)               # วันที่อัพเดทสินค้า
    picture = models.ImageField(upload_to='products/')                 # รูปภาพ
    

    def get_discount(self):
        if self.price > Decimal('1000'):
            self.discount = self.price * Decimal('0.15')   # ส่วนลด 15%
        elif self.price > Decimal('500'):
            self.discount = self.price * Decimal('0.10')   # ส่วนลด 10%
        elif self.price > Decimal('300'):
            self.discount = self.price * Decimal('0.05')   # ส่วนลด 5%
        else:
            self.discount = ('0')

    def get_sum(self):
        return self.price - self.discount
    
    def get_delivery(self):
        if self.get_sum() > 2000:
            self.delivery = 100
        else:
            self.delivery = 0
    
    def get_net(self):
        sum_value = self.get_sum()
        delivery_value = self.get_delivery()
        if sum_value is not None and delivery_value is not None:
            return int(sum_value) + int(delivery_value)
        else:
            return None  # หรือค่าที่เหมาะสมในกรณีที่ค่าเป็น None



