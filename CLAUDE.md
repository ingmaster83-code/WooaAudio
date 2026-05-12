# WooaAudio 프로젝트 지침

## 프로젝트 개요
- **사이트명:** WooaAudio
- **도메인 예정:** https://audiokit.wooahouse.com
- **형제 사이트:** https://pdfkit.wooahouse.com (WooaPDF)
- **배포:** GitHub Pages (main 브랜치 → root)
- **테마색:** #7C3AED (보라색, WooaPDF는 #FF4444 빨강)

## 기술 스택
- 순수 HTML / CSS / JS (프레임워크 없음)
- 오디오 변환·편집: FFmpeg.wasm (unpkg CDN, @ffmpeg/ffmpeg@0.11.6)
- 분석·녹음·파형: Web Audio API, MediaRecorder API, Canvas API
- PWA: manifest.json + sw.js + js/pwa-install.js

## 파일 구조
```
AUDIOKIT/
├── index.html              # 메인 (툴 목록)
├── audio-convert.html      # 오디오 포맷 변환 (FFmpeg.wasm)
├── video-to-audio.html     # 영상→오디오 추출 (FFmpeg.wasm)
├── audio-trim.html         # 오디오 자르기 (FFmpeg.wasm + Web Audio)
├── audio-merge.html        # 오디오 합치기 (FFmpeg.wasm)
├── audio-volume.html       # 음량 조절/정규화 (Web Audio API)
├── audio-fade.html         # 페이드 인/아웃 (Web Audio API)
├── audio-speed.html        # 속도 조절 (Web Audio API)
├── audio-waveform.html     # 파형 시각화 (Canvas API)
├── audio-bpm.html          # BPM 감지 (자기상관 알고리즘) + 탭 측정
├── audio-info.html         # 오디오 정보 추출 (Web Audio API)
├── audio-recorder.html     # 브라우저 녹음기 (MediaRecorder API)
├── screen-audio.html       # 화면 오디오 캡처 (getDisplayMedia)
├── about.html              # 서비스 소개
├── privacy.html            # 개인정보처리방침
├── css/style.css           # 공통 스타일 (WooaPDF 동일 구조, 보라색 테마)
├── js/pwa-install.js       # PWA 설치 유도
├── manifest.json           # PWA 매니페스트
├── sw.js                   # 서비스 워커
├── robots.txt
├── sitemap.xml
└── CNAME                   # audiokit.wooahouse.com
```

## 작업 규칙
- 새 도구 페이지 추가 시 index.html 카드, footer 링크, sitemap.xml 모두 업데이트
- 모든 페이지에 `<script src="js/pwa-install.js"></script>` 포함
- 다운로드 버튼은 반드시 `id="downloadBtn"` 사용 (PWA 배너 트리거)
- FFmpeg.wasm 사용 페이지는 반드시 로딩 UI (#ffmpegLoading) 포함
- 파일은 서버에 저장되지 않는다는 문구 유지 (신뢰도)
- Our Sites Bar에 WooaAudio를 active로 표시

## 광고 설정 (교체 필요)
- Google Analytics: G-XXXXXXXXXX → 실제 GA ID로 교체
- Google AdSense: ca-pub-XXXXXXXXXXXXXXXXX → 실제 Publisher ID로 교체
- 쿠팡 파트너스: trackingCode "AF5600192" → 실제 추적코드로 교체 (현재 WooaPDF 코드)

## FFmpeg.wasm CDN
```html
<script src="https://unpkg.com/@ffmpeg/ffmpeg@0.11.6/dist/ffmpeg.min.js"></script>
```
corePath: 'https://unpkg.com/@ffmpeg/core@0.11.0/dist/ffmpeg-core.js'

## SEO 방향
- "무료" 키워드 강조 (타이틀, 설명, 카드 뱃지)
- 브라우저 처리 / 서버 미전송 / 안전 강조
- Hero 문구: "모든 오디오 작업 무료로, 한 곳에서"

## WooaHouse Our Sites Bar 추가 필요
WooaPDF index.html의 Our Sites Bar에 아래 항목 추가:
```html
<a href="https://audiokit.wooahouse.com/" target="_blank" rel="noopener">🎵 WooaAudio</a>
```
