Name:		matrix-commander
Version:	8.0.5
Release:	1
Summary:	A simple command-line Matrix client
URL:		https://github.com/8go/matrix-commander
License:	GPLv3
Group:		Development/Python

Source0:	%url/archive/refs/tags/v%version.tar.gz#/%name-%version.tar.gz
Patch0:   python-stdlib-fix.patch

BuildRequires:	python >= 3.8
BuildRequires:	olm-python
BuildRequires:  pkgconfig(olm) 
Requires:       python3dist(matrix-nio)
Requires:       python3dist(markdown)
Requires:       python3dist(python-magic)
Requires:       python3dist(dbus-python)
Requires:       python3dist(notify2)
Requires:       python3dist(urllib3)
Requires:       python3dist(emoji)
Requires:       python3dist(async-timeout)
Requires:       moreutils
Requires:       fzf

BuildSystem:	python
BuildArch:	noarch

%description
A simple command-line Matrix client

%files
%license LICENSE
%doc README.md
%{_bindir}/%name
%{py_sitedir}/matrix_commander/*
%{py_sitedir}/matrix_commander-*.*-info
