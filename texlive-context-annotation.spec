Name:		texlive-context-annotation
Version:	47085
Release:	2
Summary:	Annotate text blocks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/context-annotation
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-annotation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-annotation.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The annotation module lets you create your own commands and
environments to mark text blocks.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/context
%{_texmfdistdir}/tex/context/third
%{_texmfdistdir}/tex/context/third/annotation
%{_texmfdistdir}/tex/context/third/annotation/t-annotation.mkvi
%{_texmfdistdir}/tex/context/third/annotation/t-annotation.lua
%{_texmfdistdir}/tex/context/interface
%{_texmfdistdir}/tex/context/interface/third
%{_texmfdistdir}/tex/context/interface/third/t-annotation.xml
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/context
%doc %{_texmfdistdir}/doc/context/third
%doc %{_texmfdistdir}/doc/context/third/annotation
%doc %{_texmfdistdir}/doc/context/third/annotation/annotation-doc.pdf
%doc %{_texmfdistdir}/doc/context/third/annotation/VERSION
%doc %{_texmfdistdir}/doc/context/third/annotation/README

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
