%global debug_package %{nil}

Name: nautilus-compare
Version: 1.0.0
Release: 1%{?dist}
Summary: Add Meld to Nautilus context menu

License: GPLv3
URL: https://launchpad.net/nautilus-compare
Source0: https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz

BuildRequires: gettext

Requires: nautilus
Requires: nautilus-python
Requires: python3-pyxdg
Requires: meld

%description
Add Compare option to Nautilus context menu

%prep
%autosetup


%build


%install
install -Dm755 src/nautilus-compare{,-preferences}.py -t %{buildroot}%{_datadir}/nautilus-compare/
install -Dm644 src/utils.py -t %{buildroot}%{_datadir}/nautilus-compare/
install -Dm644 data/nautilus-compare-preferences.desktop %{buildroot}%{_datadir}/applications/nautilus-compare-preferences.desktop
install -dm755 %{buildroot}/usr{/bin,/share/nautilus-python/extensions}
ln -s %{_datadir}/nautilus-compare/nautilus-compare.py %{buildroot}%{_datadir}/nautilus-python/extensions/nautilus-compare.py
ln -s %{_datadir}/nautilus-compare/nautilus-compare-preferences.py %{buildroot}%{_bindir}/nautilus-compare-preferences
for file in $(cd po; ls *.po; cd ..); do
    mkdir -p %{buildroot}%{_datadir}/locale/${file%.po}/LC_MESSAGES
    msgfmt -f -o %{buildroot}%{_datadir}/locale/${file%.po}/LC_MESSAGES/nautilus-compare.mo po/$file
done

%files
%{_bindir}/nautilus-compare-preferences
%{_datadir}/applications/nautilus-compare-preferences.desktop
%{_datadir}/locale/de/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/el/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/en_AU/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/es/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/et/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/fr/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/gl/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/is/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/it/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/ms/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/si/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/sr/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/nautilus-compare.mo
%{_datadir}/nautilus-compare/nautilus-compare-preferences.py
%{_datadir}/nautilus-compare/nautilus-compare.py
%{_datadir}/nautilus-compare/utils.py
%{_datadir}/nautilus-python/extensions/nautilus-compare.py

%changelog
* Tue Oct 25 2022 Dawid Stasiak <dawid.stasiak21@gmail.com>
- 
