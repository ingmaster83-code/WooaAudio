# WooaAudio 프로젝트 지침

## 개요
- **브랜드:** WooaAudio
- **URL:** https://wooaaudio.wooahouse.com
- **테마 컬러:** `#7C3AED` (보라색)
- **참고 기준:** PDFKIT 레이아웃을 그대로 따름 (공통 지침 참조)

---

## 현재 파일 구조
```
WooaAudio/
├── index.html          ← 메인 (도구 목록) — 구조 완성, 레이아웃 수정 필요
├── audio-convert.html  ← 오디오 변환 — 기능 동작, 레이아웃 수정 필요
├── css/style.css
├── js/pwa-install.js
├── manifest.json
├── sw.js
├── robots.txt
├── sitemap.xml
└── CNAME               ← wooaaudio.wooahouse.com
```

**미생성 (추후 추가):** about.html, privacy.html

---

## 알려진 레이아웃 이슈 (수정 필요)

1. **our-sites-bar 이모지 누락** — 현재 텍스트만 있음, 이모지 추가 필요 (공통 지침의 표준 HTML 사용)
2. **our-sites-bar WooaAudio 미등록** — 현재 PDFKit/ImageKit 등 타 사이트에 WooaAudio 링크 없음 (타 사이트 작업 시 추가)
3. **index.html의 첫 번째 category-dot 색상 누락** — `style="background:#7C3AED"` 추가 필요
4. **about.html/privacy.html 미생성** — footer의 해당 링크가 index.html로 연결되어 있음
5. **naver/google site-verification 메타태그 누락** — index.html, audio-convert.html 둘 다
6. **header-right 소개 링크** — audio-convert.html에 header-right 자체가 없음 (index.html은 있음)
7. **hero PWA 버튼 이모지 누락** — `📌` 이모지 추가 (PDFKIT: `📌 홈 화면에 추가`)

---

## 오디오 변환 엔진 (audio-convert.html)
- **라이브러리:** FFmpeg.wasm (CDN)
- **로딩 정책:** 파일 선택 후 변환 버튼 클릭 시점에 lazy load
- **로딩 실패 안내:** 새로고침 + 네트워크/CDN/광고차단 확장 가능성 함께 안내
- **지원 포맷:** MP3, WAV, OGG, FLAC, AAC, M4A → 상호 변환

---

## 도구 현황

| 도구 | 파일 | 상태 |
|------|------|------|
| 오디오 포맷 변환 | audio-convert.html | ✅ 동작 |
| MP3 변환 | audio-convert.html?format=mp3 | ✅ (쿼리파라미터) |
| WAV 변환 | audio-convert.html?format=wav | ✅ (쿼리파라미터) |
| FLAC 변환 | audio-convert.html?format=flac | ✅ (쿼리파라미터) |
| 오디오 자르기 | — | 🔨 준비중 |
| 오디오 합치기 | — | 🔨 준비중 |
| 볼륨 조절 | — | 🔨 준비중 |
| 속도 조절 | — | 🔨 준비중 |
| 파형 시각화 | — | 🔨 준비중 |
| 오디오 정보 | — | 🔨 준비중 |

---

## ld+json 패턴
- index.html: `"@type": "WebSite"` + `"@type": "ItemList"`
- 도구 페이지: `"@type": "WebApplication"`, `applicationCategory: "MultimediaApplication"`
