import requests
import bs4


class SiteMeta:
    def __init__(self):
        self.prepared_site_page = None
        self._null_found_meta()

    def _null_found_meta(self):
        self.twitter = None

    def get_twitter_meta(self):
        if self.prepared_site_page is None:
            return self.twitter

        if self.twitter is not None:
            return self.twitter

        self.twitter = {}

        tag = self.prepared_site_page.find("meta", {"name": "twitter:card"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["card"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:site"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["site"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:site:id"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["site:id"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:creator"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["creator"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:creator:id"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["creator:id"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:description"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["description"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:title"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["title"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:image"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["image"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:image:alt"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["image:alt"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:player"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["player"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:player:width"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["player:width"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:player:height"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["player:height"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:player:stream"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["player:stream"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:app:name:iphone"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["app:name:iphone"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:app:id:iphone"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["app:id:iphone"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:app:url:iphone"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["app:url:iphone"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:app:name:ipad"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["app:name:ipad"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:app:id:ipad"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["app:id:ipad"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:app:url:ipad"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["app:url:ipad"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:app:name:googleplay"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["app:name:googleplay"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:app:id:googleplay"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["app:id:googleplay"] = tag.attrs["content"]
        tag = self.prepared_site_page.find("meta", {"name": "twitter:app:url:googleplay"})
        if tag is not None and "content" in tag.attrs:
            self.twitter["app:url:googleplay"] = tag.attrs["content"]

        return self.twitter

    def get_facebook_meta(self):
        return self.get_og_meta()

    def get_vk_meta(self):
        if self.prepared_site_page is None:
            return {}

    def get_basic_meta(self):
        if self.prepared_site_page is None:
            return {}

    def get_og_meta(self):
        if self.prepared_site_page is None:
            return {}

    def get_dc_meta(self):
        if self.prepared_site_page is None:
            return {}

    def load_site(self, method, url, **kwargs):
        self._null_found_meta()

        try:
            response = requests.request(method, url, **kwargs)

            if response.status_code != 200:
                return False

            self.prepared_site_page = bs4.BeautifulSoup(response.text, "html.parser")
        except:
            return False

        return True