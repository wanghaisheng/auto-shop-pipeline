"""setup script for installing python dependencies in youtube-auto-upload toolkit"""


import subprocess
import time
from setupPL import checkRequirments


def getCookie(
    browserType: str = "firefox",
    proxyserver: str = "",
    channelname: str = "youtube-channel",
    url: str = "www.youtube.com",
):
    if browserType in ["firefox", "webkit", "chromium"]:
        if proxyserver:
            command = (
                "playwright codegen -b "
                + browserType
                # + ' --device "iPhone 12" '
                # + ' --device "iPad Pro 11 landscape" '
                + " --proxy-server "
                + proxyserver
                + " --lang 'en-GB' --save-storage="
                + channelname
                + "-cookie.json "
                + url
            )
        else:
            command = (
                "playwright codegen -b "
                + browserType
                # + ' --device "iPhone 12" '
                + " --lang 'en-GB' --save-storage="
                + channelname
                + "-cookie.json "
                + url
            )
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        print(result)
        if result.returncode:
            print(f"failed to save cookie file:{result.stderr}")
        else:
            print("just check your cookie file", channelname + "-cookie.json")


if __name__ == "__main__":
    checkRequirments()
    sites = [
        "https://mms.pinduoduo.com/goods/category"
    ]
# channelname is your account name or something else
# for youtube
getCookie(browserType='chromium',
        #   proxyserver='socks5://127.0.0.1:1080',
          channelname='',url=sites[0])
