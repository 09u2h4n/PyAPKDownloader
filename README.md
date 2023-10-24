# Apk Downloader Module Documentation
Apk Downloader is a Python module that allows you to download Android APK files using alternative sources such as Aptoide and ApkPure. This documentation serves as a general introduction and may require customization for your specific use case.
## Installation 🚀
You can install Apk Downloader using pip:

    pip install pyapks
    
OR you can use setup.py to set dist directory and use.

    pip install .

I recommend to use virtual environment.

    python3 -m venv venv && pip install .

## Usage 📦
The Apk Downloader module includes classes for Aptoide and ApkPure, which you can use to download APK files from the source of your choice.
### Using Aptoide 🛒
To download an APK file using the Aptoide class, you can use the following example:

    from pyapks.aptoide import Aptoide
    Downloader = Aptoide()
    Downloader.download_by_package_name(package_name="com.whatsapp", file_name="Whatsapp", version="latest", in_background=False, limit=30)
-   `package_name`: Specifies the package name of the application you want to download.
-   `file_name`: Specifies the name of the downloaded APK file.
-   `version`: Specifies the version you want to download (e.g., you can use "latest" to get the latest version).
-   `in_background`: Specifies whether the download process will run in the background.
-   `limit`: Determines the depth of the search when searching for an application. (The more it is, the slower it becomes.)
### Using ApkPure 🌐
To download an APK file using the ApkPure class, you can use the following example:

    from pyapks.apkpure import ApkPure
    Downloader = ApkPure()
    Downloader.download_by_package_name(package_name="com.whatsapp", file_name="Whatsapp", version="latest", app_ext="xapk", in_background=False)
-   `package_name`: Specifies the package name of the application you want to download.
-   `file_name`: Specifies the name of the downloaded APK file.
-   `version`: Specifies the version you want to download (e.g., you can use "latest" to get the latest version).
-   `app_ext`: Specifies the file extension of the downloaded file (e.g., you can use "xapk").
-   `in_background`: Specifies whether the download process will run in the background.

Note: Entries like `package_name="com.whatsapp"` are just examples. You can change the package name to download other applications.

## Contact and Support 📧

For more information about the Apk Downloader module, questions, or support, please refer to the [GitHub repository](https://github.com/09u2h4n/pyapks).

This documentation provides an overview of the basic usage of the Apk Downloader module.
