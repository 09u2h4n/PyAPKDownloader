from PyAPKDownloader.apkdownloadertools import ApkDownloaderTools
import requests
from bs4 import BeautifulSoup


class ApkPure:
    def __init__(self) -> None:
        self.apkpure_base_url = "https://apkpure.com/tr/"
        self.apkpure_api_base_url = "https://d.apkpure.com/b/"
        self.headers = ApkDownloaderTools().headers

    def __list_versions(self, url: str):
        lv_res = requests.get(url=url, headers=self.headers)
        lv_data = lv_res.text
        lv_soup = BeautifulSoup(lv_data, "html.parser")
        versions_element_list = lv_soup.find_all("a", class_="ver_download_link")
        return versions_element_list

    def __filter_elements(self, list_elements: list, version: str, extension: str):
        for data in list_elements:
            app_version = data["data-dt-version"]
            app_ext = data.find_next("span", class_="ver-item-t").text.lower()
            if version == "latest" and app_ext == extension:
                return data
            if app_version == version and app_ext == extension:
                return data
            else:
                continue
        print(f"Not found! version:{version}|app_extension:{app_ext}")
        exit()

    def __app_info(self, element: any):
        main_data = element
        app_name = main_data.find_next("div", class_="ver-item-n").text.strip().split()[0]
        app_version = main_data["data-dt-version"]
        app_version_code = main_data["data-dt-versioncode"]
        has_variant = bool(main_data["data-dt-variant"])
        app_ext_type = main_data.find_next("span", class_="ver-item-t").text.upper()
        app_ext = app_ext_type.lower()
        app_fullname = f"{app_name} {str(app_version).replace('.','_')}.{app_ext}"
        app_total_size = int(main_data["data-dt-filesize"])
        return {
            "app_name": app_name,
            "app_fullname": app_fullname,
            "app_version": app_version,
            "app_version_code": app_version_code,
            "has_variant": has_variant,
            "app_ext_type": app_ext_type,
            "app_ext": app_ext,
            "app_total_size": app_total_size
        }

    def __download_by_version_code(self, package_name: str, version_code: str, file_name="default", app_ext_type="XAPK" or "APK", in_background=False, total_size=None | int):
        apkpure_api_url = f"{self.apkpure_api_base_url}{app_ext_type}/{package_name}?versionCode={version_code}"
        if in_background:
            ApkDownloaderTools().download_in_t_background(url=apkpure_api_url, file_name=file_name)
        else:
            ApkDownloaderTools().download_w_progress_bar(url=apkpure_api_url, file_name=file_name, total_size=total_size)

    def download_by_package_name(self, package_name: str, file_name="default", version="latest", app_ext="xapk" or "apk", in_background=False):
        url = f"{self.apkpure_base_url}{package_name}/versions"
        list_elements = self.__list_versions(url=url)
        element = self.__filter_elements(list_elements=list_elements, version=version, extension=app_ext)
        app_info = self.__app_info(element=element)
        app_version_code = app_info["app_version_code"]
        app_ext_type = app_info["app_ext_type"]
        app_total_size = app_info["app_total_size"]
        if file_name == "default":
            file_name = app_info["app_fullname"]
        else:
            file_name = f"{file_name} {app_info['app_version']}.{app_ext}"
        self.__download_by_version_code(package_name=package_name, version_code=app_version_code, file_name=file_name, app_ext_type=app_ext_type, in_background=in_background, total_size=app_total_size)
