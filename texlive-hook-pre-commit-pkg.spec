%global tl_name hook-pre-commit-pkg
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	Pre-commit git hook for LaTeX package developers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/hook-pre-commit-pkg
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hook-pre-commit-pkg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hook-pre-commit-pkg.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a pre-commit git hook to check basic LaTeX syntax
for the use of package developers. It is installed by copying it into
the .git/.hooks file. It then checks the following file types: .sty,
.dtx, .bbx, .cbx, and .lbx. List of performed checks: Each line must be
terminated by a %, without a space before it. Empty lines are allowed,
but not lines with nothing but spaces in them. \begin{macro} and
\end{macro} must be paired. \begin{macrocode} and \end{macrocode} must
be paired. \begin{macro} must have a second argument. One space must be
printed between % and \begin{macro} or \end{macro}. % must be the first
character in the line. Four spaces must be printed between % and
\begin{macrocode} or \end{macrocode}. \cs argument must not start with a
backslash.

