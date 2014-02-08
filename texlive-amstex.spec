# revision 23089
# category Package
# catalog-ctan /macros/amstex
# catalog-date 2011-04-11 22:27:07 +0200
# catalog-license lppl
# catalog-version 2.2
Name:		texlive-amstex
Version:	2.2
Release:	4
Summary:	American Mathematical Society plain TeX macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/amstex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amstex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amstex.doc.tar.xz
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
%doc %{_texmfdistdir}/doc/amstex/base/amstinst.ps.gz
%doc %{_texmfdistdir}/doc/amstex/base/amstinst.tex
%doc %{_texmfdistdir}/doc/amstex/base/joyerr.tex
%doc %{_texmfdistdir}/doc/amstex/base/joyerr2.tex
%doc %{_mandir}/man1/amstex.1*
%doc %{_texmfdir}/doc/man/man1/amstex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/amstex <<EOF
#
# from amstex:
amstex pdftex - -translate-file=cp227.tcx *amstex.ini
EOF


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-3
+ Revision: 778423
- Rebuild after tlpobj2spec.pl bug correction.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-2
+ Revision: 749246
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 720057
- texlive-amstex
- texlive-amstex
- texlive-amstex
- texlive-amstex
- texlive-amstex
- texlive-amstex

