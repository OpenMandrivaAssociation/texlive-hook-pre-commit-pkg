Name:		texlive-hook-pre-commit-pkg
Version:	41378
Release:	2
Summary:	Pre-commit git hook for LaTeX package developpers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hook-pre-commit-pkg
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hook-pre-commit-pkg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hook-pre-commit-pkg.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a pre-commit git hook to check basic
LaTeX syntax for the use of package developers. It is installed
by copying it into the .git/.hooks file. It then checks the
following file types: .sty, .dtx, .bbx, .cbx, and .lbx. List of
performed checks: Each line must be terminated by a %, without
a space before it. Empty lines are allowed, but not lines with
nothing but spaces in them. \begin{macro} and \end{macro} must
be paired. \begin{macrocode} and \end{macrocode} must be
paired. \begin{macro} must have a second argument. One space
must be printed between % and \begin{macro} or \end{macro}. %
must be the first character in the line. Four spaces must be
printed between % and \begin{macrocode} or \end{macrocode}. \cs
argument must not start with a backslash.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/support/hook-pre-commit-pkg

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
