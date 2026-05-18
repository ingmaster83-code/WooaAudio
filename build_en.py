"""
WooaAudio 영어 버전 자동 생성 스크립트
실행: python build_en.py
결과: en/ 폴더에 영어 버전 HTML 파일 생성
"""

import os, re, sys, io, json as _json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.abspath(__file__))
EN_DIR = os.path.join(BASE, 'en')
os.makedirs(EN_DIR, exist_ok=True)

# ── 1. 페이지별 메타 번역 ─────────────────────────────────────────────────────
PAGE_META = {
    'index.html': {
        'title': 'Free Online Audio Tools – Convert, Cut, Merge, Record MP3 WAV FLAC | WooaAudio',
        'desc':  'Free online audio tools: convert MP3/WAV/FLAC/OGG/AAC, cut, merge, adjust volume, record, visualize waveform and more — all in your browser. No upload to server.',
        'kw':    'audio converter, MP3 converter, WAV converter, FLAC converter, audio cutter, audio merger, audio recorder, waveform visualizer, free audio tools, online audio editor, WooaAudio',
        'og_title': 'Free Online Audio Tools – MP3 WAV FLAC Convert & Edit | WooaAudio',
        'og_desc':  'Convert, cut, merge, record and visualize audio — all free in your browser. Files never sent to a server.',
        'app_name': 'WooaAudio',
        'faq': [
            ('Are these audio tools really free?',
             'Yes. All WooaAudio tools are completely free with no signup required and no usage limits.'),
            ('Are my audio files uploaded to a server?',
             'No. All processing is done locally in your browser. Your files never leave your device.'),
            ('Which audio formats are supported?',
             'MP3, WAV, OGG, FLAC, AAC, M4A, OPUS, and AIFF are supported across the various tools.'),
        ],
        'h1': 'All Audio Tasks — Free, in One Place',
        'tool_desc': 'Convert, cut, merge, adjust volume and more — 100% free. No signup needed, files never stored on a server.',
        'breadcrumb': 'Home',
        'cross_banner_text': 'Need to work with documents or images too?',
        'cross_banner_link_text': '📄 WooaPDF – Free PDF Tools →',
        'cross_banner_href': 'https://pdfkit.wooahouse.com/',
    },
    'audio-convert.html': {
        'title': 'Audio Converter Free Online – MP3 WAV OGG FLAC AAC Conversion | WooaAudio',
        'desc':  'Convert MP3, WAV, OGG, FLAC, AAC, M4A audio files for free in your browser. Set bitrate and sample rate. No upload — files never sent to a server.',
        'kw':    'audio converter, MP3 converter, WAV converter, FLAC converter, AAC converter, OGG converter, free audio converter online, convert audio format, browser audio converter',
        'og_title': 'Audio Format Converter Free Online | WooaAudio',
        'og_desc':  'Convert audio between MP3, WAV, OGG, FLAC, AAC and more. Set bitrate and sample rate. Free, no signup, no server upload.',
        'app_name': 'Audio Format Converter',
        'faq': [
            ('What audio formats are supported?',
             'MP3, WAV, OGG, FLAC, AAC, M4A, OPUS, and AIFF can be used as input. Output formats include MP3, WAV, OGG, FLAC, AAC, M4A, and OPUS.'),
            ('Are my files stored on a server?',
             'No. All conversion happens inside your browser only. Files are never sent to any external server.'),
            ('Why does the first conversion take longer?',
             'The FFmpeg conversion engine (~30 MB) is downloaded once on first use. Subsequent conversions use the cached version and are much faster.'),
        ],
        'h1': 'Audio Format Converter – Free Online',
        'tool_desc': 'Convert MP3, WAV, OGG, FLAC, AAC, M4A audio files in your browser. Set bitrate and sample rate. Files are never sent to a server.',
        'breadcrumb': 'Audio Convert',
        'cross_banner_text': 'Need to work with images or PDF files too?',
        'cross_banner_link_text': '🖼️ WooaImage – Image Tools →',
        'cross_banner_href': 'https://imagekit.wooahouse.com/',
    },
    'audio-cut.html': {
        'title': 'Audio Cutter Free Online – Cut MP3 WAV FLAC by Time Range | WooaAudio',
        'desc':  'Cut and trim MP3, WAV, FLAC audio files for free. Set start and end time in seconds, download the trimmed audio instantly. Browser-based, no server upload.',
        'kw':    'audio cutter, MP3 cutter, audio trimmer, cut audio online free, trim audio, audio clip extractor, WAV cutter, FLAC cutter, online audio editor',
        'og_title': 'Audio Cutter Free Online – Trim MP3 WAV FLAC | WooaAudio',
        'og_desc':  'Trim audio files by setting start and end time. Cut MP3, WAV, FLAC and more for free. No server upload.',
        'app_name': 'Audio Cutter',
        'faq': [
            ('What formats are supported?',
             'MP3, WAV, OGG, FLAC, AAC, M4A, OPUS, and AIFF can be used as input.'),
            ('What does the "Current Position" button do?',
             'While playing audio, click "Current Position" to automatically fill the start or end time with the playback position.'),
            ('Why does the first cut take longer?',
             'The FFmpeg engine (~30 MB) is downloaded once on first use and cached for subsequent operations.'),
        ],
        'h1': 'Audio Cutter – Free Online',
        'tool_desc': 'Upload an audio file and cut out the section you want by setting start and end time. Files are processed in your browser — never stored on a server.',
        'breadcrumb': 'Audio Cut',
        'cross_banner_text': 'Want to merge multiple audio files into one?',
        'cross_banner_link_text': '🔗 Audio Merge →',
        'cross_banner_href': '../audio-merge.html',
    },
    'audio-fade.html': {
        'title': 'Audio Fade In & Fade Out Free Online – Smooth Audio Fade Effect | WooaAudio',
        'desc':  'Add fade-in and fade-out effects to MP3, WAV, FLAC audio files for free. Set fade duration and apply smooth transitions. Browser-based, no server upload.',
        'kw':    'audio fade in, audio fade out, fade in fade out audio, audio fade effect, MP3 fade, WAV fade, smooth audio transition, free audio editor online',
        'og_title': 'Audio Fade In & Fade Out Free Online | WooaAudio',
        'og_desc':  'Apply smooth fade-in and fade-out effects to your audio. Free, no signup, files never uploaded.',
        'app_name': 'Audio Fade Tool',
        'faq': [
            ('What is a fade-in/fade-out effect?',
             'Fade-in gradually increases volume at the start of a track. Fade-out gradually decreases volume at the end for a smooth finish.'),
            ('Can I apply only fade-in or only fade-out?',
             'Yes. You can apply just fade-in, just fade-out, or both simultaneously.'),
            ('Are files uploaded to a server?',
             'No. All processing happens locally in your browser. Your files are never sent anywhere.'),
        ],
        'h1': 'Audio Fade In & Fade Out – Free Online',
        'tool_desc': 'Apply smooth fade-in and fade-out effects to your audio file. Set the fade duration and download the result. All processing runs in your browser.',
        'breadcrumb': 'Audio Fade',
        'cross_banner_text': 'Want to cut a specific section from your audio?',
        'cross_banner_link_text': '✂️ Audio Cutter →',
        'cross_banner_href': '../audio-cut.html',
    },
    'audio-flac.html': {
        'title': 'FLAC Converter Free Online – Convert Audio to FLAC Lossless | WooaAudio',
        'desc':  'Convert MP3, WAV, OGG, AAC audio to FLAC lossless format for free. Browser-based conversion, no server upload, no quality loss.',
        'kw':    'FLAC converter, convert to FLAC, audio to FLAC, MP3 to FLAC, WAV to FLAC, lossless audio converter, free FLAC converter online',
        'og_title': 'FLAC Converter Free Online – Lossless Audio | WooaAudio',
        'og_desc':  'Convert audio files to FLAC lossless format. Free, no signup. All processing in your browser.',
        'app_name': 'FLAC Converter',
        'faq': [
            ('What is FLAC format?',
             'FLAC (Free Lossless Audio Codec) compresses audio without any quality loss, making it ideal for archiving music.'),
            ('What formats can be converted to FLAC?',
             'MP3, WAV, OGG, AAC, M4A, OPUS, and AIFF can all be converted to FLAC.'),
            ('Are files sent to a server?',
             'No. All conversion happens locally in your browser. Your files are never uploaded anywhere.'),
        ],
        'h1': 'FLAC Converter – Free Online',
        'tool_desc': 'Convert your audio files to FLAC lossless format. Preserve full audio quality for archiving. All conversion runs in your browser — no server upload.',
        'breadcrumb': 'FLAC Convert',
        'cross_banner_text': 'Want to convert audio to MP3 instead?',
        'cross_banner_link_text': '🎧 MP3 Converter →',
        'cross_banner_href': '../audio-mp3.html',
    },
    'audio-info.html': {
        'title': 'Audio Info Free Online – Check MP3 WAV Duration, Sample Rate & Metadata | WooaAudio',
        'desc':  'Instantly check audio file info: duration, sample rate, channels, bitrate and file size. Works with MP3, WAV, FLAC and more. Browser-based, no upload.',
        'kw':    'audio info, audio metadata, MP3 info, audio duration, sample rate checker, audio file info online free, bitrate checker, audio properties',
        'og_title': 'Audio Info Free Online – Duration, Bitrate, Channels | WooaAudio',
        'og_desc':  'Check audio file properties: duration, sample rate, channels, bitrate. Free, no signup, no server upload.',
        'app_name': 'Audio Info Tool',
        'faq': [
            ('What information is displayed?',
             'Duration, sample rate, number of channels, bitrate, file size, and file format are all shown.'),
            ('What formats are supported?',
             'MP3, WAV, OGG, FLAC, AAC, M4A, OPUS, and AIFF are all supported.'),
            ('Is the audio file uploaded to a server?',
             'No. All information is read directly in your browser. No files are sent to any server.'),
        ],
        'h1': 'Audio Info – Free Online',
        'tool_desc': 'Upload an audio file to instantly view its properties: duration, sample rate, channels, bitrate, and more. All processing happens in your browser.',
        'breadcrumb': 'Audio Info',
        'cross_banner_text': 'Want to visualize the audio waveform?',
        'cross_banner_link_text': '📈 Waveform Visualizer →',
        'cross_banner_href': '../audio-waveform.html',
    },
    'audio-merge.html': {
        'title': 'Audio Merger Free Online – Combine MP3 WAV FLAC Files | WooaAudio',
        'desc':  'Merge multiple MP3, WAV, FLAC audio files into one for free. Drag & drop to reorder, then combine. Browser-based — files never sent to a server.',
        'kw':    'audio merger, merge audio files, combine MP3, join audio, MP3 merger, WAV merger, FLAC merger, audio combiner online free',
        'og_title': 'Audio Merger Free Online – Combine Audio Files | WooaAudio',
        'og_desc':  'Combine multiple audio files into one. Drag to reorder, then merge. Free, no signup, no server upload.',
        'app_name': 'Audio Merger',
        'faq': [
            ('How many files can I merge?',
             'There is no strict limit on the number of files. Add as many as you need.'),
            ('Can I reorder files before merging?',
             'Yes. Drag and drop the files to arrange them in the order you want before merging.'),
            ('Why does the first merge take longer?',
             'The FFmpeg engine (~30 MB) is downloaded once on first use and cached for all subsequent operations.'),
        ],
        'h1': 'Audio Merge – Free Online',
        'tool_desc': 'Upload multiple audio files and combine them into one. Drag to reorder, then click Merge. All processing runs in your browser.',
        'breadcrumb': 'Audio Merge',
        'cross_banner_text': 'Want to cut a section from your audio first?',
        'cross_banner_link_text': '✂️ Audio Cutter →',
        'cross_banner_href': '../audio-cut.html',
    },
    'audio-mp3.html': {
        'title': 'MP3 Converter Free Online – Convert WAV FLAC OGG AAC to MP3 | WooaAudio',
        'desc':  'Convert WAV, FLAC, OGG, AAC, M4A audio files to MP3 for free in your browser. Set bitrate from 128 to 320 kbps. No server upload.',
        'kw':    'MP3 converter, convert to MP3, WAV to MP3, FLAC to MP3, AAC to MP3, OGG to MP3, free MP3 converter online, audio to MP3',
        'og_title': 'MP3 Converter Free Online – WAV FLAC OGG to MP3 | WooaAudio',
        'og_desc':  'Convert audio files to MP3. Set bitrate 128–320 kbps. Free, no signup. All done in your browser.',
        'app_name': 'MP3 Converter',
        'faq': [
            ('What formats can be converted to MP3?',
             'WAV, FLAC, OGG, AAC, M4A, OPUS, and AIFF can all be converted to MP3.'),
            ('Which bitrate should I choose?',
             '128 kbps is fine for casual listening. 192–320 kbps is recommended for higher quality output.'),
            ('Are files sent to a server?',
             'No. All conversion happens locally in your browser. Your files are never uploaded anywhere.'),
        ],
        'h1': 'MP3 Converter – Free Online',
        'tool_desc': 'Convert audio files to MP3 format. Choose bitrate from 128 to 320 kbps. All conversion runs in your browser — no server upload.',
        'breadcrumb': 'MP3 Convert',
        'cross_banner_text': 'Want to convert to lossless FLAC instead?',
        'cross_banner_link_text': '💿 FLAC Converter →',
        'cross_banner_href': '../audio-flac.html',
    },
    'audio-pitch.html': {
        'title': 'Audio Pitch Changer Free Online – Raise or Lower Key of MP3 WAV | WooaAudio',
        'desc':  'Change the pitch of MP3, WAV, FLAC audio files for free. Raise or lower the key by semitones without changing playback speed. Browser-based.',
        'kw':    'audio pitch changer, change pitch, pitch shifter online free, raise pitch audio, lower pitch audio, key changer, semitone pitch shift, MP3 pitch',
        'og_title': 'Audio Pitch Changer Free Online – Semitone Key Shift | WooaAudio',
        'og_desc':  'Raise or lower audio pitch by semitones. Change musical key without affecting speed. Free, no signup.',
        'app_name': 'Audio Pitch Changer',
        'faq': [
            ('What is pitch shifting?',
             'Pitch shifting changes the musical key of an audio file — raising or lowering the tone — without affecting the playback speed.'),
            ('By how many semitones can I shift?',
             'You can shift pitch up or down by up to 12 semitones (1 octave) in either direction.'),
            ('Are files uploaded to a server?',
             'No. All processing happens locally in your browser. Your files are never sent anywhere.'),
        ],
        'h1': 'Audio Pitch Changer – Free Online',
        'tool_desc': 'Upload an audio file and change its pitch in semitone steps. Raise or lower the musical key without changing tempo. All runs in your browser.',
        'breadcrumb': 'Audio Pitch',
        'cross_banner_text': 'Want to change the playback speed too?',
        'cross_banner_link_text': '⏱️ Audio Speed →',
        'cross_banner_href': '../audio-speed.html',
    },
    'audio-record.html': {
        'title': 'Online Audio Recorder Free – Record Microphone & Download MP3 WAV | WooaAudio',
        'desc':  'Record audio from your microphone for free in your browser. Download recordings as MP3 or WAV instantly. Waveform visualized in real time. No server upload.',
        'kw':    'online audio recorder, microphone recorder, record audio online free, voice recorder, record MP3, record WAV, browser audio recorder, waveform recorder',
        'og_title': 'Online Audio Recorder Free – Mic Record & Download | WooaAudio',
        'og_desc':  'Record from your microphone and download as MP3 or WAV. Real-time waveform display. Free, no signup.',
        'app_name': 'Audio Recorder',
        'faq': [
            ('What format will the recording be saved in?',
             'You can download the recording as MP3 or WAV depending on your browser\'s supported formats.'),
            ('Is the recording uploaded to a server?',
             'No. Everything is processed locally in your browser. Your recordings are never stored on any server.'),
            ('Does this work on mobile?',
             'Yes. Most modern mobile browsers support microphone recording. Grant microphone permission when prompted.'),
        ],
        'h1': 'Audio Recorder – Free Online',
        'tool_desc': 'Record audio directly from your microphone. Real-time waveform display. Download instantly as MP3 or WAV. Everything runs in your browser.',
        'breadcrumb': 'Audio Record',
        'cross_banner_text': 'Want to edit your recording after saving?',
        'cross_banner_link_text': '✂️ Audio Cutter →',
        'cross_banner_href': '../audio-cut.html',
    },
    'audio-ringtone.html': {
        'title': 'Ringtone Maker Free Online – Cut MP3 to 30-Second Ringtone | WooaAudio',
        'desc':  'Create ringtones from MP3, WAV, or FLAC audio for free. Extract a 30-second or shorter clip from any song. Browser-based, no server upload.',
        'kw':    'ringtone maker, make ringtone, create ringtone online free, MP3 ringtone, cut ringtone, iPhone ringtone, Android ringtone, 30 second audio clip',
        'og_title': 'Ringtone Maker Free Online – Create MP3 Ringtones | WooaAudio',
        'og_desc':  'Cut any song to create a ringtone under 30 seconds. Free, no signup. Files never uploaded to server.',
        'app_name': 'Ringtone Maker',
        'faq': [
            ('What file formats are supported as input?',
             'MP3, WAV, OGG, FLAC, AAC, M4A, and OPUS can be used to create ringtones.'),
            ('Is there a length limit for ringtones?',
             'For best compatibility with smartphones, keep ringtones under 30 seconds.'),
            ('Are files uploaded to a server?',
             'No. All processing happens locally in your browser. Your files are never sent anywhere.'),
        ],
        'h1': 'Ringtone Maker – Free Online',
        'tool_desc': 'Extract a short clip from any audio file to create a ringtone. Set start and end time, keep it under 30 seconds, and download. All in your browser.',
        'breadcrumb': 'Ringtone Maker',
        'cross_banner_text': 'Want to cut a longer section from your audio?',
        'cross_banner_link_text': '✂️ Audio Cutter →',
        'cross_banner_href': '../audio-cut.html',
    },
    'audio-speed.html': {
        'title': 'Audio Speed Changer Free Online – Change Playback Speed of MP3 WAV | WooaAudio',
        'desc':  'Change the playback speed of MP3, WAV, FLAC audio files for free. Speed up or slow down without changing pitch. Browser-based, no server upload.',
        'kw':    'audio speed changer, change audio speed, slow down audio, speed up audio, MP3 speed changer, playback speed audio, tempo changer online free',
        'og_title': 'Audio Speed Changer Free Online – Speed Up or Slow Down | WooaAudio',
        'og_desc':  'Change audio playback speed without affecting pitch. Free, no signup. All done in your browser.',
        'app_name': 'Audio Speed Changer',
        'faq': [
            ('Will changing speed affect the pitch?',
             'You can choose to keep pitch unchanged while changing speed, or allow pitch to shift with speed.'),
            ('What speed range is available?',
             'Speed can typically be adjusted from 0.5x (half speed) to 2x (double speed).'),
            ('Are files uploaded to a server?',
             'No. All processing happens locally in your browser. Your files are never sent anywhere.'),
        ],
        'h1': 'Audio Speed Changer – Free Online',
        'tool_desc': 'Upload an audio file and change its playback speed. Speed up or slow down without affecting pitch. All processing runs in your browser.',
        'breadcrumb': 'Audio Speed',
        'cross_banner_text': 'Want to change the pitch of your audio?',
        'cross_banner_link_text': '🎵 Audio Pitch Changer →',
        'cross_banner_href': '../audio-pitch.html',
    },
    'audio-tag.html': {
        'title': 'Audio Tag Editor Free Online – Edit MP3 ID3 Tags, Title, Artist, Album | WooaAudio',
        'desc':  'Edit MP3 ID3 tags (title, artist, album, cover art) for free in your browser. View and modify audio metadata instantly. No server upload.',
        'kw':    'audio tag editor, MP3 tag editor, ID3 tag editor, edit MP3 metadata, audio metadata, album art editor, MP3 title artist album, free tag editor online',
        'og_title': 'Audio Tag Editor Free Online – ID3 MP3 Metadata | WooaAudio',
        'og_desc':  'Edit MP3 ID3 tags: title, artist, album, year, genre, and cover art. Free, no signup, no server upload.',
        'app_name': 'Audio Tag Editor',
        'faq': [
            ('What tags can I edit?',
             'You can edit title, artist, album, year, genre, track number, and album cover art (ID3 tags).'),
            ('Which formats are supported?',
             'MP3 with ID3 tags is the primary format supported. Other formats may have limited tag support.'),
            ('Are my files uploaded to a server?',
             'No. All tag reading and writing happens in your browser. Your files are never sent anywhere.'),
        ],
        'h1': 'Audio Tag Editor – Free Online',
        'tool_desc': 'Upload an MP3 to view and edit its metadata tags: title, artist, album, year, genre, and cover art. All editing happens in your browser.',
        'breadcrumb': 'Audio Tag',
        'cross_banner_text': 'Want to check full audio file properties?',
        'cross_banner_link_text': 'ℹ️ Audio Info →',
        'cross_banner_href': '../audio-info.html',
    },
    'audio-volume.html': {
        'title': 'Audio Volume Booster Free Online – Increase MP3 WAV Volume | WooaAudio',
        'desc':  'Boost or reduce the volume of MP3, WAV, FLAC audio files for free. Normalize audio levels or amplify by dB. Browser-based, no server upload.',
        'kw':    'audio volume booster, increase audio volume, MP3 volume booster, normalize audio, amplify audio, volume control audio online free, WAV volume',
        'og_title': 'Audio Volume Booster Free Online – Amplify MP3 WAV | WooaAudio',
        'og_desc':  'Boost or reduce audio volume. Normalize levels or amplify by dB. Free, no signup, no server upload.',
        'app_name': 'Audio Volume Booster',
        'faq': [
            ('Can I both increase and decrease volume?',
             'Yes. You can amplify (increase) or reduce volume, and also normalize the audio to a target level.'),
            ('What is audio normalization?',
             'Normalization adjusts the audio so its peak volume reaches a target level, making quiet recordings sound louder without clipping.'),
            ('Are files uploaded to a server?',
             'No. All processing happens locally in your browser. Your files are never sent anywhere.'),
        ],
        'h1': 'Audio Volume Booster – Free Online',
        'tool_desc': 'Upload an audio file to boost or reduce its volume. Normalize audio levels or amplify by dB. All processing runs in your browser.',
        'breadcrumb': 'Audio Volume',
        'cross_banner_text': 'Want to cut or trim the audio too?',
        'cross_banner_link_text': '✂️ Audio Cutter →',
        'cross_banner_href': '../audio-cut.html',
    },
    'audio-wav.html': {
        'title': 'WAV Converter Free Online – Convert Audio to WAV Lossless | WooaAudio',
        'desc':  'Convert MP3, FLAC, OGG, AAC audio to WAV lossless format for free. Browser-based conversion, no server upload, full quality preserved.',
        'kw':    'WAV converter, convert to WAV, audio to WAV, MP3 to WAV, FLAC to WAV, lossless WAV converter, free WAV converter online',
        'og_title': 'WAV Converter Free Online – Lossless Audio | WooaAudio',
        'og_desc':  'Convert audio files to WAV lossless format. Free, no signup. All processing in your browser.',
        'app_name': 'WAV Converter',
        'faq': [
            ('What is WAV format?',
             'WAV (Waveform Audio File Format) is an uncompressed lossless audio format with no quality loss, ideal for audio production and editing.'),
            ('What formats can be converted to WAV?',
             'MP3, FLAC, OGG, AAC, M4A, OPUS, and AIFF can all be converted to WAV.'),
            ('Are files sent to a server?',
             'No. All conversion happens locally in your browser. Your files are never uploaded anywhere.'),
        ],
        'h1': 'WAV Converter – Free Online',
        'tool_desc': 'Convert your audio files to WAV lossless format. Full quality preservation for music production. All conversion runs in your browser — no server upload.',
        'breadcrumb': 'WAV Convert',
        'cross_banner_text': 'Want to convert audio to MP3 instead?',
        'cross_banner_link_text': '🎧 MP3 Converter →',
        'cross_banner_href': '../audio-mp3.html',
    },
    'audio-waveform.html': {
        'title': 'Audio Waveform Visualizer Free Online – MP3 WAV Waveform Image | WooaAudio',
        'desc':  'Visualize audio waveforms from MP3, WAV, FLAC files for free. Save waveform as PNG image. Browser-based audio analysis — no server upload.',
        'kw':    'audio waveform, waveform visualizer, MP3 waveform, audio wave image, waveform PNG, audio visualization online free, WAV waveform, audio analyzer',
        'og_title': 'Audio Waveform Visualizer Free Online – MP3 WAV | WooaAudio',
        'og_desc':  'Visualize audio waveform and save as PNG. Free, no signup. All processing in your browser.',
        'app_name': 'Audio Waveform Visualizer',
        'faq': [
            ('What formats are supported?',
             'MP3, WAV, OGG, FLAC, AAC, M4A, and OPUS are all supported.'),
            ('Can I save the waveform image?',
             'Yes. The waveform is rendered on a canvas and can be downloaded as a PNG image.'),
            ('Is the audio file uploaded to a server?',
             'No. All processing is done locally in your browser. Your files are never sent anywhere.'),
        ],
        'h1': 'Audio Waveform Visualizer – Free Online',
        'tool_desc': 'Upload an audio file to visualize its waveform. Save the waveform as a PNG image. All processing runs locally in your browser — no server upload.',
        'breadcrumb': 'Waveform',
        'cross_banner_text': 'Want to check detailed audio file information?',
        'cross_banner_link_text': 'ℹ️ Audio Info →',
        'cross_banner_href': '../audio-info.html',
    },
    'audio-mr.html': {
        'title': 'Vocal Remover Free Online – Make Karaoke MR Backing Track | WooaAudio',
        'desc':  'Remove vocals from MP3, WAV music files for free and create a karaoke backing track (MR). Browser-based — files are never sent to a server.',
        'kw':    'vocal remover, remove vocals from song, karaoke maker, backing track maker, MR maker, vocal remover online free, instrumental track, MP3 vocal removal',
        'og_title': 'Vocal Remover Free Online – Karaoke MR Maker | WooaAudio',
        'og_desc':  'Remove vocals from MP3/WAV to create an instrumental backing track. Free, no signup, no server upload.',
        'app_name': 'Vocal Remover – MR Maker',
        'faq': [
            ('Does vocal removal work perfectly?',
             'For stereo tracks with center-panned vocals, removal is quite effective. Results may vary for mono tracks or heavily reverbed vocals.'),
            ('Are my files uploaded to a server?',
             'No. All processing happens in your browser only. Files are never sent to any external server.'),
            ('What formats are supported?',
             'MP3, WAV, OGG, FLAC, AAC, and M4A are supported.'),
            ('Why does the first conversion take longer?',
             'The FFmpeg engine (~30 MB) is downloaded once on first use and cached for subsequent operations.'),
            ('Can I use the MR for public performances?',
             'The original track copyright belongs to its creator. Use for personal practice only. Always verify copyright before public use or broadcast.'),
        ],
        'h1': 'Vocal Remover – Free Online MR Maker',
        'tool_desc': 'Remove vocals from MP3 or WAV music to create an instrumental backing track (MR). Files are processed in your browser — never stored on a server.',
        'breadcrumb': 'MR Maker',
        'cross_banner_text': 'Want to cut the resulting MR to a specific section?',
        'cross_banner_link_text': '✂️ Audio Cutter →',
        'cross_banner_href': '../audio-cut.html',
    },
    'audio-metronome.html': {
        'title': 'Online Metronome Free – BPM, Time Signature & Tap Tempo | WooaAudio',
        'desc':  'Free online metronome with BPM control, time signature selection (2/4, 3/4, 4/4, 6/8) and tap tempo. Perfect for instrument practice and music composition.',
        'kw':    'online metronome, free metronome, BPM metronome, tap tempo, metronome online free, music practice metronome, guitar metronome, drum metronome, beat counter',
        'og_title': 'Online Metronome Free – BPM & Tap Tempo | WooaAudio',
        'og_desc':  'Free online metronome. Set BPM, choose time signature, use tap tempo. No install needed.',
        'app_name': 'Online Metronome',
        'faq': [
            ('What is Tap Tempo?',
             'Tap the "Tap Tempo" button repeatedly in time with a song to automatically calculate its BPM.'),
            ('How is beat 1 (the accent) indicated?',
             'The first beat plays at a higher pitch and is highlighted more brightly on the visual indicator.'),
            ('What BPM range is supported?',
             'From 40 BPM (Grave) to 240 BPM (Prestissimo). Adjust in steps of 1 using the slider or buttons.'),
        ],
        'h1': 'Online Metronome – Free',
        'tool_desc': 'Set BPM and time signature, use tap tempo. Ideal for instrument practice and composition. No install needed.',
        'breadcrumb': 'Metronome',
        'cross_banner_text': 'Want to check your instrument tuning too?',
        'cross_banner_link_text': '🎸 Instrument Tuner →',
        'cross_banner_href': '../audio-tuner.html',
    },
    'audio-tuner.html': {
        'title': 'Guitar Tuner Online Free – Chromatic Instrument Tuner | WooaAudio',
        'desc':  'Free online chromatic tuner. Detects pitch from your microphone and shows note name, frequency, octave, and deviation in cents. Works for guitar, bass, violin and all instruments.',
        'kw':    'guitar tuner online, online tuner, chromatic tuner, instrument tuner, guitar tuning online free, bass tuner, violin tuner, ukulele tuner, pitch detector',
        'og_title': 'Guitar Tuner Online Free – Chromatic Instrument Tuner | WooaAudio',
        'og_desc':  'Detect pitch from mic and display note name, frequency, and deviation in real time. Free chromatic tuner for all instruments.',
        'app_name': 'Online Chromatic Tuner',
        'faq': [
            ('What instruments can I use this for?',
             'As a chromatic tuner, it works for guitar, bass, violin, cello, ukulele, mandolin, and any other instrument that produces a pitch.'),
            ('What is a cent?',
             'A cent is 1/100th of a semitone. ±10 cents is considered in tune; ±50 cents means you are a semitone off. Closer to 0 is more accurate.'),
            ('Do I need to grant microphone permission?',
             'Yes. Click "Start Tuning" and allow microphone access when prompted. Audio data is never sent to a server.'),
        ],
        'h1': 'Guitar Tuner Online Free – Chromatic Tuner',
        'tool_desc': 'Detects pitch from your microphone and displays the note name, frequency, octave, and tuning deviation in real time. Works for all instruments.',
        'breadcrumb': 'Instrument Tuner',
        'cross_banner_text': 'Want to practice with a metronome too?',
        'cross_banner_link_text': '🥁 Metronome →',
        'cross_banner_href': '../audio-metronome.html',
    },
    'audio-tts.html': {
        'title': 'Text to Speech Free Online – TTS Korean English Voice Reader | WooaAudio',
        'desc':  'Convert text to speech for free. Supports Korean, English and many other languages. Adjust speed and pitch. No install — works in your browser with Web Speech API.',
        'kw':    'text to speech, TTS online free, text to speech Korean, text reader online, voice synthesis free, TTS free, read text aloud, speech synthesis online',
        'og_title': 'Text to Speech Free Online – TTS Voice Reader | WooaAudio',
        'og_desc':  'Convert text to speech. Supports Korean, English and more. Adjust speed and pitch. Free, no signup.',
        'app_name': 'Text to Speech (TTS)',
        'faq': [
            ('Is Korean voice supported?',
             'Yes, Korean TTS voices available in your browser are used. Chrome and Edge support the most voices.'),
            ('Can I save the speech as an MP3 file?',
             'The Web Speech API does not directly support saving audio. Use the Audio Recorder tool alongside TTS, or use your system screen recording feature.'),
            ('How many characters can I convert at once?',
             'Up to 5,000 characters can be entered at a time.'),
            ('Which browser is recommended?',
             'Chrome or Edge is recommended for the widest language and voice support.'),
        ],
        'h1': 'Text to Speech – Free Online TTS',
        'tool_desc': 'Enter text and have it read aloud. Supports Korean, English and more. Adjust speed and pitch. All processing in your browser — no server upload.',
        'breadcrumb': 'Text to Speech',
        'cross_banner_text': 'Want to record audio directly from your microphone?',
        'cross_banner_link_text': '🎙 Audio Recorder →',
        'cross_banner_href': '../audio-record.html',
    },
    'audio-decibel.html': {
        'title': 'Decibel Meter Online Free – Sound Level Noise Measurement dB | WooaAudio',
        'desc':  'Measure ambient noise in real-time decibels (dB) using your microphone. Shows current, peak, and average dB. Free, no install. Useful for noise level monitoring.',
        'kw':    'decibel meter online, sound level meter, dB meter, noise meter online, measure noise online free, decibel measurement, sound measurement online, noise level checker',
        'og_title': 'Decibel Meter Online Free – Noise Level dB Measurement | WooaAudio',
        'og_desc':  'Measure ambient noise in real-time dB with your microphone. Shows current, peak and average. Free, no install.',
        'app_name': 'Decibel Meter',
        'faq': [
            ('Are the measurements accurate?',
             'Accuracy depends on microphone sensitivity, which varies by device. Use readings for relative comparison rather than absolute measurements. For precision, use a dedicated sound level meter.'),
            ('Do I need to grant microphone permission?',
             'Yes. Click "Start Measuring" and allow microphone access when prompted. Audio data is never sent to a server.'),
            ('What are typical noise level guidelines?',
             'Below 30 dB is very quiet (library). 30–50 dB is a quiet office. 50–70 dB is normal conversation. 70–90 dB is traffic noise. Above 90 dB can cause hearing damage.'),
        ],
        'h1': 'Decibel Meter – Free Online Noise Measurement',
        'tool_desc': 'Measure ambient noise levels in real-time dB using your microphone. Displays current, peak, and average readings with a noise level guide.',
        'breadcrumb': 'Decibel Meter',
        'cross_banner_text': 'Want to record the audio as well?',
        'cross_banner_link_text': '🎙 Audio Recorder →',
        'cross_banner_href': '../audio-record.html',
    },
}

