# ecoField – Gizlilik / Privacy

ecoField mobil uygulamasının gizlilik politikası, KVKK aydınlatma metni ve hesap silme sayfası. GitHub Pages ile yayınlanır.

- Ana sayfa (mağazalara verilecek adres): https://b2avar.github.io/ecofield-privacy/
- Türkçe: https://b2avar.github.io/ecofield-privacy/tr.html
- English: https://b2avar.github.io/ecofield-privacy/en.html
- Hesap silme / Account deletion: https://b2avar.github.io/ecofield-privacy/delete.html

## Güncelleme

Gizlilik metninin kaynağı uygulamadaki çeviri dosyalarıdır (`privacy_page.content`). Metni orada değiştirip sayfaları yeniden üret:

```
python3 build.py ~/Desktop/eco/ecoField/frontend/src/i18n/locales
git commit -am "Update privacy notice" && git push
```

İletişim: burakavar@gmail.com
