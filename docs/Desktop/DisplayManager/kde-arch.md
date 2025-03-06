
# KDE Plasma
Install
```
pacman -S xorg plasma plasma-wayland-session kde-applications 
```
Enable service
```
systemctl enable sddm.service
systemctl enable NetworkManager.service
```

LOG
```
$ sudo pacman -S xorg plasma plasma-wayland-session kde-applications 
[sudo] password for darklord: 
:: There are 48 members in group xorg:
:: Repository extra
   1) xf86-video-vesa  2) xorg-bdftopcf  3) xorg-docs  4) xorg-font-util  5) xorg-fonts-100dpi  6) xorg-fonts-75dpi
   7) xorg-fonts-encodings  8) xorg-iceauth  9) xorg-mkfontscale  10) xorg-server  11) xorg-server-common  12) xorg-server-devel
   13) xorg-server-xephyr  14) xorg-server-xnest  15) xorg-server-xvfb  16) xorg-sessreg  17) xorg-setxkbmap  18) xorg-smproxy
   19) xorg-x11perf  20) xorg-xauth  21) xorg-xbacklight  22) xorg-xcmsdb  23) xorg-xcursorgen  24) xorg-xdpyinfo  25) xorg-xdriinfo
   26) xorg-xev  27) xorg-xgamma  28) xorg-xhost  29) xorg-xinput  30) xorg-xkbcomp  31) xorg-xkbevd  32) xorg-xkbutils  33) xorg-xkill
   34) xorg-xlsatoms  35) xorg-xlsclients  36) xorg-xmodmap  37) xorg-xpr  38) xorg-xprop  39) xorg-xrandr  40) xorg-xrdb
   41) xorg-xrefresh  42) xorg-xset  43) xorg-xsetroot  44) xorg-xvinfo  45) xorg-xwayland  46) xorg-xwd  47) xorg-xwininfo
   48) xorg-xwud

Enter a selection (default=all): y
error: invalid number: y

Enter a selection (default=all): 
warning: xorg-fonts-encodings-1.0.6-1 is up to date -- reinstalling
warning: xorg-server-21.1.6-1 is up to date -- reinstalling
warning: xorg-server-common-21.1.6-1 is up to date -- reinstalling
warning: xorg-setxkbmap-1.3.3-1 is up to date -- reinstalling
warning: xorg-xhost-1.0.9-1 is up to date -- reinstalling
warning: xorg-xkbcomp-1.4.6-1 is up to date -- reinstalling
warning: xorg-xmodmap-1.0.11-1 is up to date -- reinstalling
warning: xorg-xprop-1.2.6-1 is up to date -- reinstalling
warning: xorg-xrandr-1.5.2-1 is up to date -- reinstalling
warning: xorg-xrdb-1.2.1-1 is up to date -- reinstalling
warning: xorg-xset-1.2.5-1 is up to date -- reinstalling
warning: xorg-xwayland-22.1.7-1 is up to date -- reinstalling
:: There are 47 members in group plasma:
:: Repository extra
   1) bluedevil  2) breeze  3) breeze-gtk  4) discover  5) drkonqi  6) kactivitymanagerd  7) kde-cli-tools  8) kde-gtk-config
   9) kdecoration  10) kdeplasma-addons  11) kgamma5  12) khotkeys  13) kinfocenter  14) kmenuedit  15) kpipewire  16) kscreen
   17) kscreenlocker  18) ksshaskpass  19) ksystemstats  20) kwallet-pam  21) kwayland-integration  22) kwin  23) kwrited
   24) layer-shell-qt  25) libkscreen  26) libksysguard  27) milou  28) oxygen  29) oxygen-sounds  30) plasma-browser-integration
   31) plasma-desktop  32) plasma-disks  33) plasma-firewall  34) plasma-integration  35) plasma-nm  36) plasma-pa  37) plasma-sdk
   38) plasma-systemmonitor  39) plasma-thunderbolt  40) plasma-vault  41) plasma-workspace  42) plasma-workspace-wallpapers
   43) polkit-kde-agent  44) powerdevil  45) sddm-kcm  46) systemsettings  47) xdg-desktop-portal-kde

Enter a selection (default=all): 
warning: xdg-desktop-portal-kde-5.26.5-1 is up to date -- reinstalling
:: There are 176 members in group kde-applications:
:: Repository extra
   1) akonadi-calendar-tools  2) akonadi-import-wizard  3) akonadiconsole  4) akregator  5) ark  6) artikulate  7) audiocd-kio
   8) blinken  9) bomber  10) bovo  11) cantor  12) cervisia  13) colord-kde  14) dolphin  15) dolphin-plugins  16) dragon  17) elisa
   18) falkon  19) ffmpegthumbs  20) filelight  21) granatier  22) grantlee-editor  23) gwenview  24) itinerary  25) juk  26) k3b
   27) kaddressbook  28) kajongg  29) kalarm  30) kalendar  31) kalgebra  32) kalzium  33) kamera  34) kamoso  35) kanagram  36) kapman
   37) kapptemplate  38) kate  39) katomic  40) kbackup  41) kblackbox  42) kblocks  43) kbounce  44) kbreakout  45) kbruch
   46) kcachegrind  47) kcalc  48) kcharselect  49) kcolorchooser  50) kcron  51) kde-dev-scripts  52) kde-dev-utils
   53) kdebugsettings  54) kdeconnect  55) kdegraphics-thumbnailers  56) kdenetwork-filesharing  57) kdenlive  58) kdepim-addons
   59) kdesdk-kio  60) kdesdk-thumbnailers  61) kdevelop  62) kdevelop-php  63) kdevelop-python  64) kdf  65) kdialog  66) kdiamond
   67) keditbookmarks  68) kfind  69) kfloppy  70) kfourinline  71) kgeography  72) kget  73) kgoldrunner  74) kgpg  75) khangman
   76) khelpcenter  77) kig  78) kigo  79) killbots  80) kimagemapeditor  81) kio-extras  82) kio-gdrive  83) kio-zeroconf
   84) kirigami-gallery  85) kiriki  86) kiten  87) kjumpingcube  88) kleopatra  89) klettres  90) klickety  91) klines  92) kmag
   93) kmahjongg  94) kmail  95) kmail-account-wizard  96) kmines  97) kmix  98) kmousetool  99) kmouth  100) kmplot  101) knavalbattle
   102) knetwalk  103) knights  104) knotes  105) kolf  106) kollision  107) kolourpaint  108) kompare  109) konqueror  110) konquest
   111) konsole  112) kontact  113) kontrast  114) konversation  115) kopete  116) korganizer  117) kpat  118) krdc  119) kreversi
   120) krfb  121) kruler  122) kshisen  123) ksirk  124) ksnakeduel  125) kspaceduel  126) ksquares  127) ksudoku  128) ksystemlog
   129) kteatime  130) ktimer  131) ktorrent  132) ktouch  133) ktuberling  134) kturtle  135) kubrick  136) kwalletmanager  137) kwave
   138) kwordquiz  139) lokalize  140) lskat  141) marble  142) markdownpart  143) mbox-importer  144) minuet  145) okular
   146) palapeli  147) parley  148) partitionmanager  149) picmi  150) pim-data-exporter  151) pim-sieve-editor  152) poxml
   153) print-manager  154) rocs  155) signon-kwallet-extension  156) skanlite  157) skanpage  158) spectacle  159) step  160) svgpart
   161) sweeper  162) telepathy-kde-accounts-kcm  163) telepathy-kde-approver  164) telepathy-kde-auth-handler
   165) telepathy-kde-call-ui  166) telepathy-kde-common-internals  167) telepathy-kde-contact-list  168) telepathy-kde-contact-runner
   169) telepathy-kde-desktop-applets  170) telepathy-kde-filetransfer-handler  171) telepathy-kde-integration-module
   172) telepathy-kde-send-file  173) telepathy-kde-text-ui  174) umbrello  175) yakuake  176) zanshin

Enter a selection (default=all): 
resolving dependencies...
:: There are 2 providers available for pipewire-session-manager:
:: Repository extra
   1) wireplumber
:: Repository community
   2) pipewire-media-session

Enter a number (default=1): 
:: There are 2 providers available for phonon-qt5-backend:
:: Repository extra
   1) phonon-qt5-gstreamer  2) phonon-qt5-vlc

Enter a number (default=1): 
:: There are 2 providers available for qt5-python-bindings:
:: Repository extra
   1) pyside2  2) python-pyqt5

Enter a number (default=1): 
:: There are 2 providers available for cron:
:: Repository core
   1) cronie
:: Repository community
   2) fcron

Enter a number (default=1): 
:: There are 126 providers available for tessdata:
:: Repository community
   1) tesseract-data-afr  2) tesseract-data-amh  3) tesseract-data-ara  4) tesseract-data-asm  5) tesseract-data-aze
   6) tesseract-data-aze_cyrl  7) tesseract-data-bel  8) tesseract-data-ben  9) tesseract-data-bod  10) tesseract-data-bos
   11) tesseract-data-bre  12) tesseract-data-bul  13) tesseract-data-cat  14) tesseract-data-ceb  15) tesseract-data-ces
   16) tesseract-data-chi_sim  17) tesseract-data-chi_tra  18) tesseract-data-chr  19) tesseract-data-cos  20) tesseract-data-cym
   21) tesseract-data-dan  22) tesseract-data-dan_frak  23) tesseract-data-deu  24) tesseract-data-deu_frak  25) tesseract-data-div
   26) tesseract-data-dzo  27) tesseract-data-ell  28) tesseract-data-eng  29) tesseract-data-enm  30) tesseract-data-epo
   31) tesseract-data-equ  32) tesseract-data-est  33) tesseract-data-eus  34) tesseract-data-fao  35) tesseract-data-fas
   36) tesseract-data-fil  37) tesseract-data-fin  38) tesseract-data-fra  39) tesseract-data-frk  40) tesseract-data-frm
   41) tesseract-data-fry  42) tesseract-data-gla  43) tesseract-data-gle  44) tesseract-data-glg  45) tesseract-data-grc
   46) tesseract-data-guj  47) tesseract-data-hat  48) tesseract-data-heb  49) tesseract-data-hin  50) tesseract-data-hrv
   51) tesseract-data-hun  52) tesseract-data-hye  53) tesseract-data-iku  54) tesseract-data-ind  55) tesseract-data-isl
   56) tesseract-data-ita  57) tesseract-data-ita_old  58) tesseract-data-jav  59) tesseract-data-jpn  60) tesseract-data-jpn_vert
   61) tesseract-data-kan  62) tesseract-data-kat  63) tesseract-data-kat_old  64) tesseract-data-kaz  65) tesseract-data-khm
   66) tesseract-data-kir  67) tesseract-data-kmr  68) tesseract-data-kor  69) tesseract-data-kor_vert  70) tesseract-data-lao
   71) tesseract-data-lat  72) tesseract-data-lav  73) tesseract-data-lit  74) tesseract-data-ltz  75) tesseract-data-mal
   76) tesseract-data-mar  77) tesseract-data-mkd  78) tesseract-data-mlt  79) tesseract-data-mon  80) tesseract-data-mri
   81) tesseract-data-msa  82) tesseract-data-mya  83) tesseract-data-nep  84) tesseract-data-nld  85) tesseract-data-nor
   86) tesseract-data-oci  87) tesseract-data-ori  88) tesseract-data-pan  89) tesseract-data-pol  90) tesseract-data-por
   91) tesseract-data-pus  92) tesseract-data-que  93) tesseract-data-ron  94) tesseract-data-rus  95) tesseract-data-san
   96) tesseract-data-sin  97) tesseract-data-slk  98) tesseract-data-slk_frak  99) tesseract-data-slv  100) tesseract-data-snd
   101) tesseract-data-spa  102) tesseract-data-spa_old  103) tesseract-data-sqi  104) tesseract-data-srp  105) tesseract-data-srp_latn
   106) tesseract-data-sun  107) tesseract-data-swa  108) tesseract-data-swe  109) tesseract-data-syr  110) tesseract-data-tam
   111) tesseract-data-tat  112) tesseract-data-tel  113) tesseract-data-tgk  114) tesseract-data-tgl  115) tesseract-data-tha
   116) tesseract-data-tir  117) tesseract-data-ton  118) tesseract-data-tur  119) tesseract-data-uig  120) tesseract-data-ukr
   121) tesseract-data-urd  122) tesseract-data-uzb  123) tesseract-data-uzb_cyrl  124) tesseract-data-vie  125) tesseract-data-yid
   126) tesseract-data-yor

Enter a number (default=1): 
looking for conflicting packages...
warning: dependency cycle detected:
warning: phonon-qt5-gstreamer will be installed before its phonon-qt5 dependency
warning: dependency cycle detected:
warning: python-incremental will be installed before its python-twisted dependency
warning: dependency cycle detected:
warning: tesseract-data-afr will be installed before its tesseract dependency
warning: dependency cycle detected:
warning: telepathy-kde-integration-module will be installed before its telepathy-kde-common-internals dependency

Packages (510) accounts-qml-module-0.7-4  aha-0.5.1-2  akonadi-22.12.1-2  akonadi-calendar-22.12.1-1  akonadi-contacts-22.12.1-1
               akonadi-mime-22.12.1-1  akonadi-notes-22.12.1-1  akonadi-search-22.12.1-1  analitza-22.12.1-1  appstream-qt-0.15.6-1
               archlinux-appstream-data-20230115-1  attica-5.102.0-1  audiofile-0.3.6-7  avogadro-crystals-1.0.1-1
               avogadro-molecules-1.0.0-1  avogadrolibs-1.97.0-2  avogadrolibs-qt5-1.97.0-2  baloo-5.102.0-1  baloo-widgets-22.12.1-1
               black-hole-solver-1.12.0-1  bluez-qt-5.102.0-1  breeze-icons-5.102.0-1  calendarsupport-22.12.1-1  cfitsio-1:4.2.0-1
               confuse-3.3-3  convertlit-1.8-11  coordgen-3.0.1-1  cronie-1.6.1-1  discount-2.2.7.b-1  dmidecode-3.4-1
               docbook-xml-4.5-9  docbook-xsl-1.79.2-7  ebook-tools-0.2.2-7  eventviews-22.12.1-1  farstream-0.2.9-3  flashrom-1.2-4
               fmt-9.1.0-4  frameworkintegration-5.102.0-1  freecell-solver-6.8.0-1  fwupd-1.8.10-1  fwupd-efi-1.3-1  glew-2.2.0-6
               gnugo-3.8-7  grantlee-5.3.1-1  grantleetheme-22.12.1-1  gsl-2.7.1-1  hdf5-1.12.2-1  id3lib-3.8.3-18
               incidenceeditor-22.12.1-1  jemalloc-1:5.3.0-1  kaccounts-integration-22.12.1-1  kaccounts-providers-22.12.1-1
               kactivities-stats-5.102.0-1  kcachegrind-common-22.12.1-1  kcalendarcore-5.102.0-1  kcalutils-22.12.1-1
               kcmutils-5.102.0-1  kcolorpicker-0.2.0-1  kcontacts-1:5.102.0-1  kdav-1:5.102.0-1  kdeedu-data-22.12.1-1
               kdegraphics-mobipocket-22.12.1-1  kdelibs4support-5.102.0-1  kdepim-runtime-22.12.1-1  kdesu-5.102.0-1  kdiagram-2.8.0-1
               kdnssd-5.102.0-1  kdoctools-5.102.0-1  kdsoap-2.1.1-1  kdsoap-ws-discovery-client-git20200927-2  kemoticons-5.102.0-1
               kfilemetadata-5.102.0-1  khealthcertificate-22.11-1  kholidays-1:5.102.0-1  khtml-5.102.0-1
               kidentitymanagement-22.12.1-1  kidletime-5.102.0-1  kimageannotator-0.6.0-1  kimap-22.12.1-1  kinit-5.102.0-1
               kirigami-addons-0.6.2-1  kitemmodels-5.102.0-1  kitinerary-22.12.1-2  kjs-5.102.0-1  kldap-22.12.1-1
               kmailtransport-22.12.1-1  kmbox-22.12.1-1  kmime-22.12.1-1  knewstuff-5.102.0-1  knotifyconfig-5.102.0-1
               kontactinterface-22.12.1-1  kopeninghours-22.12.1-2  kosmindoormap-22.12.1-1  kparts-5.102.0-1  kpeople-5.102.0-1
               kpeoplevcard-0.1-1  kpimtextedit-22.12.1-1  kpkpass-22.12.1-1  kplotting-5.102.0-1  kpmcore-22.12.1-1  kpty-5.102.0-1
               kpublictransport-22.12.1-1  kqtquickcharts-22.12.1-1  kquickcharts-5.102.0-1  kross-5.102.0-1  krunner-5.102.0-1
               ksanecore-22.12.1-1  ksmtp-22.12.1-1  ktexteditor-5.102.0-1  ktnef-22.12.1-1  kunitconversion-5.102.0-1
               kuserfeedback-1.2.0-1  leptonica-1.82.0-3  libaccounts-glib-1.26-1  libaccounts-qt-1.16-3  libaec-1.0.6-1
               libakonadi-22.12.1-2  libcbor-0.10.1-1  libdmtx-0.7.7-1  libebur128-1.2.6-1  libfakekey-0.3-2  libftdi-1.5-4
               libgravatar-22.12.1-1  libjcat-0.1.12-1  libkcddb-22.12.1-1  libkcompactdisc-22.12.1-1  libkdcraw-22.12.1-1
               libkdegames-22.12.1-1  libkdepim-22.12.1-1  libkeduvocdocument-22.12.1-1  libkexiv2-22.12.1-1  libkgapi-22.12.1-1
               libkleo-22.12.1-1  libkmahjongg-22.12.1-1  libkolabxml-1.2.1-2  libkomparediff2-22.12.1-1  libksane-22.12.1-1
               libksieve-22.12.1-1  libktorrent-22.12.1-1  libmbim-1.28.2-1  libmsym-0.2.3-7  libmusicbrainz5-5.1.0-5  libotr-4.1.1-3
               libqaccessibilityclient-0.4.1-2  libqalculate-4.5.1-1  libqmi-1.32.2-1  libqrtr-glib-1.2.2-2  libsignon-glib-2.1-5
               libsmbios-2.4.3-5  libwireplumber-0.4.13-1  libxaw-1.0.14-1  libxres-1.2.2-1  libxss-1.2.3-4  libzip-1.9.2-1
               maeparser-1.3.0-3  mailcommon-22.12.1-1  mailimporter-22.12.1-1  marble-common-22.12.1-2  mariadb-10.9.4-2
               mariadb-clients-10.9.4-2  mariadb-libs-10.9.4-2  mesa-utils-8.5.0-2  messagelib-22.12.1-1  mlt-7.12.0-2
               modemmanager-1.20.4-1  modemmanager-qt-5.102.0-1  molequeue-0.9.0-2  networkmanager-qt-5.102.0-1  noto-fonts-20220810-1
               openbabel-3.1.1-5  perl-parse-yapp-1.21-5  phonon-qt5-4.11.1-3  phonon-qt5-gstreamer-4.10.0-4  pimcommon-22.12.1-1
               poppler-qt5-23.01.0-3  ppp-2.4.9-3  prison-5.102.0-1  protobuf-c-1.4.1-1  pugixml-1.13-1  pulseaudio-qt-1.3-1
               purpose-5.102.0-1  pyside2-5.15.8-6  python-automat-22.10.0-1  python-constantly-15.1.0-11  python-distro-1.8.0-2
               python-hyperlink-21.0.0-4  python-incremental-22.10.0-1  python-qtpy-2.3.0-1  python-shiboken2-5.15.8-6
               python-twisted-22.10.0-1  python-zope-interface-5.5.2-1  qgpgme-1.18.0-2  qhull-2020.2-4  qqc2-desktop-style-5.102.0-1
               qt-gstreamer-1.2.0-4  qt5-location-5.15.8+kde+r3-1  qt5-networkauth-5.15.8-1  qt5-script-5.15.12-2  qt5-sensors-5.15.8-1
               qt5-tools-5.15.8+kde+r1-3  qt5-webchannel-5.15.8+kde+r3-1  qt5-webengine-5.15.12-2  qt5-webview-5.15.8-1
               qt5-xmlpatterns-5.15.8-1  qtkeychain-qt5-0.13.2-1  samba-4.17.4-4  sddm-0.19.0-9  signon-plugin-oauth2-0.25-1
               signon-ui-0.17+20171022-3  signond-8.61-1  smartmontools-7.3-1  socat-1.7.4.4-1  spglib-2.0.2-1  syndication-5.102.0-1
               syntax-highlighting-5.102.0-1  tbb-2021.5.0-2  telepathy-accounts-signon-2.1-3  telepathy-farstream-0.6.2-7
               telepathy-glib-0.24.2-2  telepathy-logger-0.8.2-5  telepathy-logger-qt-17.09.0-1  telepathy-mission-control-5.16.6-2
               telepathy-qt-0.9.8-2  tesseract-5.3.0-1  tesseract-data-afr-2:4.1.0-3  tesseract-data-osd-2:4.1.0-3
               threadweaver-5.102.0-1  ttf-hack-3.003-3  vtk-9.1.0-25  vulkan-tools-1.3.235-2  wayland-utils-1.1.0-1
               wireplumber-0.4.13-1  xapian-core-1:1.4.21-1  xerces-c-3.2.4-2  xorg-fonts-alias-100dpi-1.0.4-1
               xorg-fonts-alias-75dpi-1.0.4-1  xorg-util-macros-1.19.3-1  xorg-xmessage-1.0.6-1  akonadi-calendar-tools-22.12.1-1
               akonadi-import-wizard-22.12.1-1  akonadiconsole-22.12.1-1  akregator-22.12.1-1  ark-22.12.1-1  artikulate-22.12.1-1
               audiocd-kio-22.12.1-1  blinken-22.12.1-1  bluedevil-1:5.26.5-1  bomber-22.12.1-1  bovo-22.12.1-1  breeze-5.26.5-1
               breeze-gtk-5.26.5-1  cantor-22.12.1-1  cervisia-22.12.1-1  colord-kde-22.12.1-1  discover-5.26.5-1  dolphin-22.12.1-1
               dolphin-plugins-22.12.1-1  dragon-22.12.1-1  drkonqi-5.26.5-1  elisa-22.12.1-1  falkon-22.12.1-2  ffmpegthumbs-22.12.1-1
               filelight-22.12.1-1  granatier-22.12.1-1  grantlee-editor-22.12.1-1  gwenview-22.12.1-1  itinerary-22.12.1-1
               juk-22.12.1-1  k3b-1:22.12.1-1  kactivitymanagerd-5.26.5-1  kaddressbook-22.12.1-1  kajongg-22.12.1-1  kalarm-22.12.1-1
               kalendar-22.12.1-1  kalgebra-22.12.1-1  kalzium-22.12.1-1  kamera-22.12.1-1  kamoso-22.12.1-1  kanagram-22.12.1-1
               kapman-22.12.1-1  kapptemplate-22.12.1-1  kate-22.12.1-1  katomic-22.12.1-1  kbackup-22.12.1-1  kblackbox-22.12.1-1
               kblocks-22.12.1-1  kbounce-22.12.1-1  kbreakout-22.12.1-1  kbruch-22.12.1-1  kcachegrind-22.12.1-1  kcalc-22.12.1-1
               kcharselect-22.12.1-1  kcolorchooser-22.12.1-1  kcron-22.12.1-1  kde-cli-tools-5.26.5-1  kde-dev-scripts-22.12.1-1
               kde-dev-utils-22.12.1-1  kde-gtk-config-5.26.5-1  kdebugsettings-22.12.1-1  kdeconnect-22.12.1-1  kdecoration-5.26.5-1
               kdegraphics-thumbnailers-22.12.1-1  kdenetwork-filesharing-22.12.1-1  kdenlive-22.12.1-2  kdepim-addons-22.12.1-1
               kdeplasma-addons-5.26.5-1  kdesdk-kio-22.12.1-1  kdesdk-thumbnailers-22.12.1-1  kdevelop-22.12.1-3
               kdevelop-php-22.12.1-1  kdevelop-python-22.12.1-1  kdf-22.12.1-1  kdialog-22.12.1-1  kdiamond-22.12.1-1
               keditbookmarks-22.12.1-1  kfind-22.12.1-1  kfloppy-22.12.1-1  kfourinline-22.12.1-1  kgamma5-5.26.5-1
               kgeography-22.12.1-1  kget-22.12.1-1  kgoldrunner-22.12.1-1  kgpg-22.12.1-1  khangman-22.12.1-1  khelpcenter-22.12.1-1
               khotkeys-5.26.5-1  kig-22.12.1-2  kigo-22.12.1-1  killbots-22.12.1-1  kimagemapeditor-22.12.1-1  kinfocenter-5.26.5-1
               kio-extras-22.12.1-1  kio-gdrive-22.12.1-1  kio-zeroconf-22.12.1-1  kirigami-gallery-22.12.1-1  kiriki-22.12.1-1
               kiten-22.12.1-1  kjumpingcube-22.12.1-1  kleopatra-22.12.1-1  klettres-22.12.1-1  klickety-22.12.1-1  klines-22.12.1-1
               kmag-22.12.1-1  kmahjongg-22.12.1-1  kmail-22.12.1-1  kmail-account-wizard-22.12.1-1  kmenuedit-5.26.5-1
               kmines-22.12.1-1  kmix-22.12.1-1  kmousetool-22.12.1-1  kmouth-22.12.1-1  kmplot-22.12.1-1  knavalbattle-22.12.1-1
               knetwalk-22.12.1-1  knights-22.12.1-1  knotes-22.12.1-1  kolf-22.12.1-1  kollision-22.12.1-1  kolourpaint-22.12.1-1
               kompare-22.12.1-1  konqueror-22.12.1-1  konquest-22.12.1-1  konsole-22.12.1-1  kontact-22.12.1-1  kontrast-22.12.1-1
               konversation-22.12.1-1  kopete-22.12.1-1  korganizer-22.12.1-1  kpat-22.12.1-1  kpipewire-5.26.5-1  krdc-22.12.1-1
               kreversi-22.12.1-1  krfb-22.12.1-1  kruler-22.12.1-1  kscreen-5.26.5-1  kscreenlocker-5.26.5-1  kshisen-22.12.1-1
               ksirk-22.12.1-1  ksnakeduel-22.12.1-1  kspaceduel-22.12.1-1  ksquares-22.12.1-1  ksshaskpass-5.26.5-1  ksudoku-22.12.1-1
               ksystemlog-22.12.1-1  ksystemstats-5.26.5-1  kteatime-22.12.1-1  ktimer-22.12.1-1  ktorrent-22.12.1-1  ktouch-22.12.1-1
               ktuberling-22.12.1-1  kturtle-22.12.1-1  kubrick-22.12.1-1  kwallet-pam-5.26.5-1  kwalletmanager-22.12.1-1
               kwave-22.12.1-1  kwayland-integration-5.26.5-1  kwin-5.26.5-2  kwordquiz-22.12.1-1  kwrited-5.26.5-1
               layer-shell-qt-5.26.5-1  libkscreen-5.26.5-1  libksysguard-5.26.5-1  lokalize-22.12.1-1  lskat-22.12.1-1
               marble-22.12.1-2  markdownpart-22.12.1-1  mbox-importer-22.12.1-1  milou-5.26.5-1  minuet-22.12.1-1  okular-22.12.1-1
               oxygen-5.26.5-1  oxygen-sounds-5.26.5-1  palapeli-22.12.1-1  parley-22.12.1-1  partitionmanager-22.12.1-1
               picmi-22.12.1-1  pim-data-exporter-22.12.1-1  pim-sieve-editor-22.12.1-1  plasma-browser-integration-5.26.5-1
               plasma-desktop-5.26.5-1  plasma-disks-5.26.5-1  plasma-firewall-5.26.5-1  plasma-integration-5.26.5-1
               plasma-nm-5.26.5-1  plasma-pa-5.26.5-1  plasma-sdk-5.26.5-1  plasma-systemmonitor-5.26.5-1  plasma-thunderbolt-5.26.5-1
               plasma-vault-5.26.5-1  plasma-wayland-session-5.26.5-2  plasma-workspace-5.26.5-2  plasma-workspace-wallpapers-5.26.5-1
               polkit-kde-agent-5.26.5-1  powerdevil-5.26.5-1  poxml-22.12.1-1  print-manager-22.12.1-1  rocs-22.12.1-1
               sddm-kcm-5.26.5-1  signon-kwallet-extension-22.12.1-1  skanlite-22.12.1-1  skanpage-22.12.1-1  spectacle-22.12.1-1
               step-22.12.1-1  svgpart-22.12.1-1  sweeper-22.12.1-1  systemsettings-5.26.5-1  telepathy-kde-accounts-kcm-22.12.1-1
               telepathy-kde-approver-22.12.1-1  telepathy-kde-auth-handler-22.12.1-1  telepathy-kde-call-ui-22.12.1-1
               telepathy-kde-common-internals-22.12.1-2  telepathy-kde-contact-list-22.12.1-1  telepathy-kde-contact-runner-22.12.1-1
               telepathy-kde-desktop-applets-22.12.1-1  telepathy-kde-filetransfer-handler-22.12.1-1
               telepathy-kde-integration-module-22.12.1-1  telepathy-kde-send-file-22.12.1-1  telepathy-kde-text-ui-22.12.1-1
               umbrello-22.12.1-1  xdg-desktop-portal-kde-5.26.5-1  xf86-video-vesa-2.6.0-1  xorg-bdftopcf-1.1.1-1  xorg-docs-1.7.2-2
               xorg-font-util-1.3.3-1  xorg-fonts-100dpi-1.0.3-8  xorg-fonts-75dpi-1.0.3-8  xorg-fonts-encodings-1.0.6-1
               xorg-iceauth-1.0.9-1  xorg-mkfontscale-1.2.2-1  xorg-server-21.1.6-1  xorg-server-common-21.1.6-1
               xorg-server-devel-21.1.6-1  xorg-server-xephyr-21.1.6-1  xorg-server-xnest-21.1.6-1  xorg-server-xvfb-21.1.6-1
               xorg-sessreg-1.1.3-1  xorg-setxkbmap-1.3.3-1  xorg-smproxy-1.0.7-1  xorg-x11perf-1.6.2-1  xorg-xauth-1.1.2-1
               xorg-xbacklight-1.2.3-3  xorg-xcmsdb-1.0.6-1  xorg-xcursorgen-1.0.8-1  xorg-xdpyinfo-1.3.3-4  xorg-xdriinfo-1.0.7-1
               xorg-xev-1.2.5-1  xorg-xgamma-1.0.7-1  xorg-xhost-1.0.9-1  xorg-xinput-1.6.3-3  xorg-xkbcomp-1.4.6-1
               xorg-xkbevd-1.1.5-1  xorg-xkbutils-1.0.5-1  xorg-xkill-1.0.6-1  xorg-xlsatoms-1.1.4-1  xorg-xlsclients-1.1.5-1
               xorg-xmodmap-1.0.11-1  xorg-xpr-1.1.0-1  xorg-xprop-1.2.6-1  xorg-xrandr-1.5.2-1  xorg-xrdb-1.2.1-1
               xorg-xrefresh-1.0.7-1  xorg-xset-1.2.5-1  xorg-xsetroot-1.1.3-1  xorg-xvinfo-1.1.5-1  xorg-xwayland-22.1.7-1
               xorg-xwd-1.0.8-1  xorg-xwininfo-1.1.5-3  xorg-xwud-1.0.6-1  yakuake-22.12.1-1  zanshin-22.12.1-1

Total Download Size:   1120.53 MiB
Total Installed Size:  3343.45 MiB


```