# ── 2. 공통 문자열 치환 ──────────────────────────────────────────────────────
COMMON = [
    # lang
    ('<html lang="ko">', '<html lang="en">'),
    # locale
    ('ko_KR', 'en_US'),
    # inLanguage
    ('"inLanguage": "ko"', '"inLanguage": "en"'),
    # priceCurrency
    ('"priceCurrency": "KRW"', '"priceCurrency": "USD"'),
    ('"priceCurrency":"KRW"', '"priceCurrency":"USD"'),
    # paths: CSS, JS, manifest
    ('href="css/style.css"', 'href="../css/style.css"'),
    ('href="/manifest.json"', 'href="../manifest.json"'),
    ('src="js/', 'src="../js/'),
    ('href="js/', 'href="../js/'),

    # header nav
    ('>포맷 변환<', '>Convert<'),
    ('>MP3 변환<', '>MP3<'),
    ('>WAV 변환<', '>WAV<'),
    ('>FLAC 변환<', '>FLAC<'),
    ('>오디오 자르기<', '>Cut Audio<'),
    ('>오디오 합치기<', '>Merge Audio<'),
    ('>볼륨 조절<', '>Volume<'),
    ('>속도 조절<', '>Speed<'),
    ('>파형<', '>Waveform<'),
    ('>전체 도구 ›<', '>All Tools ›<'),
    ('>홈<', '>Home<'),

    # header-right 소개 링크
    ('>소개<', '>About<'),

    # hero section
    ('모든 오디오 작업 무료로, 한 곳에서', 'All Audio Tasks — Free, in One Place'),
    ('변환·자르기·합치기·볼륨 조절까지 <strong style="color:#FFD700;">100% 무료</strong><br>회원가입 없이, 파일은 서버에 저장되지 않아요',
     'Convert, Cut, Merge, Volume — <strong style="color:#FFD700;">100% Free</strong><br>No signup. Files never stored on a server.'),
    ('>📌 홈 화면에 추가<', '>📌 Add to Home Screen<'),

    # hero-related (index)
    ('문서 작업이 필요하다면?', 'Need to work with documents?'),
    ('WooaPDF 무료 PDF 도구 보기 →', 'WooaPDF Free PDF Tools →'),

    # index category
    ('<span class="category-title">변환</span>', '<span class="category-title">Convert</span>'),
    ('<p class="category-desc">MP3, WAV, OGG, FLAC 등 오디오 포맷 변환 도구</p>',
     '<p class="category-desc">Audio format conversion tools: MP3, WAV, OGG, FLAC and more</p>'),
    ('<span class="category-title">편집</span>', '<span class="category-title">Edit</span>'),
    ('<p class="category-desc">오디오 자르기, 합치기, 볼륨 조절 도구</p>',
     '<p class="category-desc">Audio editing tools: cut, merge, volume and more</p>'),
    ('<span class="category-title">분석</span>', '<span class="category-title">Analyze</span>'),
    ('<p class="category-desc">오디오 정보와 파형을 확인하는 도구</p>',
     '<p class="category-desc">Tools for checking audio info and waveforms</p>'),

    # tool card names (index)
    ('<div class="tool-name">오디오 포맷 변환</div>', '<div class="tool-name">Audio Format Converter</div>'),
    ('<div class="tool-name">MP3 변환</div>', '<div class="tool-name">MP3 Converter</div>'),
    ('<div class="tool-name">WAV 변환</div>', '<div class="tool-name">WAV Converter</div>'),
    ('<div class="tool-name">FLAC 변환</div>', '<div class="tool-name">FLAC Converter</div>'),
    ('<div class="tool-name">오디오 자르기</div>', '<div class="tool-name">Audio Cutter</div>'),
    ('<div class="tool-name">오디오 합치기</div>', '<div class="tool-name">Audio Merger</div>'),
    ('<div class="tool-name">볼륨 조절</div>', '<div class="tool-name">Volume Booster</div>'),
    ('<div class="tool-name">속도 조절</div>', '<div class="tool-name">Speed Changer</div>'),
    ('<div class="tool-name">오디오 녹음기</div>', '<div class="tool-name">Audio Recorder</div>'),
    ('<div class="tool-name">페이드인·페이드아웃</div>', '<div class="tool-name">Fade In & Fade Out</div>'),
    ('<div class="tool-name">피치 변경</div>', '<div class="tool-name">Pitch Changer</div>'),
    ('<div class="tool-name">벨소리 만들기</div>', '<div class="tool-name">Ringtone Maker</div>'),
    ('<div class="tool-name">파형 시각화</div>', '<div class="tool-name">Waveform Visualizer</div>'),
    ('<div class="tool-name">오디오 정보</div>', '<div class="tool-name">Audio Info</div>'),
    ('<div class="tool-name">태그 편집기</div>', '<div class="tool-name">Tag Editor</div>'),

    # tool card descs (index)
    ('<div class="tool-desc">MP3, WAV, OGG, FLAC, AAC 포맷 변환</div>',
     '<div class="tool-desc">Convert between MP3, WAV, OGG, FLAC, AAC</div>'),
    ('<div class="tool-desc">다양한 오디오 파일을 MP3로 변환</div>',
     '<div class="tool-desc">Convert any audio file to MP3</div>'),
    ('<div class="tool-desc">고품질 무압축 WAV 파일로 변환</div>',
     '<div class="tool-desc">Convert to high-quality uncompressed WAV</div>'),
    ('<div class="tool-desc">무손실 오디오 보관용 포맷 변환</div>',
     '<div class="tool-desc">Convert to lossless FLAC for archiving</div>'),
    ('<div class="tool-desc">원하는 구간만 잘라 저장</div>',
     '<div class="tool-desc">Cut and trim audio to any time range</div>'),
    ('<div class="tool-desc">여러 음원을 하나의 파일로 병합</div>',
     '<div class="tool-desc">Combine multiple audio files into one</div>'),
    ('<div class="tool-desc">소리 크기 증폭 및 정규화</div>',
     '<div class="tool-desc">Boost, reduce or normalize audio volume</div>'),
    ('<div class="tool-desc">재생 속도와 피치 조절</div>',
     '<div class="tool-desc">Adjust playback speed and pitch</div>'),
    ('<div class="tool-desc">마이크로 녹음 후 바로 다운로드, 파형 시각화</div>',
     '<div class="tool-desc">Record from mic and download, with waveform</div>'),
    ('<div class="tool-desc">오디오 시작·끝 부분에 자연스러운 페이드 효과 적용</div>',
     '<div class="tool-desc">Apply smooth fade-in and fade-out effects</div>'),
    ('<div class="tool-desc">음원 키 높이기·낮추기, 반음 단위 조절</div>',
     '<div class="tool-desc">Raise or lower pitch by semitone steps</div>'),
    ('<div class="tool-desc">음원 구간 추출로 30초 이하 벨소리 제작</div>',
     '<div class="tool-desc">Extract a clip to create a ringtone under 30 sec</div>'),
    ('<div class="tool-desc">오디오 파형을 브라우저에서 확인</div>',
     '<div class="tool-desc">Visualize audio waveform in browser</div>'),
    ('<div class="tool-desc">길이, 샘플레이트, 채널 정보 확인</div>',
     '<div class="tool-desc">Check duration, sample rate, channel info</div>'),
    ('<div class="tool-desc">MP3 제목·아티스트·앨범아트 등 ID3 태그 편집</div>',
     '<div class="tool-desc">Edit ID3 tags: title, artist, album art</div>'),

    # free/new badges
    ('>무료<', '>Free<'),

    # breadcrumb home
    ('>홈<', '>Home<'),

    # drop zone
    ('오디오 파일을 여기에 끌어다 놓으세요', 'Drop your audio file here'),
    ('MP3, WAV, OGG, FLAC, AAC, M4A, OPUS 지원 · 여러 파일 동시 선택 가능', 'Supports MP3, WAV, OGG, FLAC, AAC, M4A, OPUS · Multiple files supported'),
    ('MP3, WAV, OGG, FLAC, AAC, M4A, OPUS 지원', 'Supports MP3, WAV, OGG, FLAC, AAC, M4A, OPUS'),
    ('오디오 파일 선택', 'Select Audio File'),
    ('파일 선택', 'Select File'),

    # file panel
    ('>선택된 파일<', '>Selected Files<'),
    ('<div class="file-list-title">선택된 파일</div>', '<div class="file-list-title">Selected Files</div>'),

    # options titles
    ('<div class="options-title">변환 설정</div>', '<div class="options-title">Conversion Settings</div>'),
    ('<div class="options-title">자르기 설정</div>', '<div class="options-title">Cut Settings</div>'),
    ('<div class="options-title">합치기 설정</div>', '<div class="options-title">Merge Settings</div>'),
    ('<div class="options-title">볼륨 설정</div>', '<div class="options-title">Volume Settings</div>'),
    ('<div class="options-title">속도 설정</div>', '<div class="options-title">Speed Settings</div>'),
    ('<div class="options-title">페이드 설정</div>', '<div class="options-title">Fade Settings</div>'),
    ('<div class="options-title">피치 설정</div>', '<div class="options-title">Pitch Settings</div>'),
    ('<div class="options-title">녹음 설정</div>', '<div class="options-title">Recording Settings</div>'),
    ('<div class="options-title">태그 편집</div>', '<div class="options-title">Edit Tags</div>'),
    ('<div class="options-title">파형 설정</div>', '<div class="options-title">Waveform Settings</div>'),

    # option labels
    ('<span class="option-label">출력 포맷</span>', '<span class="option-label">Output Format</span>'),
    ('<span class="option-label">비트레이트</span>', '<span class="option-label">Bitrate</span>'),
    ('<span class="option-label">샘플레이트</span>', '<span class="option-label">Sample Rate</span>'),
    ('<span class="option-label">채널</span>', '<span class="option-label">Channels</span>'),
    ('<span class="option-label">시작 시간</span>', '<span class="option-label">Start Time</span>'),
    ('<span class="option-label">끝 시간</span>', '<span class="option-label">End Time</span>'),
    ('<span class="option-label">볼륨 배율</span>', '<span class="option-label">Volume Level</span>'),
    ('<span class="option-label">속도 배율</span>', '<span class="option-label">Speed Rate</span>'),
    ('<span class="option-label">페이드인 길이</span>', '<span class="option-label">Fade In Duration</span>'),
    ('<span class="option-label">페이드아웃 길이</span>', '<span class="option-label">Fade Out Duration</span>'),
    ('<span class="option-label">피치 조절</span>', '<span class="option-label">Pitch Shift</span>'),
    ('<span class="option-label">파형 색상</span>', '<span class="option-label">Waveform Color</span>'),
    ('<span class="option-label">배경 색상</span>', '<span class="option-label">Background Color</span>'),
    ('<span class="option-label">제목</span>', '<span class="option-label">Title</span>'),
    ('<span class="option-label">아티스트</span>', '<span class="option-label">Artist</span>'),
    ('<span class="option-label">앨범</span>', '<span class="option-label">Album</span>'),
    ('<span class="option-label">연도</span>', '<span class="option-label">Year</span>'),
    ('<span class="option-label">장르</span>', '<span class="option-label">Genre</span>'),
    ('<span class="option-label">트랙 번호</span>', '<span class="option-label">Track No.</span>'),

    # select options (format)
    ('<option value="mp3">MP3 - 범용 호환</option>', '<option value="mp3">MP3 - Universal</option>'),
    ('<option value="wav">WAV - 고품질 무압축</option>', '<option value="wav">WAV - Lossless</option>'),
    ('<option value="ogg">OGG - 웹 친화 포맷</option>', '<option value="ogg">OGG - Web Friendly</option>'),
    ('<option value="flac">FLAC - 무손실 압축</option>', '<option value="flac">FLAC - Lossless</option>'),
    ('<option value="aac">AAC - 모바일 친화</option>', '<option value="aac">AAC - Mobile Friendly</option>'),
    ('<option value="m4a">M4A - Apple 호환</option>', '<option value="m4a">M4A - Apple Compatible</option>'),
    ('<option value="opus">OPUS - 고효율 압축</option>', '<option value="opus">OPUS - High Efficiency</option>'),

    # bitrate options
    ('<option value="96k">96 kbps - 작은 용량</option>', '<option value="96k">96 kbps - Small size</option>'),
    ('<option value="128k" selected>128 kbps - 표준</option>', '<option value="128k" selected>128 kbps - Standard</option>'),
    ('<option value="192k">192 kbps - 고음질</option>', '<option value="192k">192 kbps - High quality</option>'),
    ('<option value="256k">256 kbps - 매우 고음질</option>', '<option value="256k">256 kbps - Very high quality</option>'),
    ('<option value="320k">320 kbps - 최고 음질</option>', '<option value="320k">320 kbps - Best quality</option>'),

    # sample rate options
    ('<option value="">원본 유지</option>', '<option value="">Keep original</option>'),

    # channel options
    ('<option value="1">모노</option>', '<option value="1">Mono</option>'),
    ('<option value="2">스테레오</option>', '<option value="2">Stereo</option>'),

    # cut page specifics
    ('(분 : 초)', '(min : sec)'),
    ('>현재 위치<', '>Current Position<'),

    # buttons
    ('>변환 시작<', '>Convert<'),
    ('변환 시작', 'Convert'),
    ('>✂️ 자르기 시작<', '>✂️ Cut Audio<'),
    ('✂️ 자르기 시작', '✂️ Cut Audio'),
    ('>🔗 합치기 시작<', '>🔗 Merge<'),
    ('🔗 합치기 시작', '🔗 Merge'),
    ('>🔊 볼륨 조절<', '>🔊 Adjust Volume<'),
    ('>⏱️ 속도 변경<', '>⏱️ Change Speed<'),
    ('>🎵 피치 변경<', '>🎵 Change Pitch<'),
    ('>📉 페이드 적용<', '>📉 Apply Fade<'),
    ('>🎙️ 녹음 시작<', '>🎙️ Start Recording<'),
    ('>⏹️ 녹음 중지<', '>⏹️ Stop Recording<'),
    ('>⬇️ 다운로드<', '>⬇️ Download<'),
    ('⬇️ 다운로드', '⬇️ Download'),
    ('>📈 파형 생성<', '>📈 Generate Waveform<'),
    ('>🖼️ PNG 저장<', '>🖼️ Save as PNG<'),
    ('>💾 태그 저장<', '>💾 Save Tags<'),
    ('>+ 파일 추가<', '>+ Add File<'),
    ('>파일 추가<', '>Add File<'),

    # progress
    ('변환 중...', 'Processing...'),
    ('처리 중...', 'Processing...'),
    ('자르기 중...', 'Cutting...'),
    ('합치기 중...', 'Merging...'),
    ('⏳ 처리 중입니다. 완료되면 자동으로 닫힙니다.', '⏳ Processing. This will close automatically when done.'),
    ('⏳ 변환 중입니다. 완료되면 자동으로 닫힙니다.', '⏳ Converting. This will close automatically when done.'),

    # progress spans
    ('<span id="progressText">변환 중...</span>', '<span id="progressText">Processing...</span>'),
    ('<span id="progressText">처리 중...</span>', '<span id="progressText">Processing...</span>'),

    # result titles
    ('<div class="result-title">변환 완료!</div>', '<div class="result-title">Done!</div>'),
    ('<div class="result-title">자르기 완료!</div>', '<div class="result-title">Cut Complete!</div>'),
    ('<div class="result-title">합치기 완료!</div>', '<div class="result-title">Merged!</div>'),
    ('<div class="result-title">완료!</div>', '<div class="result-title">Done!</div>'),

    # reset buttons
    ('>다시 변환<', '>Convert Again<'),
    ('>다시 자르기<', '>Cut Again<'),
    ('>다시 시작<', '>Start Over<'),
    ('다시 변환', 'Convert Again'),

    # player panel
    ('총 길이:', 'Duration:'),

    # features section
    ('<div class="feature-title">100% 안전</div>', '<div class="feature-title">100% Safe</div>'),
    ('<div class="feature-desc">파일이 서버로 전송되지 않습니다. 모든 처리가 브라우저 안에서 이루어집니다.</div>',
     '<div class="feature-desc">Files are never sent to a server. All processing happens inside your browser.</div>'),
    ('<div class="feature-title">빠른 처리</div>', '<div class="feature-title">Fast Processing</div>'),
    ('<div class="feature-desc">업로드 대기 없이 로컬에서 처리하므로 반복 작업이 간편합니다.</div>',
     '<div class="feature-desc">Local processing with no upload wait — repeat tasks are quick and easy.</div>'),
    ('<div class="feature-title">완전 무료</div>', '<div class="feature-title">Completely Free</div>'),
    ('<div class="feature-desc">회원가입 없이 주요 오디오 기능을 무료로 사용할 수 있습니다.</div>',
     '<div class="feature-desc">All major audio features are free — no signup required.</div>'),
    ('<div class="feature-title">모든 기기 지원</div>', '<div class="feature-title">All Devices</div>'),
    ('<div class="feature-desc">PC, 태블릿, 스마트폰 어디서나 사용 가능한 반응형 디자인.</div>',
     '<div class="feature-desc">Responsive design works on PC, tablet, and smartphone.</div>'),

    # footer brand desc
    ('<p>무료 온라인 오디오 도구 모음. 변환, 편집, 분석 작업을 브라우저에서 안전하게 처리하세요.</p>',
     '<p>Free online audio toolkit. Convert, edit, and analyze audio safely in your browser.</p>'),

    # footer links section heading
    ('<h4>오디오 변환·편집</h4>', '<h4>Audio Tools</h4>'),
    ('<h4>오디오 변환</h4>', '<h4>Audio Conversion</h4>'),
    ('<h4>WooaHouse 서비스</h4>', '<h4>WooaHouse Services</h4>'),

    # footer link texts
    ('>오디오 포맷 변환<', '>Audio Converter<'),
    ('>MP3 변환<', '>MP3 Converter<'),
    ('>WAV 변환<', '>WAV Converter<'),
    ('>FLAC 변환<', '>FLAC Converter<'),
    ('>오디오 자르기<', '>Audio Cutter<'),
    ('>오디오 합치기<', '>Audio Merger<'),
    ('>볼륨 조절<', '>Volume Booster<'),
    ('>속도 조절<', '>Speed Changer<'),
    ('>파형 시각화<', '>Waveform Visualizer<'),
    ('>오디오 정보<', '>Audio Info<'),
    ('>오디오 녹음기<', '>Audio Recorder<'),
    ('>페이드인·페이드아웃<', '>Fade In & Out<'),
    ('>피치 변경<', '>Pitch Changer<'),
    ('>벨소리 만들기<', '>Ringtone Maker<'),
    ('>태그 편집기<', '>Tag Editor<'),

    # footer footer text
    ('모든 권리 보유.', 'All rights reserved.'),
    ('>개인정보처리방침<', '>Privacy Policy<'),
    ('href="privacy.html"', 'href="../privacy.html"'),
    ('href="about.html"', 'href="../about.html"'),

    # FAQ heading
    ('>자주 묻는 질문<', '>Frequently Asked Questions<'),

    # cross-link banners (tool pages)
    ('이미지나 PDF 파일 작업도 필요하신가요?', 'Need to work with images or PDF files too?'),
    ('여러 음원을 하나로 합치고 싶으신가요?', 'Want to merge multiple audio files into one?'),
    ('>🔗 오디오 합치기 →<', '>🔗 Audio Merge →<'),
    ('🔗 오디오 합치기 →', '🔗 Audio Merge →'),
    ('>🖼️ WooaImage 이미지 도구 →<', '>🖼️ WooaImage Tools →<'),
    ('🖼️ WooaImage 이미지 도구 →', '🖼️ WooaImage Tools →'),

    # JS error messages
    ("'파일을 선택해주세요.'", "'Please select a file.'"),
    ("'오디오 파일을 선택해주세요.'", "'Please select an audio file.'"),
    ("'지원하지 않는 파일 형식입니다.'", "'Unsupported file format.'"),
    ("'변환 중 오류가 발생했습니다.'", "'Conversion failed.'"),
    ("'처리 중 오류가 발생했습니다.'", "'Processing failed.'"),
    ("'파일을 읽을 수 없습니다.'", "'Cannot read file.'"),

    # audio-convert specific JS messages
    ("btn.textContent = '⏳ 변환 중...';", "btn.textContent = '⏳ Converting...';"),
    ("btn.textContent = '변환 시작';", "btn.textContent = 'Convert';"),
    ("btn.textContent = '✂️ 자르기 시작';", "btn.textContent = '✂️ Cut Audio';"),

    # our-sites-bar active link → en/
    ('href="https://wooaaudio.wooahouse.com/" target="_blank" rel="noopener" class="active"',
     'href="https://wooaaudio.wooahouse.com/en/" target="_blank" rel="noopener" class="active"'),

    # pwa install button
    ('>📌 홈 화면에 추가<', '>📌 Add to Home Screen<'),

    # mobile redirect pages (audio-mp3, audio-wav, audio-flac)
    ('MP3 변환기로 이동 중입니다...', 'Redirecting to MP3 Converter...'),
    ('WAV 변환기로 이동 중입니다...', 'Redirecting to WAV Converter...'),
    ('FLAC 변환기로 이동 중입니다...', 'Redirecting to FLAC Converter...'),

    # redirect scripts (update relative path for en/ subfolder)
    ("window.location.replace('audio-convert.html?format=mp3')",
     "window.location.replace('../audio-convert.html?format=mp3')"),
    ("window.location.replace('audio-convert.html?format=wav')",
     "window.location.replace('../audio-convert.html?format=wav')"),
    ("window.location.replace('audio-convert.html?format=flac')",
     "window.location.replace('../audio-convert.html?format=flac')"),
]

