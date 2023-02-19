from speedtest import SpeedTest
from twitter import Twitter

speed_test = SpeedTest()
message = speed_test.share_text(100)
speed_test.close()

t = Twitter()
t.login()
t.send_message(message)
t.close()

