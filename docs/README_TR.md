---
[English](https://github.com/09u2h4n/PyAPKDownloader/blob/main/README.md) | [Turkish](https://github.com/09u2h4n/PyAPKDownloader/blob/main/docs/README_TR.md)
---

# PyAPKDownloader Modülü Belgeleri
PyAPKDownloader, Aptoide ve ApkPure gibi alternatif kaynakları kullanarak Android APK dosyalarını indirmenizi sağlayan bir Python modülüdür. Bu belge, genel bir tanıtım olarak hizmet verir ve belirli kullanım durumlarınıza göre özelleştirmeyi gerektirebilir.
## Kurulum 🚀
PyAPKDownloader'ı pip kullanarak kurabilirsiniz:

    pip install PyAPKDownloader

VEYA dist dizinini ayarlamak ve kullanmak için setup.py kullanabilirsiniz.

    pip install .

Sanal ortam kullanmanızı öneriyorum.

    python3 -m venv venv && pip install .

## Kullanım 📦
PyAPKDownloader modülü, seçtiğiniz kaynaktan APK dosyalarını indirmeniz için kullanabileceğiniz Aptoide ve ApkPure sınıflarını içerir.
### Aptoide Kullanımı 🛒
Aptoide sınıfını kullanarak bir APK dosyasını indirmek için aşağıdaki örneği kullanabilirsiniz:

    from PyAPKDownloader.aptoide import Aptoide
    Downloader = Aptoide()
    Downloader.download_by_package_name(package_name="com.whatsapp", file_name="Whatsapp", version="latest", in_background=False, limit=30)
-   `package_name`: İndirmek istediğiniz uygulamanın paket adını belirtir.
-   `file_name`: İndirilen APK dosyasının adını belirtir.
-   `version`: İndirmek istediğiniz sürümü belirtir (örneğin, en son sürümü almak için "latest" kullanabilirsiniz).
-   `in_background`: İndirme işleminin arka planda çalışıp çalışmayacağını belirtir.
-   `limit`: Bir uygulama ararken arama derinliğini belirler. (Daha fazla olursa, daha yavaş çalışır.)
### ApkPure Kullanımı 🌐
ApkPure sınıfını kullanarak bir APK dosyasını indirmek için aşağıdaki örneği kullanabilirsiniz:

    from PyAPKDownloader.apkpure import ApkPure
    Downloader = ApkPure()
    Downloader.download_by_package_name(package_name="com.whatsapp", file_name="Whatsapp", version="latest", app_ext="xapk", in_background=False)
-   `package_name`: İndirmek istediğiniz uygulamanın paket adını belirtir.
-   `file_name`: İndirilen APK dosyasının adını belirtir.
-   `version`: İndirmek istediğiniz sürümü belirtir (örneğin, en son sürümü almak için "latest" kullanabilirsiniz).
-   `app_ext`: İndirilen dosyanın dosya uzantısını belirtir (örneğin, "xapk" kullanabilirsiniz).
-   `in_background`: İndirme işleminin arka planda çalışıp çalışmayacağını belirtir.

Not: `package_name="com.whatsapp"` gibi girişler sadece örneklerdir. Diğer uygulamaları indirmek için paket adını değiştirebilirsiniz.

## İletişim ve Destek 📧

PyAPKDownloader modülü hakkında daha fazla bilgi, sorular veya destek için lütfen [GitHub deposuna](https://github.com/09u2h4n/PyAPKDownloader) başvurun.

Bu belge, PyAPKDownloader modülünün temel kullanımı hakkında bir genel bakış sunar.'
