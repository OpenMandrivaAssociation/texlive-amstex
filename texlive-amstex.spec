%global tl_name amstex
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.01
Release:	%{tl_revision}.1
Summary:	American Mathematical Society plain TeX macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/amstex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amstex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amstex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(amsfonts)
Requires:	texlive(amstex.bin)
Requires:	texlive(cm)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(pdftex)
Requires:	texlive(plain)
Requires:	texlive(tex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
AMS-TeX is a TeX macro package, originally written by Michael Spivak for
the American Mathematical Society (AMS) during 1983-1985 and is
described in the book 'The Joy of TeX'. It is based on Plain TeX, and
provides many features for producing more professional-looking maths
formulas with less burden on authors. This is the final archival
distribution of AMS-TeX. AMS-TeX is no longer supported by the AMS, nor
is it used by the AMS publishing program. The AMS does not recommend
creating any new documents using AMS-TeX; this distribution will be left
on CTAN to facilitate processing of legacy documents and as a historical
record of a pioneering TeX macro collection that played a key role in
popularizing TeX and revolutionizing mathematics publishing. In addition
to the "User's Guide to AMS-TeX", the AMS has also made the full text of
the most recent reprint of the second edition of "The Joy of TeX" by
Michael Spivak available as a pdf file. AMS-TeX is the historical basis
of amslatex, which should now be used to prepare submissions for the
AMS.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/tex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/amstex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/tex/amstex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%dir %{_datadir}/texmf-dist/texmf-dist/tex/amstex/base
%dir %{_datadir}/texmf-dist/texmf-dist/tex/amstex/config
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/README
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/amsguide.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/amsguide.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/amsppt.doc
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/amsppt.faq
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/amsppt.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/amstex.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/amstinst.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/amstinst.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/amstex/base/joyerr2.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/amstex.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/amstex.man1.pdf
%{_datadir}/texmf-dist/texmf-dist/tex/amstex/base/amsppt.sti
%{_datadir}/texmf-dist/texmf-dist/tex/amstex/base/amsppt.sty
%{_datadir}/texmf-dist/texmf-dist/tex/amstex/base/amsppt1.tex
%{_datadir}/texmf-dist/texmf-dist/tex/amstex/base/amstex.bug
%{_datadir}/texmf-dist/texmf-dist/tex/amstex/base/amstex.tex
%{_datadir}/texmf-dist/texmf-dist/tex/amstex/config/amstex.ini