# ── 3. 언어 선택기 CSS ────────────────────────────────────────────────────────
LANG_SWITCHER_CSS = """    .lang-switcher { display:flex; align-items:center; gap:4px; }
    .lang-switcher a { color:rgba(255,255,255,0.7); text-decoration:none; font-size:0.8rem; font-weight:600; padding:3px 8px; border-radius:12px; transition:background 0.15s; }
    .lang-switcher a.active { color:white; background:rgba(255,255,255,0.25); }
    .lang-switcher a:hover { color:white; background:rgba(255,255,255,0.18); }
    .lang-switcher span { color:rgba(255,255,255,0.3); font-size:0.75rem; }
"""

def build_page(filename, meta):
    ko_path = os.path.join(BASE, filename)
    en_path = os.path.join(EN_DIR, filename)

    with open(ko_path, encoding='utf-8') as f:
        html = f.read()

    # ── 메타 태그 교체 ──
    html = re.sub(r'<title>[^<]+</title>', f'<title>{meta["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*"',
                  f'<meta name="description" content="{meta["desc"]}"', html)
    html = re.sub(r'<meta name="keywords" content="[^"]*"',
                  f'<meta name="keywords" content="{meta["kw"]}"', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"',
                  f'<meta property="og:title" content="{meta["og_title"]}"', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*"',
                  f'<meta property="og:description" content="{meta["og_desc"]}"', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*"',
                  f'<meta property="og:url" content="https://wooaaudio.wooahouse.com/en/{filename}"', html)
    html = re.sub(r'<link rel="canonical" href="[^"]*"',
                  f'<link rel="canonical" href="https://wooaaudio.wooahouse.com/en/{filename}"', html)

    # ── hreflang 추가 (canonical 바로 뒤) ──
    hreflang = (
        f'\n  <link rel="alternate" hreflang="ko" href="https://wooaaudio.wooahouse.com/{filename}">'
        f'\n  <link rel="alternate" hreflang="en" href="https://wooaaudio.wooahouse.com/en/{filename}">'
        f'\n  <link rel="alternate" hreflang="x-default" href="https://wooaaudio.wooahouse.com/en/{filename}">'
    )
    html = re.sub(r'(<link rel="canonical"[^>]*>)', r'\1' + hreflang, html)

    # ── ld+json 업데이트 ──
    # Replace Korean name fields
    html = re.sub(r'"name": "([^"]*[가-힣][^"]*)"', f'"name": "{meta["app_name"]}"', html)
    # Replace Korean description fields
    html = re.sub(r'"description": "([^"]*[가-힣][^"]*)"', f'"description": "{meta["desc"]}"', html)
    # Replace URL in ld+json for tool pages
    html = re.sub(
        r'"url": "https://wooaaudio\.wooahouse\.com/' + re.escape(filename) + '"',
        f'"url": "https://wooaaudio.wooahouse.com/en/{filename}"',
        html
    )
    # Also fix index.html WebSite url
    if filename == 'index.html':
        html = re.sub(
            r'"url": "https://wooaaudio\.wooahouse\.com/"',
            '"url": "https://wooaaudio.wooahouse.com/en/"',
            html
        )

    # ── FAQ 교체 ──
    if meta.get('faq'):
        faq_items = meta['faq']

        # faq-item format
        faq_html_parts = []
        for i, (q, a) in enumerate(faq_items):
            is_last = (i == len(faq_items) - 1)
            mb = '' if is_last else 'margin-bottom:1.2rem;'
            faq_html_parts.append(
                f'      <div class="faq-item" style="{mb}padding:1rem;background:#f8f9fa;border-radius:8px;">\n'
                f'        <h3 style="font-size:1rem;font-weight:600;margin-bottom:0.5rem;">Q. {q}</h3>\n'
                f'        <p style="color:#555;margin:0;">{a}</p>\n'
                f'      </div>'
            )
        faq_inner = '\n'.join(faq_html_parts)
        html = re.sub(
            r'<div class="faq-list">.*?</div>\s*</section>',
            f'<div class="faq-list">\n{faq_inner}\n    </div>\n  </section>',
            html, flags=re.DOTALL
        )

        # Also replace faq-title heading
        html = re.sub(r'<h2 class="faq-title">자주 묻는 질문</h2>',
                      '<h2 class="faq-title">Frequently Asked Questions</h2>', html)
        html = re.sub(r'<h2[^>]*>자주 묻는 질문</h2>',
                      '<h2 style="font-size:1.4rem;margin-bottom:1.5rem;">Frequently Asked Questions</h2>', html)

        # FAQPage ld+json 교체 (if present)
        faq_entities = []
        for q, a in faq_items:
            faq_entities.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            })
        new_faq_json = _json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }, ensure_ascii=False, indent=2)
        html = re.sub(
            r'<script type="application/ld\+json">\s*\{[^<]*"FAQPage"[^<]*\}[^<]*</script>',
            f'<script type="application/ld+json">\n{new_faq_json}\n</script>',
            html, flags=re.DOTALL
        )

    # ── cross-link banner 교체 ──
    if meta.get('cross_banner_text'):
        # Replace the text span inside cross-link banner
        html = re.sub(
            r'<span style="font-size:0\.95rem;color:#444;">[^<]*</span>',
            f'<span style="font-size:0.95rem;color:#444;">{meta["cross_banner_text"]}</span>',
            html
        )
        # Replace the link button (with #059669 background color used in WooaAudio)
        html = re.sub(
            r'<a href="[^"]*" (?:target="_blank" )?(?:rel="noopener" )?style="background:#059669;[^"]*">[^<]*</a>',
            f'<a href="{meta["cross_banner_href"]}" target="_blank" rel="noopener" style="background:#059669;color:#fff;padding:0.5rem 1rem;border-radius:8px;text-decoration:none;font-size:0.9rem;white-space:nowrap;">{meta["cross_banner_link_text"]}</a>',
            html
        )

    # ── Tool header (h1, tool_desc, breadcrumb) ──
    if meta.get('h1'):
        replaced = re.sub(r'<h1 id="toolTitle">[^<]*</h1>',
                          f'<h1 id="toolTitle">{meta["h1"]}</h1>', html)
        if replaced == html:
            replaced = re.sub(r'<h1>([^<]*)</h1>', f'<h1>{meta["h1"]}</h1>', html, count=1)
        html = replaced

    if meta.get('tool_desc'):
        replaced = re.sub(r'<p id="toolDesc">[^<]*</p>',
                          f'<p id="toolDesc">{meta["tool_desc"]}</p>', html)
        if replaced == html:
            # tool-header의 <p> 교체 (첫 번째)
            replaced = re.sub(
                r'(<div class="tool-header">.*?<h1>[^<]*</h1>\s*)<p>[^<]*</p>',
                r'\g<1>' + f'<p>{meta["tool_desc"]}</p>',
                html, count=1, flags=re.DOTALL
            )
        html = replaced

    if meta.get('breadcrumb') and meta['breadcrumb'] != 'Home':
        html = re.sub(r'<span id="breadcrumbTitle">[^<]*</span>',
                      f'<span id="breadcrumbTitle">{meta["breadcrumb"]}</span>', html)
        # Also replace plain breadcrumb span (last span in breadcrumb div)
        html = re.sub(
            r'(<div class="breadcrumb">.*?<span>›</span>\s*)<span>([^<]+)</span>',
            r'\g<1><span>' + meta['breadcrumb'] + r'</span>',
            html, count=1, flags=re.DOTALL
        )

    # ── 공통 문자열 치환 ──
    for ko, en in COMMON:
        html = html.replace(ko, en)

    # ── 언어 선택기 CSS 삽입 ──
    if 'lang-switcher' not in html:
        html = html.replace('  </style>', LANG_SWITCHER_CSS + '  </style>', 1)
        if 'lang-switcher' not in html:
            html = html.replace('</style>', LANG_SWITCHER_CSS + '</style>', 1)

    # ── 헤더에 언어 선택기 삽입 ──
    html = re.sub(
        r'(\s*</div>\s*</header>)',
        f'\n    <div class="header-right">\n'
        f'      <div class="lang-switcher">\n'
        f'        <a href="../{filename}">KO</a>\n'
        f'        <span>|</span>\n'
        f'        <a href="{filename}" class="active">EN</a>\n'
        f'      </div>\n'
        f'      <a href="../about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none; margin-left:8px;">About</a>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</header>',
        html, count=1
    )

    # ── 쿠팡 광고 제거 ──
    # head의 g.js 제거
    html = re.sub(r'\s*<script src="https://ads-partners\.coupang\.com/g\.js"></script>\n?', '', html)
    # PartnersCoupang 블록 제거
    html = re.sub(r'<script>\s*new PartnersCoupang\.G\([^)]*\);?\s*</script>', '', html)
    # coupang-notice 제거
    html = re.sub(r'<p class="coupang-notice">[^<]*</p>', '', html)

    # ── og:locale 교체 (COMMON에서 ko_KR→en_US로 치환되지 않은 경우 대비) ──
    html = html.replace('content="ko_KR"', 'content="en_US"')

    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'  ✅ en/{filename}')


# ── 4. 실행 ──────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Building WooaAudio English pages...')
    for filename, meta in PAGE_META.items():
        ko_path = os.path.join(BASE, filename)
        if os.path.exists(ko_path):
            build_page(filename, meta)
        else:
            print(f'  ⚠️  {filename} not found, skipping')
    print(f'\nDone! {len(PAGE_META)} files generated in en/')
