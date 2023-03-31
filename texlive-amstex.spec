Name:		texlive-amstex
Version:	63708
Release:	2
Summary:	American Mathematical Society plain TeX macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/amstex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amstex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amstex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-tex
Requires:	texlive-amstex.bin

%description
AMSTeX is a TeX macro package, originally written by Michael
Spivak for the American Mathematical Society (AMS) during 1983-
1985 and is described in the book 'The Joy of TeX'. It is based
on Plain TeX, and provides many features for producing more
professional-looking maths formulas with less burden on
authors. More recently, the focus of attention has switched to
amslatex, but AMSTeX remains as a working system.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/amstex/base/amsppt.sti
%{_texmfdistdir}/tex/amstex/base/amsppt.sty
%{_texmfdistdir}/tex/amstex/base/amsppt1.tex
%{_texmfdistdir}/tex/amstex/base/amstex.bug
%{_texmfdistdir}/tex/amstex/base/amstex.tex
%{_texmfdistdir}/tex/amstex/config/amstex.ini
%_texmf_fmtutil_d/amstex
%doc %{_texmfdistdir}/doc/amstex/base/README
%doc %{_texmfdistdir}/doc/amstex/base/amsguide.pdf
%doc %{_texmfdistdir}/doc/amstex/base/amsguide.tex
%doc %{_texmfdistdir}/doc/amstex/base/amsppt.doc
%doc %{_texmfdistdir}/doc/amstex/base/amsppt.faq
%doc %{_texmfdistdir}/doc/amstex/base/amsppt.txt
%doc %{_texmfdistdir}/doc/amstex/base/amstex.txt
%doc %{_texmfdistdir}/doc/amstex/base/amstinst.tex
%doc %{_texmfdistdir}/doc/amstex/base/amstinst.pdf
%doc %{_texmfdistdir}/doc/amstex/base/joyerr2.tex
%doc %{_mandir}/man1/amstex.1*
%doc %{_texmfdistdir}/doc/man/man1/amstex.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/amstex <<EOF
#
# from amstex:
amstex pdftex - -translate-file=cp227.tcx *amstex.ini
EOF
