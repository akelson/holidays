from datetime import date
import holidays
from holidays.countries import US

class KelsonHomeHolidays(US):
    def _populate(self, year):
        super()._populate(year)

        self._add_palm_sunday("Palm Sunday")
        self._add_good_friday("Good Friday")
        self._add_easter_sunday("Resurrection Sunday")

        # Christmas and New Year's Eve
        self._add_christmas_eve_holiday()
        self._add_new_years_eve("New Year's Eve")

        self._add_holiday_oct_31("Reformation Day")

        self._add_holiday_2nd_sun_of_may("Mother's Day")
        self._add_holiday_3rd_sun_of_jun("Father's Day")

        self._add_holiday_jun_6("D-Day")
        self._add_holiday_jun_14("Flag Day")
        self._add_holiday_dec_7("Pearl Harbor Day")
        self._add_world_war_two_victory_day("Victory Day")

        if self._year >= 2022:
            self._add_holiday_jun_24("National Celebrate Life Day")

        # Lincoln's Birthday
        if self._year >= 2010:
            self._add_holiday_1_day_past_4th_thu_of_nov("Lincoln's Birthday")

        # Inauguration Day
        if self._year >= 1789 and (self._year - 1789) % 4 == 0:
            name = "Inauguration Day"
            self._add_observed(
                self._add_holiday_jan_20(name)
                if self._year >= 1937
                else self._add_holiday_mar_4(name),
                rule=holidays.SUN_TO_NEXT_MON,
            )

kelson_holidays = KelsonHomeHolidays(years=2024, categories=(holidays.PUBLIC, holidays.UNOFFICIAL)) 

for dt, name in sorted(kelson_holidays.items()):
    print(dt, name)