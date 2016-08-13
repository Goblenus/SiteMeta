import requests
import bs4


class SiteMeta:
    def __init__(self):
        self.prepared_site_page = None

    def get_twitter_meta(self):
        if self.prepared_site_page is None:
            return {}

    def get_facebook_meta(self):
        if self.prepared_site_page is None:
            return {}

    def get_vk_meta(self):
        if self.prepared_site_page is None:
            return {}

    def get_basic_meta(self):
        if self.prepared_site_page is None:
            return {}

    def load_site(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, **kwargs)

            if response.status_code != 200:
                return False

            self.prepared_site_page = bs4.BeautifulSoup(response.text, "html.parser")
        except:
            return False

        return True