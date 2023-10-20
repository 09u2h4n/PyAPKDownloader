import requests
from threading import Thread
from tqdm import tqdm


class ApkDownloaderTools:
    def __init__(self) -> None:
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}

    def download_w_progress_bar(self, url: str, file_name: str, total_size=None | int):
        print(f"#{file_name}")
        response = requests.get(url=url, stream=True, headers=self.headers)
        try:
            total_size = int(response.headers.get("content-length"))
        except ValueError:
            pass
        if total_size is None:
            return "Can't get total size of app. Please specify."
        chunk_size = 1024
        progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)
        with open(file_name, "wb") as f:
            for data in response.iter_content(chunk_size=chunk_size):
                progress_bar.update(len(data))
                f.write(data)

    def download_in_t_background(self, url: str, file_name: str):
        response = requests.get(url=url, stream=True, headers=self.headers)
        chunk_size = 1024

        def download():
            with open(file_name, "wb") as f:
                for data in response.iter_content(chunk_size=chunk_size):
                    f.write(data)
        Thread(target=download).start()
