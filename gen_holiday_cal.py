from datetime import date
import holidays
from holidays.countries import US
import ephem
from icalendar import Calendar, Event
import argparse

class KelsonHomeHolidays(US):
    def _populate(self, year):
        super()._populate(year)

        self._add_palm_sunday("Palm Sunday")
        self._add_good_friday("Good Friday")
        self._add_easter_sunday("Resurrection Sunday")

        self._add_christmas_eve_holiday()
        self._add_new_years_eve("New Year's Eve")

        self._add_holiday_oct_31("Reformation Day")

        self._add_holiday_2nd_sun_of_may("Mother's Day")
        self._add_holiday_3rd_sun_of_jun("Father's Day")

        self._add_holiday_jun_6("D-Day")
        self._add_holiday_jun_14("Flag Day")
        self._add_holiday_dec_7("Pearl Harbor Day")
        self._add_world_war_two_victory_day("Victory Day")

        # Roe v. Wade was overturned on June 24, 2022
        if self._year >= 2022:
            self._add_holiday_jun_24("National Celebrate Life Day")

        self._add_holiday_1_day_past_4th_thu_of_nov("Lincoln's Birthday")

        # Inauguration Day
        if self._year >= 1789 and (self._year - 1789) % 4 == 0:
            name = "Inauguration Day"
            self._add_observed(
                self._add_holiday_jan_20(name)
                if self._year >= 1937
                else self._add_holiday_mar_4(name),
                rule=holidays.observed_holiday_base.SUN_TO_NEXT_MON,
            )

        self._add_holiday_mar_14("Pi Day")
        
        jan_1 = date(year=year, month=1, day=1)
        self._add_holiday("Spring Equinox", ephem.next_spring_equinox(jan_1).datetime())
        self._add_holiday("Summer Solstice", ephem.next_summer_solstice(jan_1).datetime())
        self._add_holiday("Fall Equinox", ephem.next_fall_equinox(jan_1).datetime())
        self._add_holiday("Winter Solstice", ephem.next_winter_solstice(jan_1).datetime())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a custom Holiday Calendar iCal file.")
    parser.add_argument("year", type=int)
    args = parser.parse_args()

    kelson_holidays = KelsonHomeHolidays(years=args.year, categories=(holidays.PUBLIC, holidays.UNOFFICIAL)) 

    cal = Calendar()

    for dt, names in sorted(kelson_holidays.items()):
        for name in names.split("; "):
            event = Event()
            event.add('summary', name)
            event.add('dtstart', dt)
            cal.add_component(event)

    with open(f"holidays_{dt.year}.ics", "wb") as f:
        f.write(cal.to_ical())