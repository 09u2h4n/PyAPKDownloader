from pyapks.apkdownloadertools import ApkDownloaderTools
import requests


class Aptoide(object):

    def __init__(self) -> None:
        self.aptoide_web_api_base_url_get_versions = "https://ws75.aptoide.com/api/7/app/getVersions/"
        self.aptoide_web_api_base_url_get_meta = "https://ws2.aptoide.com/api/7/app/getMeta/"
        self.headers = ApkDownloaderTools().headers

    def __app_id_finder(self, package_name: str, wanted_version: str, limit=15):
        version_url = f"{self.aptoide_web_api_base_url_get_versions}package_name={package_name}/limit={limit}"
        v_res = requests.get(url=version_url, headers=self.headers)
        json_data_list = v_res.json()["list"]
        if wanted_version == "latest":
            json_data = json_data_list[0]
            app_id = json_data["id"]
            return app_id
        else:
            for json_data in json_data_list:
                app_version = json_data["file"]["vername"]
                if wanted_version == app_version:
                    app_id = json_data["id"]
                    return app_id
                else:
                    continue
            else:
                print(f"Not found\nIf you want deep search you need to decrease the \"limit\" (It is the limit of app versions' number.")
                exit()

    def __get_app_infos_by_app_id(self, app_id: str):
        app_info_url = f"{self.aptoide_web_api_base_url_get_meta}app_id={app_id}"
        i_res = requests.get(url=app_info_url, headers=self.headers)
        app_info_json = i_res.json()
        
        app_size = app_info_json["data"]["size"]
        app_version = app_info_json["data"]["file"]["vername"]
        app_download_url = app_info_json["data"]["file"]["path"]
        app_ext = app_download_url.split(".")[1]
        app_name = app_info_json["data"]["name"]
        app_fullname = f"{app_name} {app_version}.{app_ext}"

        return {
            "app_size": app_size,
            "app_version": app_version,
            "app_download_url": app_download_url,
            "app_ext": app_ext,
            "app_name": app_name,
            "app_fullname": app_fullname
        }

    def download_by_package_name(self, package_name: str, file_name="default", version="latest", in_background=False, limit=15):
        app_id = self.__app_id_finder(
            package_name=package_name, wanted_version=version, limit=limit)
        app_infos = self.__get_app_infos_by_app_id(app_id=app_id)
        d_url = app_infos["app_download_url"]
        app_size = app_infos["app_size"]
        app_ext = app_infos["app_ext"]
        app_version = app_infos["app_version"]
        if file_name == "default":
            file_name = app_infos["app_fullname"]
        else:
            file_name = f"{file_name} {app_version}.{app_ext}"
        if in_background:
            ApkDownloaderTools().download_in_t_background(url=d_url, file_name=file_name)
        else:
            ApkDownloaderTools().download_w_progress_bar(url=d_url, file_name=file_name, total_size=app_size)
