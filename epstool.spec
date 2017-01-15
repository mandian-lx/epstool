Summary:	An utility to create or extract preview images in EPS files
Name:		epstool
Version:	3.08
Release:	1
License:	GPLv2+
Group:		Graphics
URL:		http://pages.cs.wisc.edu/~ghost/gsview/%{name}.htm
Source0:	http://mirror.cs.wisc.edu/pub/mirrors/ghost/ghostgum/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-compile.patch
Patch1:		%{name}-%{version}-perms.patch

%description
Epstool is a utility to create or extract preview images in EPS files,
fix bounding boxes and convert to bitmaps.

Features:
  *  Add EPSI, DOS EPS or Mac PICT previews.
  *  Extract PostScript from DOS EPS files.
  *  Uses Ghostscript to create preview bitmaps.
  *  Create a TIFF, WMF, PICT or Interchange preview from part of a
     bitmap created by Ghostscript.
  *  works under Win32, Win64, OS/2 and Unix.
  *  works on little-endian machines (Intel) or big endian (Sun Sparc,
     Motorola) machines.

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%doc doc/epstool.htm doc/gsview.css
%doc LICENCE

#--------------------------------------------------------------------

%prep
%setup -q

# Apply all patches
%patch0 -p1 -b .orig
%patch1 -p1 -b .orig

%build
%setup_compile_flags
%make

%install
%makeinstall_std

