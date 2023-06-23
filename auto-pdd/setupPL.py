"""setup script for installing python dependencies in youtube-auto-upload toolkit"""


import subprocess
import time


def checkPLInstalled():
    print("start to check Tiktoka Studio requirements whether playwright intalled")

    try:
        from playwright.sync_api import Page, expect, sync_playwright

        return True
    except ImportError as error:
        print(error, ":( not found")
        return False


def checkBrowserInstalled():
    try:
        print(
            "start to check Tiktoka Studio requirements whether playwright browser intalled"
        )
        from playwright.sync_api import sync_playwright

        print("import pl library")

        with sync_playwright() as p:
            print("initial pl library")

            try:
                print(
                    "start to check Tiktoka Studio requirements whether chromium intalled"
                )
                chromium_browser = p.chromium.launch()
                print(
                    "start to check Tiktoka Studio requirements whether webkit/edge intalled"
                )
                webkit_browser = p.webkit.launch()

                print(
                    "start to check Tiktoka Studio requirements whether firefox intalled"
                )

                firefox_browser = p.firefox.launch()

                return True

            except:
                return False

    except:
        return False


def attempt(arg_list, max_attempts=1, name=""):
    retries = 0
    while retries < max_attempts:
        proc = subprocess.Popen(arg_list)

        # Keep running until finish or failure (may hang)
        while proc.poll() is None:
            time.sleep(0.1)

        # Proc finished, check for valid return code
        if proc.returncode == 0:
            print(f"\n[INSTALL_PYDEPS] SUCCESS for process '{name}'\n")
            break
        else:
            # Likely failure, retry
            print(f"\n[INSTALL_PYDEPS] FAILURE for process '{name}', retrying!\n")
            retries += 1
    else:
        # Retries exceeded
        raise Exception(f"[INSTALL_PYDEPS] Retries exceeded for proc '{name}'!")


def runPl():
    steps = {
        "step1": """python -m pip install -U pip setuptools wheel""".split(" "),
        "step2": """pip install pytest-playwright""".split(" "),
    }

    for step_name, step_arglist in steps.items():
        print(
            f"\n[INSTALL_PYDEPS] Attempt '{step_name}' -> Run '{' '.join(step_arglist)}'\n"
        )
        attempt(step_arglist, max_attempts=3, name=step_name)


def runBrowser():
    steps = {
        "step1": """playwright install""".split(" "),
    }

    for step_name, step_arglist in steps.items():
        print(
            f"\n[INSTALL_PYDEPS] Attempt '{step_name}' -> Run '{' '.join(step_arglist)}'\n"
        )
        attempt(step_arglist, max_attempts=3, name=step_name)


def checkRequirments():
    print("start to check Tiktoka Studio requirements whether  intalled")

    plinstall = checkPLInstalled()
    browserinstall = checkBrowserInstalled()
    if plinstall == False:
        print("Tiktoka Studio requirements-playwright not intalled")

        runPl()
    else:
        print("Tiktoka Studio requirements-playwright have intalled")
    if browserinstall == False:
        print("Tiktoka Studio requirements-browser not intalled")

        runBrowser()
        print("Tiktoka Studio requirements-auto browser intalled")

    else:
        print("Tiktoka Studio requirements-browser have intalled")