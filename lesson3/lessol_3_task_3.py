from address import Address
from mailing import Mailing

to_address = Address(
    index="190000",
    city="Санкт-Петербург",
    street="Невский",
    house="28",
    apartment="10"
)
from_address = Address(
    index="101000",
    city="Москва",
    street="Тверская",
    house="15",
    apartment="42"
)

my_mail = Mailing(to_address=to_address, from_address=from_address,
                  cost=500, track="A6790330300")

print(f"Отправление <{my_mail.track}> из <{my_mail.from_address.index}>, "
      f"<{my_mail.from_address.city}>, <{my_mail.from_address.street}>, "
      f"<{my_mail.from_address.house}>, <{my_mail.from_address.apartment}>, "
      f"в <{my_mail.to_address.index}>, <{my_mail.to_address.city}>, "
      f"<{my_mail.to_address.street}>, <{my_mail.to_address.house}>, "
      f"<{my_mail.to_address.apartment}>. Стоимость <{my_mail.cost}> рублей")
