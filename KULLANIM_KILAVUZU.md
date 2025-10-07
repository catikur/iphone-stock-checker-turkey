# iPhone Stok Kontrol Uygulaması - Kullanım Kılavuzu

## Genel Bakış

Bu uygulama, Apple Türkiye online mağazasından **iPhone 17 Pro** ve **iPhone 17 Pro Max Kozmik Turuncu** modellerinin İstanbul'daki Apple Store mağazalarında mağazadan teslim alma stok durumunu kontrol etmenizi sağlar.

**Uygulama URL'si:** https://lnh8imcw1qqm.manus.space

## Özellikler

### 1. Manuel Stok Kontrolü
Tek bir tıklama ile anlık olarak tüm ürünlerin tüm mağazalardaki stok durumunu kontrol edebilirsiniz.

**Nasıl Kullanılır:**
- Ana sayfada **"Şimdi Kontrol Et"** butonuna tıklayın
- Uygulama otomatik olarak tüm modelleri ve mağazaları kontrol eder
- Sonuçlar renkli kartlar halinde görüntülenir:
  - **Yeşil kart**: Ürün stokta var
  - **Kırmızı kart**: Ürün stokta yok

### 2. Otomatik Stok Kontrolü
Belirlediğiniz aralıklarla otomatik olarak stok kontrolü yapabilir ve stok bulunduğunda bildirim alabilirsiniz.

**Nasıl Kullanılır:**
1. **Kontrol Aralığı** alanına dakika cinsinden süre girin (minimum 5 dakika)
2. **"Başlat"** butonuna tıklayın
3. Uygulama arka planda belirlediğiniz aralıklarla kontrol yapmaya başlar
4. Stok bulunduğunda ekranda bildirim görürsünüz
5. Durdurmak için **"Durdur"** butonuna tıklayın

**Durum Bilgileri:**
- **Aktif/Pasif**: Zamanlayıcının çalışma durumu
- **Kontrol Aralığı**: Kaç dakikada bir kontrol yapıldığı
- **Son Kontrol**: En son ne zaman kontrol yapıldığı
- **Sonraki Kontrol**: Bir sonraki kontrolün ne zaman yapılacağı

### 3. Çoklu Dil Desteği
Uygulama Türkçe ve İngilizce dillerini destekler.

**Dil Değiştirme:**
- Sağ üst köşedeki **TR** veya **EN** butonlarına tıklayarak dili değiştirebilirsiniz

## Kontrol Edilen Ürünler

Uygulama aşağıdaki iPhone modellerini kontrol eder:

1. **iPhone 17 Pro 256GB Kozmik Turuncu**
2. **iPhone 17 Pro 512GB Kozmik Turuncu**
3. **iPhone 17 Pro Max 256GB Kozmik Turuncu**
4. **iPhone 17 Pro Max 512GB Kozmik Turuncu**

## Kontrol Edilen Mağazalar

Uygulama İstanbul'daki üç Apple Store mağazasını kontrol eder:

### 1. Apple Bağdat Caddesi (Kadıköy)
- **Adres:** Bağdat Caddesi, No: 342, Caddebostan, Kadıköy İstanbul 34728
- **Telefon:** (0216) 468 01 00
- **Lokasyon:** Kadıköy bölgesinde, Bağdat Caddesi üzerinde

### 2. Apple Zorlu Center (Beşiktaş)
- **Adres:** Zorlu Center, Koru Sok. No: 2, Beşiktaş İstanbul 34340
- **Telefon:** (0212) 708 37 00
- **Lokasyon:** Zorlu Center AVM içinde

### 3. Apple Akasya (Üsküdar)
- **Adres:** Akasya AVM, Acıbadem Mah, Çeçen Sok No: 25, Üsküdar İstanbul 34660
- **Telefon:** (0216) 250 71 00
- **Lokasyon:** Akasya AVM içinde

## Sonuç Kartları Nasıl Okunur

Her sonuç kartı şu bilgileri içerir:

