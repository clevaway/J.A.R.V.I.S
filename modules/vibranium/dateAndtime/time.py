from datetime import datetime


class CurrentTimeTeller:
    @staticmethod
    def tell_time():
        current_time = datetime.now()
        res = current_time.strftime("%I:%M %p")  # 12-hour clock format
        print(res)
        return res
