from helpers import android_helper


class JumpGame:
    def __init__(self):
        self.status = []

    def get_status(self):
        self.status = android_helper.get_screen_shoot()

    def action(self):
        pass

    def get_reward(self):
        pass

    def check_is_over(self):
        pass
