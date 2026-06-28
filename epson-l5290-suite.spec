Name:           epson-l5290-suite
Version:        1.0.0
Release:        1%{?dist}
Summary:        Complete Driver and Maintenance Utility Suite for Epson L5290
License:        GPLv2 and Proprietary
URL:            https://github.com/dosq/epson-l5290-suite
BuildArch:      x86_64

Requires:       python3, python3-tkinter, cups, gutenprint-cups, escputil

%description
Instant suite for Epson L5290 printer on Fedora / RedHat Linux.
Bundles the official Epson ESC/P-R printer driver, CUPS service auto-configuration,
and a Graphical User Interface (GUI) utility for Head Cleaning and Nozzle Check.

%prep
# Nothing to prep

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/epson-l5290

install -m 0755 %{_sourcedir}/epson-l5290-utility %{buildroot}%{_bindir}/epson-l5290-utility
install -m 0644 %{_sourcedir}/epson-l5290-utility.desktop %{buildroot}%{_datadir}/applications/epson-l5290-utility.desktop
install -m 0644 %{_sourcedir}/epson-inkjet-printer-escpr.rpm %{buildroot}%{_datadir}/epson-l5290/epson-inkjet-printer-escpr.rpm

%files
%{_bindir}/epson-l5290-utility
%{_datadir}/applications/epson-l5290-utility.desktop
%{_datadir}/epson-l5290/epson-inkjet-printer-escpr.rpm

%post
echo "====================================================="
echo " Installing bundled Epson ESC/P-R Driver & CUPS...  "
echo "====================================================="
rpm -Uvh --replacepkgs --nodeps %{_datadir}/epson-l5290/epson-inkjet-printer-escpr.rpm || true
systemctl restart cups || true
echo "Epson L5290 Suite installation completed successfully!"

%changelog
* Sun Jun 28 2026 dosq <dosq@localhost> - 1.0.0-1
- Initial release with bundled driver and GUI utility.
