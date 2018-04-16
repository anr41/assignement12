from locust import HttpLocust, TaskSet, task
from random import randint
import re
import resource

resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))
device_id = "unknown"

class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

    def login(self):
        d1 = randint(0, 9)
        d2 = randint(0, 9)
        d3 = randint(0, 9)
        d4 = randint(0, 9)
        device = "00" + str(d1) + str(d2) + str(d3) + str(d4)
        device = int(device)
        device = hex(device)[2:]
        device = str(device)
        hexDigits = len(device)
        neededDigits = 10 - hexDigits
        finalDevice = "1e"
        for i in range(0, neededDigits):
            finalDevice = str(finalDevice) + str(0)
        finalDevice = finalDevice + device
        username = "user_00" + str(d1) + str(d2) + str(d3) + str(d4)
        self.device_id = finalDevice
        response = self.client.get("/login/?next=/")
        csrftoken = response.cookies.get('csrftoken', '')
        self.client.post("/login/?next=/", {"csrfmiddlewaretoken": csrftoken,
                                            "username": username,
                                            "password": str(d4)+str(d3)+str(d2)+str(d1)+"00_resu"})

    @task(100)
    def load_page(self):
        self.client.get("/")

    @task(80)
    def load_lampiPage(self):
        self.client.get("/lampi")

    @task(75)
    def load_devicePage(self):
        self.client.get("/lampi/device/" + self.device_id)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 10000
