// PWA Install Banner
let deferredPrompt = null;

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  // Show install button if exists
  const btn = document.getElementById('heroInstallBtn');
  if (btn) btn.style.display = 'inline-flex';
});

document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('heroInstallBtn');
  if (btn) {
    btn.addEventListener('click', async () => {
      if (!deferredPrompt) return;
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      deferredPrompt = null;
      btn.style.display = 'none';
    });
  }

  // PWA banner after download
  const downloadBtn = document.getElementById('downloadBtn');
  if (downloadBtn) {
    downloadBtn.addEventListener('click', () => {
      setTimeout(() => {
        if (deferredPrompt) {
          const banner = document.getElementById('pwaBanner');
          if (banner) banner.style.display = 'flex';
        }
      }, 1500);
    });
  }
});

window.addEventListener('appinstalled', () => {
  deferredPrompt = null;
});
