from android_utils import get_screen_shoot


class JumpGame:
    def __init__(self):
        self.status = []

    def get_status(self):
        self.status = get_screen_shoot()

    def action(self):
        pass

    def get_reward(self):
        pass

    def check_is_over(self):
        pass
