# WooaAudio Rebuild Notes

## 작업 기준
- 작업 폴더: `H:\개인 프로젝트\WooaAudio`
- 참고 폴더: `H:\개인 프로젝트\PDFKIT`
- WooaAudio는 WooaPDF의 형제 사이트로 제작한다.

## 디자인/레이아웃 원칙
- 프로그램 기능 영역을 제외하고 WooaPDF와 레이아웃, 광고 위치, 서비스 바, 푸터 구조를 최대한 동일하게 유지한다.
- 상단 헤더, WooaHouse 서비스 바, 히어로, 모바일 상단 광고, 데스크톱 우측 광고, 결과 영역 광고, 쿠팡 파트너스 영역 배치를 WooaPDF 기준으로 맞춘다.
- 브랜드명은 `WooaAudio`, 대표 도메인은 `https://wooaaudio.wooahouse.com/`로 사용한다.
- 테마 컬러는 오디오 사이트에 맞춰 보라색 계열(`#7C3AED`)을 사용하되, 컴포넌트 크기와 간격은 WooaPDF 스타일을 따른다.

## 1차 생성 범위
- 메인 페이지: `index.html`
- 오디오 변환 페이지: `audio-convert.html`
- 공통 스타일: `css/style.css`
- PWA 보조 스크립트: `js/pwa-install.js`
- 기본 배포 보조 파일: `manifest.json`, `sw.js`, `robots.txt`, `sitemap.xml`, `CNAME`

## 오디오 변환 정책
- 페이지 진입 시 FFmpeg 엔진을 바로 로드하지 않는다.
- 사용자가 파일을 선택하고 변환 버튼을 누를 때 FFmpeg.wasm을 로드한다.
- 엔진 로드 중에는 현재 단계와 진행 상태를 화면에 표시한다.
- 엔진 로드 실패 시 새로고침만 안내하지 말고, 네트워크/CDN/광고 차단 확장 프로그램 가능성을 함께 안내한다.
- 파일은 서버로 업로드하지 않고 브라우저 안에서 처리한다는 안내를 유지한다.
