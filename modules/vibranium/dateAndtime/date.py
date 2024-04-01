from datetime import datetime


class CurrentDateTeller:
    @staticmethod
    def tell_date():
        current_date = datetime.now()
        # Day of the week, day of the month, year
        res = current_date.strftime("%A, %B %d, %Y")
        print(res)
        return res
