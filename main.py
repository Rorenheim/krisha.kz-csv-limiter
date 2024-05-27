import json
import logging
import sys
from logging.config import fileConfig
import scr.config as cfg
import scr.misc.msg as msg
from scr.crawler import run_crawler, get_response
from scr.first_page import FirstPage

fileConfig("logging.ini")
logger = logging.getLogger()

def main(max_urls) -> None:
    try:
        get_response(cfg.HOME_URL)
        url: str = FirstPage.get_url(**search_params)
        run_crawler(url, max_urls)
    except Exception as error:
        logger.critical(msg=error, exc_info=True)
        sys.exit()

if __name__ == "__main__":
    try:
        with open(cfg.SEARCH_PARAMS_FILE) as file:
            search_params: dict = json.load(file)
            if "rooms" in search_params:
                search_params["rooms"] = tuple(search_params["rooms"])
    except IOError as error:
        logger.warning(msg.READ_SEARCH_PARAMS_ERROR.format(error))
        search_params: dict = {}

    if len(sys.argv) > 1:
        max_urls = int(sys.argv[1])
    else:
        max_urls = 4  # Default limit if not provided

    main(max_urls)
