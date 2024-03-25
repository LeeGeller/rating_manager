import math
from collections import defaultdict


class Employer:
    employers_list = []

    def __init__(self, name: str, calls: int, work_day: int, purchase: int, promotions: int, registrations: int,
                 refill: int, ident: int, ok: int):
        self.name = name
        self.calls = int(calls)
        self.work_day = int(work_day)
        self.purchase = float(purchase)
        self.promotions = int(promotions)
        self.registrations = int(registrations)
        self.refill = int(refill)
        self.ident = int(ident)
        self.ok = ok
        self.average_count_of_calls()
        self.get_info_about_overfulfillment()
        self.get_all_conversion()

    def __repr__(self):
        return (f"Сотрудник: {self.name}\n"
                f"Количество звонков: {self.calls}\n"
                f"Рабочих дней: {self.work_day}\n"
                f"Покупка (часы): {self.purchase}\n"
                f"Заявки по акциям: {self.promotions}\n"
                f"Заявки по регам: {self.registrations}\n"
                f"Пополнения: {self.refill}\n"
                f"Прошли идент: {self.ident}\n"
                f"Оценка качества: {self.ok}\n"
                f"Среднее количество звонков: {self.avg_calls}\n"
                f"Перевыполнение: {self.overfulfillment}%\n"
                f"Конверсия акции: {self.conv_promotion}%\n"
                f"Конверсия регистрации: {self.conv_registration}%\n")

    @classmethod
    def add_employers_to_list(cls, employers: list) -> None:
        for employer in employers:
            cls.employers_list.append(cls(*employer.values()))

    def average_count_of_calls(self):
        avg_calls = self.calls / (self.work_day - self.purchase)
        self.avg_calls = math.ceil(avg_calls)
        return self.avg_calls

    def get_info_about_overfulfillment(self):
        min_works_day = self.promotions / 500 + self.registrations / 350
        time_spent = (self.work_day - self.purchase) / min_works_day

        applications = self.promotions + self.registrations
        overfulfillment_calls = self.calls / applications

        overfulfillment = (overfulfillment_calls - time_spent) * 100
        self.overfulfillment = math.ceil(overfulfillment)
        return self.overfulfillment

    def get_conversion(self, target_action, application):
        try:
            percent = target_action / application * 100
        except:
            percent = 0
        return round(percent, 2)

    def get_all_conversion(self):
        self.conv_promotion = self.get_conversion(self.refill, self.promotions)
        self.conv_registration = self.get_conversion(self.ident, self.registrations)

    def get_employer_dict(self):
        return {'Оператор': self.name, 'Количество звонков': self.calls, 'Среднее количество звонков': self.avg_calls,
                'Перевыполнение': self.overfulfillment, 'Пополнения': self.refill, 'Прошли идент': self.ident,
                'Оценка качества': self.ok, 'Конверсия акции': str(self.conv_promotion),
                'Конверсия регистрации': str(self.conv_registration)}
