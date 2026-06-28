#!/bin/bash
set -e

echo "=== Building Epson L5290 Suite RPM ==="

PROJ_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RPMBUILD_DIR="$HOME/rpmbuild"

mkdir -p "$RPMBUILD_DIR"/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
mkdir -p "$PROJ_DIR/output"

echo "1. Copying source files to rpmbuild/SOURCES..."
cp "$PROJ_DIR/epson-l5290-utility" "$RPMBUILD_DIR/SOURCES/"
cp "$PROJ_DIR/epson-l5290-utility.desktop" "$RPMBUILD_DIR/SOURCES/"
cp "$PROJ_DIR/epson-inkjet-printer-escpr.rpm" "$RPMBUILD_DIR/SOURCES/"
cp "$PROJ_DIR/epson-l5290-suite.spec" "$RPMBUILD_DIR/SPECS/"

chmod +x "$RPMBUILD_DIR/SOURCES/epson-l5290-utility"

echo "2. Building RPM package..."
rpmbuild -bb "$RPMBUILD_DIR/SPECS/epson-l5290-suite.spec"

echo "3. Copying finished RPM to output folder..."
cp "$RPMBUILD_DIR"/RPMS/x86_64/epson-l5290-suite-*.rpm "$PROJ_DIR/output/"

echo "=========================================================="
echo " SUCCESS! Built RPM package is saved at:"
echo " $PROJ_DIR/output/"
echo " You can upload this .rpm file directly to GitHub Releases!"
echo "=========================================================="
