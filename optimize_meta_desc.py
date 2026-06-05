"""
WooaAudio KO 페이지 메타 디스크립션 CTR 최적화
- 최우선: 음원 키 변환(10)+mp3 음정 낮추기(4)+변형 = 17 노출 → audio-pitch.html
- 중요: 오디오 편집 무료(14)+mp3 편집 무료(7) = 21 노출 → index
        mp3 길이 편집(9+3) + 오디오 자르기 무료(3) = 17 노출 → audio-cut.html
        mp3 합치기(6+2+2) = 11 노출 → audio-merge.html
        mp3 mr 변환(3) → audio-mr.html / 데시벨 측정기 웹사이트(2) → audio-decibel.html
- 공통: "설치 없이 브라우저에서 무료로 사용 가능합니다" 보일러플레이트 제거
"""
import re, os

BASE = 'C:/개인/wooahouse/wooaaudio'

PAGES = {
    # ── index: 오디오 편집 무료 21 노출 ────────────────────────────────
    'index.html': (
        'MP3, WAV, OGG, FLAC, AAC 오디오 변환·자르기·합치기',
        '오디오 편집 무료 — MP3·WAV·FLAC 자르기·합치기·변환·볼륨·속도·음정까지 브라우저에서 즉시 처리. mp3 편집 무료, 설치·로그인 없이 바로 사용, 파일은 서버에 저장되지 않아 안전. 우아오디오(WooaAudio)'
    ),
    # ── 17 노출 0%: 음원 키 변환 → audio-pitch.html ───────────────────
    'audio-pitch.html': (
        'MP3, WAV 오디오 파일의 피치(음정)를 반음 단위로',
        '음원 키 변환·mp3 음정 변환 무료 — MP3·WAV 음정을 반음 단위로 -12~+12 범위에서 즉시 조절. mp3 음정 낮추기·높이기 가능, 설치·로그인 없이 바로 사용.'
    ),
    # ── mp3 길이 편집(12) + 오디오 자르기(5) = 17 노출 ─────────────────
    'audio-cut.html': (
        'MP3, WAV, FLAC 오디오 파일에서 원하는 구간만 잘라',
        '오디오 자르기·mp3 길이 편집 무료 — MP3·WAV·FLAC 원하는 구간을 잘라 즉시 다운로드. 시작·끝 시간을 초 단위로 설정, wav 자르기 지원, 설치·로그인 없이 바로 사용.'
    ),
    # ── mp3 합치기 11 노출 ───────────────────────────────────────────
    'audio-merge.html': (
        'MP3, WAV, FLAC 등 여러 오디오 파일을 순서대로 배치해',
        'mp3 합치기·오디오 파일 합치기 무료 — MP3·WAV·FLAC 여러 파일을 순서대로 배치해 하나로 즉시 합치기. 드래그로 순서 조절, 설치·로그인 없이 바로 사용.'
    ),
    # ── mp3 MR 변환 3 노출 ──────────────────────────────────────────
    'audio-mr.html': (
        'MP3, WAV 음악에서 보컬을 제거',
        'mp3 MR 변환·보컬 제거 무료 — MP3·WAV 음악에서 보컬을 분리해 반주(MR)를 즉시 생성. 설치·로그인 없이 브라우저에서 바로 처리, 파일은 서버에 저장되지 않아 안전.'
    ),
    # ── 데시벨 측정기 웹사이트 2 노출 ─────────────────────────────────
    'audio-decibel.html': (
        '마이크로 주변 소음을 실시간 데시벨(dB)로 측정',
        '데시벨 측정기 무료 웹사이트 — 마이크로 주변 소음을 실시간 dB로 측정. 현재·최대·평균값 표시, 층간소음·환경소음 확인, 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    # ── mp3 편집 페이드인 100% CTR + 보강 ──────────────────────────────
    'audio-fade.html': (
        'MP3, WAV 오디오 파일에 페이드인·페이드아웃 효과를 무료로 추가',
        'mp3 페이드인·페이드아웃 효과 무료 — MP3·WAV 오디오에 자연스러운 페이드 효과를 즉시 추가. 시작 부분 점점 크게·끝 부분 점점 작게, 설치·로그인 없이 바로 사용.'
    ),
    # ── 벨소리 관련 ─────────────────────────────────────────────────
    'audio-ringtone.html': (
        'MP3, WAV 오디오에서 원하는 구간을 추출해 30초 이하 벨소리',
        '벨소리 만들기 무료 — MP3·WAV에서 원하는 구간을 추출해 30초 이하 벨소리를 즉시 제작. 페이드인·아웃 적용, 아이폰·갤럭시 벨소리 만들기 안내, 설치·로그인 없이 바로 사용.'
    ),
    # ── 나머지 전체 (보일러플레이트 제거 + 키워드 선행) ──────────────────
    'audio-convert.html': (
        'MP3, WAV, OGG, FLAC, AAC, M4A 오디오 파일을 브라우저에서 무료로 변환',
        '오디오 변환기 무료 — MP3·WAV·OGG·FLAC·AAC·M4A 포맷을 즉시 변환. 비트레이트·샘플레이트 설정, 파일은 서버에 업로드되지 않아 안전, 설치·로그인 없이 바로 사용.'
    ),
    'audio-mp3.html': (
        'WAV, FLAC, OGG, AAC, M4A 오디오 파일을 브라우저에서 무료로 MP3로 변환',
        'WAV·FLAC→MP3 변환 무료 — WAV·FLAC·OGG·AAC·M4A를 MP3로 즉시 변환. 비트레이트 128~320kbps 설정, 파일은 서버에 업로드되지 않아 안전, 설치·로그인 없이 바로 사용.'
    ),
    'audio-wav.html': (
        'MP3, FLAC, OGG, AAC, M4A 오디오 파일을 브라우저에서 무료로 WAV로 변환',
        'MP3→WAV 변환 무료 — MP3·FLAC·OGG·AAC·M4A를 WAV 무손실로 즉시 변환. 음질 저하 없이 변환, wav 파일 편집에 최적, 설치·로그인 없이 바로 사용.'
    ),
    'audio-flac.html': (
        'MP3, WAV, OGG, AAC, M4A 오디오 파일을 브라우저에서 무료로 FLAC 무손실 포맷으로 변환',
        'FLAC 변환기 무료 — MP3·WAV·OGG·AAC·M4A를 FLAC 무손실로 즉시 변환. 최고 음질 유지, 파일은 서버에 업로드되지 않아 안전, 설치·로그인 없이 바로 사용.'
    ),
    'audio-volume.html': (
        'MP3, WAV, FLAC 오디오 파일의 볼륨을 브라우저에서 무료로 조절',
        '오디오 볼륨 조절 무료 — MP3·WAV·FLAC 볼륨을 즉시 증폭, 자동 볼륨 정규화(Normalize) 지원. 파일은 서버에 저장되지 않아 안전, 설치·로그인 없이 바로 사용.'
    ),
    'audio-speed.html': (
        'MP3, WAV, FLAC 오디오 파일의 재생 속도를 0.5x~2.0x 범위에서',
        '오디오 속도 조절 무료 — MP3·WAV·FLAC 재생 속도를 0.5x~2.0x로 즉시 변환. 피치 보존 옵션으로 음정 변화 없이 속도만 조절, 설치·로그인 없이 바로 사용.'
    ),
    'audio-record.html': (
        '브라우저에서 마이크로 바로 녹음하고 WAV 파일로 다운로드',
        '오디오 녹음기 무료 — 브라우저에서 마이크로 바로 녹음, WAV 파일로 즉시 다운로드. 실시간 파형 시각화·녹음 시간 표시, 설치·로그인 없이 바로 사용.'
    ),
    'audio-waveform.html': (
        'MP3, WAV, FLAC 오디오 파일의 파형(웨이브폼)을 브라우저에서 무료로 시각화',
        '오디오 파형 시각화 무료 — MP3·WAV·FLAC 파형(웨이브폼)을 즉시 시각화, PNG로 저장 가능. 오디오 분석·편집에 최적, 설치·로그인 없이 바로 사용.'
    ),
    'audio-info.html': (
        'MP3, WAV, FLAC 오디오 파일의 재생 시간, 샘플레이트, 채널',
        '오디오 파일 정보 확인 무료 — 재생시간·샘플레이트·채널(모노/스테레오)·비트레이트를 즉시 확인. 파일은 서버에 저장되지 않아 안전, 설치·로그인 없이 바로 사용.'
    ),
    'audio-tag.html': (
        'MP3 파일의 제목·아티스트·앨범·장르·앨범아트 등 ID3 태그를 브라우저에서 무료로 편집',
        'MP3 ID3 태그 편집 무료 — 제목·아티스트·앨범·장르·앨범아트를 브라우저에서 즉시 편집. 서버 저장 없음, 설치·로그인 없이 바로 사용.'
    ),
    'audio-metronome.html': (
        '온라인 메트로놈으로 BPM과 박자를 자유롭게 설정',
        '온라인 메트로놈 무료 — BPM·박자를 자유롭게 설정, 탭 템포 기능 지원. 2/4·3/4·4/4·6/8 박자, 악기 연습·작곡에 최적, 설치·로그인 없이 바로 사용.'
    ),
    'audio-tuner.html': (
        '마이크로 악기 음을 감지해 음이름·주파수·음정 편차를 실시간 표시',
        '악기 튜너 무료 — 마이크로 음이름·주파수·음정 편차를 실시간 감지. 기타·베이스·바이올린 등 크로매틱 튜너, 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'audio-tts.html': (
        '텍스트를 음성으로 변환하세요. 한국어·영어 등 다양한 언어',
        '텍스트 음성 변환(TTS) 무료 — 한국어·영어 등 다양한 언어 지원, 속도·음높이 조절 가능. 독서 보조·발음 연습·콘텐츠 제작에 최적, 설치·로그인 없이 바로 사용.'
    ),
}

ok_count = 0
fail_count = 0

for fname, (match_prefix, new_desc) in PAGES.items():
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f'  SKIP (없음): {fname}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<meta name="description" content=")[^"]*(")'

    def desc_replacer(m, mp=match_prefix, nd=new_desc):
        if mp in m.group(0):
            return m.group(1) + nd + m.group(2)
        return m.group(0)

    new_content = re.sub(pattern, desc_replacer, content)

    if new_content == content:
        print(f'  MISS: {fname} — "{match_prefix[:40]}"')
        fail_count += 1
        continue

    new_content = re.sub(
        r'(<meta property="og:description" content=")[^"]*(")',
        lambda x, nd=new_desc: x.group(1) + nd + x.group(2), new_content
    )
    new_content = re.sub(
        r'(<meta name="twitter:description" content=")[^"]*(")',
        lambda x, nd=new_desc: x.group(1) + nd + x.group(2), new_content
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'  OK: {fname}')
    ok_count += 1

print(f'\n완료: {ok_count}개 교체, {fail_count}개 실패')