- **Ürün Adı ve Kapasite**: Hangi iPhone modeli kontrol edildi
- **Mağaza Adı**: Hangi Apple Store kontrol edildi
- **Lokasyon**: Mağazanın bulunduğu semt ve şehir
- **Adres**: Mağazanın tam adresi
- **Telefon**: Mağazanın iletişim numarası
- **Stok Durumu**: Ürünün stokta olup olmadığı
  - ✓ **Stokta var** (Yeşil): Ürün mağazada mevcut
  - ✗ **Stokta yok** (Kırmızı): Ürün mağazada mevcut değil
- **Kontrol Zamanı**: Bu bilginin ne zaman alındığı

## Kullanım Senaryoları

### Senaryo 1: Hızlı Kontrol
İstediğiniz iPhone modelinin herhangi bir mağazada stokta olup olmadığını hızlıca öğrenmek istiyorsunuz.

**Çözüm:**
1. Uygulamayı açın
2. "Şimdi Kontrol Et" butonuna tıklayın
3. Tüm sonuçları inceleyin ve yeşil kartları arayın

### Senaryo 2: Sürekli Takip
Stok geldiğinde hemen haberdar olmak istiyorsunuz.

**Çözüm:**
1. Kontrol aralığını 30 dakika olarak ayarlayın
2. "Başlat" butonuna tıklayın
3. Uygulamayı açık bırakın
4. Stok bulunduğunda otomatik bildirim alırsınız

### Senaryo 3: Belirli Bir Mağaza
Sadece Kadıköy Bağdat Caddesi mağazasını takip etmek istiyorsunuz.

**Çözüm:**
1. Manuel veya otomatik kontrol yapın
2. Sonuçlar arasında "Apple Bağdat Caddesi" yazan kartları inceleyin
3. Diğer mağazaların sonuçlarını görmezden gelebilirsiniz

## Önemli Notlar

1. **Gerçek Zamanlı Veri**: Uygulama Apple'ın resmi API'sinden gerçek zamanlı stok bilgilerini çeker.

2. **Kontrol Sıklığı**: Otomatik kontrolde minimum 5 dakika aralık belirleyebilirsiniz. Çok sık kontrol yapmak gereksizdir çünkü stoklar genellikle günde birkaç kez güncellenir.

3. **Tarayıcı Açık Kalmalı**: Otomatik kontrol özelliğinin çalışması için tarayıcı sekmesinin açık kalması gerekir.

4. **Bildirimler**: Stok bulunduğunda ekranda yeşil bildirim kutusu görünür. Bu bildirimler 5 saniye sonra otomatik olarak kaybolur.

5. **Mobil Uyumlu**: Uygulama mobil cihazlarda da sorunsuz çalışır.

## Sık Sorulan Sorular

**S: Uygulama ücretsiz mi?**
C: Evet, uygulama tamamen ücretsizdir.

**S: Hangi iPhone modellerini destekliyor?**
C: Sadece iPhone 17 Pro ve iPhone 17 Pro Max Kozmik Turuncu rengini destekler. Diğer renkler veya modeller için destek yoktur.

**S: Başka şehirlerdeki mağazaları da kontrol edebilir miyim?**
C: Hayır, uygulama şu anda sadece İstanbul'daki üç Apple Store'u kontrol eder.

**S: Stok bilgileri ne kadar güvenilir?**
C: Stok bilgileri doğrudan Apple'ın resmi API'sinden alınır, bu nedenle %100 güvenilirdir. Ancak stoklar hızla değişebilir, bu yüzden stok gördüğünüzde hemen işlem yapmanız önerilir.

**S: Otomatik kontrolü kapatırsam veriler kaybolur mu?**
C: Hayır, en son kontrol sonuçları ekranda kalır. İstediğiniz zaman tekrar başlatabilirsiniz.

**S: Uygulamayı telefonuma indirebilir miyim?**
C: Uygulama web tabanlıdır, indirmeye gerek yoktur. Tarayıcınızdan erişebilirsiniz. İsterseniz ana ekrana kısayol ekleyebilirsiniz.

## Teknik Destek

Uygulama ile ilgili sorun yaşarsanız:
- Sayfayı yenilemeyi deneyin (F5 veya Ctrl+R)
- Tarayıcınızın önbelleğini temizleyin
- Farklı bir tarayıcı deneyin (Chrome, Firefox, Safari önerilir)

## Gizlilik

Uygulama hiçbir kişisel bilginizi toplamaz veya saklamaz. Sadece Apple'ın halka açık stok bilgilerine erişir.
